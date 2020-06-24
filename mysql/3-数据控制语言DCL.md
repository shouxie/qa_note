
#### 数据控制语言DCL

MySQL的权限体系大致分为5个层级，全局层级、数据库层级、表层级、列层级和子程序层级。


层级|描述|
-|-|
全局层级|适用于一个给定服务器的所有数据库。这些权限存储在mysql.user表中。GRANT ALL ON *.*和REVOKE ALL ON *.*只授予和撤销全局权限|
数据库层级|适用于一个给定数据库中的所有目标。这些权限存储在mysql.db和mysql.host表中。GRANT ALL ON db_name.*和REVOKE ALL ON db_name.*只授予和撤销数据库权限|
表层级|适用于一个给定表中的所有列。这些权限存储在mysql.talbes_priv表中。GRANT ALL ON db_name.tbl_name和REVOKE ALL ON db_name.tbl_name只授予和撤销表权限|
列层级|适用于一个给定表中的单一列。这些权限存储在mysql.columns_priv表中。当使用REVOKE时，您必须指定与被授权列相同的列|
子程序层级|CREATE ROUTINE, ALTER ROUTINE, EXECUTE和GRANT权限适用于已存储的子程序。这些权限可以被授予为全局层级和数据库层级。而且，除了CREATE ROUTINE外，这些权限可以被授予为子程序层级，并存储在mysql.procs_priv表中|

- 用户管理:

在MySQL中，使用CREATE USER来创建用户，用户创建后没有任何权限。
```sql
#创建用户
CREATE USER '用户名' [@'主机名'] [IDENTIFIED BY '密码'];
#注意：MySQL的用户账号由两部分组成：用户名和主机名，即用户名@主机名，主机名可以是IP或机器名称，
主机名为%表示允许任何地址的主机远程登录MySQL数据库。
#删除用户
DROP USER '用户名' [@'主机名'];
#修改密码
ALTER USER '用户名'@'主机名' IDENTIFIED BY '新密码';
```

- 权限管理
```sql
在MySQL数据库中，使用grant命令授权、revoke命令撤销授权。
#授权
grant all privileges on databaseName.tableName to '用户名' [@'主机名'] ;
#撤销授权
revoke all privileges on databaseName.tableName from '用户名' [@'主机名'] ;
#刷新权限
FLUSH PRIVILEGES;
#查看权限
show grants for '用户名' [@'主机名'] ;
```
>使用grant和revoke进行授权、撤销授权时，需要指定具体是哪些权限，这些权限大体可以分为3类，
数据类、结构类和管理类.

数据|结构|管理|
-|-|-|
SELECT,INSERT,UPDATE,DELETE,FILE|CREATE,ALTER,INDEX,DROP,CREATE TEMPORARY TABLES,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EXECUTE,CREATE VIEW,EVENT,TRIGGER|USAGE,GRANT,SUPER,PROCESS,RELOAD,SHUTDOWN,SHOW DATABASES,LOCK TABLES,REFERENCES,REPUCATION CUENT,REPUCATION,SLAVE,CREATE USER|

#### 禁止ROOT用户远程登录

> 1. root是MySQL数据库的超级管理员，几乎拥有所有权限，一旦泄露后果非常严重；
> 2. root是MySQL数据库的默认用户，所有人都知道，如果不禁止远程登录，可以针对root用户暴力破解密码。