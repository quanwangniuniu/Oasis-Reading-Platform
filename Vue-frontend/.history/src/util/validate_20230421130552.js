const phoneRegEx = new RegExp("^1[3456789]\\d{9}$");
const usernameRegEx = new RegExp("^[\\u4E00-\\u9FA5A-Za-z0-9]+$")
const codeRegEx = new RegExp("^\\d{4}$")


const validatePhone = (rule, value) => {
  if (!phoneRegEx.test(value)) {
    return new Error("手机号格式不正确");
  } else {
    return true
  }
}

const validateUsername = (rule, value) => {
  if (!usernameRegEx.test(value)) {
    return new Error("用户名不能包含特殊字符");
  } else {
    return true
  }
}

const validateCode = (rule, value) => {
  if (!codeRegEx.test(value)) {
    return new Error("验证码为四位数字");
  } else {
    return true
  }
}

export { 
  validatePhone,
  validateUsername,
  validateCode,
}