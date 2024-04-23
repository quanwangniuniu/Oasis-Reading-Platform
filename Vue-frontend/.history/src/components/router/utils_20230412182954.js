export const checkUser = (from, to, next) => {
    if(localStorage.getItem('token') === null || localStorage.getItem('type') != 1){
        next('/login')
    }else{
        next()
    }
}