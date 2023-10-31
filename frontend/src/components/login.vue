

<script setup>
import axios from 'axios';
import qs from 'qs';
import { reactive, ref } from 'vue';

const isreg = ref(false)

</script>

<template>
    <div class="Login">
        <el-form :model="form" label-width="80px" size="default" :rules="rules(isreg)" ref="msgForm">
            <el-form-item label="用户名" prop="username">
                <el-input v-model="form.username" :validate-event="true" required />
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="form.password" :validate-event="true" type="password" required />
            </el-form-item>
            <Transition>
                <el-form-item v-show="isreg" label="确认密码" prop="confirmPassword">
                    <el-input v-model="form.confirmPassword" :validate-event="true" type="password" required />
                </el-form-item>
            </Transition>
            <el-form-item class="btn">
                <el-button type="primary" v-show="!isreg"
                    @click="log({ 'user': form.username, 'pwd': form.password })">登录</el-button>
                <el-button type="primary" v-show="isreg"
                    @click="reg({ 'user': form.username, 'pwd': form.password })">注册</el-button>
                <el-button @click="cancel">取消</el-button>
                <el-divider border-style="none" />
                <div class="el-alert__title" v-show="!isreg">没有账号?
                    <a @click="isreg = !isreg">注册</a>
                </div>
                <div class="el-alert__title" v-show="isreg">已有账号?
                    <a @click="isreg = !isreg">登录</a>
                </div>
            </el-form-item>
        </el-form>

    </div>
</template>
<script>
export default {
    data() {
        const form = reactive({
            username: '',
            password: '',
            confirmPassword: '',
        })
        const validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请重新输入密码！'))
            } else if (value !== this.form.password) {
                callback(new Error("两次输入的密码不匹配！"))
            } else {
                callback()
            }
        }
        const rule = reactive({
            username: [
                { required: true, message: '请输入用户名', trigger: 'blur' },
                { min: 3, max: 15, message: '长度在 3 到 15 个字符', trigger: 'blur' },
                { pattern: /^[a-zA-Z0-9_-]{3,15}$/, message: '用户名只能包含字母、数字、下划线和减号', trigger: 'blur' }
            ],
            password: [
                { required: true, message: '请输入密码', trigger: 'blur' },
                { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' },
                { pattern: /^[a-zA-Z0-9_@]{6,20}$/, message: '密码只能包含字母、数字、下划线和@', trigger: 'blur' }
            ],
            confirmPassword: [
                { required: true, message: '请再次输入密码', trigger: 'blur' },
                { validator: validatePass, trigger: 'blur' }
            ]
        })
        return {
            form,
            rule
        };
    },
    methods: {
        reg(form) {
            this.$refs.msgForm.validate((valid) => {
                if (valid) {
                    //提交表单
                    console.log(valid)
                    axios.post(`/api/user/reg`, qs.stringify(form)).then((res) => {
                        this.$emit('reg', res.data);
                    })
                }
                else {
                    this.$message({
                        message: '注册失败！请检查输入框中用户名和密码是否符合要求！',
                        showClose: true,
                        type: 'error'
                    })
                }
            })
            // console.log(form)

        },
        log(form) {
            this.$refs.msgForm.validate((valid) => {
                if (valid) {
                    //提交表单
                    console.log(valid)
                    axios.post(`/api/user/login`, qs.stringify(form)).then((res) => {
                        this.$emit('log', res.data);
                    })
                }
                else {
                    this.$message({
                        message: '请输入正确的用户名和密码！',
                        showClose: true,
                        type: 'error'
                    })
                }
            })
            // this.$refs.msgForm.validate().then((valid) => {

            // })
        },
        rules(isreg) {
            if (isreg) {
                return this.rule
            }
            else return {
                username: this.rule.username,
                password: this.rule.password
            };
        },
        cancel() {
            this.$emit('cancel')
        }
    }
}
</script>
<style>
.v-enter-active {
    transition: all 0.3s ease-in;
}

.v-leave-active {
    transition: all 0.3s ease-out;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}

label {
    position: absolute;
    top: 0;
    left: 0;
    padding: 0 5px !important;
    font-size: 16px;
    justify-content: flex-start !important;
    color: #000 !important;
    pointer-events: none;
    transition: .5s;
}

.btn>.el-form-item__content {
    margin: 0 !important;
    display: flex;
    justify-content: center;
}

.Login el-form-item__content {
    width: 100%;
    padding: 10px 0;
    font-size: 16px;
    /* color: #fff; */
    /* margin-bottom: 40px; */
    border: none !important;
    border-bottom: 1px solid #000;
    outline: none;
    background: transparent;

}

.el-input__wrapper {
    background: transparent !important;
}

.Login .el-form-item {
    position: relative;
    margin-bottom: 40px;
}

.btn {
    margin-bottom: 10px !important
}

.el-form-item:has(input:focus) label {
    top: -90%;
    left: 0;
    color: #03e9f4;
    font-size: 12px;
}

.el-form-item:has(input:valid) label {
    top: -90%;
    left: 0;
    color: #03e9f4;
    font-size: 12px;
}

.Login .el-button {
    margin: 0 10px;
    background: rgba(57, 88, 69, 0.4);
    border-radius: 999px;
    box-shadow: rgba(57, 88, 69, 0.4) 0 10px 20px -10px;
    box-sizing: border-box;
    color: #FFFFFF;
    cursor: pointer;
    font-family: Inter, Helvetica, "Apple Color Emoji", "Segoe UI Emoji", NotoColorEmoji, "Noto Color Emoji", "Segoe UI Symbol", "Android Emoji", EmojiSymbols, -apple-system, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", sans-serif;
    font-size: 16px;
    font-weight: 700;
    line-height: 24px;
    opacity: 1;
    outline: 0 solid transparent;
    padding: 10px 10px;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    width: fit-content;
    word-break: break-word;
    border: 0;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: all 2s ease-out;
    --el-color-primary: white;
    /* box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px; */
}

.Login .el-button:hover {
    background-color: rgba(12, 80, 38, 0.67);
}

.el-divider {
    margin: 5px;
}

.el-alert__title {
    box-sizing: border-box;
    color: #909399;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", 微软雅黑, Arial, sans-serif;
    font-size: 13px;
    line-height: 18px;
    vertical-align: text-top;
}

.el-alert__title a {
    font-weight: bolder;
    color: cornflowerblue !important;
}
</style>                                 