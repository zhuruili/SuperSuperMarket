<!-- <template>
    <div class="register-container">
        <h2>注册</h2>
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
                <button type="submit">注册</button>
                <button type="button" @click="handleCancel">取消</button>
            </div>
        </form>
    </div>
    <tabbar></tabbar>
</template> -->
<template>
    <div class="container">
        <div class="heading">注册</div>
        <form action="" class="form">
          <input v-model="username" required="" class="input" type="text" name="username" id="username" placeholder="用户名">
          <input v-model="password" required="" class="input" type="password" name="password" id="password" placeholder="密码">
          <span @click="haveAcount" class="forgot-password"><a href="#">已有账号登录</a></span>
          <input @click="handleRegister" class="login-button" type="submit" value="注册">
  
        </form>
        <div class="social-account-container">
            <span class="title">Or Sign up with</span>
            <div class="social-accounts">
              <button class="social-button google">
                <svg class="svg" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 488 512">
                  <path d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z"></path>
                </svg></button>
              <button class="social-button apple">
                <svg class="svg" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 384 512">
                  <path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"></path>
                </svg>
              </button>
              <button class="social-button twitter">
                <svg class="svg" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512">
                  <path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"></path>
                </svg>
              </button>
            </div>
          </div>
          <span class="agreement"><a href="#">Learn user licence agreement</a></span>
      </div>
  </template>
<script setup>

import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const username = ref('');
const password = ref('');
const router = useRouter();
const haveAcount=()=>{
    router.push("/mine")
}
const handleRegister = () => {
    console.log(username.value, password.value);
    axios.post('http://127.0.0.1:5678/register', { username: username.value, password: password.value }).then((res) => {
        alert('注册成功')
    })
    router.push("/mine")

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


  .container {
    position: absolute;
    display: flex;
    left: 200px;
    top:0px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100vh; /* 可以设置一个固定的宽度 */
    background: #F8F9FD;
    margin-left: 13.33333rem;
    height: 100vh;
    background: linear-gradient(0deg, white 0%, #f4f7fb 100%);
    border-radius: 1.06667rem;
    padding: 0.66667rem 0.93333rem;
    border: 0.13333rem solid white;
    box-shadow: rgba(133, 189, 215, 0.8784313725) 0 0.8rem 0.8rem -0.53333rem;
    margin: 0.53333rem;
  }

  .heading {
    text-align: center;
    font-weight: 900;
    font-size: 30px;
    color: rgb(16, 137, 211);
  }

  .form {
    margin-top: 20px;
  }

  .form .input {
    width: 100%;
    background: white;
    border: none;
    padding: 15px 20px;
    border-radius: 20px;
    margin-top: 15px;
    box-shadow: #cff0ff 0px 10px 10px -5px;
    border-inline: 2px solid transparent;
  }

  .form .input::-moz-placeholder {
    color: rgb(170, 170, 170);
  }

  .form .input::placeholder {
    color: rgb(170, 170, 170);
  }

  .form .input:focus {
    outline: none;
    border-inline: 2px solid #12B1D1;
  }

  .form .forgot-password {
    display: block;
    margin-top: 10px;
    margin-left: 10px;
  }

  .form .forgot-password a {
    font-size: 11px;
    color: #0099ff;
    text-decoration: none;
  }

  .form .login-button {
    display: block;
    width: 100%;
    font-weight: bold;
    background: linear-gradient(45deg, rgb(16, 137, 211) 0%, rgb(18, 177, 209) 100%);
    color: white;
    padding-block: 15px;
    margin: 20px auto;
    border-radius: 20px;
    box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 20px 10px -15px;
    border: none;
    transition: all 0.2s ease-in-out;
  }

  .form .login-button:hover {
    transform: scale(1.03);
    box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 23px 10px -20px;
  }

  .form .login-button:active {
    transform: scale(0.95);
    box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 15px 10px -10px;
  }

  .social-account-container {
    margin-top: 25px;
  }

  .social-account-container .title {
    display: block;
    text-align: center;
    font-size: 10px;
    color: rgb(170, 170, 170);
  }

  .social-account-container .social-accounts {
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 5px;
  }

  .social-account-container .social-accounts .social-button {
    background: linear-gradient(45deg, rgb(0, 0, 0) 0%, rgb(112, 112, 112) 100%);
    border: 5px solid white;
    padding: 5px;
    border-radius: 50%;
    width: 40px;
    aspect-ratio: 1;
    display: grid;
    place-content: center;
    box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 12px 10px -8px;
    transition: all 0.2s ease-in-out;
  }

  .social-account-container .social-accounts .social-button .svg {
    fill: white;
    margin: auto;
  }

  .social-account-container .social-accounts .social-button:hover {
    transform: scale(1.2);
  }

  .social-account-container .social-accounts .social-button:active {
    transform: scale(0.9);
  }

  .agreement {
    display: block;
    text-align: center;
    margin-top: 15px;
  }

  .agreement a {
    text-decoration: none;
    color: #0099ff;
    font-size: 9px;
  }

</style>