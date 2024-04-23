import instance from './config'

export const api_addComment = (rateObj) =>{
    return instance({
        url: '/comment/add',
        method: 'post',
        data:{
            rateObj: JSON.stringify(user)
        }
    })
}