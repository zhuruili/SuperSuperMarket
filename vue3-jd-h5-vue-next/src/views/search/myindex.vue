<template>
    <div class="search-page">
      <header class="search-header">
        <span class="btn-left" @click="$router.go(-1)">
            <svg-icon icon-class="white-btn"></svg-icon>
        </span>
        <div class="search-bar">
            <select v-model="selectedCategory">
                <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
            </select>
            <input v-model="searchQuery" placeholder="搜索商品" />
            <button @click="search">搜索</button>
        </div>
    </header>
        <main class="search-results">
            <div v-if="products.length === 0" class="no-products">暂无商品</div>
            <div v-else class="product-list">
                <div v-for="product in products" :key="product.id" class="product-item">
                <div class="product-image-container">
                    <img :src="product.pic_url" :alt="product.title" />
                    <div class="product-buttons">
                        <button @click="purchase(product)">立即购买</button>
                        <button @click="addToCart(product)">加入购物车</button>
                    </div>
                </div>
                <div class="product-info">
                    <p v-html="product.title"></p>
                    <div class="price-sale">
                    <p class="price">{{ '￥' + product.price }}</p>
                    <p class="sale">{{ product.sale }}</p>
                    </div>
                    <p class="shop-name">{{ product.shop_name }}</p>
                </div>
                </div>
            </div>
        </main>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const categories = ref(['电脑', '手机', '女装', '食品', '宠物', '美妆', '鲜花', '图书']);
const selectedCategory = ref(categories.value[0]);
const searchQuery = ref('');
const products = ref([]);
const router = useRouter();

const goBack = () => {
    router.push('/');
};

const search = () => {
    // 实现搜索逻辑
    console.log('搜索', selectedCategory.value, searchQuery.value);
    // 刷新商品列表
    products.value = [];

    axios.post('http://127.0.0.1:5678/search', { category: selectedCategory.value, query: searchQuery.value }).then((res) => {
        console.log(res.data.data)
        for (let i = 0; i < res.data.data.length; i++) {
            products.value.push({ id: res.data.data[i][0], title: res.data.data[i][1], pic_url: res.data.data[i][2], price: res.data.data[i][3], sale: res.data.data[i][4], shop_name: res.data.data[i][5], storage: res.data.data[i][6], kind: res.data.data[i][7], url: res.data.data[i][8] })
        }
    })
};

const addToCart = (product) => {
  // 实现加入购物车逻辑
    console.log('加入购物车', product);
    const user_name = localStorage.getItem('username')
    axios.post('http://127.0.0.1:5678/addToCart', { user_name:user_name, item_id:product.id, count:'1' }).then((res) => {
        console.log(res.data)
        alert('加入购物车成功')
    })
};

const purchase = (product) => {
  // 实现立即购买逻辑
    console.log('立即购买', product);
    const user_name = localStorage.getItem('username')
    axios.post('http://127.0.0.1:5678/purchase', { user_name:user_name, item_id:product.id,  state:'0',  price:product.price,  count:'1' }).then((res) => {
        console.log(res.data)
        alert('购买成功')
    })
};
</script>

<style scoped>
.search-page {
  padding: 20px;
}
/* "暂无商品" 提示样式 */
.search-results .no-products {
  width: 100%;
  text-align: center;
  font-size: 24px; /* 增加字体大小 */
  color: #ff5000;  /* 使用醒目的橙色 */
  font-weight: bold;
  padding: 50px 0; /* 增加上下内边距 */
  background: linear-gradient(45deg, rgba(255, 80, 0, 0.8), rgba(255, 123, 50, 0.8)); /* 渐变背景 */
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* 轻微阴影提升层次感 */
  animation: fadeIn 0.5s ease-in-out; /* 添加渐变效果 */
}

/* 渐变动画效果 */
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.search-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.search-bar {
  display: flex;
  align-items: center;
}

.search-bar select,
.search-bar input {
  margin-right: 10px;
  padding: 5px;
}

.search-results {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.product-item {
  width: calc(16.66% - 10px); /* 每行放置六个商品 */
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  position: relative;
}

.product-item:hover {
  transform: translateY(-5px);
}

.product-image-container {
  position: relative;
}

.product-item img {
  width: 100%;
  height: auto;
}

.product-buttons {
  display: none;
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.7);
  padding: 10px;
  border-radius: 5px;
}

.product-item:hover .product-buttons {
  display: flex;
  gap: 10px;
}

.product-buttons button {
  background-color: #fff;
  color: #333;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 3px;
  transition: background-color 0.3s;
}

.product-buttons button:hover {
  background-color: #ddd;
}

.product-info {
  padding: 10px;
  text-align: center;
}

.product-info p {
  margin: 5px 0;
}

.product-info .price-sale {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.product-info .price {
  font-size: 15px;
  color: #ff5000;
}

.product-info .sale {
  font-size: 12px;
  color: #999;
}

.product-info .shop-name {
  font-size: 10px;
  color: #666;
  text-align: left;
}
/* 页面整体样式 */
.search-page {
  padding: 20px;
  background-color: #f4f4f4;
  font-family: 'Helvetica Neue', sans-serif;
}

/* 搜索头部 */
.search-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  background: linear-gradient(45deg, #ff5000, #ffb300); /* 炫酷渐变背景 */
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease-in-out;
}

/* 搜索框布局 */
.search-bar {
  display: flex;
  align-items: center;
  width: 100%;
}

.search-bar select,
.search-bar input {
  padding: 12px 20px;
  font-size: 16px;
  border: none;
  border-radius: 30px;
  margin-right: 20px;
  transition: 0.3s;
}

.search-bar select {
  background-color: #fff;
  color: #333;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.search-bar input {
  width: 100%;
  background-color: #fff;
  color: #333;
  border-radius: 30px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}

.search-bar select:hover,
.search-bar input:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.search-bar button {
  padding: 10px 20px;
  background-color: #ff5000;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-bar button:hover {
  background-color: #ff7f32;
}

/* 搜索结果部分 */
.search-results {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product-item {
  width: calc(16.66% - 20px);
  border: 1px solid #ddd;
  border-radius: 10px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  position: relative;
}

.product-item:hover {
  transform: translateY(-10px);
}

.product-image-container {
  position: relative;
}

.product-item img {
  width: 100%;
  height: auto;
}

.product-buttons {
  display: none;
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.7);
  padding: 10px;
  border-radius: 5px;
}

.product-item:hover .product-buttons {
  display: flex;
  gap: 10px;
}

.product-buttons button {
  background-color: #fff;
  color: #333;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 3px;
  transition: background-color 0.3s;
}

.product-buttons button:hover {
  background-color: #ddd;
}

.product-info {
  padding: 10px;
  text-align: center;
}

.product-info p {
  margin: 5px 0;
}

.product-info .price-sale {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.product-info .price {
  font-size: 18px;
  color: #ff5000;
  font-weight: bold;
}

.product-info .sale {
  font-size: 14px;
  color: #999;
}

.product-info .shop-name {
  font-size: 12px;
  color: #666;
  text-align: left;
}


/* 头部再优化 */
/* 顶部搜索栏样式 */
.search-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #f9f9f9;
}

/* 返回按钮样式 */
.btn-left {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.search-bar {
  display: flex;
  align-items: center;
  gap: 10px;  /* 增加间距，确保元素之间不挤 */
  flex: 1;  /* 让搜索框占据剩余空间 */
  max-width: 800px; /* 限制最大宽度 */
}

/* 下拉框样式 */
.search-bar select {
  padding: 8px 12px;
  border: 2px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  background-color: #fff;
  transition: border-color 0.3s ease;
}

.search-bar select:focus {
  border-color: #ff5000;  /* 聚焦时改变边框颜色 */
  outline: none;
}

/* 搜索框样式 */
.search-bar input {
  flex: 1;
  padding: 10px 15px;
  border: 2px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  transition: border-color 0.3s ease;
  width: 70%;  /* 占据更多空间 */
}

.search-bar input:focus {
  border-color: #ff5000;
  outline: none;
}

/* 搜索按钮样式 */
.search-bar button {
  background-color: #ff5000;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.search-bar button:hover {
  background-color: #ff3300;  /* 悬浮时的颜色 */
}
</style>