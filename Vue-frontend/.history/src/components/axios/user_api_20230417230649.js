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