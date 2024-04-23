<script setup>
const props = defineProps(['comment-info'])
</script>

<template>
    <div>
        <div class="container">
            <div class="userinfo">
                <div>

                </div>
            </div>
            <div class="">
                {{ props.comment.comment }}
            </div>
        </div>        
    </div>

 
</template>

<style scoped>
.container{
    height: 200px;
    background-color: red;
}
</style>
