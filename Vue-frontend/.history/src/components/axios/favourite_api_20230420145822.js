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

export const api_addFolder = (folder_name) => {
    return instance({
        url: '/favourite/folder/add',
        method: 'post',
        data:{
            folder_name: folder_name
        }        
    })   
}

export const api_getFavourites = () => {
    return instance({
        url: '/favourite/abstract',
        method: 'get',   
    })   
}