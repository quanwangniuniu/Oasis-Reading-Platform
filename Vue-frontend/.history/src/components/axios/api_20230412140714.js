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