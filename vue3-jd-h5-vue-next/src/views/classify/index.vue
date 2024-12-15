<template>
  <div class="classify">
    <header class="home-header">商品分类</header>
    <section class="search-wrap" ref="searchWrap">
      <list-scroll class="nav-side-wrapper">
        <ul class="nav-side">
          <li
            v-for="(item, index) in categories"
            :key="index"
            :class="{ active: currentIndex === index }"
            @click="selectMenu(index)"
          >
            <span>{{ item.slice(0, 2) }}</span>
            <span>{{ item.slice(2) }}</span>
          </li>
        </ul>
      </list-scroll>
      <div class="search-content">
        <div class="products">
          <ul>
            <li v-for="product in products" :key="product.id" class="product-item">
              <img :src="product.pic_url" :alt="product.title" class="item-img" />
              <p class="product-title" v-html="product.title"></p>
              <p class="price">{{ '￥' + product.price }}</p>
              <p class="sale">{{ product.sale + ' ' + product.shop_name }}</p>
              <button @click="purchase(product)">立即购买</button>
              <button @click="addToCart(product)">加入购物车</button>
            </li>
          </ul>
        </div>
      </div>
    </section>
    <tabbar></tabbar>
  </div>
</template>

<script setup>
import ListScroll from "@/components/scroll/ListScroll";
import { ref, reactive, onMounted, getCurrentInstance } from "vue";
import { useRouter } from "vue-router";
import axios from 'axios';

const { ctx } = getCurrentInstance();
const $router = useRouter();

const searchWrap = ref(null);

const categories = [
  '电脑',
  '手机',
  '女装',
  '食品',
  '宠物',
  '美妆',
  '鲜花',
  '图书'
];

const state = reactive({
  currentIndex: 0
});

const products = ref([]);

const selectMenu = index => {
  state.currentIndex = index;
  // 根据选择的分类加载产品
  loadProducts(categories[index]);
};

const purchase = product => {
  console.log('purchase:', product);
  const user_name = localStorage.getItem('username')
  axios.post('http://127.0.0.1:5678/purchase', { user_name:user_name, item_id:product.item_ID
,  state:'0',  price:product.price,  count:'1' }).then((res) => {
      console.log(res.data)
      alert('购买成功')
  })
};

const addToCart = product => {
  console.log('addToCart:', product);
};

const loadProducts = async (category) => {
  try {
    const res = await axios.post('http://127.0.0.1:5678/category', {
      category: category
    });
    products.value = res.data;
    console.log('products:', res);
  } catch (error) {
    console.error('Error loading products:', error);
  }
};

const setSearchWrapHeight = () => {
  const { clientHeight } = document.documentElement;
  searchWrap.value.style.height = clientHeight - 100 + "px";
};

const selectProduct = sku => {
  $router.push({ path: "/classify/recommend", query: { sku } });
};

onMounted(async () => {
  setSearchWrapHeight();
  ctx.$eventBus.$emit("changeTag", 1);
  // 初始加载第一个分类的产品
  loadProducts(categories[0]);
});
</script>

<style scoped>
.classify {
  height: 100%;
  .home-header {
    font-size: 18px;
    color: #3a3a3a;
    font-weight: 600;
    text-align: center;
    line-height: 50px;
    background-color: #fff;
  }
  .search-wrap {
    display: flex;
    width: 100%;
    background: #fff;
    .nav-side-wrapper {
      width: 88px;
      height: 100vh; /* 固定高度 */
      position: sticky; /* 固定位置 */
      top: 0; /* 从顶部开始 */
      overflow-y: auto; /* 允许滚动 */
      .nav-side {
        width: 100%;
        background: #f8f8f8;
        li {
          width: 100%;
          height: 77px;
          text-align: center;
          font-weight: 600;
          font-size: 14px;
          display: flex;
          justify-content: center;
          align-items: center;
          color: #949497;
          flex-direction: column;
          cursor: pointer;
          &.active {
            color: #d8182d;
            border-left: 3px solid transparent;
            border-color: #d8182d;
            background: #fff;
          }
        }
      }
    }
    .search-content {
      width: calc(100% - 88px);
      height: 100vh; /* 固定高度 */
      overflow-y: auto; /* 允许滚动 */
      padding: 0 16px;
      background: #fff;
      padding-bottom: 30px;
      .products {
        ul {
          list-style: none;
          padding: 0;
          display: flex;
          flex-wrap: wrap;
          .product-item {
            width: calc(33.33% - 10px);
            margin-bottom: 20px;
            text-align: center;
            font-size: 14px;
            .item-img {
              width: 100px;
              height: 100px;
            }
            .product-title {
              color: #3a3a3a;
              font-size: 14px;
              font-weight: 600;
              margin: 5px 0;
            }
            .price {
              font-size: 16px;
              color: #ff5000;
            }
            .sale {
              font-size: 12px;
              color: #999;
            }
            .shop-name {
              font-size: 12px;
              color: #666;
            }
            button {
              background-color: #d8182d;
              color: #fff;
              border: none;
              padding: 5px 10px;
              cursor: pointer;
              border-radius: 3px;
              margin-top: 5px;
              transition: background-color 0.3s;
              &:hover {
                background-color: #b7151a;
              }
            }
          }
        }
      }
    }
  }
}
</style>