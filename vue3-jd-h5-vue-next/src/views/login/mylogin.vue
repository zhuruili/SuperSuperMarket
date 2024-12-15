<template>
    <div class="register-container">
        <h2>登录</h2>
        <form @submit.prevent="handleRegister">
            <div class="form-group">
                <label for="username">用户名:</label>
                <input type="text" id="username" v-model="username" required />
            </div>
            <div class="form-group">
                <label for="password">密码:</label>
                <input type="password" id="password" v-model="password" required />
            </div>
            <div class="button-group">
                <button @click="handleLogin"  type="submit">登录</button>
                <button type="button" @click="handleCancel">取消</button>
            </div>
        </form>
    </div>
    <tabbar></tabbar>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axois from 'axios';
const username = ref('');
const password = ref('');
const router = useRouter();
import AxiosPlugin, { httpInstance } from '@/plugins/axios'

const handleRegister = async() => {
    try {
        console.log('handleLogin');
        // 发送登录请求
        const response = await httpInstance.post("http://localhost:8889/login", {
            username: username.value,
            password: password.value
        }, {
            headers: {
                'Content-Type': 'application/json'  // 设置正确的 Content-Type
            }
        });
        console.log(response);
        // 假设返回的 response 中有一个 `token` 字段，表示登录成功
        if (response.status==200) {
            console.log("Login successful!");

            // 将 token 存储在 localStorage 中，或其他合适的地方
           // localStorage.setItem('token', response.data.token);
            localStorage.setItem('username', response.data.username);
            localStorage.setItem('userId', response.data.userID);
           // localStorage.setItem('password', password.value);
            localStorage.setItem("isLogin",true);
            console.log(localStorage.getItem("userId"))
            // 跳转到登录成功后的页面，例如首页
            router.push('/mine');
        } else {
            console.log("Login failed:", response.data.message);
            alert(response.data.message);  // 提示错误消息
        }
    } catch (error) {
        console.log("Error during login:", error);
        alert("An error occurred while logging in");
    }

};

const handleCancel = () => {
    username.value = '';
    password.value = '';
};
</script>

<style scoped lang="scss">
.register-container {
    max-width: 300px;
    max-height: 250px;
    margin: 150px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    background-color: #f9f9f9;
}

h2 {
    margin-bottom: 20px;
    color: #333;
}

.form-group {
    margin-bottom: 15px;
    text-align: left;
}

label {
    display: block;
    margin-bottom: 5px;
    color: #555;
}

input {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.button-group {
    display: flex;
    justify-content: space-between;
}

button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button[type="button"] {
    background-color: #6c757d;
}

button:hover {
    background-color: #0056b3;
}

button[type="button"]:hover {
    background-color: #5a6268;
}
</style>