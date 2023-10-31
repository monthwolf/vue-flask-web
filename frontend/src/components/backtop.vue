<template>
    <!-- 边栏小部件 -->
    <div class="wrapper">
        <div id="scrollme">
            <div class="backtop">
                <span></span>
                <span></span>
                <p>{{ name }}</p>
            </div>
        </div>
    </div>
</template>
<script setup>
const props = defineProps({
    name: {
        type: String,
        default: '回到顶部',
    },
    top: {
        type: String,
        default: '85%',
    },
    left: {
        type: String,
        default: '96%',
    }
})
</script>

<style scoped>
/* backtop回到顶部样式 */
.wrapper {
    width: 100vw;
    overflow: hidden;
    padding: 0;
    margin: 0;
}

#scrollme {
    margin: 0 auto;
    /* height: 50px; */
    position: absolute;
    top: v-bind(top);
    left: v-bind(left);
    width: 60px;
    z-index: 6;
    /* color: #698fb7; */
    color: #ffe873;
}

.backtop {
    height: 50px;
    background-color: rgba(0, 0, 0, 0.146);
    cursor: pointer;
}

.backtop p {
    font-size: 12px;
    font-family: "Source Code Pro", monospace;
    font-weight: bolder;
    letter-spacing: 2px;
    margin-bottom: 50px;
    opacity: 0;
    transition: all 0.6s ease;
    -webkit-transition: all 0.6s ease;
    padding-top: 15px;
    text-align: center;
    margin: 0 auto;
}

#scrollme:hover p {
    opacity: 1;
    padding-top: 12px;
    font-size: 11px;
}

.backtop span {
    width: 20px;
    height: 2px;
    left: calc(50% - 10px);
    position: absolute;
    content: "";
    top: 20px;
    border-radius: 20px;
    transition: all 0.4s ease-in-out;
    -webkit-transition: all 0.4s ease-in-out;
    background-color: #ffe873;
}

.backtop span:nth-child(1) {
    transform: rotate(45deg);
    margin-left: 6px;
    z-index: 1;
}

.backtop span:nth-child(2) {
    transform: rotate(-45deg);
    margin-left: -7px;
    z-index: 1;
}

#scrollme:hover span {
    top: 35px;
    width: 20px;
    transition: all 0.4s ease-in-out;
    -webkit-transition: all 0.4s ease-in-out;
}

#scrollme:hover span:nth-child(1) {
    left: calc(50% - 5px);
    transform: rotate(180deg);

}

#scrollme:hover span:nth-child(2) {
    right: calc(50% - 5px);
    transform: rotate(-180deg);
}
</style>
    