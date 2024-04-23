import instance from './config'

export const api_getBooks = () =>{
    return instance({
        url: '/books',
        method: 'get',
    })
}

export const api_getBooksByPage = (page) => {
    return instance({
        url: '/books/page/' + page,
        method: 'get',
    })
}

export const api_getTotalPages = (page) => {
    return instance({
        url: '/books/pages',
        method: 'get',
    })
}

export const api_getBookById = (id) => {
    return instance({
        url: '/books/' + id,
        method: 'get',        
    })   
}

export const api_getBookByTitle = (title) => {
    return instance({
        url: '/getBookByTitle',
        params: {title: title},
        method: 'get',        
    })   
}

export const api_addBook = (bookItem) => {
    return instance({
        url: '/addBook',
        method: 'post',
        data:{
            bookItem: JSON.stringify(bookItem)
        }
        
    })
}

export const api_updateBook = (bookItem) => {
    return instance({
        url: '/updateBook',
        method: 'post',
        data:{
            bookItem: JSON.stringify(bookItem)
        }
        
    })
}

export const api_deleteBookById = (id) => {
    return instance({
        url: '/books/' + id,
        method: 'delete',        
    })   
}

export const api_login = (phone, password) => {
    return instance({
        url: '/login',
        method: 'post',   
        data:{
            username: phone,
            password: password
        }
    })
}