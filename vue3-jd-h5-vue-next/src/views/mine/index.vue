<template>
  <div class="login-regist" v-show="!is_login">
      <!-- <router-link to="/mylogin" class="order-item" tag="span">登录</router-link>
      <router-link to="/register/myRegister" class="order-item" tag="span">/注册</router-link> -->
      <form class="form">
      <div class="flex-column">
        <label>用户名 </label></div>
        <div class="inputForm">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" viewBox="0 0 32 32" height="20"><g data-name="Layer 3" id="Layer_3"><path d="m30.853 13.87a15 15 0 0 0 -29.729 4.082 15.1 15.1 0 0 0 12.876 12.918 15.6 15.6 0 0 0 2.016.13 14.85 14.85 0 0 0 7.715-2.145 1 1 0 1 0 -1.031-1.711 13.007 13.007 0 1 1 5.458-6.529 2.149 2.149 0 0 1 -4.158-.759v-10.856a1 1 0 0 0 -2 0v1.726a8 8 0 1 0 .2 10.325 4.135 4.135 0 0 0 7.83.274 15.2 15.2 0 0 0 .823-7.455zm-14.853 8.13a6 6 0 1 1 6-6 6.006 6.006 0 0 1 -6 6z"></path></g></svg>
          <input v-model="username" placeholder="Enter your Username" class="input" type="text">
        </div>

      <div class="flex-column">
        <label>密码 </label></div>
        <div class="inputForm">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" viewBox="-64 0 512 512" height="20"><path d="m336 512h-288c-26.453125 0-48-21.523438-48-48v-224c0-26.476562 21.546875-48 48-48h288c26.453125 0 48 21.523438 48 48v224c0 26.476562-21.546875 48-48 48zm-288-288c-8.8125 0-16 7.167969-16 16v224c0 8.832031 7.1875 16 16 16h288c8.8125 0 16-7.167969 16-16v-224c0-8.832031-7.1875-16-16-16zm0 0"></path><path d="m304 224c-8.832031 0-16-7.167969-16-16v-80c0-52.929688-43.070312-96-96-96s-96 43.070312-96 96v80c0 8.832031-7.167969 16-16 16s-16-7.167969-16-16v-80c0-70.59375 57.40625-128 128-128s128 57.40625 128 128v80c0 8.832031-7.167969 16-16 16zm0 0"></path></svg>        
          <input v-model="password" placeholder="Enter your Password" class="input" type="password">
        </div>

      <div class="flex-row">
        <div>
        <input type="radio">
        <label>记住我</label>
        </div>
        <span class="span">忘记密码?</span>
      </div>
      <button class="button-submit" @click="handleRegister">登录</button>
      <p class="p">没有账号? <router-link to="/register/myRegister" class="span" >注册</router-link>

      </p><p class="p line">Or With</p>

      <div class="flex-row">
        <button class="btn google">
          <svg xml:space="preserve" style="enable-background:new 0 0 512 512;" viewBox="0 0 512 512" y="0px" x="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" id="Layer_1" width="20" version="1.1">
  <path d="M113.47,309.408L95.648,375.94l-65.139,1.378C11.042,341.211,0,299.9,0,256
  	c0-42.451,10.324-82.483,28.624-117.732h0.014l57.992,10.632l25.404,57.644c-5.317,15.501-8.215,32.141-8.215,49.456
  	C103.821,274.792,107.225,292.797,113.47,309.408z" style="fill:#FBBB00;"></path>
  <path d="M507.527,208.176C510.467,223.662,512,239.655,512,256c0,18.328-1.927,36.206-5.598,53.451
  	c-12.462,58.683-45.025,109.925-90.134,146.187l-0.014-0.014l-73.044-3.727l-10.338-64.535
  	c29.932-17.554,53.324-45.025,65.646-77.911h-136.89V208.176h138.887L507.527,208.176L507.527,208.176z" style="fill:#518EF8;"></path>
  <path d="M416.253,455.624l0.014,0.014C372.396,490.901,316.666,512,256,512
  	c-97.491,0-182.252-54.491-225.491-134.681l82.961-67.91c21.619,57.698,77.278,98.771,142.53,98.771
  	c28.047,0,54.323-7.582,76.87-20.818L416.253,455.624z" style="fill:#28B446;"></path>
  <path d="M419.404,58.936l-82.933,67.896c-23.335-14.586-50.919-23.012-80.471-23.012
  	c-66.729,0-123.429,42.957-143.965,102.724l-83.397-68.276h-0.014C71.23,56.123,157.06,0,256,0
  	C318.115,0,375.068,22.126,419.404,58.936z" style="fill:#F14336;"></path>
  </svg>
          Google 
        </button><button class="btn apple">
  <svg xml:space="preserve" style="enable-background:new 0 0 22.773 22.773;" viewBox="0 0 22.773 22.773" y="0px" x="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" id="Capa_1" width="20" height="20" version="1.1"> <g> <g> <path d="M15.769,0c0.053,0,0.106,0,0.162,0c0.13,1.606-0.483,2.806-1.228,3.675c-0.731,0.863-1.732,1.7-3.351,1.573 c-0.108-1.583,0.506-2.694,1.25-3.561C13.292,0.879,14.557,0.16,15.769,0z"></path> <path d="M20.67,16.716c0,0.016,0,0.03,0,0.045c-0.455,1.378-1.104,2.559-1.896,3.655c-0.723,0.995-1.609,2.334-3.191,2.334 c-1.367,0-2.275-0.879-3.676-0.903c-1.482-0.024-2.297,0.735-3.652,0.926c-0.155,0-0.31,0-0.462,0 c-0.995-0.144-1.798-0.932-2.383-1.642c-1.725-2.098-3.058-4.808-3.306-8.276c0-0.34,0-0.679,0-1.019 c0.105-2.482,1.311-4.5,2.914-5.478c0.846-0.52,2.009-0.963,3.304-0.765c0.555,0.086,1.122,0.276,1.619,0.464 c0.471,0.181,1.06,0.502,1.618,0.485c0.378-0.011,0.754-0.208,1.135-0.347c1.116-0.403,2.21-0.865,3.652-0.648 c1.733,0.262,2.963,1.032,3.723,2.22c-1.466,0.933-2.625,2.339-2.427,4.74C17.818,14.688,19.086,15.964,20.67,16.716z"></path> </g></g></svg>

          Apple 

  </button></div></form>

      <tabbar></tabbar>
  </div>
  <div class="mine-layout" v-show="is_login">
    <section class="mine-header">
      <img src="../../assets/image/product/store-headerM.png" class="header-img" />
      <!-- <div class="login-regist">
        <router-link to="/login" class="order-item" tag="span">登录</router-link>
        <router-link to="/register/phoneRegister" class="order-item" tag="span">/注册</router-link>
      </div> -->
      <ul class="user-info">
        <li class="user-name"> {{ username }} </li>
        <!-- <li class="node-info">
          <span class="sharing-node" @click="toShow">分享节点</span>
          <span class="business-node">商家节点</span>
        </li> -->
      </ul>
    </section>
    <section class="my-info">
      <ul class="info-list">
        <li class="info-item">
          <b>15</b>
          <span>商品关注</span>
        </li>
        <li class="info-item">
          <b>05</b>
          <span>店铺关注</span>
        </li>
        <li class="info-item">
          <b>56</b>
          <span>我的足迹</span>
        </li>
      </ul>
    </section>
    <section class="order-all">
      <router-link to="/order" class="look-orders" tag="span"
        >查看全部订单>></router-link
      >
      <ul class="order-list">
        <router-link to="/order/orderDetail" class="order-item" tag="li">
          <svg-icon icon-class="pending-pay"></svg-icon>
          <span>待付款</span>
        </router-link>
        <router-link to="/order/toBeDelivered" class="order-item" tag="li">
          <svg-icon icon-class="be-delivered"></svg-icon>
          <span>待发货</span>
        </router-link>
        <router-link to="/order/pendingReceipt" class="order-item" tag="li">
          <svg-icon icon-class="pending-receipt"></svg-icon>
          <span>待收货</span>
        </router-link>
        <router-link to="/order" class="order-item" tag="li">
          <svg-icon icon-class="all-orders"></svg-icon>
          <span>退换/售后</span>
        </router-link>
      </ul>
    </section>

    <section class="mine-content">
      <ul class="options-list">
        <router-link to="wallet/myWallet" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="my-assets"></svg-icon>
            <span>我的钱包</span>
          </div>
          <van-icon name="arrow" color="#DBDBDB" />
        </router-link>
        <router-link to="/node/nodeApplication" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="node-application"></svg-icon>
            <span>节点申请</span>
          </div>
          <van-icon name="arrow" color="#DBDBDB" />
        </router-link>
        <router-link to="/wallet/myWallet" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon
              class="incon"
              icon-class="businessmen-stationed"
            ></svg-icon>
            <span>商家入驻</span>
          </div>
          <van-icon name="arrow" color="#DBDBDB" />
        </router-link>
        <router-link to="/wallet/myWallet" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="sharing-links"></svg-icon>
            <span>分享链接</span>
          </div>
          <van-icon name="arrow" color="#DBDBDB" />
        </router-link>
      </ul>
    </section>

    <section class="mine-content">
      <ul class="options-list">
        <router-link to="/mine/shippingAddress" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="shipping-address"></svg-icon>
            <span>收货地址</span>
          </div>
          <van-icon name="arrow" color="#DBDBDB" />
        </router-link>
        <router-link to="/mine/messageCenter" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="message-center"></svg-icon>
            <span>消息中心</span>
          </div>
          <van-icon color="#DBDBDB" name="arrow" />
        </router-link>
        <router-link to="/mine/helpCenter" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="help-center"></svg-icon>
            <span>帮助中心</span>
          </div>
          <van-icon color="#DBDBDB" name="arrow" />
        </router-link>
        <router-link to="/mine/setting" class="option-item" tag="li">
          <div class="item-info">
            <svg-icon class="incon" icon-class="setting"></svg-icon>
            <span>设置</span>
          </div>
          <van-icon color="#DBDBDB" name="arrow" />
        </router-link>
      </ul>
    </section>

    <van-dialog
      class="node-dialog"
      v-model="show"
      confirmButtonText="我知道啦"
      close-on-click-overlay
      confirmButtonColor="#3A3A3A"
      confirm-button-color="#FCE14B"
      :show-cancel-button="false"
      :show-confirm-button="false"
    >
      <article>
        <header class="dialog-header">
          <img src="../../assets/image/product/header-good.png" />
        </header>
        <van-divider
          :style="{
            color: '#3A3A3A',
            borderColor: '#FFE31F',
            fontWeight: '600',
            fontSize: '14px',
            padding: '0 15px'
          }"
          >我的节点数据</van-divider
        >
        <ul class="my-node-data">
          <li class="data-item">
            <img src="../../assets/image/product/share-node-img.png" alt />
            <span class="node-text">分享节点</span>
          </li>
          <li class="data-item">
            <img src="../../assets/image/product/area-node-img.png" alt />
            <span class="node-text">区级节点</span>
          </li>
          <li class="data-item">
            <img src="../../assets/image/product/municipal-node-img.png" alt />
            <span class="node-text">市级节点</span>
          </li>
          <li class="data-item">
            <img src="../../assets/image/product/state-node-img.png" alt />
            <span class="node-text">州级节点</span>
          </li>
          <li class="data-item">
            <img src="../../assets/image/product/industry-node-img.png" alt />
            <span class="node-text">行业节点</span>
          </li>
          <li class="data-item">
            <img src="../../assets/image/product/super-node-img.png" alt />
            <span class="node-text">超级节点</span>
          </li>
        </ul>
        <van-divider
          :style="{
            color: '#3A3A3A',
            borderColor: '#FFE31F',
            fontWeight: '600',
            fontSize: '14px',
            padding: '0 15px'
          }"
        />
        <div class="node-bottom">
          <span class="know-btn" @click="handleClose">我知道啦</span>
          <img
            class="gray-img"
            src="../../assets/image/product/gray-node-img.png"
          />
        </div>
      </article>
    </van-dialog>
    <tabbar></tabbar>
  </div>
</template>

<script>
import { ref, onMounted, getCurrentInstance, watchEffect } from "vue";
import AxiosPlugin, { httpInstance } from '@/plugins/axios'
import { useRouter } from "vue-router";
export default {
  name: "mine",
  setup() {
   // const is_login = ref(localStorage.getItem("isLogin") === 'true');
   const is_login = ref(true);
    const username = ref("");
    const password = ref("");
    const show = ref(false);
    const columns = ref(1);
    const router = useRouter();
    const { ctx } = getCurrentInstance();

    const handleClose = () => {
      show.value = false;
    };
    const handleRegister=async()=>{
      event.preventDefault(); // 防止表单提交刷新页面
      try {
        console.log('handleLogin');
        // 发送登录请求
        const response = await httpInstance.post("http://localhost:8889/login", {
            username: username.value,
            password: password.value
        }, {
            headers: {
                'Content-Type': 'application/json'  // 设置正确的 Content-Type
            }
        });
        console.log(response);
        // 假设返回的 response 中有一个 `token` 字段，表示登录成功
        if (response.status==200) {
            console.log("Login successful!");

            // 将 token 存储在 localStorage 中，或其他合适的地方
           // localStorage.setItem('token', response.data.token);
            localStorage.setItem('username', username.value);
            localStorage.setItem('userId', response.data.userID);
           // localStorage.setItem('password', password.value);
            localStorage.setItem("isLogin",true);
            is_login.value = true;
            console.log(localStorage.getItem("userId"))
            // 跳转到登录成功后的页面，例如首页
            router.push('/mine');
        } else {
            console.log("Login failed:", response.data.message);
            alert(response.data.message);  // 提示错误消息
        }
    } catch (error) {
        console.log("Error during login:", error);
        alert("An error occurred while logging in");
    }
    }

    const toShow = () => {
      show.value = true;
    };

    onMounted(() => {
      ctx.$eventBus.$emit("changeTag", 3);
    });

    watchEffect(() => {
      is_login.value = localStorage.getItem("isLogin") === 'true';
      username.value = localStorage.getItem("username");
      password.value = localStorage.getItem("password");
    });

    return { show, columns, toShow,handleRegister, handleClose, is_login, username, password };
  }
};
</script>

<style scoped lang="scss">
.login-regist {
    display: flex;
    justify-content: center;
    margin-top: 300px;
    .order-item {
        font-size: 16px;
        color: #333;
        margin: 0 10px;
    }   
}
.mine-layout {
  padding: 30px 16px;
  min-height: 812px;
  padding-bottom: 50px;

  background: linear-gradient(#fe4f70, #ff9351);
  .mine-header {
    display: flex;
    padding-left: 24px;
    justify-content: flex-start;
    align-items: center;
    flex-direction: row;
    padding-bottom: 20px;
    .header-img {
      width: 70px;
      height: 70px;
    }
    .user-info {
      padding-left: 16px;
      font-size: 15px;
      color: #fff;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      .node-info {
        padding-top: 5px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        .sharing-node {
          padding-left: 18px;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 78px;
          height: 25px;
          font-size: 11px;
          text-align: center;
          background: url("../../assets/image/product/sharing-node.png")
            no-repeat center center;
          background-size: 100% 100%;
          border-radius: 11px 11px;
        }
        .business-node {
          margin-left: 5px;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 60px;
          height: 22px;
          font-size: 11px;
          text-align: center;
          background-color: #71c0f6;
          border-radius: 11px 11px;
        }
      }
    }

    .login-regist {
      font-size: 15px;
      color: #fff;
      padding-left: 16px;
    }
  }
  .my-info {
    font-size: 13px;
    color: #fff;
    padding-bottom: 16px;
    .info-list {
      display: flex;
      justify-content: space-around;
      align-items: center;
      .info-item {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        b {
          font-size: 16px;
        }
      }
    }
  }
  .order-all {
    box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border-radius: 8px;
    .look-orders {
      font-size: 11px;
      font-weight: 600;
      color: #3a3a3a;
      padding-left: 19px;
      padding-top: 14px;
      padding-bottom: 18px;
    }
    .order-list {
      padding-bottom: 18px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      .order-item {
        font-size: 14px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        span {
          padding-top: 5px;
          font-weight: 600;
        }
      }
    }
  }
  .mine-content {
    box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.1);
    background-color: #fff;
    border-radius: 8px;
    padding: 0 16px;
    margin-top: 18px;
    .options-list {
      padding-top: 20px;
      .option-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 16px;
        padding-bottom: 22px;
        .item-info {
          display: flex;
          justify-content: center;
          align-items: center;
          font-size: 15px;
          color: #888;
          .incon {
            padding-right: 16px;
          }
          .header-img {
            width: 50px;
            height: 50px;
            padding-right: 16px;
          }
        }
      }
    }
  }
  .node-dialog {
    .dialog-header {
      text-align: center;
    }
    .my-node-data {
      padding: 10px 40px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-wrap: wrap;
      .data-item {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-left: 10px;
        margin-bottom: 20px;
        .node-text {
          font-size: 13px;
          padding-top: 5px;
          color: #3a3a3a;
        }
      }
    }
    .node-bottom {
      position: relative;
      .know-btn {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
        line-height: 40px;
        width: 154px;
        border-radius: 20px 20px;
        background-color: #fce14b;
        margin-bottom: 30px;
      }
      .gray-img {
        position: absolute;
        right: 12px;
        top: 0;
      }
    }
  }
}
.form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: #ffffff;
    padding: 30px;
    width: 450px;
    border-radius: 20px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  ::placeholder {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  .form button {
    align-self: flex-end;
  }

  .flex-column > label {
    color: #151717;
    font-weight: 600;
  }

  .inputForm {
    border: 1.5px solid #ecedec;
    border-radius: 10px;
    height: 50px;
    display: flex;
    align-items: center;
    padding-left: 10px;
    transition: 0.2s ease-in-out;
  }

  .input {
    margin-left: 10px;
    border-radius: 10px;
    border: none;
    width: 100%;
    height: 100%;
  }

  .input:focus {
    outline: none;
  }

  .inputForm:focus-within {
    border: 1.5px solid #2d79f3;
  }

  .flex-row {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
    justify-content: space-between;
  }

  .flex-row > div > label {
    font-size: 14px;
    color: black;
    font-weight: 400;
  }

  .span {
    font-size: 14px;
    margin-left: 5px;
    color: #2d79f3;
    font-weight: 500;
    cursor: pointer;
  }

  .button-submit {
    margin: 20px 0 10px 0;
    background-color: #151717;
    border: none;
    color: white;
    font-size: 15px;
    font-weight: 500;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    cursor: pointer;
  }

  .p {
    text-align: center;
    color: black;
    font-size: 14px;
    margin: 5px 0;
  }

  .btn {
    margin-top: 10px;
    width: 100%;
    height: 50px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 500;
    gap: 10px;
    border: 1px solid #ededef;
    background-color: white;
    cursor: pointer;
    transition: 0.2s ease-in-out;
  }

  .btn:hover {
    border: 1px solid #2d79f3;
    ;
  }
</style>
