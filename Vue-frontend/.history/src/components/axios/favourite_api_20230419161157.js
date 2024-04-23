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

export const api_deleteFavourite = (book_id, type) => {
    return instance({
        url: '/comment/delete/' + book_id + '/' + type,
        method: 'delete',        
    })   
}