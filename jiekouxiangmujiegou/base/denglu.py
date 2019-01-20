import requests


host = " http://106.14.119.162:8090"

def denglu(s,user,pwd):


    url = host+"/user/login"
    data = {"username":user,
            "password":pwd,
            "code":"1234"
            }

    res = s.post(url,data=data)
    return res.content.decode("utf-8")

def is_denglu_sucess(result):
    if "SUCCESS" in result:
        print("登录成功")
        return True
    elif "该用户不存在，请您联系管理员" in result:
        print("用户名错误")
        return False
    elif "用户名或密码不正确" in result:
        print("密码错误")
        return False
    else:
        print("其他情况，登录失败")
        return False







if __name__=="__main__":
    s = requests.session()
    a = denglu(s,"123123123123","123127773123123")
    print(a)

    login_result = is_denglu_sucess(a)
    print("。。。。。。。。。。。")
    print(login_result)