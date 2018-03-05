---
title: 向Github添加SSH Key
date: 2018-01-23 20:35:39
tags: Git
---

# 1.生成SSH Key

~~~
$ ssh-keygen -t rsa -C "邮箱" #密码可以不填
~~~

~/.ssh/生成两个文件，id_rsa是私钥，id_rsa.pub是公钥

# 2.SSH Key添加到SSH agent中
~~~
$ ssh-add ~/.ssh/id_rsa
~~~
出现Could not open a connection to your authentication agent的错误
~~~
ssh-agent bash
~~~

# 3.将公钥添加到GitHub中
https://github.com/settings/keys

# 4.同客户端多用户情况
创建按本地认证文件 ~/.ssh/config
~~~bash
#用proxy代理的情况
#ProxyCommand connect.exe -H [user:password@]proxy.example.com:port %h %p

Host A.github.com
    HostName github.com
    User A
    IdentityFile ~/.ssh/id_rsa_A

Host B.github.com
    HostName github.com
    User B
    IdentityFile ~/.ssh/id_rsa_B

Host C.gitlab.com
    HostName gitlab.com
    User C
    IdentityFile ~/.ssh/id_rsa_C
~~~

连接测试
~~~
ssh -vT A.github.com
~~~

# 5.Git命令
~~~
git clone A.github.com:A/A.git
~~~
