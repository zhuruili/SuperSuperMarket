<template>
    <div class="login-regist">
        <router-link to="/mylogin" class="order-item" tag="span">登录</router-link>
        <router-link to="/register/myRegister" class="order-item" tag="span">/注册</router-link>
    </div>
</template>

<script setup>

</script>

<style scoped lang="scss">
.login-regist {
    display: flex;
    justify-content: center;
    margin-top: 300px;
    .order-item {
        font-size: 16px;
        color: #333;
        margin: 0 10px;
    }   
}
</style>