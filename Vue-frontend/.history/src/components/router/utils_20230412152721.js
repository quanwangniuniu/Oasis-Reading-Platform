export const checkToken = (from, to, next) => {
    if(localStorage.getItem('token') === null){
        next('/login')
    }else{
        next()
    }
}