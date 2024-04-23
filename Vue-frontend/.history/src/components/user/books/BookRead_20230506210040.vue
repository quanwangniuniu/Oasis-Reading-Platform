<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import ePub from 'epubjs'

const props = defineProps(['url'])
const url = ref(props.url)


let book = ePub(url.value).on('book:pageChanged', function (location) { console.log(location.anchorPage, location.pageRange) });;
let rendition = book.renderTo("area", {
    width: '1000px',
    height: '500px',
    flow: "paginated",
    spread: 'both', // none-单栏 both-两栏
    allowScriptedContent: true,
});


onBeforeMount(() => {
    rendition.display();
    book.ready.then(() => {
        return this.book.locations.generate(750 * (window.innerWidth / 375) * (getFontSize(this.fileName) / 16))
    }).then(() => {
        // 完成分页后，允许拖动
        this.setBookAvailable(true)
        // 完成分页后，刷新位置信息
        this.refreshLocation()
    })
})



function nextPage() {
    rendition.next();
}

function prevPage() {
    rendition.prev();
}
</script>

<template>
    <div>
        <div id="area">


        </div>

        <div class="operation">
            <n-space>
                <n-button strong secondary type="primary" @click="prevPage">
                    上一页
                </n-button>
                <n-button strong secondary type="primary" @click="nextPage">
                    下一页
                </n-button>
            </n-space>
        </div>


    </div>
</template>

<style scoped>
.operation {
    display: flex;
    justify-content: center;
}
</style>
