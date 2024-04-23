import {createRouter, createWebHashHistory} from 'vue-router'
import Books from '../user/books/Books.vue'
import Movies from '../user/movies/Favourites.vue'
import Explore from '../user/explore/Explore.vue'
import Login from '../user/login/Login.vue'
import SpecificBook from '../user/books/SpecificBook.vue'
import User from '../User.vue'
import Admin from '../Admin.vue'
import UserInfo from '../user/info/UserInfo.vue'
import BookSearch from '../user/books/BookSearch.vue'
import Transit from '../user/books/Transit.vue'
import BookManagement from '../admin/bookManagement/BookManagement.vue'
import MovieManagement from '../admin/movieManagement/MovieManagement.vue'
import AddBook from '../admin/movieManagement/AddBook.vue'
import EditBook from '../admin/movieManagement/EditBook.vue'


import {checkUser} from './utils.js'

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
        {path:'/user', component: User, alias:['/'], children:[
            {path:'books', component: Books},
            {path:'search',name:'search', component: BookSearch},
            {path:'transit',name:'transit', component: Transit},
            {path:'books/:id', component: SpecificBook,beforeEnter: checkUser},
            {path:'movies', component: Movies},
            {path:'explore', component: Explore},
            {path:'login', component: Login},
            {path:'info', component: UserInfo, beforeEnter: checkUser},
        ]},
        {path:'/admin', component: Admin,children:[
            {path:'books', component: BookManagement, children: [
                {path:'add', component: AddBook},
                {path:'edit', component: EditBook},
            ]},
            {path:'movies', component: MovieManagement}
        ]}
    ]
})

export default router