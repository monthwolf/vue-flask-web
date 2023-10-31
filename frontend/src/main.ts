import { createApp } from "vue";
import { createPinia } from 'pinia';
import "element-plus/dist/index.css";
import './assets/index.css';
import 'animate.css';
import '@/assets/index1.css';
import '@/assets/style.css';
import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import '@/assets/bootstrap.min.css';
import $ from 'jquery';
import '@/assets/new_file3.css';
const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.component("EasyDataTable", Vue3EasyDataTable);
app.use(router);
app.use(ElementPlus);
app.mount("#app");


