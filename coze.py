from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json
import time

# 实例化APP
app = Flask(__name__, static_url_path='/static')
CORS(app)

api_key = "pat_Aw3Y808NYQcpIvUayh8tNcu5E1EGJBxUjQmpBKcPr7yp2vTPnfu26fRjbdAAFeWI"
botid = "7504635877285675046"
baseUrl = 'https://api.coze.cn/v3/chat'
headers = {
    "Authorization": f"Bearer {api_key}",
    'Content-Type': 'application/json'
}
# 返回的内容
response_content = ''

def process_chat_response(response_data):
    """处理聊天API返回的响应数据，提取回答内容"""
    global response_content
    if response_data['code']:
        print("应答异常：", response_data['msg'])
    else:
        data = response_data['data']
        for item in data:
            if item['type'] == 'answer':
                print("大模型应答：", item['content'])
                response_content = item['content']

def check_chat_completion(conversation_id, chat_id):
    """检查聊天任务是否完成，并在完成时获取回答内容"""
    params = {"bot_id": botid, "task_id": chat_id}
    get_chat_status_url = baseUrl + f'/retrieve?conversation_id={conversation_id}&chat_id={chat_id}&'

    while True:
        response = requests.get(get_chat_status_url, headers=headers, params=None)
        if response.status_code == 200:
            response_data = response.json()
            print(f"response_data:\n{json.dumps(response_data, indent=4, ensure_ascii=False)}")
            status = response_data['data']['status']
            if status == 'completed':
                # 从响应中提取实际的应答内容
                get_chat_answer_url = baseUrl + f'/message/list?chat_id={chat_id}&conversation_id={conversation_id}'
                response = requests.get(get_chat_answer_url, headers=headers, params=params)
                if response.status_code == 200:
                    response_data = response.json()
                    print("模型返回数据:\n", json.dumps(response_data, indent=4, ensure_ascii=False))
                    process_chat_response(response_data)
                    return True
                break
            else:
                print(f"任务仍在处理中，状态: {status}")
                time.sleep(1)  # 等待1秒后再次检查
        else:
            print(f"请求失败，状态码: {response.status_code}")
            break
    return False

def send_user_question(question_text):
    """向聊天API发送用户问题并处理响应"""
    data = {
        "bot_id": botid,
        "user_id": "123",
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {
                "role": "user",
                "content": question_text,
                "content_type": "text"
            }
        ]
    }

    # 发送POST请求
    print(f"请求信息:{json.dumps(data, indent=4, ensure_ascii=False)}")
    response = requests.post(baseUrl, headers=headers, data=json.dumps(data))

    # 检查响应状态码
    if response.status_code == 200:
        # 解析响应内容
        response_data = response.json()
        print("响应内容:", json.dumps(response_data, indent=4, ensure_ascii=False))
        chat_id = response_data['data']['id']
        answer = response_data.get("answer")
        conversation_id = response_data['data']['conversation_id']
        print(f"chat_id={chat_id},智能体应答: {answer}")

        check_chat_completion(conversation_id, chat_id)

    else:
        print("请求失败，状态码:", response.status_code)
        print("错误信息:", response.text)

@app.route('/message', methods=['POST'])
# 定义应答函数，用于获取输入信息并返回相应的答案
def reply():
    # 从请求中获取参数信息
    req_msg = request.form['msg']
    send_user_question(req_msg)
    print('response_content', response_content)
    return jsonify({'text': response_content})

@app.route("/")
# 在网页上展示对话
def index():
    print('/')
    return render_template('index.html')

# 启动APP
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8808)