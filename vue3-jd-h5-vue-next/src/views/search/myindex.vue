<template>
    <div class="search-page">
        <header class="search-header">
            <button @click="goBack">返回</button>
            <div class="search-bar">
                <select v-model="selectedCategory">
                    <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
                </select>
                <input v-model="searchQuery" placeholder="搜索商品" />
                <button @click="search">搜索</button>
            </div>
        </header>
        <main class="search-results">
            <div v-if="products.length === 0">暂无商品</div>
            <div v-else class="product-list">
                <div v-for="product in products" :key="product.id" class="product-item">
                    <img :src="product.image" :alt="product.name" />
                    <div class="product-info">
                        <h3>{{ product.name }}</h3>
                        <p>{{ product.price }}</p>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const categories = ref(['电子产品', '服装', '食品', '家居', '美妆', '运动', '图书', '其他']);
const selectedCategory = ref(categories.value[0]);
const searchQuery = ref('');
const products = ref([]);

const goBack = () => {
    // 实现返回逻辑
    console.log('返回');
};

const search = () => {
    // 实现搜索逻辑
    console.log('搜索', selectedCategory.value, searchQuery.value);
    axios.post('http://127.0.0.1:5678/search', { query: searchQuery.value }).then((res) => {
    console.log(res)
    })
    // 模拟搜索结果
    products.value = [
        { id: 1, name: '研商10.4寸12寸15寸工控一体机嵌入式全封闭纯平面电容触摸显示屏车间', price: '¥100', image: 'http://g.search3.alicdn.com/img/i3/4388775026/O1CN017OECTQ1mzxcnZuGqW_!!0-saturn_solar.jpg' },
        { id: 2, name: '【浙江国补20%】华硕天选5 Pro 14代酷睿i9 16英寸游戏笔记本', price: '¥200', image: 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/2214117264228/O1CN01abCE341h6TaKWXkq7_!!2214117264228-2-scmitem6000.png' },
    ];
};
</script>

<style scoped>
.search-page {
    padding: 20px;
}

.search-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.search-bar {
    display: flex;
    align-items: center;
}

.search-bar select,
.search-bar input {
    margin-right: 10px;
}

.search-results {
    margin-top: 20px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
}

.product-item {
    width: 48%;
    margin: 1%;
    border: 1px solid #ccc;
    padding: 10px;
    box-sizing: border-box;
}

.product-item img {
    width: 100%;
    height: auto;
}

.product-info {
    text-align: center;
}
</style>