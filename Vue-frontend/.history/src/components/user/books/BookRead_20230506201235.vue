<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import ePub from 'epubjs'

const props = defineProps(['url'])
const url = ref(props.url)

var book = ePub("./1682939086158.epub");
let rendition = book.renderTo("area", { method: "default", width: "100%", height: "100%" });


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
