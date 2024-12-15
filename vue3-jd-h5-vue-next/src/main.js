/*
 * @version: v 1.0.0
 * @Github: https://github.com/GitHubGanKai
 * @Author: GitHubGanKai
 * @Date: 2020-12-27 20:10:38
 * @LastEditors: gankai
 * @LastEditTime: 2021-01-02 13:39:04
 * @FilePath: /refactor-with-vue3/src/main.js
 */
import { createApp } from 'vue';
import Vant from 'vant';
import 'lib-flexible/flexible';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from '@/plugins/axios';
import icons from '@/icons'; // icon
import components from '@/components'; // components
import 'vant/lib/index.css'; // 全局引入样式
import './mock/mock';
import eventBus from './utils/eventBus';
import { registerPlugins } from './utils/util';

const plugins = [Vant, store, router, axios,icons, components, eventBus]; // 移除 axios
const app = createApp(App);

// 直接提供 axios 实例
app.provide('axios', axios);

// 只注册 Vue 插件
app.use(registerPlugins(plugins));

app.mount('#app');
