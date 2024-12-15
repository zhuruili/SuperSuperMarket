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
                <div class="product-image-container">
                    <img :src="product.pic_url" :alt="product.title" />
                    <div class="product-buttons">
                        <button @click="addToCart(product)">加入购物车</button>
                        <button @click="viewDetails(product)">查看详情</button>
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
};

const viewDetails = (product) => {
  // 实现查看详情逻辑
    console.log('查看详情', product);
};
</script>

<style scoped>
.search-page {
  padding: 20px;
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
</style>