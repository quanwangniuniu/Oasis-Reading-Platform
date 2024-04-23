import { createRouter, createWebHashHistory } from 'vue-router'
import Books from '../user/books/Books.vue'
import Favourites from '../user/movies/Favourites.vue'
import Explore from '../user/explore/Explore.vue'
import Login from '../user/login/Login.vue'
import Register from '../user/login/Register.vue'
import StartUp from '../user/login/StartUp.vue'
import SpecificBook from '../user/books/SpecificBook.vue'
import User from '../User.vue'
import Transit from '../user/Transit.vue'
import Admin from '../Admin.vue'
import UserInfo from '../user/info/UserInfo.vue'
import BookSearch from '../user/books/BookSearch.vue'
import SearchTransit from '../user/books/Transit.vue'
import BookManagement from '../admin/bookManagement/BookManagement.vue'
import MovieManagement from '../admin/movieManagement/MovieManagement.vue'
import AddBook from '../admin/bookManagement/AddBook.vue'
import BookList from '../admin/bookManagement/BookList.vue'
import EditBook from '../admin/bookManagement/EditBook.vue'
import AnalyseBook from '../admin/bookManagement/AnalyseBook.vue'



import { checkUser } from './utils.js'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/user', component: User, alias: ['/'], redirect:'/books', children: [
        { path: 'books', component: Books },
        { path: 'search', component: BookSearch, beforeEnter: checkUser },
        { path: 'searchTransit', component: SearchTransit },
        { path: 'books/:id', name:'specific', component: SpecificBook, beforeEnter: checkUser },
        { path: 'favourites', component: Favourites },
        { path: 'login', component: Login },
        { path: 'register', component: Register },
        { path: 'info', component: UserInfo, beforeEnter: checkUser },
        // { path: 'transit', component: Transit},
      ]
    },
    {
      path: '/admin', component: Admin, children: [
        {
          path: 'managebooks', component: BookManagement, children: [
            { path: 'add', component: AddBook },
            { path: 'list', component: BookList },
            { path: 'edit', component: EditBook },
          ]
        },
        { path: 'books', component: Books },
        { path: 'search', component: BookSearch, beforeEnter: checkUser },
        { path: 'searchTransit', component: SearchTransit },
        { path: 'books/:id', component: SpecificBook, beforeEnter: checkUser },
        { path: 'favourites', component: Favourites },
        { path: 'login', component: Login },
        { path: 'register', component: Register },
        { path: 'info', component: UserInfo, beforeEnter: checkUser },
        // { path: 'transit', component: Transit},
      ]
    },
    { path: '/transit', component: Transit},
  ]
})

export default router