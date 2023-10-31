import { defineStore } from "pinia";
export const useUserStore = defineStore("user", () => {
  const account = sessionStorage.getItem("account") || "";
  //   function increment() {
  //     count.value++;
  //   }
  const islogin = sessionStorage.getItem("islogin") || false;
  function updateAccount(account) {
    console.log(account);
    sessionStorage.setItem("account", account);
  }
  function updateIslogin(islogin) {
    console.log(islogin);
    sessionStorage.setItem("islogin", islogin);
  }
  return {
    account,
    islogin,
    updateAccount,
    updateIslogin,
  };
});
