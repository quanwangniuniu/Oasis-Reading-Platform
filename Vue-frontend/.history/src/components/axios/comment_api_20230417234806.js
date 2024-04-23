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

export const api_isComment = (book_id) =>{
    return instance({
        url: '/comment/check',
        method: 'get',
        params: {book_id: book_id},
    })
}