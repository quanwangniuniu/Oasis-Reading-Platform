<script setup>
import Header from './Header.vue'
import TravelHeader from './user/headers/TravelHeader.vue'
import UserHeader from './user/headers/UserHeader.vue'

let isLogin = () =>{
    return localStorage.getItem('token') != null
}
</script>

<template>
    <div>
      <TravelHeader v-if="!isLogin()"></TravelHeader>
      <UserHeader v-if="isLogin()"></UserHeader>
    </div> 
    <router-view></router-view>
  </template>

<style scoped>
</style>
