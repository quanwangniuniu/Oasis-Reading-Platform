import instance from './config'

export const api_addUser = (user) =>{
    return instance({
        url: '/user/add',
        method: 'post',
        data:{
            user: JSON.stringify(user)
        }
    })
}

export const api_getUserAvatar = (user) =>{
    return instance({
        url: '/avatar',
        method: 'get',
    })
}

export const api_getUserInfo = (user) =>{
    return instance({
        url: '/user',
        method: 'get',
    })
}

export const api_updateUserInfo = (user) =>{
    return instance({
        url: '/user/update',
        method: 'post',
        data:{
            user:JSON.stringify(user)
        }
    })
}