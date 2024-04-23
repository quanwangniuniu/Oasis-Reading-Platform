export const checkToken = (from, to, next) => {
    if(localStorage.getItem('token') === null){
        next('/login')
    }else{
        next()
    }
}


export const checkUserOrTraveler = (from, to, next) => {
    // 没token, 说明是游客, 放行
    if(localStorage.getItem('token') === null || localStorage.getItem('type') != 2){
        next()
    }else{
        next('/login')
    }
}