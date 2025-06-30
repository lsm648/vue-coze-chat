<template>
    <div class="home-container">
        <div class="overlay">
            <img src="../assets/img/7.jpg" alt="bot" class="bot-avatar" />
            <h1 class="title">你好，我是芥川</h1>
            <p class="subtitle">你的专属前端小助手</p>
            <button class="start-button" @click="startChat">开始聊天</button>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const router = useRouter()
const startChat = () => {
    ElMessage.success("欢迎您~")
    setTimeout(() => {
        router.push('/chat')
    }, 1000)

}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

.home-container {
    width: 100vw;
    height: 100vh;
    background: linear-gradient(135deg, #2c2f3d, #1a1b23);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
}

.overlay {
    text-align: center;
    animation: fadeIn 1.2s ease-out;
}

.bot-avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 20px;
    animation: float 3s ease-in-out infinite;
    box-shadow: 0 0 20px rgba(0, 136, 255, 0.4);
}

.title {
    font-size: 2.8em;
    color: #f1f1f1;
    margin-bottom: 10px;
    font-family: 'Orbitron', sans-serif;
}

.subtitle {
    color: #aaa;
    font-size: 1.2em;
    margin-bottom: 40px;
}

.start-button {
    padding: 14px 30px;
    font-size: 16px;
    border: none;
    border-radius: 30px;
    background-color: #1d90f5;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 0 10px rgba(0, 136, 255, 0.5);
}

.start-button:hover {
    background-color: #0078e7;
    box-shadow: 0 0 15px rgba(0, 136, 255, 0.7);
    transform: scale(1.05);
}

/* 动画效果 */
@keyframes float {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scale(0.95);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}
</style>