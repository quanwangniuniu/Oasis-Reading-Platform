import instance from './config'

export const api_getBooks = () =>{
    return instance({
        url: '/books',
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
            bookItem: bookItem
            // title: bookItem.title,
            // author: bookItem.author,
            // publisher: bookItem.publisher,
            // ISBN: bookItem.isbn,
            // description: bookItem.description,
            // publish_year: bookItem.publish_year,
            // page:bookItem.page,
            // binding: bookItem.binding,
            // price:bookItem.price,
            // seriers:bookItem.seriers,
            // url:bookItem.url
        }
        
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