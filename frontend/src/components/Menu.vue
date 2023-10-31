<template style="position:relative">
  <!-- 菜单栏组件 -->
  <el-menu mode="horizontal" :ellipsis="false" :router="true" :default-active="activeIndex">
    <div v-for="(submenus, index) in menu">
      <div v-if="isItem(submenus)">
        <el-sub-menu :index="submenus.index" :key="submenus.key">
          <template #title><b>{{ submenus.title }}</b></template>
          <el-menu-item v-for="(item) in submenus.menus" :index="item.index" :key="item.key">
            <b>{{ item.title }}</b>
          </el-menu-item>
        </el-sub-menu>
      </div>
      <div v-else>
        <el-menu-item :index="submenus.index" :key="submenus.key">
          <b v-html="submenus.title">
          </b>
        </el-menu-item>
      </div>
    </div>
  </el-menu>
  <el-menu mode="horizontal" :ellipsis="false">
    <el-menu-item index="apidoc" key="4" @click="	window.location.href = 'http://127.0.0.1:5000/static/index.html'">
      <b>
        <a class="api" href="http://127.0.0.1:5000/static/index.html">API文档</a>
      </b>
    </el-menu-item>
    <el-menu-item class="login" :index="menuNoRouter[0].index" :key="menuNoRouter[0].key" @click="checkLogin" ref="active"
      v-if="!islogin">
      <b>{{ menuNoRouter[0].title }}</b>
    </el-menu-item>
    <el-sub-menu :index="menuNoRouter[1].index" :key="menuNoRouter[1].key" v-else>
      <template #title><b>{{ account }}</b></template>
      <el-menu-item v-for="(item) in menuNoRouter[1].menus" :index="item.index" :key="item.key"
        @click="userControll(item.key)">
        <b>{{ item.title }}</b>
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
  <div v-show="login">
    <Login @reg="reg_s" @log="log_s" @cancel="cancel"></Login>
  </div>
  <div class="mask" v-show="login"></div>
</template>
<style lang="scss">
a.api {
  &:link {
    color: rgb(0, 0, 0);
    text-decoration: none;
  }

  //未访问：蓝色、无下划线 
  &:active {
    color: rgb(0, 0, 0);
  }

  //激活：红色 
  &:visited {
    color: rgb(0, 0, 0);
    text-decoration: none;
  }

  //已访问：紫色、无下划线 
  &:hover {
    color: white;
    text-decoration: none;
  }

  //鼠标移近：红色、下划线 
}

.Login {
  position: absolute;
  top: 600%;
  left: 40%;
  z-index: 11;
  width: max-content;
  height: auto;
  display: flex;
  flex-direction: column;
  padding: 40px;
  text-align: center;
  box-sizing: border-box;
  background-color: rgba(127, 255, 212, 0.746);
  // background: inherit;
  border-radius: 18px;
  box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
}

.mask {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  left: 0;
  bottom: 0;
  z-index: 10;
  /* display: none; */
}
</style>
<script>

import { ref, reactive, computed } from "vue";
import Login from "@/components/login.vue";
import { useUserStore } from '@/stores/user'
/*
const Menu = ref();
Menu.value.open("2");

onMounted(()=>{
        Menu.value.open("2");
    })
*/

export default {
  name: "Menu",
  components: {
    Login
  },
  data() {
    const store = useUserStore();
    const login = ref(false);//控制登录注册界面的显示
    const islogin = computed(() => JSON.parse(store.islogin));
    const account = computed(() => store.account);
    // console.log(user)
    const menu = reactive([
      {
        index: "/",
        key: "1",
        title: "主页",
      },
      {
        index: "/cards",
        key: "2",
        title: "留言墙",

      },
      {
        index: "/about",
        key: "3",
        title: "关于我们",
      },
    ]);
    const menuNoRouter = reactive([
      {
        index: "/login",
        key: "4",
        title: "登录",
      },
      {
        index: "/console",
        key: "5",
        menus: [
          {
            key: "username",
            title: "我的卡片",
            index: "/mycards",
          },
          {
            key: "logout",
            title: "退出账号",
            index: "/7-2",
          },
        ]
      },
    ])
    const active = ref(null);
    return {
      activeIndex: "",
      menu,
      menuNoRouter,
      active,
      login,
      account,
      islogin,
      store
    }
  },
  watch: {
    $route() {
      this.setCurrentRoute();
    },
  },
  created() {
    this.setCurrentRoute();

  },
  methods: {
    isItem(submenus) {
      if ("menus" in submenus) {
        // console.log(true);
        return true;
      } else {
        // console.log(false);
        return false;
      }
    },
    userControll(key) {
      if (key == "logout") {
        setTimeout(() => {
          this.store.updateIslogin(false);
          this.store.updateAccount('');
          console.log(this.islogin);
          location.reload();
        }, 600)
      }
      if (key == "username") {
        this.$router.push('/mycards');
      }
    },
    setCurrentRoute() {
      this.activeIndex = this.$route.path; // 通过他就可以监听到当前路由状态并激活当前菜单
    },
    checkLogin() {//改变菜单栏登录激活状态
      this.login = !this.login;
      setTimeout(() => {
        this.$refs.active.rootMenu.activeIndex = ''
      }, 200)
        ;
    },
    reg_s(res) {
      // console.log(res);
      if (res.success) {
        // this.account = res.data.user;
        this.store.updateAccount(res.data.user);
        this.$message({
          message: res.msg,
          type: 'success',
          showClose: true,
          duratione: 1000,
          onclose: () => {
            location.reload();
            // this.islogin = !this.islogin;//控制登录和用户菜单的显示
            this.store.updateIslogin(!this.islogin);
            this.login = !this.login;//控制登录窗口的显示
            return;
          }
        })
        location.reload();
        // this.islogin = !this.islogin;
        this.store.updateIslogin(!this.islogin);
        this.login = !this.login;
      }
      else {
        this.$message({
          message: res.msg,
          type: 'error',
          showClose: true,
          duratione: 1000,
        })
      }
    },
    log_s(res) {
      if (res.success) {
        // this.account = res.data.user;
        this.store.updateAccount(res.data.user);
        this.$message({
          message: res.msg,
          type: 'success',
          showClose: true,
          duratione: 1000,
          onclose: () => {
            location.reload();
            // this.islogin = !this.islogin;
            this.store.updateIslogin(!this.islogin);
            console.log(this.islogin);
            this.login = !this.login;
            return;
          }
        })
        location.reload();
        // this.islogin = !this.islogin;
        this.store.updateIslogin(!this.islogin);
        console.log(this.islogin);
        this.login = !this.login;
      }
      else {
        this.$message({
          message: res.msg,
          type: 'error',
          showClose: true,
          duratione: 1000,
        })
      }
    },
    cancel() {
      this.login = !this.login;
    }

  },
};
</script>