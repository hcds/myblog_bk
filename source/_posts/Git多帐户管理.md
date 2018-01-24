
# 1、查看当前项目（repo）用户名和邮箱

~~~git
git config user.name
git config user.email
~~~

**当前目录没有repo显示全局用户名邮箱**

# 2、修改全局用户名和邮箱
~~~git
git config --global user.name "your name"
git config --global user.email "your email"
~~~

# 3、修改当前项目用户名和邮箱
~~~git
git config user.name "your name"
git config user.email "your email"
~~~

# 4、查看Git设置
~~~git
git config --list
~~~