export const checkToken = (from, to, next) => {
    if(localStorage.getItem('token') === null){
        next('/login')
    }else{
        next()
    }
}


export const checkUserOrTraveler = (from, to, next) => {
    // 没token, 说明是游客, 放行
    console.log(to.path)
    if(localStorage.getItem('token') === null || localStorage.getItem('type') != 2 || from.path == '/login'){
        next()
    }else{
        next('/login')
    }
}