<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import ePub from 'epubjs'

const props = defineProps(['url'])
const url = ref(props.url)

let book = ePub(url.value);
let rendition = book.renderTo("area", {
    width: '1000px',
    height: '500px',
    flow: "paginated",
    spread: 'both', // none-单栏 both-两栏
    allowScriptedContent: true,
});

onBeforeMount(() => {
    rendition.display();
})



function nextPage() {
    rendition.next();
}
</script>

<template>
    <div>
        <div id="area">


        </div>
        <n-button strong secondary type="primary">
            Primary
        </n-button>
        <n-button strong secondary type="primary">
            Primary
        </n-button>
    </div>
</template>

<style scoped></style>
