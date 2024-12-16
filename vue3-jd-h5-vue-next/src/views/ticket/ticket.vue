<template>
  <div class="coupon-container">
    <!-- 顶部策略标题 -->
    <div class="strategy-title">
      <span class="btn-left" @click="$router.go(-1)">
        <svg-icon icon-class="white-btn"></svg-icon>
      </span>
      <h2>STRATEGY</h2>
      <p>先领券再购物 立享折上折</p>
      <span>津贴可以使用积分兑换/详情页/会场等方式领取</span>
    </div>

    <!-- 优惠券区域 -->
    <div class="coupons">
      <div v-for="(coupon, index) in coupons" :key="index" class="coupon-item">
        <!-- 实际满减 -->
        <div class="discount-circle">
          <p class="actual-discount">{{ coupon.discount }}</p>
          <p class="threshold">{{coupon.info}}</p>
        </div>

        <!-- 优惠券详细:哪个类别 过期时间 -->
        <div class="coupon-details">
          <div class="store-coupon">
            <p class="value">{{ coupon.kind }}券</p>
            <p class="desc">{{ coupon.due_time }}过期</p>
            <button @click="useCoupon(index)" class="btn click-btn">CLICK ON ></button>
          </div>
          <!-- 库存 -->
          <div class="platform-coupon">
            <p class="value">库存{{ coupon.storage }}</p>
            <p class="desc">开始时间{{ coupon.create_time }}</p>
            <button @click="useCoupon(index)" class="btn use-btn">拿立即使用</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive,onMounted,ref } from "vue";
import axios from "axios";
import AxiosPlugin, { httpInstance } from '@/plugins/axios'
// 定义优惠券数据

const coupons = ref([
  {
    id:1,
    discount: 150,
    
    kind: "电脑",
    storage: 100,
    info: "满1000减50",
    create_time: "2023-12-25",
    due_time: "2023-12-31",
    
  },
  {
    id:2,
    discount: 450,

    kind: "电脑",
    storage: 100,
    info: "满1000减50",
    create_time: "2023-12-25",
    due_time: "2023-12-31",
   
  },
  {
    id:3,
    discount: 800,
    kind: "电脑",
    storage: 100,
    info: "满1000减50",
    create_time: "2023-12-25",
    due_time: "2023-12-31",
    
  },
  {
    id:4,
    discount: 1200,
    
    kind: "电脑",
    storage: 100,
    info: "满1000减50",
    create_time: "2023-12-25",
    due_time: "2023-12-31",
    
  },
]);

const kinds = ref({
   1:'电脑',
   2:'手机',
   3:'女装',
   4:'食品',
   5:'宠物',
   6:'美妆',
   7:'鲜花',
   8:'图书'
});

 onMounted (async () => {
  
  try {
    console.log("res")
    const response = await httpInstance.post("http://127.0.0.1:8889/get_ticket");
    console.log(response);
    if (response.data.status === 'success') {
      coupons.value = response.data.data.map(ticket => ({
        id: ticket.ticket_ID,
        discount: ticket.discount,
        kind: kinds.value[ticket.kind],
        storage: ticket.store,
        info: ticket.info,
        create_time: ticket.create_time,
        due_time: ticket.due_time
      }));
console.log(coupons)
    } else {
      errorMessage.value = response.data.message || "获取优惠券失败";
    }
  } catch (e) {
    console.log("没有优惠券");
  }
});

const useCoupon=async(index)=>{
  console.log("jj"+index)//这个是第几个：
  try {
    const userId = localStorage.getItem('userId');
    console.log("id"+coupons.value[index].id);
    const res = await httpInstance.post('http://127.0.0.1:8889/addticket', {
      coupon_id: coupons.value[index].id,
      user_id: userId,
    },{headers: {
    'Content-Type': 'application/json'
  }});
console.log(res);
    if (res.data.status === 200) {
      alert('领取成功');
      //列表更新库存：
      //coupons.value[index].storage -= 1; // 减少库存
      coupons.value.splice(index, 1); // 从列表中删除已领取的优惠券
    } else {
      alert(res.data.message || '领取失败');
    }
 } catch (e) {
   alert('领取失败');
 }


  //库存不足，失败：alert('库存不足')
}
</script>

<style scoped>
/* 背景与容器样式 */
.coupon-container {
  background: linear-gradient(to bottom, #e6c0e8, #6b217e);
  /* padding: 40px 20px; */
  min-height: 100vh; /* 让背景覆盖视口 */
  text-align: center;
  color: #fff;
  font-family: Arial, sans-serif;
}

/* 策略标题样式 */
.strategy-title h2 {
  color: #e65ba5;
  font-size: 28px;
  margin-bottom: 10px;
}

.strategy-title p {
  font-size: 18px;
  font-weight: bold;
}

.strategy-title span {
  font-size: 14px;
}

/* 优惠券布局 */
.coupons {
  display: flex;
  justify-content: space-around;
  margin-top: 40px;
}

.coupon-item {
  background: #fff;
  color: #333;
  border-radius: 10px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  width: 220px;
  padding: 20px 10px;
  text-align: center;
}

/* 圆形满减样式 */
.discount-circle {
  background: #6b217e;
  color: #fff;
  border-radius: 50%;
  width: 100px;
  height: 100px;
  margin: 0 auto 15px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.actual-discount {
  font-size: 24px;
  font-weight: bold;
}

.threshold {
  font-size: 12px;
}

/* 优惠券详情样式 */
.coupon-details {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.store-coupon,
.platform-coupon {
  background: #f5f5f5;
  border-radius: 5px;
  padding: 10px 0;
}

.value {
  font-size: 22px;
  font-weight: bold;
  color: #e65ba5;
}

.desc {
  font-size: 12px;
  margin: 5px 0;
}

/* 按钮样式 */
.btn {
  border: none;
  color: #fff;
  font-size: 12px;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 15px;
}

.click-btn {
  background: #e65ba5;
}

.use-btn {
  background: #6b217e;
}
.btn-left{
  position: absolute;
  left: 20px;
  top:20px
}
</style>
