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
        url: '/favourite/delete/' + book_id + '/' + type,
        method: 'delete',        
    })   
}

export const api_getAllFolders = () => {
    return instance({
        url: '/favourite/folder/',
        method: 'get',        
    })   
}