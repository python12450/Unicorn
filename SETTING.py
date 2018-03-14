#coding=utf8
MAIL_ENABLE=True #使用Mailgun来发送通知文件
MAILGUN_APIKEY="key-xxxxxxxxxxxxxxxxx"
MAILGUN_DOMAIN="xxxxxxx.net"#可以选择花几块钱在阿里云上买个垃圾域名
MAILGUN_SENDER="noreply@xxxxxxxx.net"#你发送通知用的MG的邮箱
MAILGUN_TO="23333333333@qq.com"#接受通知的邮箱，推荐QQ邮箱（先把自己的Mailgun邮箱加入白名单）


RESULT_STORAGE="sqlite"#可选为json，但是极度不推荐修改为json

ITEM_STORAGE="json"#在在线编辑物品功能完善前请保持这样OTL

FRIENDLY_WAIT=10#用于防止过快的访问日本雅虎拍卖而被封IP,单位是秒
