import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    {
        path: '/',
        name: 'Home',
        component: import('@/view/Home.vue')
    },
    {
        path: '/chat',
        component: import('@/view/ChatWindow.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
