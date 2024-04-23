import axios from 'axios'


const baseURL = 'http://127.0.0.1:5000'  

//创建axios实例, 设置baseurl
let instance = axios.create({
    baseURL: baseURL
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

export {instance, baseURL};
