<script setup>
</script>

<template>
    <div class="step-container">
        <n-steps :current="1" :status="currentStatus">
            <n-step title="I Me Mine" description="All through the day, I me mine I me mine, I me mine" />
            <n-step title="Let It Be" description="When I find myself in times of trouble Mother Mary comes to me" />
            <n-step title="Come Together" description="Here come old flat top He come grooving up slowly" />
            <n-step title="Something" description="Something in the way she moves Attracts me like no other lover" />
        </n-steps>
    </div>
</template>

<style scoped>
.step-container{
    width: 800px;
}
</style>
