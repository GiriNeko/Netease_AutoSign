#coding:utf-8
from configparser import ConfigParser
import requests
import json

#api检测以及登陆状态检查
def apitest():
    res=s.post(url=config['api']['url'] + config['api']['status'])
    res_json=json.loads(res.text)
    if res_json['code']==200:
        print("api工作正常，发现有登陆账号：" + res_json['profile']['nickname'] + " 准备登出")
        logout=s.post(url=config['api']['url'] + config['api']['logout'])
        logout_json=json.loads(logout.text)
        if logout_json['code']==200:
            print("登出调用完毕，准备检查是否登出成功")
            check()
        else:
            print("api似乎出错了呢")
            exit(logout_json['code'])
    else:
        print("api工作正常")

#登录模块
def login():
    if '@' in user:
        print('邮箱登录')
        login_url = config['api']['url'] + config['api']['login_email']
        logindata = {
            "email":user,
            config['api']['password']:pwd,
        }
    else:
        print('手机号登录')
        login_url = config['api']['url'] + config['api']['login_phone']
        logindata = {
            "phone":user,
            "countrycode":code,
            config['api']['password']:pwd,
        }

    login=s.post(url=login_url,data=logindata)
    login_json=json.loads(login.text)
    if login_json['code']==200:
        print("登陆成功，你好 " + login_json['profile']['nickname'])
    elif login_json['code']==501:
        print("登陆失败，账号不存在")
        exit(login_json['msg'])
    else:
        print(login_json['code'])
        exit(login_json['msg'])


#检查登陆状态模块
def check():
    check=s.post(url=config['api']['url'] + config['api']['refresh'])
    check_json=json.loads(check.text)
    if check_json['code']==301:
        print("登出完毕")
    else:
        print("登出失败")
        exit(check_json['profile']['nickname'])

#签到模块 手机
def signin(type):
    signin=s.post(url = config['api']['url'] + config['api']['signin'],data={
        'type':type
    })
    signin_json=json.loads(signin.text)
    if signin_json['code']==200:
        print("签到成功，云贝:+ " + signin_json['point'] )
    elif signin_json['code']==-2:
        print("你已经签到过啦")
    else:
        print("签到失败" + signin_json['code'] + signin_json['msg'])

# 入口
print("读取配置")
s=requests.Session()
config = ConfigParser()
config.read('config.json', encoding='UTF-8-sig')
if config['main']['use_secret']=='true':
    print('准备从secret中读取账户信息')
    user = input()
    code = input()
    pwd = input()
elif config['main']['use_bash']=='false':
    print('准备从配置文件中读取账户信息')
else:
    print('你tm在config里填了什么东西，滚，重新填！')
    exit(config['main']['use_bash'])
print("测试api")
apitest()
print("开始登录")
login()
print("开始手机端签到")
signin(0)
print("开始电脑端签到")
signin(1)
print('操作完毕，登出')
logout=s.post(url=config['api']['url'] + config['api']['logout'])
logout_json=json.loads(logout.text)
check()


