<template>
  <!-- 主页组件 -->
  <div ref="content">
    <!-- Backtop的用法 -->
    <!-- <Backtop name="显示爹文件" top="距离顶部多长" left="距离左边多长" /> -->

    <Page data-attr="图片长廊" color="#d3dce6" font-size="35px" top="13px">
      <template #content>
        <div class="home">
          <el-carousel :interval="4000" type="card" height="50vh">
            <el-carousel-item v-for="item in images" :key="item.id">
              <img :src="item.idView" class="image" style="height:100%;width:100%">
            </el-carousel-item>
          </el-carousel>
        </div>

        <!-- 上面插入原生html -->
      </template>
    </Page>
    <Page data-attr="风采展示" color="#d3dce6" font-size="35px" top="13px">
      <!-- 这个 -->
      <template #content>
        <div class="content content3">
          <div class="contentHead">
            <h2>红心向党</h2>
          </div>
          <div class="zhibo">
            <img src="@/assets/11.jpg" alt="">
            <div>
              <h5>红心向党聚能量，奋楫笃行铭初心。</h5>
              <p>
                <a href="javascript:void(0)" class="toSearch">
                  今年是中国共产党成立102周年，也是全面贯彻落实党的二十大精神的开局之年。在合庆镇党委号召引领下，各基层党组织坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻落实党的二十大精神，开展“七一”系列活动，献礼党的生日，进一步凝聚人心、汇聚力量。
                </a>
              </p>
            </div>
          </div>
          <div class="agendaList content3-tab">
            <div class="title">
              <span class="redMark">d</span>
              <span>理论强“心”谈感悟</span>
            </div>
            <ul>
              <li>
                <img src="@/assets/12.jpg" alt="">
                <div class="li-top"><a href="javascript:void(0)"
                    class="toSearch">合庆镇召开庆祝中国共产党成立102周年大会暨镇党委书记上党课专题报告会，推动全面贯彻落实党的二十大精神。</a>
                  <div class="bottomWord">人民日报 10-14</div>
                </div>
              </li>
              <li>
                <img src="@/assets/13.jpg" alt="">
                <div class="li-top"><a href="javascript:void(0)" class="toSearch">合庆镇开展“百名书记上讲台
                    千名党员谈感悟”活动，兴起学习贯彻习近平新时代中国特色社会主义思想的热潮。</a>
                  <div class="bottomWord">人民网 10-16</div>
                </div>

              </li>
            </ul>
          </div>
          <div class="agendaList content3-tab">
            <div class="title">
              <span class="redMark">d</span>
              <span>溯源初“心”再出发</span>
            </div>
            <ul>
              <li>
                <img src="@/assets/15.jpg" alt="">
                <div class="li-top"><a href="javascript:void(0)" class="toSearch">合庆镇各基层党组织开展“寻访初心之地
                    重温入党誓词”活动，让每一名党员感悟中国共产党人历久弥坚的初心使命。</a>
                  <div class="bottomWord">人民网 10-15</div>
                </div>
              </li>
              <li>
                <img src="@/assets/14.jpg" alt="">
                <div class="li-top"><a href="javascript:void(0)"
                    class="toSearch">高举右拳，面向鲜红的党旗庄严宣誓，字字铿锵，彰显了党员同志们不忘初心、牢记使命的坚定政治信念。</a>
                  <div class="bottomWord">新华社 10-16</div>
                </div>

              </li>
            </ul>
          </div>
          <div class="agendaList content3-tab">
            <div class="title">
              <span class="redMark">d</span>
              <span>铸牢忠“心”葆本色</span>
            </div>
            <ul>
              <li>
                <img src="@/assets/16.jpg" style="height: 110px;" alt="">
                <div class="li-top"><a href="javascript:void(0)"
                    class="toSearch">各基层党组织向我镇75名老党员颁发“光荣在党50年”纪念章，表达了崇高的敬意。</a>
                  <div class="bottomWord">人民网 10-23</div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </template>
    </Page>


    <!-- Page的用法 -->
    <!-- <Page data-attr="栏目名" color="文字颜色" font-size="字体大小" top="距离边框顶部的长度"></Page> -->


    <Page data-attr="建功新程" color="#d3dce6" font-size="35px" top="13px">
      <template #content>
        <div class="content content2">
          <div class="contentHead">
            <h2>奋楫笃行</h2>
          </div>
          <section id="grid" class="grid clearfix">
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-1.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>踔厉奋发</h2>
                  <p>行稳致远，以实干笃定前行。征途漫漫，惟有奋斗。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-2.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>赓续前行</h2>
                  <p>奋楫争先，以奋斗开启未来。“时间属于奋进者，历史属于奋进者！”</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>

            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-3.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>知责于心</h2>
                  <p>“以青春之我，创建青春之家庭，青春之国家，青春之民族”。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-4.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>担责于身</h2>
                  <p>强化理论学习，传播奋斗火种，把学习作为立身之基。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-5.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>履责于行</h2>
                  <p>践行实干担当，传递火热力量，全心全意为人民服务。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-6.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>凝心铸魂</h2>
                  <p>厚植群众情怀，提升群众幸福感，要把为群众服务的工作做实。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-7.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>见贤思齐</h2>
                  <p>以人为镜，见贤思齐强担当。以先进为标杆，以典型为榜样。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
            <a href="#" data-path-hover="m 180,34.57627 -180,0 L 0,0 180,0 z">
              <figure>
                <img src="@/assets/index-content2-8.jpg" />
                <svg viewBox="0 0 180 320" preserveAspectRatio="none">
                  <path d="M 180,160 0,218 0,0 180,0 z" />
                </svg>
                <figcaption>
                  <h2>臻于至善</h2>
                  <p>征途漫漫，道阻其长。唯笃志力行，方能领悟大道，修养身心。</p>
                  <button>查看</button>
                </figcaption>
              </figure>
            </a>
          </section>
        </div>
      </template>
    </Page>

    <Page data-attr="英雄人物" color="#d3dce6" font-size="35px" top="13px">
      <template #content>
        <div class="padding-30 rounded bordered" style="width: 1600px;">
          <div class="row gy-5">
            <div class="col-sm-6">
              <!-- post large -->
              <div class="post">
                <div class="thumb rounded">

                  <div class="inner">
                    <img src="@/assets/潘东升.jpg" alt="post-title" style='width: 700px;' />
                  </div>
                </div>
                <ul class="meta list-inline mt-4 mb-0">
                  <li class="list-inline-item" style="font-size: 30px;">潘东升</li>
                  <li class="list-inline-item" style="font-size: 30px;">1964年9月-2021年9月25日</li>
                </ul>
                <h5 class="post-title mb-3 mt-3" style="font-size: 25px;">鞠躬尽瘁护人民利益，忠诚担当铸警界丰碑。</h5>
                <p class="excerpt mb-0" style="color: #000;">
                  2021年9月25日，因长期超负荷工作，积劳成疾，在工作岗位突发疾病，因公牺牲，年仅57岁。从警37年，潘东升将毕生精力和全部心血都献给了崇高的人民公安事业，为捍卫政治安全、维护社会安定、保障人民安宁作出了积极贡献。潘东升牺牲后，被追授“时代楷模”“全国公安系统一级英雄模范”“福建省优秀共产党员”“八闽楷模”等称号。
                </p>
              </div>
              <!-- post -->
              <div class="post post-list-sm square before-seperator">
                <div class="thumb rounded">

                  <div class="inner">
                    <img src="@/assets/9.jpeg" alt="post-title" />
                  </div>

                </div>
                <div class="details clearfix">
                  <h6 class="post-title my-0">回首岁月心向党，忆苦思甜勇担当。</h6>
                  <ul class="meta list-inline mt-1 mb-0">
                    <li class="list-inline-item">
                      1951年5月23日在北京签订了《中央人民政府和西藏地方政府关于和平解放西藏办法的协议》，终于实现了中华人民共和国大陆的统一，这是西藏发展史上一个具有划时代意义的转折点。它标志着西藏永远摆脱了帝国主义侵略的羁绊，标志着中华民族大团结和祖国统一进入新的发展阶段，开辟了西藏从黑暗走向光明、从落后走向进步、从贫穷走向富裕、从封闭走向开放的新时代。
                    </li>
                  </ul>
                </div>
              </div>
              <!-- post -->
              <div class="post post-list-sm square before-seperator">
                <div class="thumb rounded">

                  <div class="inner">
                    <img src="@/assets/7.jpeg" alt="post-title" />
                  </div>

                </div>
                <div class="details clearfix">
                  <h6 class="post-title my-0">奋勇前进跟党走，砥砺前行新征程。</h6>
                  <ul class="meta list-inline mt-1 mb-0">
                    <li class="list-inline-item">
                      纵观西藏和平解放以来的发展历程，我们党领导藏族人民为推动西藏经济繁荣、社会进步付出了大量心血，西藏的经济社会发展取得了令世人惊叹的伟大成就，经济快速发展，文化日益繁荣，社会祥和进步，人民安居乐业，从城市中心到田间乡头；从教育新城到产业园区；都呈现出勃勃生机。
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="col-sm-6">
              <!-- post large -->
              <div class="post">
                <div class="thumb rounded">
                  <div class="inner">
                    <img src="@/assets/万步炎.jpg" alt="post-title" style='width: 700px; height: 388px;' />
                  </div>

                </div>
                <ul class="meta list-inline mt-4 mb-0">
                  <li class="list-inline-item" style="font-size: 30px;">万步炎</li>
                  <li class="list-inline-item" style="font-size: 30px;">1964年1月</li>
                </ul>
                <h5 class="post-title mb-3 mt-3" style="font-size: 25px;">逐梦深海，做矢志先锋。</h5>
                <p class="excerpt mb-0" style="color: #000;">
                  作为湖南科技大学海洋矿产资源探采装备与安全技术国家地方联合工程实验室主任、“海牛”科研团队负责人，万步炎从领衔研发中国首台深海钻机，到研制“海牛Ⅱ号”，不断刷新世界深海海底钻机钻探深度。他本人多次荣获国家级或部级科技奖项，展现了中国科技人才的不懈追求和瞄准世界一流研究在科技创新方面的突出表现。
                </p>
              </div>
              <!-- post -->
              <div class="post post-list-sm square before-seperator">
                <div class="thumb rounded">

                  <div class="inner">
                    <img src="@/assets/8.jpeg" alt="post-title" />
                  </div>

                </div>
                <div class="details clearfix">
                  <h6 class="post-title my-0">不忘初心共繁荣，展望未来扬风华。</h6>
                  <ul class="meta list-inline mt-1 mb-0">
                    <li class="list-inline-item">
                      西藏的成就是党和西藏各族人民一起奋勇前进的战果，也是代表了我国少数民族和全国各地共同繁荣发展的景象。携手共创美好明天，已经成为了家家户户的共同目标；中国梦，也成为了中国人民共同的梦。在党的领导下和全国各族人民的大力支持下，在西藏人民的共同努力下，西藏已经不是七十年前遍地皆是‘贫穷’和‘落后’的民族。
                    </li>
                  </ul>
                </div>
              </div>
              <!-- post -->
              <div class="post post-list-sm square before-seperator">
                <div class="thumb rounded">

                  <div class="inner">
                    <img src="@/assets/6.jpg" alt="post-title" />
                  </div>

                </div>
                <div class="details clearfix">
                  <h6 class="post-title my-0">曾缚苍龙开伟业，又乘骏马续长征。</h6>
                  <ul class="meta list-inline mt-1 mb-0">
                    <li class="list-inline-item">
                      中国要强盛、要复兴，就一定要大力发展科学技术，努力成为世界主要科学中心和创新高地。形势逼人，挑战逼人，使命逼人。我国广大科技工作者要把握大势、抢占先机，直面问题、迎难而上，瞄准世界科技前沿，引领科技发展方向，肩负起历史赋予的重任，努力建设世界科技强国。
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </Page>
  </div>
  <div class="end">
    <ul class="end-tab1">
      <li class="title">参考资料</li>
      <li>百度百科</li>
      <li>人民网相关报道</li>
      <li>新华社相关报道</li>
      <li>其他报道</li>
    </ul>
    <ul class="end-tab2">
      <li class="title">素材来源</li>
      <li>人民网</li>
      <li>新华社</li>
      <li>央视网</li>
      <li>河海公众号</li>
      <li>其他互联网资源</li>
    </ul>
    <ul class="end-tab3">
      <li class="title">参考资料</li>
      <li>人民网</li>
      <li>新华社</li>
      <li>央视网</li>
      <li>河海公众号</li>
      <li>其他互联网资源</li>
    </ul>
    <ul class="end-tab4">
      <li class="title">素材来源</li>
      <li>人民网</li>
      <li>新华社</li>
      <li>央视网</li>
      <li>河海公众号</li>
      <li>其他互联网资源</li>
    </ul>
  </div>
</template>

<script>
import Backtop from "@/components/backtop.vue";
import Cards from "@/components/Cards.vue";
import Page from "@/components/content.vue";  //@ src文件夹  @/assets
//import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

export default {
  // defineComponent: {
  //   name: "HomeView",
  //   components: {
  //     //HelloWorld,
  //   },
  // },
  components: {
    Backtop,
    Page,
    Cards
  },
  methods: {
    toTop() {
      document.documentElement.scrollTop = 0;
    }
  },
  data() {
    return {
      images: [{ id: 0, idView: require('@/assets/1.jpg') },
      { id: 1, idView: require('@/assets/2.jpg') },  //这么写
      { id: 2, idView: require('@/assets/3.jpg') },
      { id: 3, idView: require('@/assets/4.jpg') },
      { id: 4, idView: require('@/assets/5.jpg') },
      { id: 5, idView: require('@/assets/0.jpg') },
      ],
    }
  }
}
</script>


<style lang="scss">
.exportedElement {
  --bg-color: rgb(249, 247, 241) !important; //主页背景颜色
}

.home {
  overflow: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
  height: 100%;
  width: 100%;
  //background-color: #ff0000;

}

.home::-webkit-scrollbar {
  display: none;
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
