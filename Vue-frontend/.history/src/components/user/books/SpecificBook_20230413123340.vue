<script setup>
import {reactive, ref} from 'vue'
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/api'
const router = useRouter();
const id = router.currentRoute.value.params.id

let book = ref({})

onBeforeMount(
  async function(){
    book.value = (await getBookById(id)).data
    console.log(book.value)
  }
)

// onBeforeMount(() =>{
//     getBookById(id).then(res=>{
//       book.value = res.data
//     })
// });

</script>


<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      <div class="book-info">
        <div class="img">
            <img :src=book.url alt="">
        </div>

        <div class="info">
          <div class="book-title">
            {{ book.title }}
          </div>
        </div>

        <div>

        </div>
      </div>
      <div class="add-rate"></div>
      <div class="book-description">
        {{ book.description }}  

      </div>
      <div class="book-comments"></div>
    </div>

    <table border="1" cellpadding="0" cellspacing="0" >
	<tr>
		<td><h3 style="font-family: 黑体;">黑体：SimHei</h3></td>
		<td><h3 style="font-family: 华文黑体;">华文黑体：STHeiti</h3></td>
		<td><h3 style="font-family: 微软正黑体;">微软正黑体：Microsoft JhengHei</h3></td>
		<td><h3 style="font-family: 微软雅黑体;">微软雅黑体：Microsoft YaHei</h3></td>
		<td><h3 style="font-family: 华文细黑;">华文细黑：STXihei</h3></td>
	</tr>
	<tr>
		<td><h3 style="font-family: 楷体;">楷体：KaiTi</h3></td>
		<td><h3 style="font-family: 楷体_GB2312;">楷体_GB2312：KaiTi_GB2312</h3></td>
		<td><h3 style="font-family: 华文楷体;">华文楷体：STKaiti</h3></td>
		<td><h3 style="font-family: 华文行楷;">华文行楷：STXingkai</h3></td>
		<td></td>
	</tr>
	<tr>
		<td><h3 style="font-family: 宋体;">宋体：SimSun</h3></td>
		<td><h3 style="font-family: 新宋体;">新宋体：NSimSun</h3></td>
		<td><h3 style="font-family: 仿宋;">仿宋：FangSong</h3></td>
		<td><h3 style="font-family: 仿宋_GB2312;">仿宋_GB2312：FangSong_GB2312</h3></td>
		<td><h3 style="font-family: 华文宋体;">华文宋体：STSong</h3></td>
	</tr>
	<tr>
		<td><h3 style="font-family: 华文中宋;">华文中宋：STZhongsong</h3></td>
		<td><h3 style="font-family: 华文仿宋;">华文仿宋：STFangsong</h3></td>
		<td></td>
		<td></td>
		<td></td>
	</tr>
	<tr>
		<td><h3 style="font-family: 华文新魏;">华文新魏：STXinwei</h3></td>
		<td><h3 style="font-family: 华文琥珀;">华文琥珀：STHupo</h3></td>
		<td><h3 style="font-family: 隶书;">隶书：LiSu</h3></td>
		<td><h3 style="font-family: 华文隶书;">华文隶书：STLiti</h3></td>
		<td><h3 style="font-family: 华文彩云;">华文彩云：STCaiyun</h3></td>
	</tr>
	<tr>
		<td><h3 style="font-family: 方正舒体;">方正舒体：FZShuTi</h3></td>
		<td><h3 style="font-family: 方正姚体;">方正姚体：FZYaoti</h3></td>
		<td><h3 style="font-family: 幼圆;">幼圆：YouYuan</h3></td>
		<td><h3 style="family:\5B8B\4F53;">PingFangSC-Medium</h3></td>
		<td></td>
	</tr>
</table>

  </div>
</template>

<style scoped>

    .top-container{
      margin: 50px 50px 0px 50px;
      display: flex;
      justify-content: space-between;
    }
    
    .title{
      width: 200px;
    }

    .title span:nth-child(1){
      font-size: 30px;
    }
    .title span:nth-child(2){
      font-size: 20px;
    }
    .container{
      display: flex;
      justify-content:space-between;
      flex-flow:row wrap;
      margin: 20px 50px 0px 50px;
      background-color: white;
      box-shadow: 0 0 5px 3px rgb(214, 214, 214); 
    }

    .book-info{
      box-sizing:border-box;
      flex:2;
      height: 600px;
      padding: 50px;
      display: flex;
    }

    .info{
      box-sizing:border-box;
      padding: 20px;
      height: 500px;
      width: 100%;
      background-color: rgb(202, 114, 114,0.1);
    }

    .book-title{
      font-size:30px;
    }

    .img{
      height: 500px;
      width: 300px;
    }

    .img img{
      height: 500px;
      width: 300px;
    }
    
    .add-rate{
      width: 500px;
      height: 400px;
      background-color: green;
    }

    .book-description{
      width: 100%;
      padding: 0px 50px 0 50px;
      white-space: pre-line;
      font-size: medium;
      color:rgb(73, 73, 73)
    }

    .book-comments{
      width: 100%;
      height: 200px;
      background-color: blue;
    }



</style>
