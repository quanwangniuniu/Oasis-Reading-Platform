const phoneRegEx = new RegExp("^1[3456789]\\d{9}$");
const usernameRegEx = new RegExp("^[\\u4E00-\\u9FA5A-Za-z0-9]+$")
const codeRegEx = new RegExp("^\\d{4}$")
const passwordRegEx = new RegExp("^(?=.*\\d)(?=.*[a-zA-Z])[0-9a-zA-Z]{6,}$")
const emailRegEx = new RegExp("^[\\w-]+(\\.[\\w-]+)*@([\\w-]+\\.)+[a-zA-Z]{2,7}$")

const validatePhone = (rule, value) => {
  if(value.length == 0){
    return new Error("手机号不能为空"); 
  }else if (!phoneRegEx.test(value)) {
    return new Error("手机号格式不正确");
  } else {
    return true
  }
}

const validateUsername = (rule, value) => {
  if(value.length == 0){
    return new Error("用户名不能为空"); 
  }else if (!usernameRegEx.test(value)) {
    return new Error("用户名不能包含特殊字符");
  } else {
    return true
  }
}

const validateCode = (rule, value) => {
  if(value.length == 0){
    return new Error("验证码不能为空"); 
  }else if (!codeRegEx.test(value)) {
    return new Error("验证码为四位数字");
  } else {
    return true
  }
}

const validatePassword = (rule, value) => {
  if(value.length < 6){
    return new Error("密码至少要六位以上")
  }else if(!passwordRegEx.test(value)){
    return new Error("密码需要包含字母和数字")
  }else {
    return true
  }
}

const validateEmail = (rule, value) => {
  if(value == null || value.length == 0){
    return new Error("邮箱不能为空")
  }else if(!emailRegEx.test(value)){
    return new Error("邮箱格式不正确")
  }else {
    return true
  }
}

export { 
  validatePassword,
  validatePhone,
  validateUsername,
  validateCode,
  validateEmail
}