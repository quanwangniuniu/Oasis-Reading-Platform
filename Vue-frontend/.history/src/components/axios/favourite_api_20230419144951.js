import instance from './config'

export const api_addFavourite = (favouriteObj) =>{
    return instance({
        url: '/favourite/add',
        method: 'post',
        data:{
            favouriteObj: JSON.stringify(favouriteObj)
        }
    })
}