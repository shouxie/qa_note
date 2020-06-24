<!--
 * @Author: shouxie
 * @Date: 2020-02-29 12:12:01
 * @Description:  
--> 

在.zshrc 里面加source ~/.bash_profile 解决zsh: command not found: mysql

--我的密码：Qpp_111111
--用户名：root

1. 关闭MySQL服务
2. 重启MySQL时关闭权限验证
3. 修改root密码
4. 正常启动MySQL服务

mysql 忘记初始密码

#### step1:关闭mysql服务：

苹果->系统偏好设置->最下边点mysql 在弹出页面中 关闭mysql服务（点击stop mysql server）

#### step2:

进入终端输入：cd /usr/local/mysql/bin/回车后

登录管理员权限sudo su

回车后输入以下命令来禁止mysql验证功能./mysqld_safe --skip-grant-tables &

回车后mysql会自动重启（偏好设置中mysql的状态会变成running）

#### step3:

输入命令 ./mysql回车后，

输入命令FLUSH PRIVILEGES;

回车后，输入命令SET PASSWORD FOR'root'@'localhost'= PASSWORD('你的新密码');

以上几步完成后密码就修改成功了，现在就可以用新设置的密码去登陆mysql 了。
 

mysql8以上 

**ALTER user 'root'@'localhost' IDENTIFIED BY 'Pwd_2018';**



#### linux中修改mysql root密码;
linux 下安装 参考README.md

1. 关闭service：sudo service mysql stop
2. 修改配置文件：sudo vim /etc/mysql/mysql.conf.d/mysqld.conf(只读文件，用sudo权限写)
    在文件的[mysqld]标签下添加一句：skip-grant-tables   # 不需要权限验证
    wq!
3. 重启 sudo service mysql restart
4. mysql -u root进入mysql
```sql
  mysql -u root
    use mysql;
    show tables;
    flush privileges;
    alter user 'root'@'localhost' identifity by '111111';
     -- 会遇到 mysql "ERROR 1524 (HY000): Plugin 'unix_socket' is not loaded"  #不正确的auth插件。可能需要重新启动mysql服务；参考https://stackoverflow.com/questions/37879448/mysql-fails-on-mysql-error-1524-hy000-plugin-auth-socket-is-not-loaded

     use mysql;
     flash privileges;
      update user set authentication_string=PASSWORD("") where User='root';
      flush privileges;
      alter user 'root'@'localhost' identified by '111111';
```

5. 重置密码之后，把skip-grant-tables 去掉
sudo vim /etc/mysql/mysql.conf.d/mysqld.conf

6. 新密码登录：mysql -u root -p