<script setup>
import card from '../components/Cards.vue';
import Backtop from '../components/backtop.vue';
import Timeline from '../components/timeline.vue';
import AddCard from '../components/AddCard.vue';
import axios from 'axios';
import { ref } from 'vue';

</script>
<script>
export default {
    data() {
        const isAdd = ref(false);
        const Cards = ref([]);
        return {
            Cards,
            isAdd
        };
    },
    mounted() {
        if (sessionStorage.account == null || sessionStorage.account == '') {
            this.$router.push('/failed')
            this.$message({
                message: '请注册/登录后再访问该页面！',
                type: 'error'
            })
            setTimeout(() => this.$router.push('/'), 2000)
        }
        else {
            axios.get('/api/cards/all', {
                params: { user: sessionStorage.account }
            }).then(res => this.Cards = res.data.data)

        }
    },
    methods: {
        changeAddShow() {
            this.isAdd = !this.isAdd;
        },
        toTop() {
            this.$refs.top.scrollTo({
                top: 0,
                behavior: 'smooth',
            });
        }
    }
}
</script>
<template>
    <div class="CardView">
        <div class="Cards">
            <div class="postCards" ref="top">
                <button class="t" @click="toTop">留言板</button>
                <div class="container">
                    <!-- 就是这个data-image用来绑定图片，我写了一个问号表达式来判断，如果img存在就用，没有就用默认的五星红旗 -->
                    <card v-for="card in Cards" :data-image='card.img ? card.img : require("@/assets/index2.jpg")'>
                        <template #header>
                            <h1>{{ card.create_time }}</h1>
                        </template>
                        <template #content>
                            <p>{{ card.content }}</p>
                        </template>
                    </card>
                </div>
            </div>
            <Timeline></Timeline>
        </div>
    </div>
    <div v-show="isAdd">
        <AddCard @cancel="changeAddShow" />
    </div>
    <div class="mask" v-show="isAdd"></div>
    <Backtop name="写留言" top="79%" left="96%" @click="changeAddShow" />
</template>


<style lang="scss">
$hoverEasing: cubic-bezier(0.23, 1, 0.32, 1);
$returnEasing: cubic-bezier(0.445, 0.05, 0.55, 0.95);

//  {
//     margin: 40px 0;
//     font-family: "Raleway";
//     font-size: 14px;
//     font-weight: 500;
//     background-color: #BCAAA4;
//     -webkit-font-smoothing: antialiased;
// }
.postCards {
    // background-image: url("~@/assets/bg1.jpg");
    position: sticky;
    overflow-y: scroll;
    top: 0;
    background-attachment: fixed;
    margin: 0 10px;
    // padding-top: 1%;
    height: 100%;
    // padding-top: 5px;
    border-top-width: 50px;
    border-top-color: transparent;
    border-radius: 3rem 3rem 0 0;
    -ms-overflow-style: none;
    scrollbar-width: none;
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
}

.postCards::-webkit-scrollbar {
    display: none;
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

.Cards {
    width: 60%;
    height: 100%;
}

.CardView {
    position: relative;
    height: 100%;
}


.t {
    display: inline-block;
    position: sticky;
    z-index: 1;
    overflow: hidden;
    text-align: center;
    text-decoration: none;
    font-family: "Raleway";
    font-weight: 600;
    font-size: 2em;
    top: 0;
    background-color: #fff;
    padding: 0.75em 1em;
    color: blue;
    border: 0.11em solid blue;
    // border-radius: 2em 2em 0 0;
    transition: 3s;
    width: 100%;
}

.t:before,
.t:after {
    content: "";
    position: absolute;
    top: -1.5em;
    z-index: -1;
    width: 200%;
    aspect-ratio: 1;
    border: none;
    border-radius: 40%;
    background-color: rgba(0, 0, 255, 0.25);
    transition: 3s;
}

.t:before {
    left: -80%;
    transform: translate3d(0, 5em, 0) rotate(-340deg);
}

.t:after {
    right: -80%;
    transform: translate3d(0, 5em, 0) rotate(390deg);
}

.t:hover {
    color: white;
}

.t:hover:before,
.t:hover:after {
    transform: none;
    background-color: rgba(0, 0, 255, 0.75);
}


p {
    line-height: 1.5em;
}

h1+p,
p+p {
    margin-top: 10px;
}

.container {
    max-width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around
}

.card-wrap {
    margin: 10px;
    transform: perspective(800px);
    transform-style: preserve-3d;
    cursor: pointer;
    // background-color: #fff;
    height: max-content;

    &:hover {
        .card-info {
            transform: translateY(0);
        }

        .card-info p {
            opacity: 1;
        }

        .card-info,
        .card-info p {
            transition: 0.6s $hoverEasing;
        }

        .card-info:after {
            transition: 5s $hoverEasing;
            opacity: 1;
            transform: translateY(0);
        }

        .card-bg {
            transition:
                0.6s $hoverEasing,
                opacity 5s $hoverEasing;
            opacity: 0.8;
        }

        .card {
            transition:
                0.6s $hoverEasing,
                box-shadow 2s $hoverEasing;
            box-shadow:
                rgba(white, 0.2) 0 0 40px 5px,
                rgba(white, 1) 0 0 0 1px,
                rgba(black, 0.66) 0 30px 60px 0,
                inset #333 0 0 0 5px,
                inset white 0 0 0 6px;
        }
    }
}

.card {
    position: relative;
    flex: 0 0 240px;
    width: 270px;
    height: 360px;
    background-color: #333;
    overflow: hidden;
    border-radius: 10px;
    align-items: center;
    box-shadow:
        rgba(black, 0.66) 0 30px 60px 0,
        inset #333 0 0 0 5px,
        inset rgba(white, 0.5) 0 0 0 6px;
    transition: 1s $returnEasing;
}

.card-bg {
    opacity: 0.5;
    position: absolute;
    // top: -20px;
    // left: -20px;
    width: 100%;
    height: 100%;
    padding: 20px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: fill;
    transition:
        1s $returnEasing,
        opacity 5s 1s $returnEasing;
    pointer-events: none;
}

.card-info {
    padding: 20px;
    position: absolute;
    // top: 20%;
    color: #fff;
    transform: translateY(200px);
    transition: 0.6s 1.6s cubic-bezier(0.215, 0.61, 0.355, 1);

    p {
        opacity: 0;
        text-shadow: rgba(black, 1) 0 2px 3px;
        transition: 0.6s 1.6s cubic-bezier(0.215, 0.61, 0.355, 1);
    }

    * {
        position: relative;
        z-index: 1;
    }

    &:after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        z-index: 0;
        width: 100%;
        height: 100%;
        background-image: linear-gradient(to bottom, transparent 0%, rgba(#000, 0.6) 100%);
        background-blend-mode: overlay;
        opacity: 0;
        transform: translateY(100%);
        transition: 5s 1s $returnEasing;
    }
}

.card-info h1 {
    font-family: "Playfair Display";
    font-size: 36px;
    color: white;
    font-weight: 700;
    text-shadow: rgba(black, 0.5) 0 10px 10px;
}
</style>