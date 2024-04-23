import {instance} from './config'

export const api_addComment = (rateObj) =>{
    return instance({
        url: '/comment/add',
        method: 'post',
        data:{
            rateObj: JSON.stringify(rateObj)
        }
    })
}

export const api_isCommented = (book_id) =>{
    return instance({
        url: '/operation/check',
        method: 'get',
        params: {book_id: book_id},
    })
}

export const api_getComments = (book_id, page) => {
    return instance({
        url: '/comment/' + book_id + '/' + page,
        method: 'get',        
    })   
}

export const api_getUserComments = (page) => {
    return instance({
        url: '/comment/user/' + page,
        method: 'get',        
    })   
}

export const api_deleteCommentById = (book_id) => {
    return instance({
        url: '/comment/delete/' + book_id,
        method: 'delete',        
    })   
}