<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import ePub from 'epubjs'

const props = defineProps(['url'])
const url = ref(props.url)

let book = ePub(url.value);
let rendition = book.renderTo("area", {
    width: "300",
    height: "400", // 分页模式下 最好固定宽高
    flow: "paginated",
    spread: 'none', // none-单栏 both-两栏
    allowScriptedContent: true,
});
let displayed = rendition.display();


function nextPage() {
    // 在这里编写需要执行的代码
    console.log("函数已被调用");
    console.log(book)
    console.log(rendition)
}
</script>

<template>
    <div>
        <div id="area">


        </div>
        <button @click="nextPage">next</button>
    </div>
</template>

<style scoped></style>
