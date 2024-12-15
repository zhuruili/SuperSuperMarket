<template>
    <div class="classify-container">
        <div class="categories">
            <ul>
                <li v-for="(category, index) in categories" :key="index" @click="selectCategory(index)" :class="{ active: selectedCategory === index }">
                    {{ category.name }}
                </li>
            </ul>
        </div>
        <div class="products">
            <ul>
                <li v-for="product in products" :key="product.id">
                    <img :src="product.image" alt="product.name" />
                    <p>{{ product.name }}</p>
                    <p>{{ product.price }}</p>
                </li>
            </ul>
        </div>
    </div>
    <tabbar></tabbar>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const categories = ref([
    { name: 'Category 1' },
    { name: 'Category 2' },
    { name: 'Category 3' },
    { name: 'Category 4' },
    { name: 'Category 5' },
    { name: 'Category 6' },
    { name: 'Category 7' },
    { name: 'Category 8' }
]);

const selectedCategory = ref(0);
const products = ref([]);

const fetchProducts = async (categoryIndex) => {
    try {
        const response = await axios.get(`/api/products?category=${categories.value[categoryIndex].name}`);
        products.value = response.data;
    } catch (error) {
        console.error('Error fetching products:', error);
    }
};

const selectCategory = (index) => {
    selectedCategory.value = index;
    fetchProducts(index);
};

onMounted(() => {
    fetchProducts(selectedCategory.value);
});
</script>

<style scoped>
.classify-container {
    display: flex;
}

.categories {
    width: 20%;
    background-color: #f5f5f5;
    padding: 10px;
}

.categories ul {
    list-style: none;
    padding: 0;
}

.categories li {
    padding: 10px;
    cursor: pointer;
}

.categories li.active {
    background-color: #007bff;
    color: white;
}

.products {
    width: 80%;
    padding: 10px;
}

.products ul {
    list-style: none;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
}

.products li {
    width: 45%;
    margin: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    text-align: center;
}

.products img {
    max-width: 100%;
    height: auto;
}
</style>