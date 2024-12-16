<template>
  <div class="shopping-cart">
    <h1>购物车</h1>
    <div class="cart-item" v-for="(item, index) in cartItems" :key="index">
      <div class="item-header">
        <input
          type="checkbox"
          v-model="item.selected"
          @change="updateTotal"
        />
        <span style="font-size: 20px;">{{ '店铺名称：' + item.storeName }}</span>
      </div>

      <div class="item-body">
        <img :src="item.productImage" alt="商品图片" class="item-image" />
        <div class="item-details">
          <h3 v-html="item.productName"></h3>
          <div class="item-quantity">
            <button @click="decreaseQuantity(index)">-</button>
            <span style="font-size: 20px;">{{ item.quantity }}</span>
            <button @click="increaseQuantity(index)">+</button>
          </div>
          <p class="item-price">单价：￥{{ item.Price }}</p>
        </div>
      </div>
    </div>

    <div class="cart-footer">
      <div class="footer-actions">

      </div>
      <div class="footer-summary">
        <button @click="checkout">结算</button>
      </div>
    </div>
  </div>
  <tabbar></tabbar>
</template>

<script setup>
import { ref, computed, onMounted, toRaw } from "vue";
import axios from 'axios';

const cartItems = ref([]);

const allSelected = computed({
  get: () => cartItems.value.every((item) => item.selected),
  set: (value) => {
    cartItems.value.forEach((item) => (item.selected = value));
  },
});

const totalPrice = computed(() => {
  return cartItems.value
    .filter((item) => item.selected)
    .reduce((sum, item) => sum + item.price * item.quantity, 0);
});

const increaseQuantity = (index) => {
  cartItems.value[index].quantity++;
  updateTotal();
};

const decreaseQuantity = (index) => {
  if (cartItems.value[index].quantity > 1) {
    cartItems.value[index].quantity--;
    updateTotal();
  }
};

const toggleAllSelection = () => {
  allSelected.value = !allSelected.value;
};

const removeSelected = () => {
  cartItems.value = cartItems.value.filter((item) => !item.selected);
};

const checkout = () => {
  const user_name = localStorage.getItem('username')
  console.log(cartItems)
  const items = toRaw(cartItems.value).map(item => ({
    item_id: item.item_id,
    item_num: item.quantity
  }));
  console.log(items)
  axios.post('http://127.0.0.1:5678/Cart/checkout', { user_name: user_name, items: items }).then((res) => {
      alert('结算成功')
    })
};

const updateTotal = () => {
    totalPrice.value;
  console.log(totalPrice.value);
};

const refresh = () => {
    const user_name = localStorage.getItem('username')
    axios.post('http://127.0.0.1:5678/getCart', { user_name:user_name }).then((res) => {
        const data = res.data.data
        // console.log(data)
        const temp = []
        cartItems.value = data.map(item => {
        return {
          id: item.cart_id,
            item_id: item.item_id,
            storeName: item.shop_name,
            orderNumber: item.cart_id,
            productImage: item.pic_url,
            productName: item.title,
            productPrice: item.price,
            // specifications: item.specifications,
            quantity: item.count,
            Price: item.price,
            status: item.state,
            selected: false,
        }
        })
    })
};



onMounted(() => {
  refresh();
});
</script>

<style scoped>
.shopping-cart {
  width: 80%;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  color: #333;
  padding-bottom: 100px; /* 为了给固定的底部结算部分留出空间 */
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.cart-item {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 15px;
  margin-bottom: 15px;
  background: #f9f9f9;
}

.item-header {
  display: flex;
  align-items: left;
  margin-bottom: 10px;
}

.item-header input {
  margin-right: 10px;
}

.item-body {
  display: flex;
  align-items: center;
}

.item-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin-right: 15px;
}

.item-details {
  flex: 1;
}

.item-quantity {
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.item-quantity button {
  width: 30px;
  height: 30px;
  border: none;
  background: #c9d2dc;
  color: white;
  border-radius: 3px;
  cursor: pointer;
}

.item-quantity span {
  margin: 0 10px;
}

.item-price {
  font-size: 16px;
  font-weight: bold;
  color: #e74c3c;
}

.cart-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  background: #f1f1f1;
  border-top: 1px solid #ddd;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

.footer-actions {
  display: flex;
  align-items: center;
}

.footer-actions input {
  margin-right: 5px;
}

.footer-summary p {
  font-size: 18px;
  font-weight: bold;
}

.footer-summary button {
  padding: 10px 20px;
  border: none;
  margin-bottom: 50px;
  background: #ff0000;
  color: white;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}
</style>