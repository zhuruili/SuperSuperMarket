<!--
 * @version: v 1.0.0
 * @Github: https://github.com/GitHubGanKai
 * @Author: GitHubGanKai
 * @Date: 2021-01-01 17:05:34
 * @LastEditors: gankai
 * @LastEditTime: 2021-01-02 16:39:20
 * @FilePath: /refactor-with-vue3/src/views/mine/setting.vue
-->
<template>
  <div class="setting-page">
    <header class="page-header">
      <van-icon name="arrow-left" @click="$router.go(-1)" />
      <div class="header-content">设置</div>
    </header>

    <section class="setting-content">
      <ul class="setting-list">
        <li class="setting-item">
          <span class="setting-msg">消息提醒</span>
          <van-switch v-model="checked" active-color="#D8182D" size="20px" />
        </li>
        <li class="setting-item">
          <span class="setting-msg">清除缓存</span>
          <van-icon class="icon" name="arrow" />
        </li>
        <li class="setting-item">
          <span class="setting-msg">我的权限</span>
          <!-- <van-switch v-model="checked" active-color="#D8182D" size="20px" /> -->
           <!-- <span class="power">{{power}}</span> -->
           <button>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 36 36"
      width="36px"
      height="36px"
    >
      <rect width="36" height="36" x="0" y="0" fill="#fdd835"></rect>
      <path
        fill="#e53935"
        d="M38.67,42H11.52C11.27,40.62,11,38.57,11,36c0-5,0-11,0-11s1.44-7.39,3.22-9.59 c1.67-2.06,2.76-3.48,6.78-4.41c3-0.7,7.13-0.23,9,1c2.15,1.42,3.37,6.67,3.81,11.29c1.49-0.3,5.21,0.2,5.5,1.28 C40.89,30.29,39.48,38.31,38.67,42z"
      ></path>
      <path
        fill="#b71c1c"
        d="M39.02,42H11.99c-0.22-2.67-0.48-7.05-0.49-12.72c0.83,4.18,1.63,9.59,6.98,9.79 c3.48,0.12,8.27,0.55,9.83-2.45c1.57-3,3.72-8.95,3.51-15.62c-0.19-5.84-1.75-8.2-2.13-8.7c0.59,0.66,3.74,4.49,4.01,11.7 c0.03,0.83,0.06,1.72,0.08,2.66c4.21-0.15,5.93,1.5,6.07,2.35C40.68,33.85,39.8,38.9,39.02,42z"
      ></path>
      <path
        fill="#212121"
        d="M35,27.17c0,3.67-0.28,11.2-0.42,14.83h-2C32.72,38.42,33,30.83,33,27.17 c0-5.54-1.46-12.65-3.55-14.02c-1.65-1.08-5.49-1.48-8.23-0.85c-3.62,0.83-4.57,1.99-6.14,3.92L15,16.32 c-1.31,1.6-2.59,6.92-3,8.96v10.8c0,2.58,0.28,4.61,0.54,5.92H10.5c-0.25-1.41-0.5-3.42-0.5-5.92l0.02-11.09 c0.15-0.77,1.55-7.63,3.43-9.94l0.08-0.09c1.65-2.03,2.96-3.63,7.25-4.61c3.28-0.76,7.67-0.25,9.77,1.13 C33.79,13.6,35,22.23,35,27.17z"
      ></path>
      <path
        fill="#01579b"
        d="M17.165,17.283c5.217-0.055,9.391,0.283,9,6.011c-0.391,5.728-8.478,5.533-9.391,5.337 c-0.913-0.196-7.826-0.043-7.696-5.337C9.209,18,13.645,17.32,17.165,17.283z"
      ></path>
      <path
        fill="#212121"
        d="M40.739,37.38c-0.28,1.99-0.69,3.53-1.22,4.62h-2.43c0.25-0.19,1.13-1.11,1.67-4.9 c0.57-4-0.23-11.79-0.93-12.78c-0.4-0.4-2.63-0.8-4.37-0.89l0.1-1.99c1.04,0.05,4.53,0.31,5.71,1.49 C40.689,24.36,41.289,33.53,40.739,37.38z"
      ></path>
      <path
        fill="#81d4fa"
        d="M10.154,20.201c0.261,2.059-0.196,3.351,2.543,3.546s8.076,1.022,9.402-0.554 c1.326-1.576,1.75-4.365-0.891-5.267C19.336,17.287,12.959,16.251,10.154,20.201z"
      ></path>
      <path
        fill="#212121"
        d="M17.615,29.677c-0.502,0-0.873-0.03-1.052-0.069c-0.086-0.019-0.236-0.035-0.434-0.06 c-5.344-0.679-8.053-2.784-8.052-6.255c0.001-2.698,1.17-7.238,8.986-7.32l0.181-0.002c3.444-0.038,6.414-0.068,8.272,1.818 c1.173,1.191,1.712,3,1.647,5.53c-0.044,1.688-0.785,3.147-2.144,4.217C22.785,29.296,19.388,29.677,17.615,29.677z M17.086,17.973 c-7.006,0.074-7.008,4.023-7.008,5.321c-0.001,3.109,3.598,3.926,6.305,4.27c0.273,0.035,0.48,0.063,0.601,0.089 c0.563,0.101,4.68,0.035,6.855-1.732c0.865-0.702,1.299-1.57,1.326-2.653c0.051-1.958-0.301-3.291-1.073-4.075 c-1.262-1.281-3.834-1.255-6.825-1.222L17.086,17.973z"
      ></path>
      <path
        fill="#e1f5fe"
        d="M15.078,19.043c1.957-0.326,5.122-0.529,4.435,1.304c-0.489,1.304-7.185,2.185-7.185,0.652 C12.328,19.467,15.078,19.043,15.078,19.043z"
      ></path>
    </svg>
    <span class="now">go!</span>
    <span class="play">{{power}}</span>
  </button>
        </li>

        <li v-show="power == '管理员'||power == '商家'" class="setting-item">
          <span class="setting-msg">创建商品</span>
          <button @click="createOrder">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 36 36"
      width="36px"
      height="36px"
    >
      <rect width="36" height="36" x="0" y="0" fill="#fdd835"></rect>
      <path
        fill="#e53935"
        d="M38.67,42H11.52C11.27,40.62,11,38.57,11,36c0-5,0-11,0-11s1.44-7.39,3.22-9.59 c1.67-2.06,2.76-3.48,6.78-4.41c3-0.7,7.13-0.23,9,1c2.15,1.42,3.37,6.67,3.81,11.29c1.49-0.3,5.21,0.2,5.5,1.28 C40.89,30.29,39.48,38.31,38.67,42z"
      ></path>
      <path
        fill="#b71c1c"
        d="M39.02,42H11.99c-0.22-2.67-0.48-7.05-0.49-12.72c0.83,4.18,1.63,9.59,6.98,9.79 c3.48,0.12,8.27,0.55,9.83-2.45c1.57-3,3.72-8.95,3.51-15.62c-0.19-5.84-1.75-8.2-2.13-8.7c0.59,0.66,3.74,4.49,4.01,11.7 c0.03,0.83,0.06,1.72,0.08,2.66c4.21-0.15,5.93,1.5,6.07,2.35C40.68,33.85,39.8,38.9,39.02,42z"
      ></path>
      <path
        fill="#212121"
        d="M35,27.17c0,3.67-0.28,11.2-0.42,14.83h-2C32.72,38.42,33,30.83,33,27.17 c0-5.54-1.46-12.65-3.55-14.02c-1.65-1.08-5.49-1.48-8.23-0.85c-3.62,0.83-4.57,1.99-6.14,3.92L15,16.32 c-1.31,1.6-2.59,6.92-3,8.96v10.8c0,2.58,0.28,4.61,0.54,5.92H10.5c-0.25-1.41-0.5-3.42-0.5-5.92l0.02-11.09 c0.15-0.77,1.55-7.63,3.43-9.94l0.08-0.09c1.65-2.03,2.96-3.63,7.25-4.61c3.28-0.76,7.67-0.25,9.77,1.13 C33.79,13.6,35,22.23,35,27.17z"
      ></path>
      <path
        fill="#01579b"
        d="M17.165,17.283c5.217-0.055,9.391,0.283,9,6.011c-0.391,5.728-8.478,5.533-9.391,5.337 c-0.913-0.196-7.826-0.043-7.696-5.337C9.209,18,13.645,17.32,17.165,17.283z"
      ></path>
      <path
        fill="#212121"
        d="M40.739,37.38c-0.28,1.99-0.69,3.53-1.22,4.62h-2.43c0.25-0.19,1.13-1.11,1.67-4.9 c0.57-4-0.23-11.79-0.93-12.78c-0.4-0.4-2.63-0.8-4.37-0.89l0.1-1.99c1.04,0.05,4.53,0.31,5.71,1.49 C40.689,24.36,41.289,33.53,40.739,37.38z"
      ></path>
      <path
        fill="#81d4fa"
        d="M10.154,20.201c0.261,2.059-0.196,3.351,2.543,3.546s8.076,1.022,9.402-0.554 c1.326-1.576,1.75-4.365-0.891-5.267C19.336,17.287,12.959,16.251,10.154,20.201z"
      ></path>
      <path
        fill="#212121"
        d="M17.615,29.677c-0.502,0-0.873-0.03-1.052-0.069c-0.086-0.019-0.236-0.035-0.434-0.06 c-5.344-0.679-8.053-2.784-8.052-6.255c0.001-2.698,1.17-7.238,8.986-7.32l0.181-0.002c3.444-0.038,6.414-0.068,8.272,1.818 c1.173,1.191,1.712,3,1.647,5.53c-0.044,1.688-0.785,3.147-2.144,4.217C22.785,29.296,19.388,29.677,17.615,29.677z M17.086,17.973 c-7.006,0.074-7.008,4.023-7.008,5.321c-0.001,3.109,3.598,3.926,6.305,4.27c0.273,0.035,0.48,0.063,0.601,0.089 c0.563,0.101,4.68,0.035,6.855-1.732c0.865-0.702,1.299-1.57,1.326-2.653c0.051-1.958-0.301-3.291-1.073-4.075 c-1.262-1.281-3.834-1.255-6.825-1.222L17.086,17.973z"
      ></path>
      <path
        fill="#e1f5fe"
        d="M15.078,19.043c1.957-0.326,5.122-0.529,4.435,1.304c-0.489,1.304-7.185,2.185-7.185,0.652 C12.328,19.467,15.078,19.043,15.078,19.043z"
      ></path>
    </svg>
    <span class="now">now!</span>
    <span @click="createOrder" class="play">创建</span>
  </button>
        </li>
        <li v-show="power == '管理员'" class="setting-item">
          <span class="setting-msg">备份</span>
          <button @click="copy">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 36 36"
      width="36px"
      height="36px"
    >
      <rect width="36" height="36" x="0" y="0" fill="#fdd835"></rect>
      <path
        fill="#e53935"
        d="M38.67,42H11.52C11.27,40.62,11,38.57,11,36c0-5,0-11,0-11s1.44-7.39,3.22-9.59 c1.67-2.06,2.76-3.48,6.78-4.41c3-0.7,7.13-0.23,9,1c2.15,1.42,3.37,6.67,3.81,11.29c1.49-0.3,5.21,0.2,5.5,1.28 C40.89,30.29,39.48,38.31,38.67,42z"
      ></path>
      <path
        fill="#b71c1c"
        d="M39.02,42H11.99c-0.22-2.67-0.48-7.05-0.49-12.72c0.83,4.18,1.63,9.59,6.98,9.79 c3.48,0.12,8.27,0.55,9.83-2.45c1.57-3,3.72-8.95,3.51-15.62c-0.19-5.84-1.75-8.2-2.13-8.7c0.59,0.66,3.74,4.49,4.01,11.7 c0.03,0.83,0.06,1.72,0.08,2.66c4.21-0.15,5.93,1.5,6.07,2.35C40.68,33.85,39.8,38.9,39.02,42z"
      ></path>
      <path
        fill="#212121"
        d="M35,27.17c0,3.67-0.28,11.2-0.42,14.83h-2C32.72,38.42,33,30.83,33,27.17 c0-5.54-1.46-12.65-3.55-14.02c-1.65-1.08-5.49-1.48-8.23-0.85c-3.62,0.83-4.57,1.99-6.14,3.92L15,16.32 c-1.31,1.6-2.59,6.92-3,8.96v10.8c0,2.58,0.28,4.61,0.54,5.92H10.5c-0.25-1.41-0.5-3.42-0.5-5.92l0.02-11.09 c0.15-0.77,1.55-7.63,3.43-9.94l0.08-0.09c1.65-2.03,2.96-3.63,7.25-4.61c3.28-0.76,7.67-0.25,9.77,1.13 C33.79,13.6,35,22.23,35,27.17z"
      ></path>
      <path
        fill="#01579b"
        d="M17.165,17.283c5.217-0.055,9.391,0.283,9,6.011c-0.391,5.728-8.478,5.533-9.391,5.337 c-0.913-0.196-7.826-0.043-7.696-5.337C9.209,18,13.645,17.32,17.165,17.283z"
      ></path>
      <path
        fill="#212121"
        d="M40.739,37.38c-0.28,1.99-0.69,3.53-1.22,4.62h-2.43c0.25-0.19,1.13-1.11,1.67-4.9 c0.57-4-0.23-11.79-0.93-12.78c-0.4-0.4-2.63-0.8-4.37-0.89l0.1-1.99c1.04,0.05,4.53,0.31,5.71,1.49 C40.689,24.36,41.289,33.53,40.739,37.38z"
      ></path>
      <path
        fill="#81d4fa"
        d="M10.154,20.201c0.261,2.059-0.196,3.351,2.543,3.546s8.076,1.022,9.402-0.554 c1.326-1.576,1.75-4.365-0.891-5.267C19.336,17.287,12.959,16.251,10.154,20.201z"
      ></path>
      <path
        fill="#212121"
        d="M17.615,29.677c-0.502,0-0.873-0.03-1.052-0.069c-0.086-0.019-0.236-0.035-0.434-0.06 c-5.344-0.679-8.053-2.784-8.052-6.255c0.001-2.698,1.17-7.238,8.986-7.32l0.181-0.002c3.444-0.038,6.414-0.068,8.272,1.818 c1.173,1.191,1.712,3,1.647,5.53c-0.044,1.688-0.785,3.147-2.144,4.217C22.785,29.296,19.388,29.677,17.615,29.677z M17.086,17.973 c-7.006,0.074-7.008,4.023-7.008,5.321c-0.001,3.109,3.598,3.926,6.305,4.27c0.273,0.035,0.48,0.063,0.601,0.089 c0.563,0.101,4.68,0.035,6.855-1.732c0.865-0.702,1.299-1.57,1.326-2.653c0.051-1.958-0.301-3.291-1.073-4.075 c-1.262-1.281-3.834-1.255-6.825-1.222L17.086,17.973z"
      ></path>
      <path
        fill="#e1f5fe"
        d="M15.078,19.043c1.957-0.326,5.122-0.529,4.435,1.304c-0.489,1.304-7.185,2.185-7.185,0.652 C12.328,19.467,15.078,19.043,15.078,19.043z"
      ></path>
    </svg>
    <span class="now">now!</span>
    <span @click="copy" class="play">备份</span>
  </button>
        </li>
        <li v-show="power == '管理员'" class="setting-item">
          <span class="setting-msg">恢复</span>
          <button @click="recovery">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 36 36"
      width="36px"
      height="36px"
    >
      <rect width="36" height="36" x="0" y="0" fill="#fdd835"></rect>
      <path
        fill="#e53935"
        d="M38.67,42H11.52C11.27,40.62,11,38.57,11,36c0-5,0-11,0-11s1.44-7.39,3.22-9.59 c1.67-2.06,2.76-3.48,6.78-4.41c3-0.7,7.13-0.23,9,1c2.15,1.42,3.37,6.67,3.81,11.29c1.49-0.3,5.21,0.2,5.5,1.28 C40.89,30.29,39.48,38.31,38.67,42z"
      ></path>
      <path
        fill="#b71c1c"
        d="M39.02,42H11.99c-0.22-2.67-0.48-7.05-0.49-12.72c0.83,4.18,1.63,9.59,6.98,9.79 c3.48,0.12,8.27,0.55,9.83-2.45c1.57-3,3.72-8.95,3.51-15.62c-0.19-5.84-1.75-8.2-2.13-8.7c0.59,0.66,3.74,4.49,4.01,11.7 c0.03,0.83,0.06,1.72,0.08,2.66c4.21-0.15,5.93,1.5,6.07,2.35C40.68,33.85,39.8,38.9,39.02,42z"
      ></path>
      <path
        fill="#212121"
        d="M35,27.17c0,3.67-0.28,11.2-0.42,14.83h-2C32.72,38.42,33,30.83,33,27.17 c0-5.54-1.46-12.65-3.55-14.02c-1.65-1.08-5.49-1.48-8.23-0.85c-3.62,0.83-4.57,1.99-6.14,3.92L15,16.32 c-1.31,1.6-2.59,6.92-3,8.96v10.8c0,2.58,0.28,4.61,0.54,5.92H10.5c-0.25-1.41-0.5-3.42-0.5-5.92l0.02-11.09 c0.15-0.77,1.55-7.63,3.43-9.94l0.08-0.09c1.65-2.03,2.96-3.63,7.25-4.61c3.28-0.76,7.67-0.25,9.77,1.13 C33.79,13.6,35,22.23,35,27.17z"
      ></path>
      <path
        fill="#01579b"
        d="M17.165,17.283c5.217-0.055,9.391,0.283,9,6.011c-0.391,5.728-8.478,5.533-9.391,5.337 c-0.913-0.196-7.826-0.043-7.696-5.337C9.209,18,13.645,17.32,17.165,17.283z"
      ></path>
      <path
        fill="#212121"
        d="M40.739,37.38c-0.28,1.99-0.69,3.53-1.22,4.62h-2.43c0.25-0.19,1.13-1.11,1.67-4.9 c0.57-4-0.23-11.79-0.93-12.78c-0.4-0.4-2.63-0.8-4.37-0.89l0.1-1.99c1.04,0.05,4.53,0.31,5.71,1.49 C40.689,24.36,41.289,33.53,40.739,37.38z"
      ></path>
      <path
        fill="#81d4fa"
        d="M10.154,20.201c0.261,2.059-0.196,3.351,2.543,3.546s8.076,1.022,9.402-0.554 c1.326-1.576,1.75-4.365-0.891-5.267C19.336,17.287,12.959,16.251,10.154,20.201z"
      ></path>
      <path
        fill="#212121"
        d="M17.615,29.677c-0.502,0-0.873-0.03-1.052-0.069c-0.086-0.019-0.236-0.035-0.434-0.06 c-5.344-0.679-8.053-2.784-8.052-6.255c0.001-2.698,1.17-7.238,8.986-7.32l0.181-0.002c3.444-0.038,6.414-0.068,8.272,1.818 c1.173,1.191,1.712,3,1.647,5.53c-0.044,1.688-0.785,3.147-2.144,4.217C22.785,29.296,19.388,29.677,17.615,29.677z M17.086,17.973 c-7.006,0.074-7.008,4.023-7.008,5.321c-0.001,3.109,3.598,3.926,6.305,4.27c0.273,0.035,0.48,0.063,0.601,0.089 c0.563,0.101,4.68,0.035,6.855-1.732c0.865-0.702,1.299-1.57,1.326-2.653c0.051-1.958-0.301-3.291-1.073-4.075 c-1.262-1.281-3.834-1.255-6.825-1.222L17.086,17.973z"
      ></path>
      <path
        fill="#e1f5fe"
        d="M15.078,19.043c1.957-0.326,5.122-0.529,4.435,1.304c-0.489,1.304-7.185,2.185-7.185,0.652 C12.328,19.467,15.078,19.043,15.078,19.043z"
      ></path>
    </svg>
    <span class="now">now!</span>
    <span @click="recovery" class="play">恢复</span>
  </button>
        </li>
        <router-link tag="li" class="setting-item" to="/setting/aboutAs">
          <span class="setting-msg">关于我们</span>
          <van-icon class="icon" name="arrow" />
        </router-link>
      </ul>
    </section>
    <van-button plain size="large" type="danger" style="color: white;" @click="handleLogout">退出登录</van-button>
  <div class="create-order" v-show="Is_createOrder">
    <div class="form">
      <p class="title">CreateOrder </p>
      <p class="message">Create now and get full access to our Item. </p>
          <div class="flex">
          <label>
              <input v-model="title" class="input" type="text" placeholder="" required="">
              <span>商品名</span>
          </label>

          <label>
  <select v-model="kind" class="input" required="">
    <option value="" disabled selected>选择品类</option>
    <option value="1">电脑</option>
    <option value="2">手机</option>
    <option value="3">女装</option>
    <option value="4">食品</option>
    <option value="5">宠物</option>
    <option value="6">美妆</option>
    <option value="7">鲜花</option>
    <option value="8">图书</option>
  </select>
  <span>品类</span>
</label>
      </div>  

      <label>
          <input v-model="price" class="input" type="number" placeholder="" required="">
          <span>商品价格</span>
      </label> 

      <label>
          <input v-model="store" class="input" type="number" placeholder="" required="">
          <span>库存量</span>
      </label>
      <label>
          <input v-model="sale" class="input" type="number" placeholder="" required="">
          <span>销量</span>
      </label>
      <button @click="submit" class="submit">Submit</button>
      
  </div>

  </div>
  
  </div>
</template>

<script setup>
import { ref ,onMounted} from "vue";
import { useRouter } from "vue-router";
import AxiosPlugin, { httpInstance } from '@/plugins/axios'
const power = ref("");
const router = useRouter();
const checked = ref(false);
const Is_createOrder=ref(false)
const title = ref("");
const price = ref("");
const store = ref("");
const sale = ref("");
const kind = ref("");


const recovery=async()=>{
try{
  const res=await httpInstance.get("http://127.0.0.1:3456/recovery");
  console.log(res)
  alert("恢复成功");
}
catch(e){
  console.log(e);
}
}
const copy=async()=>{
  try{
  const res=await httpInstance.get("http://127.0.0.1:3456/BackupDatabase");
  console.log(res)
  alert("备份成功");
}
catch(e){
  console.log(e);
}
}

const submit=async()=>{
console.log("提交");

console.log(kind.value);
Is_createOrder.value=false
//构造数据，创建商品:
const shop_name=localStorage.getItem("userId");
const pic_url="http://g.search3.alicdn.com/img/i3/4388775026/O1CN017OECTQ1mzxcnZuGqW_!!0-saturn_solar.jpg"
const url="http://detail.tmall.com/item.htm?id=718107875372&ns=1&xxc=ad_ztc&skuId=5155423409135"

  // 获取表单中的其他信息
  const title_value = title.value;
  const price_value = parseFloat(price.value);  // 转换为浮动类型
  const store_value = parseInt(store.value);  // 转换为整数
  const sale_value = sale.value;
  const kind_value = kind.value;

  try {
    // 发起 POST 请求到后端接口
    const res = await httpInstance.post("http://127.0.0.1:8889/addItem", {
      title: title_value,
      pic_url: pic_url,
      price: price_value,
      sale: sale_value,
      shop_name: shop_name,
      store: store_value,
      kind: kind_value,
      url: url
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    // 处理返回结果
    if (res.data.success) {
      console.log('商品添加成功');
    } else {
      console.log('商品添加失败');
    }
  } catch (e) {
    console.log('请求失败', e);
  }
}

const handleLogout = () => {
  localStorage.setItem("isLogin", false);
  console.log("退出登录");
  console.log(localStorage.getItem("isLogin"));
  router.push("/mine");
};
const createOrder=async()=>{
  event.preventDefault(); // 防止表单提交刷新页面
  console.log("创建订单");
  Is_createOrder.value=true
  //router.push('/createOrder')
}
onMounted(async()=>{
  try{
    const res=await httpInstance.post("http://localhost:8889/getPower",{
      userId:localStorage.getItem("userId")
    },{headers: {
    'Content-Type': 'application/json'
  }})
  console.log(res);
  if(res.data.power==1){
power.value="商家"
  }
  if(res.data.power==0){
    power.value="普通用户"
}
if(res.data.power==2){
power.value="管理员"
}
}
  catch(e){
    console.log(e);
  }


});

</script>

<style scoped lang="scss">
.setting-page {
  padding: 0 16px;
  height: 100vh;
  .page-header {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding: 10px;
    .header-content {
      text-align: center;
      font-size: 16px;
      font-weight: 600;
      flex: 1;
    }
  }
  .setting-content {
    padding: 20px 20px 0 20px;
    margin-bottom: 20px;
    background-color: #fff;
    border-radius: 8px;
    .setting-list {
      .setting-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 20px;
        .icon {
          color: #949497;
          opacity: 0.5;
          font-size: 15px;
        }
        .setting-msg {
          color: #3a3a3a;
          font-size: 15px;
        }
      }
    }
  }
  ::v-deep .van-button--large {
    height: 44px;
    line-height: 44px;
  }
}
/* button: */
button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 0 10px;
    color: white;
    text-shadow: 2px 2px rgb(116, 116, 116);
    text-transform: uppercase;
    cursor: pointer;
    border: solid 2px black;
    letter-spacing: 1px;
    font-weight: 600;
    font-size: 17px;
    background-color: hsl(49deg 98% 60%);
    border-radius: 50px;
    position: relative;
    overflow: hidden;
    transition: all 0.5s ease;
  }

  button:active {
    transform: scale(0.9);
    transition: all 100ms ease;
  }

  button svg {
    transition: all 0.5s ease;
    z-index: 2;
  }

  .play {
    transition: all 0.5s ease;
    transition-delay: 300ms;
  }

  button:hover svg {
    transform: scale(3) translate(50%);
  }

  .now {
    position: absolute;
    left: 0;
    transform: translateX(-100%);
    transition: all 0.5s ease;
    z-index: 2;
  }

  button:hover .now {
    transform: translateX(10px);
    transition-delay: 300ms;
  }

  button:hover .play {
    transform: translateX(200%);
    transition-delay: 300ms;
  }
// 创建订单：
.form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-width: 350px;
    padding: 20px;
    border-radius: 20px;
    position: relative;
    background-color: #1a1a1a;
    color: #fff;
    border: 1px solid #333;
  }

  .title {
    font-size: 28px;
    font-weight: 600;
    letter-spacing: -1px;
    position: relative;
    display: flex;
    align-items: center;
    padding-left: 30px;
    color:  hsl(49deg 98% 60%);
  }

  .title::before {
    width: 18px;
    height: 18px;
  }

  .title::after {
    width: 18px;
    height: 18px;
    animation: pulse 1s linear infinite;
  }

  .title::before,
  .title::after {
    position: absolute;
    content: "";
    height: 16px;
    width: 16px;
    border-radius: 50%;
    left: 0px;
    background-color: hsl(49deg 98% 60%);
  }

  .message, 
  .signin {
    font-size: 14.5px;
    color: rgba(255, 255, 255, 0.7);
  }

  .signin {
    text-align: center;
  }

  .signin a:hover {
    text-decoration:  hsl(49, 91%, 47%);
  }

  .signin a {
    color:  hsl(49deg 98% 60%);
  }

  .flex {
    display: flex;
    width: 100%;
    gap: 6px;
  }

  .form label {
    position: relative;
  }

  .form label .input {
    background-color: #333;
    color: #fff;
    width: 100%;
    padding: 20px 05px 05px 10px;
    outline: 0;
    border: 1px solid rgba(105, 105, 105, 0.397);
    border-radius: 10px;
  }

  .form label .input + span {
    color: rgba(255, 255, 255, 0.5);
    position: absolute;
    left: 10px;
    top: 0px;
    font-size: 0.9em;
    cursor: text;
    transition: 0.3s ease;
  }

  .form label .input:placeholder-shown + span {
    top: 12.5px;
    font-size: 0.9em;
  }

  .form label .input:focus + span,
  .form label .input:valid + span {
    color: hsl(49deg 98% 60%);
    top: 0px;
    font-size: 0.7em;
    font-weight: 600;
  }

  .input {
    font-size: medium;
  }

  .submit {
    border: none;
    outline: none;
    padding: 10px;
    border-radius: 10px;
    color: #fff;
    font-size: 16px;
    transform: .3s ease;
    background-color: hsl(49deg 98% 60%);
  }

  .submit:hover {
    background-color:  hsl(49deg 98% 60%);
  }

  @keyframes pulse {
    from {
      transform: scale(0.9);
      opacity: 1;
    }

    to {
      transform: scale(1.8);
      opacity: 0;
    }
  }
  .create-order{
    z-index: 1;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
