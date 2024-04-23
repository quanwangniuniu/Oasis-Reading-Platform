import {createRouter, createWebHashHistory} from 'vue-router'
import Books from '../user/books/Books.vue'
import Movies from '../user/movies/Favourites.vue'
import Explore from '../user/explore/Explore.vue'
import Login from '../user/login/Login.vue'
import SpecificBook from '../user/books/SpecificBook.vue'
import User from '../User.vue'
import Admin from '../Admin.vue'

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
        {path:'/user', component: User, alias:['/'], children:[
            {path:'books', component: Books},
            {path:'movies', component: Movies},
            {path:'explore', component: Explore},
            {path:'login', component: Login},
        ]},
        {path:'/admin', component: Admin}
    ]
})

export default router