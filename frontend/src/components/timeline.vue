<template lang="pug">
Backtop(@click="toTop")
<div class="cont Timeline" ref="timeline">

<div class="time" style="width:100%">
#timeline-1.timeline-container
    .timeline-header
        h2.timeline-header__title 百 年 党 史
        h3.timeline-header__subtitle 致我们可爱的党
    .timeline
        .timeline-item(data-text='中共⼀⼤')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/古田会议.png')
                h2.timeline__content-title
                    | 1921.7
                p.timeline__content-desc
                    | 上海浙江嘉兴   
                p.timeline__content-desc
                    | 确定了党的名称为“中国共产党”。宣告了中国共产党的正式成⽴。选举陈独秀为中央局书记。
        .timeline-item(data-text='中共二大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/中共二大.png')
                h2.timeline__content-title
                    | 1922.7
                p.timeline__content-desc
                    | 上海   
                p.timeline__content-desc
                    | 分析了国际形势，制定了党的最⾼纲领和最低纲领。在中国近代史上第⼀次提出了彻底的反帝反封建的⺠主⾰命纲领。
        .timeline-item(data-text='中共三⼤')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/中共三大.png')
                h2.timeline__content-title 1923.6
                p.timeline__content-desc
                    | ⼴州   
                p.timeline__content-desc
                    | 决定全体共产党员以个⼈名义加⼊国⺠党，以建⽴各⺠主阶级的统⼀战线，同时 保持共产党在组织上、政治上的独⽴性。
        .timeline-item(data-text='国共第⼀次合作')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/国共第一次合作.png')
                h2.timeline__content-title 1924
                p.timeline__content-desc
                    | ⼴州   
                p.timeline__content-desc
                    | 会上确定了“联俄、联共、扶助农⼯”的政策，并确⽴新三⺠主义。国⺠党⼀⼤的 召开，标志着第⼀次国共合作的正式形成。
        .timeline-item(data-text='中共四⼤')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/中共四大.png')
                h2.timeline__content-title 1925.1
                p.timeline__content-desc
                    | 上海   
                p.timeline__content-desc
                    | ⼤会着重讨论了⽆产阶级在⺠族⾰命运动中的地位，提出⽆产阶级在⺠主⾰命中 的领导权问题和⼯农联盟问题。
        .timeline-item(data-text='南昌起义、⼋七会议、秋收起义')
            .timeline__content
                img.timeline__img(src="@/assets/timeline/南昌起义.png")
                h2.timeline__content-title 1927
                p.timeline__content-desc
                    | 南昌、汉⼝、湖南   
                p.timeline__content-desc
                    | 1.南昌起义打响了武装反抗国⺠党统治的第⼀枪。
                p.timeline__content-desc
                    | 2.⼋七会议总结了 失败教训，纠正了陈独秀右倾投降主义错误，确定了⼟地⾰命和武装反抗国⺠党反动派统治 的总⽅针，提出政权是从枪杆⼦中取得的。
                p.timeline__content-desc
                    | 3.秋收起义：⽂家市决策提出战略重⼼转移；三 湾改编；创⽴了第⼀个农村⾰命根据地井冈⼭⾰命根据地。
        .timeline-item(data-text='中共五⼤')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/中共五大.png')
                h2.timeline__content-title 1927.4
                p.timeline__content-desc
                    | 汉⼝   
                p.timeline__content-desc
                    | 批评了陈独秀的右倾错误，实际上没有解决任何问题。
        .timeline-item(data-text='古⽥会议')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/古田会议.png')
                h2.timeline__content-title  1929.12
                p.timeline__content-desc
                    | 福建古⽥
                p.timeline__content-desc
                    | 提出建设新型军队，提出“思想上建党、政治上建军”的原则。
        .timeline-item(data-text='遵义会议')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/遵义会议.png')
                h2.timeline__content-title 1935.1
                p.timeline__content-desc
                    | 遵义
                p.timeline__content-desc
                    | 开始确⽴了以⽑泽东为代表的新的中央的正确领导；总·甲国共产党第⼀次独⽴ ⾃主地运⽤⻢克思列宁主义原理解决中国⾰命问题；是中国共产党从幼年⾛向成熟的标志。 
        .timeline-item(data-text='瓦窑堡会议')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/瓦窑堡会议.png')
                h2.timeline__content-title 1935.12
                p.timeline__content-desc 
                    | 陕北 瓦窑堡
                p.timeline__content-desc
                    | 决定建⽴最⼴泛的抗⽇⺠族统⼀战线。
        .timeline-item(data-text='洛川会议')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/洛川会议.png')
                h2.timeline__content-title 1937.8
                p.timeline__content-desc
                    | 洛川
                p.timeline__content-desc
                    | 会议决定把党的⼯作重⼼放在战区和敌后，建⽴敌后抗⽇根据地。
        .timeline-item(data-text='中共七⼤')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/中共七大.png')
                h2.timeline__content-title 1945.4
                p.timeline__content-desc
                    | 延安
                p.timeline__content-desc
                    | 《论联合政府》提出党的三⼤作⻛：理论联系实践，密切联系群众，批评与⾃我 批评。
        .timeline-item(data-text='七届⼆中全会')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/七届二中全会.png')
                h2.timeline__content-title 1949.3
                p.timeline__content-desc
                    | ⻄柏坡
                p.timeline__content-desc
                    | ⼯作重⼼由农村转移到城市；关于在新形势下加强党的建设的问题。
        .timeline-item(data-text=' 中共⼋⼤')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/中共八大.png')
                h2.timeline__content-title 1956
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 分析了国内形势和主要⽭盾的变化，指出我国国内的主要⽭盾是⼈⺠对经济⽂化 迅速发展的需求同当前经济⽂化不能满⾜⼈⺠需要的状况之间的⽭盾。
        .timeline-item(data-text='⼗⼀届三中全会')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十一届三中全会.png')
                h2.timeline__content-title 1978.12
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 邓⼩平：《解放思想，实事求是，团结⼀致向前看》，重新确⽴了解放思想、实事 求是的原则；作出了把党的⼯作重点转移到社会主义现代化建设上来的战略决策；提出了改⾰开放的重要思想。
        .timeline-item(data-text='中共十二大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十二大.png')
                h2.timeline__content-title 1982.9
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 邓⼩平正式提出了提出⾛⾃⼰的道路“建设有中国特⾊的社会主义”的新命题。完 整系统地提出了全⾯建设社会主义的纲领和各项⽅针政策。它标志着建设有中国特⾊社会主 义思想的正式确⽴。
        .timeline-item(data-text='中共十三大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十三大.png')
                h2.timeline__content-title 1987.10
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | ⾸次系统地阐述了关于社会主义初级阶段的理论：已经进⼊社会主义初级阶段， ⻓期处于社会主义初级阶段。
                p.timeline__content-desc
                    | 党在社会主义初级阶段的基本路线：⼀个中⼼：经济建设(核_⼼)。两个基本点：四项基 本原则(⽴国之本)、改⾰开放(强国之路)。
        .timeline-item(data-text='中共十四大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十四大.png')
                h2.timeline__content-title 1992.10
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | ⾸次使⽤“邓⼩平同志建设有中国特⾊的社会主义理论”的提法。确定我国经济体 制改⾰⽬标是建⽴社会主义市场经济体制。
        .timeline-item(data-text='中共十五大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十五大.png')
                h2.timeline__content-title 1997.9
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 把邓⼩平理论确定为党的指导思想。把依法治国确定为治国的基本⽅略，完整地 提出和深刻阐述了党在社会主义初级阶段的基本纲领。
        .timeline-item(data-text='中共十六大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十六大.png')
                h2.timeline__content-title 2002.11
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | ⾼举邓⼩平理论伟⼤旗帜，全⾯贯彻“三个代表”重要思想，继往开来，与时俱进， 提出全⾯建设⼩康社会的奋⽃⽬标。
        .timeline-item(data-text='中共十七大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十七大.png')
                h2.timeline__content-title 2007.10
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | ⾼举中国特⾊社会主义伟⼤旗帜，以邓⼩平理论和“三个代表”重要思想为指导， 深⼊贯彻落实科学发展观，继续解放思想，坚持改⾰开放，推动科学发展，促进社会和谐，为夺取全⾯建设⼩康社会新胜利⽽奋⽃。
        .timeline-item(data-text='中共十八大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十八大.png')
                h2.timeline__content-title 2012.11
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 明确了科学发展观是党必须⻓期坚持的指导思想，并写⼊党章。制定了坚持⾛中 国特⾊社会主义政治发展道路和推进政治体制改⾰前进⽅向。提出了全⾯建成⼩康社会⽬标。
        .timeline-item(data-text='中共十九大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十九大.png')
                h2.timeline__content-title 2017.10
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 不忘初⼼，牢记使命，⾼举中国特⾊社会主义伟⼤旗帜，决胜全⾯建 成⼩康社会，夺取新时代中国特⾊社会主义伟⼤胜利，为实现中华⺠族伟⼤复兴的中国梦不懈奋⽃。
        .timeline-item(data-text='⼗九届六中全会')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/十九届六中全会.png')
                h2.timeline__content-title 2021.11
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | 审议通过了《中共中央关于党的百年奋⽃重⼤成就和历史经验的决议》和《关于 召开党的第⼆⼗次全国代表⼤会的决议》。
        .timeline-item(data-text='中共二十大')
            .timeline__content
                img.timeline__img(src='@/assets/timeline/二十大.png')
                h2.timeline__content-title 2022.10
                p.timeline__content-desc
                    | 北京
                p.timeline__content-desc
                    | ⾼举中国特⾊社会主义伟⼤旗帜，全⾯贯彻新时代中国特⾊社会主义思想，弘扬 伟⼤建党精神，⾃信⾃强、守正创新，蹲厉奋发、勇驰⾏，为全⾯建设社会主义现代化国家、 全⾯推进中华⺠族伟⼤复兴⽽团结奋⽃。
</div>
</div>
</template>

<script>
import Backtop from './backtop.vue';
export default {
    components: {
        Backtop
    },
    mounted() {
        (function ($) {
            $.fn.timeline = function () {
                var selectors = {
                    id: $(this),
                    item: $(this).find(".timeline-item"),
                    activeClass: "timeline-item--active",
                    img: ".timeline__img"
                };
                // console.log(selectors.item);
                selectors.item.eq(0).addClass(selectors.activeClass);
                selectors.id.css(
                    "background-image",
                    "url(" + selectors.item.first().find(selectors.img).attr("src") + ")"
                );
                var itemLength = selectors.item.length;
                $('.Timeline').scroll(function () {
                    var max, min;
                    var pos = $(this).scrollTop();
                    selectors.item.each(function (i) {
                        var m1 = selectors.item.eq(0).offset().top;
                        // var m2 = m1 + selectors.item.eq(0).height();
                        // console.log({ 'm1': m1, 'm2': m2 })
                        min = $(this).offset().top - m1;
                        max = $(this).height() + $(this).offset().top - m1;
                        var that = $(this);
                        // console.log({
                        //     'i': i,
                        //     'min': min,
                        //     'max': max,
                        //     'pos': pos,
                        //     'height': $(this).height(),
                        //     'this': $(this)
                        // });
                        if (i == itemLength - 2 && pos > min + $(this).height() / 2) {

                            selectors.item.removeClass(selectors.activeClass);
                            selectors.id.css(
                                "background-image",
                                "url(" + selectors.item.last().find(selectors.img).attr("src") + ")"
                            );
                            selectors.item.last().addClass(selectors.activeClass);
                        } else
                            if (pos <= max && pos >= min) {
                                selectors.id.css(
                                    "background-image",
                                    "url(" + $(this).find(selectors.img).attr("src") + ")"
                                );
                                selectors.item.removeClass(selectors.activeClass);
                                $(this).addClass(selectors.activeClass);
                            }
                    });
                });
            };
        })(jQuery);
        // console.log($("#timeline-1"))
        $("#timeline-1").timeline();
    },
    methods: {
        toTop() {
            // console.log(this.$refs);
            this.$refs.timeline.scrollTo({
                top: 0,
                behavior: 'smooth'
            })
        },

    },
}


</script>

<style lang="scss">
// 我的
body {
    font-family: "Microsoft YaHei";
    background: #eee;
    /* This is just a helper in case the element has a transparent background or white colors. */
}

.cont {
    top: 0;
    right: 0;
    position: absolute;
    width: 40%;
    height: 100%;
    overflow-y: scroll;

}

.cont {
    overflow: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.cont::-webkit-scrollbar {
    display: none;
}

@media only screen and (min-width: 768px) and (max-width: 959px) {
    div#page>div {
        width: 768px;
    }
}

@media only screen and (max-width: 767px) {
    div#page>div {
        width: 100%;
    }
}

@media only screen and (min-width: 620px) and (max-width: 767px) {
    div#page>div {
        width: 100%;
    }
}

@media only screen and (max-width: 619px) {
    div#page>div {
        width: 100%;
    }
}

div.contentHead {
    box-shadow: rgba(142, 142, 142, 0.2) 0 3px 3px;
    box-sizing: border-box;
    color: #D3DCE6;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 35px;
    line-height: 19px;
    margin-left: -20px;
    padding: 15px;
    text-align: center;
    user-select: none;
}

h2.timeline__content-title {
    box-sizing: border-box;
    color: #C00516 !important;
    display: inline-block;
    font-family: Poppins, sans-serif;
    font-size: calc(1.325rem + .9vw);
    font-weight: 700;
    line-height: 1.2;
    margin: 0;
    text-align: left;
    user-select: none;
}

@media (min-width: 1200px) {
    .exportedElement>div:nth-child(1)>h2 {
        font-size: 2rem;
    }
}

// 原来的



@import url('https://fonts.googleapis.com/css?family=Cardo|Pathway+Gothic+One');

// Responsive
@mixin responsive() {
    @media only screen and (max-width: 767px) {
        @content;
    }
}

$content-font: Cardo !important;
$heading-font: '楷体', sans-serif !important;
$timeline-width: 700px;
$timeline-container-width: 100%;

.timeline {
    display: flex;
    margin: 0 auto;
    flex-wrap: wrap;
    flex-direction: column;
    max-width: $timeline-width;
    position: relative;

    &__content {
        &-title {
            font-weight: normal;
            font-size: 66px;
            margin: -10px 0 0 0;
            transition: .4s;
            padding: 0 10px;
            box-sizing: border-box;
            font-family: $heading-font;
            color: #fff;
        }

        &-desc {
            margin: 10px;
            font-size: 15px;
            box-sizing: border-box;
            color: rgba(#ffffffa6, .7) !important;
            font-family: $content-font;
            text-align: left;
            font-weight: normal;
            line-height: 25px;
        }

        &-desc:nth-of-type(1) {
            text-align: right;
            font-size: 20px !important;
            font-weight: bolder;
            color: #ff0000 !important;
        }
    }

    &:before {
        position: absolute;
        left: 50%;
        width: 2px;
        height: 100%;
        margin-left: -1px;
        content: "";
        background: rgba(255, 255, 255, .07);

        @include responsive() {
            left: 40px;
        }
    }

    &-item {
        padding: 40px 0;
        opacity: .3;
        filter: blur(2px);
        transition: .5s;
        box-sizing: border-box;
        width: calc(50% - 40px);
        display: flex;
        position: relative;
        transform: translateY(-80px);

        &:before {
            content: attr(data-text);
            text-align: justify;
            letter-spacing: 3px;
            width: 100%;
            position: absolute;
            color: rgba(#fff, .8);
            font-size: 20px;
            font-family: $heading-font;
            font-weight: bolder;
            border-left: 2px solid rgba(#fff, .5);
            top: 60% !important;
            margin-top: -5px;
            padding-left: 15px;
            opacity: 0;
            right: calc(-100% - 56px);
        }

        &:nth-child(even) {
            align-self: flex-end;

            & p {
                text-align: left;
            }

            &:before {
                right: auto;
                text-align: right;
                left: calc(-100% - 56px);
                padding-left: 0;
                border-left: none;
                border-right: 2px solid rgba(#fff, .5);
                padding-right: 15px;
            }
        }

        &--active {
            opacity: 1;
            transform: translateY(0);
            filter: blur(0px);

            &:before {
                top: 50%;
                transition: .3s all .2s;
                opacity: 1;
            }

            .timeline__content-title {
                margin: -50px 0 20px 0;
            }
        }

        @include responsive() {
            align-self: baseline !important;
            width: 100%;
            padding: 0 30px 150px 80px;

            &:before {
                left: 10px !important;
                padding: 0 !important;
                top: 50px;
                text-align: center !important;
                width: 60px;
                border: none !important;
            }

            &:last-child {
                padding-bottom: 40px;
            }
        }
    }

    &__img {
        max-width: 100%;
        box-shadow: 0 10px 15px rgba(0, 0, 0, .4);
    }

    &-container {
        width: $timeline-container-width;
        position: relative;
        padding: 80px 10px;
        transition: .3s ease 0s;
        background-attachment: fixed;
        background-size: cover;

        &:before {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(99, 99, 99, 0.8);
            content: "";
        }
    }

    &-header {
        width: 100%;
        text-align: center;
        margin-bottom: 80px;
        position: relative;

        &__title {
            color: #c50000;
            font-size: 46px;
            word-spacing: 4vw;
            font-family: $content-font;
            font-weight: normal;
            margin: 0;
        }

        &__subtitle {
            color: rgba(255, 255, 255, .5);
            font-family: $heading-font;
            font-size: 22px;
            letter-spacing: 5px;
            margin: 10px 0 0 0;
            font-weight: normal;
        }
    }
}

.timeline-desc:nth-child(even) {
    text-align: right;
}

.timeline-desc:nth-child(odd) {
    text-align: left;
}

// DEMO
.demo-footer {
    padding: 60px 0;
    text-align: center;

    a {
        color: #999;
        display: inline-block;
        font-family: $content-font;
    }
}
</style>