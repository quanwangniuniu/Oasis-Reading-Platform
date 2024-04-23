import {createRouter, createWebHashHistory} from 'vue-router'
import Books from '../user/books/Books.vue'
import Movies from '../user/movies/Favourites.vue'
import Explore from '../user/explore/Explore.vue'
import Login from '../user/login/Login.vue'
import SpecificBook from '../user/books/SpecificBook.vue'
import User from '../User.vue'
import Admin from '../Admin.vue'
import UserInfo from '../user/info/UserInfo.vue'

import {checkUser, checkUserOrTraveler} from './utils.js'

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
        {path:'/user', component: User, alias:['/'], beforeEnter:checkUserOrTraveler, children:[
            {path:'books', component: Books},
            {path:'books/:id', component: SpecificBook,beforeEnter: checkUser},
            {path:'movies', component: Movies},
            {path:'explore', component: Explore},
            {path:'login', component: Login},
            {path:'info', component: UserInfo, beforeEnter: checkUser},
        ]},
        {path:'/admin', component: Admin}
    ]
})

export default router