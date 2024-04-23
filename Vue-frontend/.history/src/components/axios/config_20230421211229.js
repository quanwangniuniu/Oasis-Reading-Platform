import axios from 'axios'

//创建axios实例, 设置baseurl
let instance = axios.create({
    baseURL: 'http://114.67.248.226:5000'
})

//设置请求拦截器, 所有请求都带上token
instance.interceptors.request.use(
    (config) =>{
        let token = localStorage.getItem('token');
        if(token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    }
)

export default instance;