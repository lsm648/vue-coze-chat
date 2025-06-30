// src/api.js
import axios from 'axios'

// 创建 axios 实例
const service = axios.create({
    baseURL: 'https://47.83.5.240:8888', // Flask 后端地址
    timeout: 20000,
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    timeoutError: 20000 // 请求超时时间
})

// 请求拦截器（可选）
service.interceptors.request.use(
    config => {
        console.log('请求发送前的配置:', config);
        return config
    },
    error => {
        console.error('请求错误:', error);
        return Promise.reject(error)
    }
)

// 响应拦截器（可选）
service.interceptors.response.use(
    response => response.data,
    // console.log('响应数据:', response),
    error => {
        console.error('网络请求失败:', error)
        return Promise.reject(error)
    }
)

// 封装一个发送消息的函数
export const sendChatMessage = (message) =>{
    return service.post('/message', new URLSearchParams({ msg: message }))
}
