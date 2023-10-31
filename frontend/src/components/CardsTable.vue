<template>
  <EasyDataTable v-model:items-selected="itemsSelected" :headers="headers" :items="items" buttons-pagination
    table-class-name="customize-table" :filter-options="filterOptions" show-index :loading="loading"
    :rows-items="[5, 10, 20]" :rows-per-page='5'>
    <template #header-operation="header">
      <div class="query-box">
        <el-button type="danger" @click="handleDelete(itemsSelected)">批量删除</el-button>
      </div>
    </template>
    <template #header-content="header">
      <div class="filter-column" style="align-items: center;
    display: flex;">
        <Filter style="width: 1em; height: 1em; margin-right: 8px" @click.stop="showConFilter = !showConFilter" />
        {{ header.text }}
        <div class="filter-menu filter-age-menu" v-if="showConFilter">
          <el-input v-model="conCriteria" placeholder="" size="normal"></el-input>
        </div>
      </div>
    </template>
    <template #header-create_time="header">
      <div class="filter-column" style="align-items: center;
    display: flex;">
        <Filter style="width: 1em; height: 1em; margin-right: 8px" @click.stop="showTimeFilter = !showTimeFilter" />
        {{ header.text }}
        <div>
          <SortDown v-if="timeSortDown" style="width: 1.2em; height: 1.2em; margin:0 8px" @click="changeSort" />
          <SortUp v-else style="width: 1.2em; height: 1.2em; margin:0 8px" @click="changeSort" />
        </div>
        <div class="filter-menu filter-age-menu" v-if="showTimeFilter">
          <el-input v-model="timeCriteria" placeholder="" size="normal"></el-input>
        </div>
      </div>
    </template>
    <template #item-operation="item">
      <el-button type="primary" size="default" @click="deleteItem(item)" color="red">
        <template #icon>
          <img src="@/assets/delete.jpg" alt="删除" class="operation-icon" />
        </template>
        删除
      </el-button>
    </template>
  </EasyDataTable>
  <!-- <div class="edit-item" v-if="isEditing">
    content:<input type="text" v-model="editingItem.content" />
    <br />
    create_time:<input type="text" v-model="editingItem.create_time" />
    <br />
    <button @click="submitEdit">ok</button>
  </div> -->

  <div>
    <h3>
      看一下选择的数据~ฅ( ̳• · • ̳ฅ)
    </h3>
    <pre v-for="item in itemsSelected">{{ JSON.stringify(item) }}</pre>
  </div>
</template>


<script lang="ts">
import type { Header, Item, FilterOption } from "vue3-easy-data-table";
import { defineComponent, ref, computed, ComponentInternalInstance, getCurrentInstance, reactive } from "vue";
import {
  Filter,
  SortUp,
  SortDown,
} from '@element-plus/icons-vue'
import axios from "axios";
import qs from "qs";
import router from "../router";
import { ElMessage } from "element-plus";
// import { mockClientItems } from "./mock";
// import { mockClientItems, mockServerItems } from "./mock";
export default defineComponent({
  setup() {
    // 表头
    const loading = ref(true);
    const headers: Header[] = [
      { text: "用户名", value: "username" },
      { text: "留言内容", value: "content", width: 400 },
      { text: "创建时间", value: "create_time" },
      { text: "管理", value: "operation" },
    ];
    // ];
    //数据（这个就不用改了，到时候得请求api得到）
    const items = ref<Item[]>([]);

    const timeCriteria = ref('');
    const conCriteria = ref('');
    if (sessionStorage.account != (null || '')) {
      console.log(sessionStorage.account)
      axios.get('/api/cards/get', {
        params: { 'user': sessionStorage.account },
      }).then((res) => {
        items.value = res.data.data;
        loading.value = false;
      })
    }
    else {
      console.log('未登录')
      router.push('/failed')
      ElMessage({
        message: '请注册/登录后再访问该页面！',
        type: 'error'
      })
      setTimeout(() => router.push('/'), 2000)
    }
    // function getMyCards() {
    //   if (sessionStorage.account != null || '') {
    //     axios.get('/api/cards/get', {
    //       params: { 'user': sessionStorage.account },
    //     }).then((res) => {
    //       items.value = res.data.data;
    //       loading.value = false;
    //     })
    //   }
    // }
    //删除
    const handleDelete = (itemsSelected: Item[]) => {
      let check = 1;
      for (const item of itemsSelected) {
        axios.post('/api/cards/delete', qs.stringify({
          user: item.username,
          create_time: item.create_time
        })
        ).then((res) => {
          if (res.data.success != true) {
            check = 0
          };
        })
      }
      if (!check) {
        ElMessage.error('批量删除出现错误！')
        setTimeout(() => location.reload(), 1000)
      }
      else {
        ElMessage.success('批量删除成功！')
        setTimeout(() => location.reload(), 1000)
      }
    }
    const filterOptions = computed((): FilterOption[] => {
      const filterOptionsArray: FilterOption[] = [];
      filterOptionsArray.push({
        field: 'create_time',
        criteria: timeCriteria.value,
        comparison: (value: string, criteria: string): boolean => (value != null && criteria != null &&
          typeof value === 'string' && value.includes(`${criteria}`)),
      });
      filterOptionsArray.push({
        field: 'content',
        criteria: conCriteria.value,
        comparison: (value: string, criteria: string): boolean => (value != null && criteria != null &&
          typeof value === 'string' && value.includes(`${criteria}`)),
      });
      return filterOptionsArray;
    });
    const timeSortDown = ref(true);
    function changeSort() {
      if (timeSortDown.value) {
        timeSortDown.value = !(timeSortDown.value);
        items.value.sort((a, b) => {
          // console.log(Number(new Date(a.create_time) > new Date(b.create_time)))
          return Number(new Date(a.create_time) < new Date(b.create_time)) - 1;
        })
        // console.log(items.value);
      }
      else {
        timeSortDown.value = !(timeSortDown.value);
        items.value.sort((a, b) => {
          // console.log(Number(new Date(a.create_time) < new Date(b.create_time)))
          return Number(new Date(a.create_time) > new Date(b.create_time)) - 1;
        });
        // console.log(items.value);
      }
    }
    const showTimeFilter = ref(false);
    const showConFilter = ref(false);


    // 这个别动
    const itemsSelected = ref<Item[]>([]);

    const deleteItem = (val: Item) => {
      axios.post('/api/cards/delete', qs.stringify({
        user: val.username,
        create_time: val.create_time
      })).then((res) => {
        if (res.data.success === true) {
          ElMessage.success('删除成功!');
          setTimeout(() => location.reload(), 1000);
        }
        else
          ElMessage.error('删除失败!')
      });
    };
    // const editItem = (val: Item) => {
    //   isEditing.value = true;
    //   const { username, content, create_time } = val;
    //   editingItem.username = username;
    //   editingItem.content = content;
    //   editingItem.create_time = create_time;
    // };
    // const submitEdit = () => {
    //   isEditing.value = false;
    //   const item = items.value.find((item) => item.username === editingItem.username);
    //   item.content= editingItem.content;
    //   item.create_time = editingItem.create_time;
    // };
    console.log(itemsSelected)
    return {
      handleDelete,
      headers,
      items,
      loading,
      itemsSelected,
      filterOptions,
      showTimeFilter,
      showConFilter,
      timeCriteria,
      conCriteria,
      changeSort,
      timeSortDown,
      deleteItem,
    };
  },
  components: {
    Filter,
    SortDown,
    SortUp,
  }
});


</script>
<style>
.operation-wrapper .operation-icon {
  width: 20px;
  cursor: pointer;
}

.el-input {
  margin-left: 5px;
}

.el-input__wrapper {
  box-shadow: 0 0 3px #e24017;
  --el-input-hover-border-color: var(--easy-table-footer-background-color);
  --el-input-focus-border-color: var(--easy-table-footer-background-color);
}

.customize-table {
  --easy-table-border: 1px solid #d43224;
  --easy-table-row-border: 1px solid #b34f21;

  --easy-table-header-font-size: 14px;
  --easy-table-header-height: 8vh;
  --easy-table-header-font-color: #de3724;
  --easy-table-header-background-color: #efcec0;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #110505;
  --easy-table-body-even-row-background-color: #e4e5e7;

  --easy-table-body-row-font-color: #de3724;
  --easy-table-body-row-background-color: #efcec0;
  --easy-table-body-row-height: 12vh;
  --easy-table-body-row-font-size: 14px;

  --easy-table-body-row-hover-font-color: #2d3a4f;
  --easy-table-body-row-hover-background-color: #eee;

  --easy-table-body-item-padding: 10px 15px;

  --easy-table-footer-background-color: #e24017;
  --easy-table-footer-font-color: #f7f4f1;
  --easy-table-footer-font-size: 14px;
  --easy-table-footer-padding: 0px 10px;
  --easy-table-footer-height: 5vh;

  --easy-table-scrollbar-track-color: #2d3a4f;
  --easy-table-scrollbar-color: #2d3a4f;
  --easy-table-scrollbar-thumb-color: #4c5d7a;
  --easy-table-scrollbar-corner-color: #2d3a4f;

  --easy-table-loading-mask-background-color: #2d3a4f;
}
</style>
