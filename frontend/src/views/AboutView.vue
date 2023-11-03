<script setup>
import { ref, reactive, onMounted } from "vue";
const imgList = reactive({//测试
  img1: 'http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155',
  img2: 'http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155',
  img3: 'http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155',
})

onMounted(() => {
  // 定义星星的颜色
  const STAR_COLOR = '#fff';
  // 定义星星的大小
  const STAR_SIZE = 3;
  // 定义星星的最小缩放比例
  const STAR_MIN_SCALE = 0.2;
  // 定义溢出阈值
  const OVERFLOW_THRESHOLD = 50;
  // 定义星星的数量
  const STAR_COUNT = (window.innerWidth + window.innerHeight) / 8;
  // 获取canvas元素
  const canvas = document.querySelector('canvas');
  // 获取canvas的绘图上下文
  const context = canvas.getContext('2d');
  // 定义缩放比例
  let scale = 1; // device pixel ratio
  // 定义宽度和高度
  let width;
  let height;
  // 定义星星数组
  let stars = [];
  // 定义鼠标指针的位置
  let pointerX;
  let pointerY;
  // 定义速度对象
  let velocity = { x: 0, y: 0, tx: 0, ty: 0, z: 0.0009 };
  // 定义触摸输入标志
  let touchInput = false;
  // 生成星星
  generate();
  // 调整大小
  resize();
  // 运行动画
  step();
  // 当窗口大小改变时，重新调整大小
  window.onresize = resize;
  // 当鼠标在canvas上移动时，更新鼠标指针位置
  canvas.onmousemove = onMouseMove;
  // 当触摸屏在canvas上移动时，更新鼠标指针位置
  canvas.ontouchmove = onTouchMove;
  // 当触摸屏离开canvas时，更新鼠标指针位置
  canvas.ontouchend = onMouseLeave;
  // 当鼠标离开文档时，更新鼠标指针位置
  document.onmouseleave = onMouseLeave;
  // 生成星星
  function generate() {
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push({
        x: 0,
        y: 0,
        z: STAR_MIN_SCALE + Math.random() * (1 - STAR_MIN_SCALE),
      });
    }
  }
  // 将星星放置到随机位置
  function placeStar(star) {
    star.x = Math.random() * width;
    star.y = Math.random() * height;
  }
  // 回收星星并重新放置到新的位置
  function recycleStar(star) {
    // 初始化方向为 'z'
    let direction = 'z';
    // 获取速度的绝对值
    let vx = Math.abs(velocity.x);
    let vy = Math.abs(velocity.y);
    // 如果速度的绝对值大于1，则根据速度的大小随机确定方向
    if (vx > 1 || vy > 1) {
      let axis;
      // 如果水平速度大于垂直速度，则根据水平速度的比例随机确定水平或垂直方向
      if (vx > vy) {
        axis = Math.random() < vx / (vx + vy) ? 'h' : 'v';
      } else {
        axis = Math.random() < vy / (vx + vy) ? 'v' : 'h';
      }
      // 根据方向确定具体的移动方向
      if (axis === 'h') {
        direction = velocity.x > 0 ? 'l' : 'r';
      } else {
        direction = velocity.y > 0 ? 't' : 'b';
      }
    }
    // 随机设置星星的缩放比例
    star.z = STAR_MIN_SCALE + Math.random() * (1 - STAR_MIN_SCALE);
    // 根据方向设置星星的位置
    if (direction === 'z') {
      // 如果方向为 'z'，则将星星放置在屏幕中心
      star.z = 0.1;
      star.x = Math.random() * width;
      star.y = Math.random() * height;
    } else if (direction === 'l') {
      // 如果方向为 'l'，则将星星放置在屏幕左侧
      star.x = -OVERFLOW_THRESHOLD;
      star.y = height * Math.random();
    } else if (direction === 'r') {
      // 如果方向为 'r'，则将星星放置在屏幕右侧
      star.x = width + OVERFLOW_THRESHOLD;
      star.y = height * Math.random();
    } else if (direction === 't') {
      // 如果方向为 't'，则将星星放置在屏幕顶部
      star.x = width * Math.random();
      star.y = -OVERFLOW_THRESHOLD;
    } else if (direction === 'b') {
      // 如果方向为 'b'，则将星星放置在屏幕底部
      star.x = width * Math.random();
      star.y = height + OVERFLOW_THRESHOLD;
    }
  }
  // 调整大小
  function resize() {
    // 获取设备像素比例
    scale = window.devicePixelRatio || 1;
    // 设置画布的宽度和高度
    width = window.innerWidth * scale;
    height = window.innerHeight * scale;
    canvas.width = width;
    canvas.height = height;
    // 将所有星星重新放置到屏幕上
    stars.forEach(placeStar);
  }
  // 动画的每一帧
  function step() {
    // 清空画布
    context.clearRect(0, 0, width, height);
    // 更新星星的位置和速度
    update();
    // 绘制星星
    render();
    // 请求下一帧动画
    requestAnimationFrame(step);
  }
  // 更新星星的位置和速度
  function update() {
    // 缓动速度
    velocity.tx *= 0.8;
    velocity.ty *= 0.8;
    // 更新速度
    velocity.x += (velocity.tx - velocity.x) * 0.6;
    velocity.y += (velocity.ty - velocity.y) * 0.6;
    // 遍历所有星星
    stars.forEach((star) => {
      // 根据速度和缩放比例更新星星的位置
      star.x += velocity.x * star.z;
      star.y += velocity.y * star.z;
      // 根据速度和缩放比例更新星星的位置（使星星围绕屏幕中心旋转）
      star.x += (star.x - width / 2) * velocity.z * star.z;
      star.y += (star.y - height / 2) * velocity.z * star.z;
      // 更新星星的缩放比例
      star.z += velocity.z;
      // 如果星星超出屏幕范围，则重新放置到屏幕上
      if (
        star.x < -OVERFLOW_THRESHOLD ||
        star.x > width + OVERFLOW_THRESHOLD ||
        star.y < -OVERFLOW_THRESHOLD ||
        star.y > height + OVERFLOW_THRESHOLD
      ) {
        recycleStar(star);
      }
    });
  }
  // 绘制星星
  function render() {
    // 遍历所有星星
    stars.forEach((star) => {
      // 设置绘制星星的样式
      context.beginPath();
      context.lineCap = 'round';
      context.lineWidth = STAR_SIZE * star.z * scale;
      context.globalAlpha = 0.5 + 0.5 * Math.random();
      context.strokeStyle = STAR_COLOR;
      // 绘制星星的路径
      context.beginPath();
      context.moveTo(star.x, star.y);
      // 计算星星的尾巴坐标
      let tailX = velocity.x * 2;
      let tailY = velocity.y * 2;
      // 如果尾巴坐标的绝对值小于0.1，则设置为0.5
      if (Math.abs(tailX) < 0.1) tailX = 0.5;
      if (Math.abs(tailY) < 0.1) tailY = 0.5;
      // 绘制星星的尾巴
      context.lineTo(star.x + tailX, star.y + tailY);
      context.stroke();
    });
  }
  // 移动鼠标指针
  function movePointer(x, y) {
    // 如果之前有记录鼠标指针的位置，则计算鼠标指针的移动距离，并更新速度
    if (typeof pointerX === 'number' && typeof pointerY === 'number') {
      let ox = x - pointerX;
      let oy = y - pointerY;
      velocity.tx = velocity.tx + (ox / 8) * scale * (touchInput ? 1 : -1);
      velocity.ty = velocity.ty + (oy / 8) * scale * (touchInput ? 1 : -1);
    }
    // 更新鼠标指针的位置
    pointerX = x;
    pointerY = y;
  }
  // 当鼠标在canvas上移动时的事件处理函数
  function onMouseMove(event) {
    touchInput = false;
    movePointer(event.clientX, event.clientY);
  }
  // 当触摸屏在canvas上移动时的事件处理函数
  function onTouchMove(event) {
    touchInput = true;
    movePointer(event.touches[0].clientX, event.touches[0].clientY, true);
    event.preventDefault();
  }
  // 当鼠标离开canvas时的事件处理函数
  function onMouseLeave() {
    pointerX = null;
    pointerY = null;
  }
})

</script>
<template>
  <!-- 关于我们页面组件 -->

  <div class="about">
    <div id="star-container"></div>
    <div class="banner">
      <el-image :src="require('@/assets/背景1.jpg')" fit="contain" :lazy="false"></el-image>
    </div>
    <div class="about-us">
      <h1 class="about_title animate__animated animate__fadeInDown animate__slow animate__repeat-1 animate__delay-1s">
        <b style="">
          我们的团队
        </b>

      </h1>

      <canvas>
      </canvas>
      <!-- 在这个div标签里面加哦 -->
      <div class="row">

        <div class="containers col-lg-4 col-md-4">
          <div class="pic">
            <img src='http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155'>
          </div>
        </div>

        <div class="about_con col-lg-4 col-md-4">
          <left>
            <h1 class="contenthead">xx</h1>
            <h2 class="contents">xx专业</h2>
          </left>

          <h2 class="contents"><br />
            Captain. <br />
            团队负责人，全能型选手，完成大部分的技术工作，负责整合代码以及解答队员一些技术问题

            <br /><br />
            Team leader, versatile player, responsible for completing most of the technical work, integrating code, and
            answering team members' technical questions<span>&hearts;</span>
            <br /><br />

            <!-- <p><span style="text-align:right; color:#000000; font-size:18px;">* No matter what u say, that gal is sorta
                cute.</span></p> -->
          </h2>
        </div>
      </div>
      <br><br />

      <div class="row">
        <!-- <div class="col-lg-4 col-md-4 " style="border:1px solid blue;"></div> -->
        <div class="about_con  col-md-4 col-lg-4  offset-md-4 offset-lg-4 ">
          <right>
            <h1 class="contenthead">xx</h1>
            <h2 class="contents">xx专业</h2>
          </right>
          <h2 class="contents"><br />
            Member. <br />
            队员，负责写数据库以及一小部分网页内容
            <br /><br />
            Team member, responsible for writing databases and a small portion of webpage content<span>&hearts;</span>
            <br /><br />

            <!-- <p><span style="text-align:right; color:#000000; font-size:18px;">* No matter what u say, that gal is sorta
                cute.</span></p> -->
          </h2>
        </div>

        <div class="containers col-lg-4 col-md-4">
          <div class="pic">
            <img src='http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155'>
          </div>
        </div>
      </div>
      <br><br />
      <div class="row">
        <div class="containers col-lg-4 col-md-4">
          <div class="pic">
            <img src='http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155'>
          </div>
        </div>


        <div class="about_con col-lg-4 col-md-4">
          <left>
            <h1 class="contenthead">xx</h1>
            <h2 class="contents">xx专业</h2>
          </left>

          <h2 class="contents"><br />
            Member. <br />
            队员，负责写首页部分的静态页面
            <br /><br />
            Team member, responsible for writing the static page of the homepage section<span>&hearts;</span>


          </h2>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss">
// @import '../assets/font/font-awesome.min.css';
@import '../assets/font/css.css';
@import '../assets/font/css1.css';



body {
  background: url('https://s-media-cache-ak0.pinimg.com/736x/f4/ac/6a/f4ac6aac3afb587f6cae04155656fca3.jpg');
}

// .containers {
//   width: 550px;
//   height: 100%;
//   margin-left: 10px;
// }

// .containers:nth-child() {
//   width: 550px;
//   height: 100%;
//   margin-right: 10px;
// }

// 星星
canvas {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
}

.pic {
  box-shadow: 6px 6px 7px #888888;
  width: 300px;
  height: 300px;
  position: relative;
  overflow: hidden;
  margin-top: 10px;
  margin-left: 135px;
  -ms-transform: rotate(-30deg);
  -webkit-transform: rotate(-30deg);
  transform: rotate(-30deg);
}

.pic:before {
  content: '';
  margin-top: -63px;
  margin-left: -80px;
  position: absolute;
  width: 450px;
  height: 450px;
  background: url('http://ultraimg.com/images/a0ed6d.jpg') center center;
  -ms-transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg);
  transform: rotate(-45deg);
}

.row:nth-of-type(odd) {

  .containers {
    // width: 550px;
    height: 100%;
    margin-left: 10px;
  }

}

.row:nth-of-type(even) {
  .containers {
    // width: 550px;
    height: 100%;
    margin-right: 10px;

    .pic {
      -ms-transform: rotateY(180deg) rotate(-30deg);
      -webkit-transform: rotateY(180deg) rotate(-30deg);
      transform: rotateY(180deg) rotate(-30deg);
    }


    .pic::before {
      -ms-transform: rotateY(180deg) rotate(-45deg);
      -webkit-transform: rotateY(180deg) rotate(-45deg);
      transform: rotateY(180deg) rotate(-45deg);
    }
  }

  // flex-wrap: wrap;
}

.pic:hover {
  box-shadow: 3px 3px 70px rgb(255, 155, 101);
  cursor: pointer;
}

.about_con {
  height: 100%;
  width: 500px;
}

p {
  font-family: 'Open Sans Condensed', sans-serif !important;
}

h2.contents {
  font-family: 'Dancing Script', cursive !important;
  color: #FFFFFF;
  text-shadow: #000000 0 2px 2px;
}

.contenthead {
  width: max-content;
  left: 0;
  position: relative;
  // text-align: left;
  font-family: 'Open Sans Condensed', sans-serif;
  font-size: 50px;
  font-weight: 400;
  color: #FFFFFF;
  text-shadow: #000000 0 2px 2px;
  border-bottom: 4px solid rgb(144, 113, 255);
  // text-decoration: underline solid #B80C08 4px;
}

right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

sup {
  font-family: 'Open Sans Condensed', sans-serif;
  font-style: italic;
  font-size: smaller;
}

span {
  color: pink;
}

.about {
  margin: 0 0;
  padding: 0;
  overflow: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.about::-webkit-scrollbar {
  display: none;
}

.banner {
  display: flex;
  height: auto;
  width: 100%;
  position: relative;
  align-items: last baseline;
  justify-content: center;
  box-shadow: 0px 5px 10px 2px #e97c42;
}

h1.about_title {
  text-align: center;
  padding-top: 30px;
  margin-bottom: 100px;

  b {
    color: #FFFFFF;
    font-family: Nunito;
    font-size: 150%;
    font-weight: 700;
    text-align: center;
    text-shadow: #000000 0 2px 2px;
    transform: translateZ(.25px) scale(.75);
    transform-origin: 50% 100%;

  }
}

.about-us {
  position: relative;
  background: linear-gradient(0, #B80C08, #F1844A);
  padding: 0 1%;
  padding-bottom: 5%;
  text-align: left;
}
</style>
