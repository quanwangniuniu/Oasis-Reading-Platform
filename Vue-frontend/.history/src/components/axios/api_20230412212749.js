import instance from './config'

export const getBooks = () =>{
    return instance({
        url: '/books',
        method: 'get',
    })
}

export const getUserType = () => {
    return instance({
        url: '/login',
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
        data: {title: 'title'},
        method: 'get',        
    })   
}