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