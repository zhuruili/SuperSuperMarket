
<template>
    <div>
  <div id="app">
    <!-- 标题 -->
    <h1 style="color: white;text-align: center;margin: 50px">CodingSir-抽奖大转盘</h1>


    <!-- 抽奖部分 -->
    <div class="container-out">
      <div class="container-in">
        <div class="content-out" v-for="(box,index) in list"
             :style="{left:box.left+'px',top:box.top+'px','background-color':index==indexSelect?colorSelect:colorDefault}">
          <img class="pond-name-img" :src="box.image_url" alt="">
          <div class="pond-name">{{box.name}}</div>
        </div>
      </div>
      <div class="start-btn" v-on:click="startBtn">
        <img src="@/imgs/pond-button.png" style="height:80px;width:100%;" alt="">
        <img src="@/imgs/pond-cj.png" :style="{'top':btntop+'px'}"
             style="position:absolute;left:5px;height:68px;width:89px;top:0;" alt="">
      </div>
      <div class="circle" v-for="(item,index) in circleList"
           :style="{'top':item.topCircle+'px','left':item.leftCircle+'px','background-color':index%2==0?colorFirst:colorSecond}">
      </div>
    </div>
  
    <!-- 抽奖结果展示 -->
    <div class="prize" v-show="prize==1">
      <div class="prize-box">
        <img class="prize-img" src="/imgs/pond-success.png" alt="">
        <div class="prize-msg">
          <div style="margin-bottom: 10px">恭喜你</div>
          <div>抽中了{{prize_name}}</div>
          <div class="continue" v-on:click="conTinue">可以继续抽奖</div>
        </div>
      </div>
    </div>
    <div class="prize" v-show="prize==2">
      <div class="prize-box">
        <img class="prize-img2" src="/imgs/pond-empty.png" alt="">
        <div class="prize-msg">
          <div style="margin-bottom: 10px">很遗憾</div>
          <div>洗洗手重新再抽奖试试！</div>
          <div class="continue" v-on:click="conTinue">可以继续抽奖</div>
        </div>
      </div>
    </div>
    <div class="men" v-show="men"></div>
  </div>
</div>

</template>

<script setup>
import { ref, onMounted } from 'vue';

//
const list = ref([
  { id: 1, type: 1, name: '10元代金卷', image_url: '../imgs/djj.jpg' },
  { id: 2, type: 2, name: '谢谢参与', image_url: '../imgs/xxcy.png' },
  { id: 3, type: 1, name: 'iphone16', image_url: '../imgs/iphone.png' },
  { id: 4, type: 1, name: '1小时体验券', image_url: '../imgs/1tyq.png' },
  { id: 5, type: 1, name: '20元优惠券', image_url: '../imgs/20yhq.png' },
  { id: 6, type: 2, name: '谢谢参与', image_url: '../imgs/xxcy.png' },
  { id: 7, type: 1, name: '666积分奖励', image_url: '../imgs/jf.png' },
  { id: 8, type: 1, name: '1元现金红包', image_url: '../imgs/1xj.png' }
]);

const circleList = ref([]);
const colorFirst = ref("#F12416");
const colorSecond = ref("#FFFFFF");
const colorDefault = ref("#F5F0FC");
const colorSelect = ref("green");
const btntop = ref(0);
const time = ref(null);
const indexSelect = ref(-1);
const lottert = ref(0);
const prize = ref(0);
const prize_name = ref('');
const men = ref(false);

const init = () => {
  let left = 9;
  let top = 9;
  for (let i = 0; i < 8; i++) {
    if (i === 0) {
      left = 9;
      top = 9;
    } else if (i < 3 && i !== 0) {
      left += 98 + 4;
    } else if (i >= 3 && i < 5) {
      top += 79 + 4;
    } else if (i >= 5 && i < 7) {
      left -= 98 + 4;
    } else if (i >= 7 && i < 8) {
      top -= 79 + 4;
    }
    list.value[i].top = top;
    list.value[i].left = left;
  }

  const cleft = 4;
  const ctop = 4;
  const dian = [];
  for (let j = 0; j < 24; j++) {
    if (j === 0) {
      cleft = 4;
      ctop = 4;
    } else if (j < 6) {
      ctop = 2;
      cleft += 55;
    } else if (j === 6) {
      ctop = 2;
      cleft = 330;
    } else if (j < 12) {
      ctop += 46;
      cleft = 331.5;
    } else if (j === 12) {
      ctop = 272.5;
      cleft = 330;
    } else if (j < 18) {
      ctop = 275;
      cleft -= 55;
    } else if (j === 18) {
      ctop = 273;
      cleft = 5;
    } else {
      if (!(j < 24)) return;
      ctop -= 46;
      cleft = 2.5;
    }
    dian.push({ topCircle: ctop, leftCircle: cleft });
  }

  circleList.value = dian;

  setInterval(() => {
    if (colorFirst.value === "#FFFFFF") {
      colorFirst.value = "#F12416";
      colorSecond.value = "#FFFFFF";
    } else {
      colorFirst.value = "#FFFFFF";
      colorSecond.value = "#F12416";
      btntop.value = 0;
    }
  }, 900);

  time.value = setInterval(() => {
    btntop.value = btntop.value === 0 ? -3 : 0;
  }, 900);
};

const startBtn = () => {
  clearInterval(time.value);
  men.value = true;
  btntop.value = 0;
  lottert.value = 0;
  let i = indexSelect.value;
  let s = 0;

  const timer = setInterval(() => {
    i++;
    i %= 8;
    s += 30;
    indexSelect.value = i;
    if (lottert.value > 0 && i + 1 === lottert.value) {
      clearInterval(timer);
      time.value = setInterval(() => {
        btntop.value = btntop.value === 0 ? -3 : 0;
      }, 900);
      if (list.value[i].type === 2) {
        prize.value = 2;
      } else {
        prize_name.value = list.value[i].name;
        prize.value = 1;
      }
    }
  }, 200 + s);

  setTimeout(() => {
    lottert.value = randomNum(1, 8);
  }, 2000);
};

const randomNum = (minNum, maxNum) => {
  return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
};

const conTinue = () => {
  men.value = false;
  prize.value = 0;
};

onMounted(init);
</script>


<style>

body, div, dl, dt, dd, ul, ol, pre, code, form, th, td, hr, button, nav, section {
    margin: 0;
    padding: 0;
}

html {
    background: #f12416;
}

#page {
    width: 100%;
}

.pond-head img {
    width: 100%;
    height: 215px;
}

.container-out {
    height: 283px;
    width: 340px;
    background-color: #F47915;
    margin: 16px auto 15px auto;
    border-radius: 8px;
    position: relative;
}

.circle {
    position: absolute;
    display: block;
    border-radius: 50%;
    height: 7px;
    width: 7px;
}

.content-out {
    position: absolute;
    height: 72px;
    width: 98px;
    background-color: #f5f0fc;
    border-radius: 8px;
    box-shadow: 0 8px 0 #FFCEC0;
}

.container-in {
    width: 320px;
    height: 263px;
    background-color: #f12416;
    border-radius: 10px;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    margin: auto;
}

.pond-name-img {
    position: absolute;
    top: 6px;
    left: 0;
    width: 100%;
    height: 46px;
    z-index: 1;
}

.pond-name {
    position: absolute;
    top: 75%;
    color: #c62015;
    width: 98px;
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    font-size: 9pt;
    text-align: center;
}

.start-btn {
    position: absolute;
    margin: auto;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    border-radius: 8px;
    height: 79px;
    width: 98px;
    color: #f6251e;
    text-align: center;
    font-weight: bolder;
    line-height: 77px;
}

.prize {
    background: rgba(0, 0, 0, 0.25);
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    -ms-grid-row-align: center;
    align-items: center;
    z-index: 100;
}

.prize-box {
    margin: 0 auto;
    position: relative;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.prize-img {
    width: 100vw;
    max-height: 231px;
    max-width: 375px;
}

.prize-img2 {
    width: 100vw;
    max-height: 120px;
    max-width: 375px;
}

.prize-msg {
    margin-top: -7px;
    width: 78.5vw;
    max-width: 294.5px;
    text-align: center;
    background: #ffffff;
    padding-bottom: 6px;
    font-size: 13pt;
}

.prize_name {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.continue {
    width: 240px;
    height: 40px;
    margin: 28px auto;
    background: #ff5c5c;
    line-height: 40px;
    color: #ffffff;
    border-radius: 20px;
}

.men {
    position: fixed;
    width: 100vw;
    height: 100vh;
    z-index: 1;
    left: 0;
    top: 0;
}

</style>








