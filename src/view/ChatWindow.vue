<template>
    <div class="chat-container">
        <div class="bot-info">
            <div class="bot-box">
                <img src="../assets/img/7.jpg" alt="Bot Icon" class="img" />
                <div class="bot-text">
                    <div class="bot-name">我是聊天机器人芥川</div>
                    <div class="bot-function">你可以问我关于前端的问题我会尽全力解答</div>
                </div>
            </div>
        </div>
        <div class="chat-box">
                <div class="chat-message"
                    :class="{ 'message-right': msg.sender === '你', 'message-left': msg.sender !== '你' }"
                    v-for="(msg, index) in messages" :key="index">

                    <!-- 芥川的消息 -->
                    <img v-if="msg.sender !== '你'" src="../assets/img/7.jpg" alt="bot" class="avatar" />

                    <div class="message-bubble">
                        {{ msg.text }}
                    </div>

                    <!-- 我发的消息 -->
                    <img v-if="msg.sender === '你'" src="../assets/img/user.jpg" alt="you" class="avatar" />
                </div>
        </div>
        <div class="input-area">
            <input v-model="inputMessage" @keyup.enter="sendMessage" placeholder="请输入消息..." />
            <el-button @click="sendMessage" class="submit-button" :loading="isLoading">发送</el-button>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { sendChatMessage } from '../api/index.js'
import { ElMessage } from 'element-plus'

const inputMessage = ref('')
const messages = ref([])
const isLoading = ref(false)

// 滚动条自动滚动到最新消息的位置
watch(messages, () => {
    const chatBox = document.querySelector('.chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
})

const sendMessage = async () => {
    if (!inputMessage.value.trim()) {
        console.log("输入内容为空")

        ElMessage.warning("请输入消息内容~")

        document.querySelector('input').classList.add('error')

        setTimeout(() => {
            document.querySelector('input').classList.remove('error')
        }, 300)
        return
    }


    const userText = inputMessage.value.trim()
    messages.value.push({ sender: '你', text: userText })
    inputMessage.value = ''
    isLoading.value = true

    // 添加临时的 "加载中" 消息
    const loadingMessage = { sender: '机器人', text: '正在头脑风暴...' }
    messages.value.push(loadingMessage)

    try {
        const response = await sendChatMessage(userText)
        loadingMessage.text = response.text;
    } catch (error) {

        loadingMessage.text = '无法获取回复，请稍后再试。'
        ElMessage.error(`请求失败: ${error.message}`)
    }

    inputMessage.value = ''
    isLoading.value = false
}
</script>

<style scoped>
.chat-container {
    width: 60vw;
    height: 80vh;
    margin: auto;
    background-color: rgb(39, 42, 55);
    color: #f1f1f1;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-radius: 40px;
}

.bot-info {
    height: 80px;
    display: flex;
    align-items: center;
    color: #f1f1f1;
    border-radius: 40px 40px 0 0;
}

.bot-box {
    display: flex;
    margin: 0 40px;
}

.img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 10px;
    margin: 0 20px 0 0;

}

.bot-name {
    font-size: 1.6em;
    margin: 5px 0 5px 0;
    font-weight: bold;
}

.chat-box {
    height: 70%;
    background-image: url("@/assets/img/snapchat.png");
    background-repeat: no-repeat; 
    background-position: center; 
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid #4a4a4a;
    padding: 15px 0;
    overflow-y: auto;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
}

.chat-message {
    display: flex;
    margin: 10px 20px;
}

.message-right {
    justify-content: flex-end;
}

.message-left {
    justify-content: flex-start;
}

.message-bubble {
    max-width: 60%;
    padding: 10px 15px;
    border-radius: 20px;
    line-height: 1.5;
    word-wrap: break-word;
}

.message-right .message-bubble {
    background-color: #1d90f5;
    color: white;
    border-bottom-right-radius: 0;
}

.message-left .message-bubble {
    background-color: #3e4049;
    color: #f1f1f1;
    border-bottom-left-radius: 0;
}

.avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    object-fit: cover;
    margin: 0 8px;
    align-self: flex-end;
}


.input-area {
    height: 80px;
    display: flex;
    gap: 10px;
    align-items: center;
}

input {
    height: 40px;
    flex: 1;
    padding: 10px;
    font-size: 16px;
    border: none;
    border-radius: 20px;
    background-color: #2e313f;
    color: #f1f1f1;
    outline: none;
    margin: 0 10px 10px 10px;
    transition: box-shadow 0.3s ease;
}

input::placeholder {
    color: #aaa;
}

input:focus {
    box-shadow: 0px 0px 10px 0px rgba(0, 136, 255);
}

input.error {
    animation: shake 0.3s ease-in-out;
    border: 1px solid red;
}

@keyframes shake {
    0%, 100% {
        transform: translateX(0);
    }
    25% {
        transform: translateX(-5px);
    }
    75% {
        transform: translateX(5px);
    }
}
.submit-button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #1d90f5;
    margin-right: 20px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #1d90f5;
    box-shadow: 0px 0px 10px 0px rgba(0, 136, 255);
}

.chat-box::-webkit-scrollbar {
    width: 8px;
}

.chat-box::-webkit-scrollbar-thumb {
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 4px;
}

.chat-box::-webkit-scrollbar-track {
    background: transparent;
}
</style>
