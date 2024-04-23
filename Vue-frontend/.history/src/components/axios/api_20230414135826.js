import instance from './config'

export const getBooks = () =>{
    return instance({
        url: '/books',
        method: 'get',
    })
}

export const getBookById = (id) => {
    return instance({
        url: '/books/' + id,
        method: 'get',        
    })   
}

export const getBookByTitle = (title) => {
    return instance({
        url: '/getBookByTitle',
        params: {title: title},
        method: 'get',        
    })   
}

export const addBook = (bookItem) => {
    return instance({
        url: '/addBook',
        
    })
}


export const api_login = (username, password) => {
    return instance({
        url: '/login',
        method: 'post',
        data: {
            username: username,
            password: password
        }
    })
}