<template>
  <div class="coupon-container">
    <!-- 顶部策略标题 -->
    <div class="strategy-title">
      <h2>STRATEGY</h2>
      <p>先领券再购物 立享折上折</p>
      <span>天猫津贴可以使用积分兑换/详情页/会场等方式领取</span>
    </div>

    <!-- 优惠券区域 -->
    <div class="coupons">
      <div v-for="(coupon, index) in coupons" :key="index" class="coupon-item">
        <!-- 实际满减 -->
        <div class="discount-circle">
          <p class="actual-discount">{{ coupon.discount }}</p>
          <p class="threshold">满{{ coupon.threshold }}减{{ coupon.discount }}</p>
        </div>

        <!-- 优惠券详细 -->
        <div class="coupon-details">
          <div class="store-coupon">
            <p class="value">￥{{ coupon.storeCoupon.value }}</p>
            <p class="desc">满{{ coupon.storeCoupon.threshold }}减{{ coupon.storeCoupon.value }}</p>
            <button class="btn click-btn">CLICK ON ></button>
          </div>
          <div class="platform-coupon">
            <p class="value">￥{{ coupon.platformCoupon.value }}</p>
            <p class="desc">满{{ coupon.platformCoupon.threshold }}减{{ coupon.platformCoupon.value }}</p>
            <button class="btn use-btn">拿立即使用</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";

// 定义优惠券数据
const coupons = reactive([
  {
    discount: 150,
    threshold: 1100,
    storeCoupon: { value: 50, threshold: 1000 },
    platformCoupon: { value: 100, threshold: 1000 },
  },
  {
    discount: 450,
    threshold: 3300,
    storeCoupon: { value: 150, threshold: 3000 },
    platformCoupon: { value: 300, threshold: 3000 },
  },
  {
    discount: 800,
    threshold: 6500,
    storeCoupon: { value: 300, threshold: 6000 },
    platformCoupon: { value: 500, threshold: 5000 },
  },
  {
    discount: 1200,
    threshold: 8800,
    storeCoupon: { value: 400, threshold: 8000 },
    platformCoupon: { value: 800, threshold: 8000 },
  },
]);
</script>

<style scoped>
/* 背景与容器样式 */
.coupon-container {
  background: linear-gradient(to bottom, #e6c0e8, #6b217e);
  padding: 40px 20px;
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
</style>
