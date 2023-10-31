<script setup>
import { ref, reactive } from "vue";
import Backtop from "@/components/backtop.vue"
const imgList = reactive({//测试
  img1: 'http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155',
  img2: 'http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155',
  img3: 'http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155',
})
const loading = ref(true);
setTimeout(() => loading.value = false, 1000);
</script>
<template>
  <!-- 关于我们页面组件 -->

  <div class="about">
    <div class="banner">
      <el-image :src="require('@/assets/背景1.jpg')" fit="contain" :lazy="false"></el-image>
    </div>
    <div class="about-us">
      <h1 class="about_title animate__animated animate__fadeInDown animate__slow animate__repeat-1 animate__delay-1s">
        <b style="
    background-image: linear-gradient(90deg,#fdfafa 0,#4f4d4c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;">
          我们的团队
        </b>

      </h1>
      <!-- 在这个div标签里面加哦 -->
      <div class="row">
        <div class="containers col-lg-4 col-md-4">
          <div class="pic">
            <img src='http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155'>
          </div>
        </div>

        <div class="about_con col-md-offset-4 col-lg-offset-4">
          <left>
            <h1 class="contenthead">About Us</h1>
          </left>

          <h2>嗷呜嗷呜嗷呜 <br /><br />
            This is Shaik Maqsood. I'm a Freakin frontend developer, jus came up with this concept of having a
            45<sup>o</sup> trasformed DIV with a -45<sup>o</sup> background.<br /><br />
            Can't belive that it worked.
            <br /><br />
            Show your L<span>&hearts;</span>VE if you like my pen.
            <br /><br />
            <p>(NOTICE: The lady in the PIC is not me, I'm a guy :P)</p>
            <p><span style="text-align:right; color:#000000; font-size:18px;">* No matter what u say, that gal is sorta
                cute.</span></p>
          </h2>
        </div>
      </div>
      <br><br />
      <div class="row">
        <div class="containers  col-md-6 col-lg-offset-6">
          <div class="pic">
            <img src='http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155'>
          </div>
        </div>

        <div class="about_con col-md-offset-6 col-lg-offset-6">
          <center>
            <h1 class="contenthead">关于我们</h1>
          </center>

          <h2>Hi Folks, <br /><br />
            This is Shaik Maqsood. I'm a Freakin frontend developer, jus came up with this concept of having a
            45<sup>o</sup> trasformed DIV with a -45<sup>o</sup> background.<br /><br />
            Can't belive that it worked.
            <br /><br />
            Show your L<span>&hearts;</span>VE if you like my pen.
            <br /><br />
            <p>(NOTICE: The lady in the PIC is not me, I'm a guy :P)</p>
            <p><span style="text-align:right; color:#000000; font-size:18px;">* No matter what u say, that gal is sorta
                cute.</span></p>
          </h2>
        </div>
      </div>
      <br><br />

      <div class="row">
        <div class="containers col-lg-6 col-md-6">

          <div class="pic">
            <img src='http://thirdqq.qlogo.cn/g?b=oidb&k=MeibQYwUUWCQjBlLqYnmNHQ&kti=ZTPOSAAAAAE&s=100&t=1695971155'>
          </div>
        </div>

        <div class="about_con col-md-offset-6 col-lg-offset-6">
          <center>
            <h1 class="contenthead">关于我们</h1>
          </center>

          <h2>Hi Folks, <br /><br />
            This is Shaik Maqsood. I'm a Freakin frontend developer, jus came up with this concept of having a
            45<sup>o</sup> trasformed DIV with a -45<sup>o</sup> background.<br /><br />
            Can't belive that it worked.
            <br /><br />
            Show your L<span>&hearts;</span>VE if you like my pen.
            <br /><br />
            <p>(NOTICE: The lady in the PIC is not me, I'm a guy :P)</p>
            <p><span style="text-align:right; color:#000000; font-size:18px;">* No matter what u say, that gal is sorta
                cute.</span></p>
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

.containers {
  width: 550px;
  height: 100%;
  margin-left: 10px;
}

.pic {
  box-shadow: 6px 6px 7px #888888;
  width: 300px;
  height: 300px;
  position: relative;
  overflow: hidden;
  margin-top: 100px;
  margin-left: 135px;
  -ms-transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
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

.pic:hover {
  box-shadow: 3px 3px 7px #888888;
  cursor: pointer;
}

.about_con {
  height: 100%;
  width: 500px;
}

p {
  font-family: 'Open Sans Condensed', sans-serif !important;
}

h2 {
  font-family: 'Dancing Script', cursive !important;
}

.contenthead {
  width: max-content;
  left: 0;
  position: relative;
  // text-align: left;
  font-family: 'Open Sans Condensed', sans-serif;
  font-size: 50px;
  font-weight: 400;
  border-bottom: 4px solid #f89;
  // text-decoration: underline solid #B80C08 4px;
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
  padding-top: 1%;
  margin-bottom: 5%;
}

.about-us {
  background: linear-gradient(0, #B80C08, #F1844A);
  padding: 0 1%;
  padding-bottom: 5%;
  text-align: left;
}
</style>
