<!--
 * @version: v 1.0.0
 * @Github: https://github.com/GitHubGanKai
 * @Author: GitHubGanKai
 * @Date: 2020-12-27 20:41:48
 * @LastEditors: gankai
 * @LastEditTime: 2021-01-02 20:29:34
 * @FilePath: /refactor-with-vue3/src/views/home/index.vue
-->
<template>
  <div class="home">
    <header class="home-header" :class="{ active: headerActive }">
      <div class="header-search">
        <svg-icon class="search-icon" icon-class="search"></svg-icon>
        <router-link tag="span" class="search-title" to="./search"
          >推荐搜索 关键词</router-link
        >
      </div>
      <svg-icon
        class="customer-service-icon"
        icon-class="customer-service"
      ></svg-icon>
    </header>
    <van-swipe
      class="swiper-carousel"
      lazy-render
      :autoplay="3000"
      :show-indicators="false"
    >
      <van-swipe-item v-for="(image, index) in homeImgs" :key="index">
        <img class="lazy_img" @click="handleClick" :src="require('@/assets/image/autoChange/首页轮播1.png')" />
      </van-swipe-item>
    </van-swipe>

    <section class="home-tags">
      <ul class="tags-content">
        <router-link tag="li" class="tags-item" to="./search">
          <svg-icon
            class="tags-icon"
            icon-class="chain-cat-boutique"
          ></svg-icon>
          <span class="item-text">链猫精品</span>
        </router-link>
        <router-link tag="li" class="tags-item" to="./search">
          <svg-icon class="tags-icon" icon-class="cm-area"></svg-icon>
          <span class="item-text">CM专区</span>
        </router-link>
        <router-link tag="li" class="tags-item" to="./search">
          <svg-icon class="tags-icon" icon-class="collar-cm"></svg-icon>
          <span class="item-text">领CM币</span>
        </router-link>
        <router-link tag="li" class="tags-item" to="./ticket">
          <svg-icon class="tags-icon" icon-class="coupon-svg"></svg-icon>
          <span class="item-text">领券</span>
        </router-link>
        <router-link tag="li" class="tags-item" to="./search">
          <svg-icon class="tags-icon" icon-class="chain-cat-member"></svg-icon>
          <span class="item-text">链猫会员</span>
        </router-link>
      </ul>
    </section>
 

    <!-- <section class="spike-area">
      <ul class="spike-top">
        <router-link class="top-left" to="/chainCatSpike" tag="li">
          <div class="item-top">
            <span class="item-title">链猫秒杀</span>
            <div class="time-text">
              <span class="eight-time">8点场</span>
              <van-count-down :time="timeData" class="time-count-down">
                <template v-slot="timeData">
                  <span class="time-item" v-if="timeData.hours < 10">{{
                    "0" + timeData.hours
                  }}</span>
                  <span class="time-item" v-else>{{ timeData.hours }}</span>
                  <i class="tow-point">:</i>
                  <span class="time-item" v-if="timeData.minutes < 10">{{
                    "0" + timeData.minutes
                  }}</span>
                  <span class="time-item" v-else>{{ timeData.minutes }}</span>
                  <i class="tow-point">:</i>
                  <span class="time-item" v-if="timeData.seconds < 10">{{
                    "0" + timeData.seconds
                  }}</span>
                  <span class="time-item" v-else>{{ timeData.seconds }}</span>
                </template>
              </van-count-down>
            </div>
          </div>
          <div class="item-info">
            <div class="item-content">
              <img src="../../assets/image/home/demo1.png" />
              <span class="new-price">¥298</span>
              <span class="old-price">¥399</span>
            </div>
            <div class="item-content">
              <img src="../../assets/image/home/demo2.png" />
              <span class="new-price">¥298</span>
              <span class="old-price">¥399</span>
            </div>
            <div class="item-content">
              <img src="../../assets/image/home/demo3.png" />
              <span class="new-price">¥298</span>
              <span class="old-price">¥399</span>
            </div>
          </div>
        </router-link>
        <router-link class="top-right" to="/foundGoodGoods" tag="li">
          <div class="right-header">
            <span class="cat-spike-text">发现好货</span>
            <span class="tag-text">品质好物</span>
          </div>
          <span class="good-item">好物不贵</span>
          <div class="item-imgs">
            <img src="../../assets/image/home/demo4.png" />
            <img src="../../assets/image/home/demo5.png" />
          </div>
        </router-link>
      </ul>

      <ul class="spike-center">
        <router-link class="center-item" to="/specialSpike" tag="li">
          <span class="center-title">特价秒杀</span>
          <span class="center-descr">10元抢购</span>
          <img src="../../assets/image/home/demo6.png" />
        </router-link>
        <router-link class="center-item" to="/brandSpike" tag="li">
          <span class="center-title">品牌秒杀</span>
          <span class="center-descr" style="color: #dd3749">笔记本秒杀</span>
          <img src="../../assets/image/home/demo7.png" />
        </router-link>
        <router-link class="center-item" to="/newProductLaunch" tag="li">
          <span class="center-title">新品首发</span>
          <span class="center-descr" style="#FC6380">小黑盒新品</span>
          <img src="../../assets/image/home/demo8.png" />
        </router-link>
        <router-link class="center-item" to="/premiumRanking" tag="li">
          <span class="center-title">优品排行</span>
          <span class="center-descr" style="color: #91c95b">榜上好物购</span>
          <img src="../../assets/image/home/demo9.png" />
        </router-link>
      </ul>
      <ul class="spike-bottom">
        <li class="bottom-left">
          <div class="bottom-left-header">
            <span class="big-buy">大牌购走</span>
            <span class="goods-name">
              戴尔
              <svg-icon icon-class="right-arrow"></svg-icon>
            </span>
          </div>
          <span class="belive-big">信赖大品牌</span>
          <div class="bottom-images">
            <img src="../../assets/image/home/demo10.png" />
            <img src="../../assets/image/home/demo11.png" />
          </div>
        </li>
        <router-link class="bottom-left" to="/loveShop" tag="li">
          <div class="bottom-left-header">
            <span class="big-buy">爱逛好店</span>
            <span class="goods-name addColor">懂你所要</span>
          </div>
          <span class="belive-big">来逛个够</span>
          <div class="bottom-images">
            <img src="../../assets/image/home/demo12.png" />
            <img src="../../assets/image/home/demo13.png" />
          </div>
        </router-link>
      </ul>
    </section> -->
      <div class="product-list">
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

    <tabbar></tabbar>
  </div>
</template>

<script>
import { ref, reactive, onMounted, toRefs, getCurrentInstance } from "vue";
import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";
import Tabbat from "@/components/tabbar";
import axios from 'axios'

export default {
  name: "home",
  components: {
    Tabbat
  },
  setup(props, context) {
    const { ctx } = getCurrentInstance();
    const $store = useStore();
    // ctx.$store === $store  ==>true 其实是同一个对象！

    const $router = useRouter();
    const $route = useRoute(); // 可以拿到所有和路由相关的参数
    const active = ref("");
    const timeData = ref(36000000);
    const headerActive = ref(false);
    const products = ref([]);

    const state = reactive({
      homeImgs: [],
      tabArray: []
    });

    const ball = reactive({
      show: false,
      el: ""
    });

    const refreshHome = async () => {
      axios.post('http://127.0.0.1:5678/', {}).then(res => {
        console.log(res.data.length)
        // 刷新商品列表
        products.value = [];

        for (let i = 0; i < res.data.length; i++) {
            products.value.push({ id: res.data[i]['item_ID'], title: res.data[i]['title'], pic_url: res.data[i]['pic_url'], price: res.data[i]['price'], sale: res.data[i]['sale'], shop_name: res.data[i]['shop_name'], storage: res.data[i]['store'], kind: res.data[i]['kind'], url: res.data[i]['url'] })
        }
      })
    };

    ctx.$http.get("http://test.happymmall.com/home/homeData").then(res => {
      const { images, tabList } = res.data;
      state.tabArray = tabList;
      state.homeImgs = images;
    });

    onMounted(() => {
      ctx.$eventBus.$emit("changeTag", 0);
      window.addEventListener("scroll", pageScroll);
      refreshHome();
    });

    const addToCart = (event, tag) => {
      $store.commit("cart/addToCart", tag);
      ball.show = true;
      ball.el = event.target;
    };

    const beforeEnter = el => {
      const dom = ball.el;
      const rect = dom.getBoundingClientRect();
      const x = rect.left - window.innerWidth * 0.6;
      const y = -(window.innerHeight - rect.top);
      el.style.display = "block";
      el.style.transform = `translate3d(0,${y}px,0)`;
      const inner = el.querySelector(".inner");
      inner.style.transform = `translate3d(${x}px,0,0)`;
    };

    const enter = (el, done) => {
      document.body.offsetHeight;
      el.style.transform = "translate3d(0,0,0)";
      const inner = el.querySelector(".inner");
      inner.style.transform = "translate3d(0,0,0)";
      el.addEventListener("transitionend", done);
    };

    const afterEnter = el => {
      ball.show = false;
      el.style.display = "none";
    };

    const handleClick = linkUrl => {
      $router.push("/classify/product");
    };

    const pageScroll = () => {
      const scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      scrollTop > 100
        ? (headerActive.value = true)
        : (headerActive.value = false);
    };

    return {
      active,
      timeData,
      headerActive,
      ...toRefs(ball),
      ...toRefs(state),
      addToCart,
      beforeEnter,
      enter,
      afterEnter,
      handleClick,
      pageScroll,
      refreshHome,
      products
    };
  }
};
</script>

<style scoped>
.show-results {
  padding: 20px;
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
