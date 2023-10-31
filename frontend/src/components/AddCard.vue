<script  lang="ts" setup>
import axios from 'axios'
import qs from 'qs';
import { ref, defineEmits } from 'vue'
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import router from '../router'
import type { UploadProps, UploadRequestOptions } from 'element-plus'

// if (sessionStorage.account == null || sessionStorage.account == '') {
//     router.push('/failed')
//     ElMessage({
//         message: '请注册/登录后再访问该页面！',
//         type: 'error'
//     })
//     setTimeout(() => router.push('/'), 2000)
// }
const emit = defineEmits(['cancel']);
function cancel() {
    emit('cancel');
}
const imageUrl = ref('')
const content = ref('')
const img = ref('')
let formData = new FormData()
const handleAvatarSuccess: UploadProps['onSuccess'] = (
    response,
    uploadFile
) => {
    imageUrl.value = URL.createObjectURL(uploadFile.raw!)
    console.log(uploadFile, formData.entries)
    // disabled.value = true
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
    console.log(rawFile.type)
    if ((rawFile.type !== 'image/jpeg') && (rawFile.type !== 'image/png')) {
        ElMessage.error('Avatar picture must be JPG format!')
        return false
    } else if (rawFile.size / 1024 / 1024 > 5) {
        ElMessage.error('上传的封面图不能超过5MB')
        return false
    }
    return true
}

function upload(file: UploadRequestOptions) {
    formData.append('smfile', file.file, file.file.uid.toString());
    console.log(formData.get('smfile'))
    file.onSuccess((res: any) => res);
}
function uploadToWeb() {
    if (imageUrl.value != '') {
        axios.post('/smms/v2/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Authorization': 'mWmwgu7hm7tkjIHgG4ZSghZbWlSW64Fg',
            },
        }).then((res) => {
            if (res.data.success === false) {
                if (res.data.code = 'image_repeated') {
                    img.value = res.data.images
                }
                else {
                    ElMessage.error('图片上传失败,请重试!')
                    // setTimeout(() => location.reload(), 1000)
                    return;
                }
            }
            else img.value = res.data.data.url;
            if (content.value.length < 6) {
                console.log('error')
                ElMessage.error('内容不能少于6个字!')
                return;
            }
            axios.post('/api/cards/add', qs.stringify({
                user: sessionStorage.account,
                content: content.value,
                img: img.value,
            })).then((res) => {
                if (res.data.success === true) {
                    // console.log(res);
                    ElMessage.success('上传成功')
                    setTimeout(() => location.reload(), 1000)
                }
                else {
                    ElMessage.error('上传失败,请重试!')
                    // setTimeout(() => location.reload(), 1000)
                }
            })
        });
    }
    else {
        if (content.value.length < 6) {
            console.log('error')
            ElMessage.error('内容不能少于6个字!')
            return;
        }
        axios.post('/api/cards/add', qs.stringify({
            user: sessionStorage.account,
            content: content.value,
            img: '',
        })).then((res) => {
            if (res.data.success === true) {
                console.log(res);
                ElMessage.success('上传成功')
                setTimeout(() => location.reload(), 1000)
            }
            else {
                ElMessage.error('上传失败,请重试!')
                // setTimeout(() => location.reload(), 1000)
            }
        })
    }
}
</script>
<template>
    <div class="addCard">
        <el-form ref="form" label-width="80px" :inline="false" size="normal">
            <h1>留言卡</h1>
            <el-form-item label="">
                <el-upload class="avatar-uploader" :drag="true" action="#" :show-file-list="false"
                    :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload" :http-request="upload">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar" />

                    <el-link v-else type="info" :underline="false">
                        <el-icon class="avatar-uploader-icon">
                            <Plus />
                        </el-icon>
                        添加封面
                    </el-link>
                </el-upload>
            </el-form-item>
            <el-form-item>
                <el-input type="textarea" v-model="content" placeholder="请输入留言内容" maxlength="250" show-word-limit />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="uploadToWeb">立即创建</el-button>
                <el-button @click="cancel">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<style scoped>
.avatar-uploader .avatar {
    width: 300px;
    height: 400px;
    display: block;
    object-fit: contain;
}
</style>

<style>
.el-link__inner {
    flex-direction: column;
}

.el-form-item__content {
    margin: 10px 10px !important;
    justify-content: center;
}

.addCard {
    background-color: azure;
    z-index: 20;
    position: absolute;
    top: 20%;
    left: 40%;
    width: fit-content;
    height: fit-content;
    padding: 10px 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    box-shadow: rgb(180, 216, 255) 0px 20px 30px -10px;
}

.el-textarea__inner {
    width: 20vw;
    height: 20vh;
}

.el-upload-dragger {
    width: 300px;
    height: 300px;
    justify-content: center;
    align-items: center;
    display: flex;
}

.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d !important;
    width: 300px;
    height: 178px;
    text-align: center;
}
</style>