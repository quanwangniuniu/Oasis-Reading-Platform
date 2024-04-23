import instance from './config'

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
        url: '/comment/check',
        method: 'get',
        params: {book_id: book_id},
    })
}

export const api_getComments = (id, page) => {
    return instance({
        url: '/comment/' + id + '/' + page,
        method: 'get',        
    })   
}