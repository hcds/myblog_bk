
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

# 3.取消全局配置
~~~git
git config --global --unset user.name
git config --global --unset user.email
~~~
# 4、修改当前项目用户名和邮箱
~~~git
git config user.name "your name"
git config user.email "your email"
~~~

# 5、查看Git设置
~~~git
git config --list
~~~
git config --list查看当前配置，在当前项目下面查看的配置是全局配置+当前项目的配置，使用的时候会优先使用当前项目的配置。