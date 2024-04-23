<script setup>
import Header from './Header.vue'
import TravelHeader from './user/headers/TravelHeader.vue'
import UserHeader from './user/headers/UserHeader.vue'

let isLogin = () =>{
  console.log(localStorage.getItem('token') )
  console.log(localStorage.getItem('type') )
    return localStorage.getItem('token') === null && localStorage.getItem('type') === 1
}
</script>

<template>
    <div>
      <TravelHeader v-if="isLogin()"></TravelHeader>
      <UserHeader v-if="!isLogin()"></UserHeader>
    </div> 
    <router-view></router-view>
  </template>

<style scoped>
</style>
