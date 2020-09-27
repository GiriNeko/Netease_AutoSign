# Netease_AutoSign
Auto sign for netease music.
本项目可以自动以移动端、桌面端的方式来为你的网易云账号签到。
支持Github Actions运行。
并提供了丰富的api接口模块化，你可以轻易替换为其他网易云api。
（默认的api是我自建的，并非官方源。项目来自https://github.com/Binaryify/NeteaseCloudMusicApi）



## 食用方法（secret)
1.fork本项目
2.在config.json中将use_secret设置为true
3.点击settings→secrets
4.添加三个项：USER PWD CODE,分别以账户名 密码（密码需要经过md5加密，格式为32位小写） 区号（使用邮箱做用户名时，区号可乱填）并用#隔开
5.star本项目，即可在actions中看到签到程序运行

## TODO
- [ ] 使用配置文件提取账户信息
- [ ] 服务器酱推送

## 灵感来自
https://github.com/ZainCheung/netease-cloud
https://github.com/t00t00-crypto/wyy-action
https://github.com/Binaryify/NeteaseCloudMusicApi
