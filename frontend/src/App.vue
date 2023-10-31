<script setup >
import Backtop from "@/components/backtop.vue";
import { ref, computed } from 'vue'
import { useScroll } from '@vueuse/core'

const content = ref(null)

const { x, y, arrivedState } = useScroll(content)

const isShow = computed(() => {
  if (y.value < 200) {
    return false;
  }
  else return true;
});
function toTop() {
  content.value.$el.scrollTo({
    top: 0,
    behavior: 'smooth'
  })

}
</script>

<template>
  <el-container direction="vertical" style="width: 100%">
    <el-header style="position:relative">
      <img class="logo" alt="Vue logo" src="@/assets/logo.svg" />
      <Menu></Menu>
    </el-header>
    <el-main height="80vh" ref="content">
      <Backtop v-show="isShow" @click="toTop" />

      <routerView></routerView>

    </el-main>
  </el-container>
</template>
<script>
import Menu from '@/components/Menu.vue';

export default {
  components: {
    Menu,
  },
  mounted() {
    console.log(this.$route.path)
  }
}
</script>