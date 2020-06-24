<!--
 * @Author: shouxie
 * @Date: 2020-02-29 09:10:09
 * @Description:
--> 

我的：mac root密码 11111111
windows root密码 111111
linux（mac上的ubuntu） root密码 111111

#### 数据
> 数据是事实或观察的结果，它是对客观事物的逻辑归纳，是信息的表现形式和载体，可以是符号、
文字、数字、语音、图像、视频等。

**RDBMS**是Relational Database Management System的简称，即**关系型数据库管理系统**，是
指采用了关系模型来组织数据的数据库，其以行和列的形式存储数据，以便于用户理解，关系型数据库这一系列的行和列被称为表，一组表组成了数据库，用户通过查询来检索数据库中的数据。

**RDBMS的特点：**
1. 数据以表格的形式出现
2. 每行为一条记录
3. 每列为记录名称所对应的数据域（Field）
4. 许多的行和列组成一张单表（Table）
5. 若干单表组成数据库（Database）
6. 查询方式：关系型数据库采用结构化查询语言（即SQL）来对数据库进行查询
7. 事务性：关系型数据库强调ACID规则，即原子性（Atomicity）、一致性（Consistency）、隔离性（
Isolation）、持久性（Durability））
8. 读写性能：关系型数据库十分强调数据的一致性，并为此降低读写性能付出了巨大的代价，在面对海量数量处理、高并发数据读写等场景时性能下降的非常厉害


```linux
mysql -h 主机名 -u 用户名 -p
```
-h：指定客户端所要登录的 MySQL 主机名, 登录本机(localhost 或 127.0.0.1)该参数可以省略

-u : 登录的用户名

-p : 告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项

登陆本机mysql数据库
mysql -u root -p

#### linux 下安装
```shell
sudo apt install mysql-server mysql-client
ps -aux | grep mysql
sudo service mysql start|stop
```
