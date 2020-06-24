<!--
 * @Author: shouxie
 * @Date: 2020-05-20 10:13:13
 * @Description: 
 -->
### apt-get

```
# 下载安装
apt-get install packageName 
# 移除包
apt-get remove packageName
# 移除包和配置文件
apt-get pruge packageName 
# 检查安装包是否有升级文件，有则升级软件包
apt-get upgrade packageName
# 自动移除不需要的包
apt-get autoremove packageName
```

### 如何安装ssh
```
sudo apt-get install openssh-server
```

```
# 查看服务是否启动
ps -aux | grep ssh
# 启动，停止，重启
sudo service ssh start
sudo service ssh stop
sudo service ssh restart
```

### 运行.sh文件
1. cd 到文件目录执行 ./xxx.sh
2, sh xxx.sh

### echo 命令的含义是：将引号中内容写入某文件中

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

### exec $SHELL :重新初始化 shell 环境

#### 远程连接
1. 
```
# p：port
ssh -p 22 用户名@ip地址
# 提示输入密码
```
2. 软件连接
xshell finalshell putty。。。

### linux 目录结构

home 普通用户的家
home - qpp xiaoming ... 每个用户有个文件夹
～ 当前用户的家
/： 根目录
pwd： 查看当前路径（所在位置）

#### home 下目录
- root： 超级管理员目录（普通用户没有权限访问）
- bin： 常用命令
- boot： 启动文件和操作系统的核心文件
- cdrom： 光驱
- dev： 存放设备的目录
- etc： 系统的配置文件

### linux 常用命令
- pwd： 查看当前所在目录位置
- ls： 查看当前目录的文件，文件夹 
     - . 开头的文件是隐藏文件
     - -a ： all 列出所有文件，包含隐藏文件
     - -l： list 以列表形式列出文件所有信息
     - ls ch* 列出所有以‘ch’开头的文件
     - ls -al简写：ll

- man： 说明书 man ls 列出ls命令详细信息
- history： 记录曾经使用过的命令，当成是日志

### 绝对路径和相当路径

### 文件跳转
cd 命令
```
cd ~ # 回到当前用户家目录
cd / # 根目录
cd - # 回到来源目录
cd ..
```
### 创建目录

```
#（sudo）不在当前用户目录下
mkdir 目录名
mkdir -p a/a1/a2 # 创建多条目录
```

### 删除目录
```
# 删除空目录
rmdir 目录名
rmdir a/a1/a2/... 
# 递归的删除目录
# 即使是递归，目录中也不能有文件
rmdir -p a/a1/a2/... 
```

### 文件创建和文件查看

```
# 文件创建
touch 文件名
# 打开文件或编辑文件
gedit a.txt
# 查看文件
cat a.txt
# 倒叙查看文件
tac a.txt
# 查看文件并且显示c行号
cat -n a.txt
# 将键盘中的内容输出到文件中
cat > a.txt
# 可以输入内容到文件，ctrl c保存退出


# 分页查看 空格键翻页 q退出
more a.txt
# 查看  搜索： ‘/’ 后面跟要搜索的内容 q表示退出
less a.txt
# 默认获取前10行
head a.txt

# head -n number 文件名：表示获取前number行
# 默认获取后10行
tail a.txt
# tail -n number 文件名：表示获取后number行
```
### 删除文件
rm 文件名
rm 绝对路径/文件名
rm -i 文件名 # 删除之前确认
rm -f 文件名 # 递归的删除
rm -rf 目录 # 递归的删除文件夹和里面的内容
```

```

### 复制文件

cp 源文件 目标目录（文件夹）
cp -r 源目录 目标目录（文件夹）

### 移动文件

mv 源文件 目标文件夹（目录）

  - 参数
    - -f force 覆盖前不询问
    - -i interactive 覆盖前询问
    - -n --no-clobber 不覆盖已存在文件
    如果指定了-i -f -n中的多个，仅最后一个生效

mv -t 目录 文件1，文件2...
mv -t code code1/*.txt
mv 目录1 目录2 # 将目录1移到目录2下面
mv 文件1 文件2 # 重命名文件1为文件2

### 文件查找
find 路径 参数 文件

```
# 当前目录查找
find -name a.txt
find . -name a.txt
find / -name a.txt

# find /-size[+-][大小k,G,M...] + 大于 - 小于
find / -size+ 1000k

# 查找修改文件3天内的
find / -mtime -3
# 查找修改文件3天以前
find / -mtime +3

# mtime：修改文件的时间 atime： 访问文件的时间 ctime：修改状态的时间
```

### whereis which
查看命令所在脚本目录
where 命令
which 命令
```
whereis ls
which ls
```

### grep

global search regular expression(RE) and print out the line 全面搜索正则表达式并把行打印出来

-a   --text   #不要忽略二进制的数据。 将 binary 文件以 text 文件的方式搜寻数据 

-A<显示行数>   --after-context=<显示行数>   #除了显示符合范本样式的那一列之外，并显示该行之后的内容。   

-b   --byte-offset   #在显示符合样式的那一行之前，标示出该行第一个字符的编号。   

-B<显示行数>   --before-context=<显示行数>   #除了显示符合样式的那一行之外，并显示该行之前的内容。   

-c    --count   #计算符合样式的行数。   

-C<显示行数>    --context=<显示行数>或-<显示行数>   #除了显示符合样式的那一行之外，并显示该行之前后的内容。   

-d <动作>      --directories=<动作>   #当指定要查找的是目录而非文件时，必须使用这项参数，否则grep指令将回报信息并停止动作。   

-e<范本样式>  --regexp=<范本样式>   #指定字符串做为查找文件内容的样式。

-E      --extended-regexp   #将样式为延伸的普通表示法来使用。   

-f<规则文件>  --file=<规则文件>   #指定规则文件，其内容含有一个或多个规则样式，让grep查找符合规则条件的文件内容，格式为每行一个规则样式。   

-F   --fixed-regexp   #将样式视为固定字符串的列表。

-G   --basic-regexp   #将样式视为普通的表示法来使用。 

-h   --no-filename   #在显示符合样式的那一行之前，不标示该行所属的文件名称。   

-H   --with-filename   #在显示符合样式的那一行之前，表示该行所属的文件名称。   

-i    --ignore-case   #忽略字符大小写的差别。   

-l    --file-with-matches   #列出文件内容符合指定的样式的文件名称。   

-L   --files-without-match   #列出文件内容不符合指定的样式的文件名称。   

-n   --line-number   #在显示符合样式的那一行之前，标示出该行的列数编号。   

-q   --quiet或--silent   #不显示任何信息。   

-r   --recursive   #此参数的效果和指定“-d recurse”参数相同。   

-s   --no-messages   #不显示错误信息。   

-v   --revert-match   #显示不包含匹配文本的所有行。   

-V   --version   #显示版本信息。   

-w   --word-regexp   #只显示全字符合的列。   

-x    --line-regexp   #只显示全列符合的列。   

-y   #此参数的效果和指定“-i”参数相同。


命令格式：grep [option] pattern file
```
grep 's' *
# 运行结果：
#a.txt:sdfg
#a.txt:sdfvefref
#grep: code1: Is a directory
```

### 管道符 |

连接多个linux命令
命令1 | 命令2 将命令1连接到命令2 上
使用管道操作符“|”可以把一个命令的标准输出传送到另一个命令的标准输入中，连续的|意味着第一个命令的输出为第二个命令的输入，第二个命令的输入为第一个命令的输出，依次类推

### | 结合grep使用

```
ps -ef |grep pycharm
# ps是进程查看命令，其中-e为显示所有进程，-f为全格式显示。 grep是一个非常高效的查询工具，可以查询文本中带有某关键字的行。 这个命令的功能是，查询带有关键字 pycharm 的进程。会一条一条列出
```

### 软链接soft和硬链接hard

https://blog.csdn.net/gao_zhennan/article/details/79127232

link/ln [-s] 源文件 目标文件

软链接：ln -s 源文件 目标文件
硬链接：ln 源文件 目标文件
源文件：即你要对谁建立链接

1，软链接可以理解成快捷方式。它和windows下的快捷方式的作用是一样的。
2，硬链接等于cp -p 加 同步更新。

#### 区别: 
软链接文件的大小和创建时间和源文件不同。软链接文件只是维持了从软链接到源文件的指向关系，不是源文件的内容，大小不一样容易理解。
硬链接文件和源文件的大小和创建时间一样。硬链接文件的内容和源文件的内容一模一样，相当于copy了一份。
但是简单的copy的文件创建文件的时间应该是复制文件时的时间，肯定不会像硬链接那样和创建源文件的时间相同。但是只要加一个选项-p,时间就一样了
那么cp -p的文件是不是就相当于硬链接了呢？其实不然，对于源文件的内容有修改，硬链接文件会同步更新修改，始终保持和源文件的内容相同，而复制的文件则不可能做到这一点。
所以，硬链接等于cp -p加同步更新。

软链接像快捷方式，方便我们打开源文件，这一点在windows中深有体会

那硬链接有哪些应用呢？
在多用户的操作系统里，你写一个脚本，程序等，没有完成，保存后等下次有时间继续写，但是其他用户有可能将你未写完的东西当成垃圾清理掉，这时，你对你的程序，脚本等做一个硬链接，利用硬链接的同步更新，就可以方式，别人误删你的源文件了。

#### 删除源文件多软链接和硬链接的影响
查看软链接文件，查看的文件不存在。和windows一样，删除源文件，快捷方式也用不了。但是删除源文件，为什么硬链接文件还可以查看呢？
这里要简单说下i节点了。i节点是文件和目录的唯一标识，每个文件和目录必有i节点，不然操作系统就无法识别该文件或系统，就像没有上户口的黑户。linux操作系统是不识别些字母的，像这些jys ,jys.hard操作系统根本不知道是什么玩意。
可以看出硬链接文件和源文件i节点号相同，并且一个i节点可以对应多个文件名
如图，删除了jys,只是删除了从920586到jys的映射关系，不影响它和jys.hard的映射关系。此图也解释了硬链接的同步更新，对源文件修改，操作系统只认i节点，于是操作系统就将修改内容写进所有i节点相同名字不同的文件。写到这里我突发奇想，如果对硬链接文件进行修改那么源文件会不会同步更新呢？留给读者自己试验吧！

### 文件权限
r：read 读 4
w： write 写 2
x： ext 执行 1

(拥有者user)(所属用户组的其他用户group)(其他任何用户other)  所有用户（all）

设置文件权限：
chmod [ugoa] [+-=] [rwx] 文件/文件夹

```
chmod g+w a.txt
chmod o-r a.txt
chmod o=rwx a.txt

```

rwxrwxrwx 777
r--r--r-- 444
rw------- 600
r(读))w(写)x(执行)  => 2^2 + 2^1 + 2^0 = 7
```shell
chomd 600 testFile
chomd go-rw testFile
#g(group),o(others),u(user) + 和 - 分别表示增加和去掉相应的权限

# 递归添加权限
 chmod -R g+w code

```
drwxr-xr-x 中的d：
d： 文件夹
l： 链接文件
-： 普通文件
b： block 块设备
c： char 字符设备


操作软链接文件权限，实际操作的是源文件，同时他的硬链接权限也会变

### 用户和用户组
一个用户必须有一个主组
一个用户可以有多个组
一个组有多个用户

一对一：某个用户可以是某个组的唯一成员；
多对一：多个用户可以是某个唯一的组的成员，不归属其它用户组；比如beinan和linuxsir两个用户只归属于beinan用户组；
一对多：某个用户可以是多个用户组的成员；比如beinan可以是root组成员，也可以是linuxsir用户组成员，还可以是adm用户组成员；
    多对多：多个用户对应多个用户组，并且几个用户可以是归属相同的组；其实多对多的关系是前面三条的扩展；理解了上面的三条，这条也能理解；

/etc/passwd 注：用户（user）的配置文件；
 /etc/shadow 注：用户（user）影子口令文件；改文件只有root用户可以修改
 /etc/group 注：用户组（group）配置文件；

 #### 新建用户
 useradd [options] 用户名

useradd 用户名 在/home不会生成他的主目录，在配置文件中可以看到存在用户

选项:
-c comment 指定一段注释性描述。
-d 目录 指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。
-g 用户组 指定用户所属的用户组。
-G 用户组，用户组 指定用户所属的附加组。
-s Shell文件 指定用户的登录Shell。
-u 用户号 指定用户的用户号，如果同时有-o选项，则可以重复使用其他用户的标识号。

```shell
sudo useradd -m testUser
# cat /etc/passwd
tail -n 1 /etc/passwd

# 最后一行显示
# testUser:x:1002:1002::/home/testUser:/bin/sh
```
 #### 删除用户

 userdel -r 用户名 # 删除用户和用户的主目录
 
```shell
sudo userdel -r testUser
tail -n 2 /etc/passwd
# 没有testUser信息，同时/home下也没有testUser主目录
```

#### 修改用户密码
sudo passwd 用户名

#### 切换用户
su 用户名
输入此用户的密码
sudo su root # 切换root用户
sudo su - # 切换root用户，并且回到root的主目录

#### /etc/passwd

超级用户 root 0
程序用户 1-499
普通用户 500-65535

用户名 密码 uid gid 用户说明 家目录 shell解释器

用户的密码存在/etc/shadow，该文件只有root有权限可以修改
组账户信息放在/etc/group

#### sudo
设置sudo提升权限的时候不需要输入密码，需要修改/etc/sudoers 文件
```
%sudo ALL=(ALL:ALL) NOPASSWORD:ALL
```

如果新添加的用户不属于sudo组，是不能使用sudo提升权限的，需要添加sudo组
```
# 以属于sudo组的用户登录
sudo usermod -a -G sudo 用户名
```
#### groupadd，groupdel等
groupadd，groupdel
groupmod -a 新组名 旧组名
groups 显示所有的组

#### who whoami

#### 设置文件/目录的归属

chown
格式：
chown 属主 文件或目录
chown :属组 文件或目录
chown 属主:属组 文件或目录

注：同时设置属主和属组，用:隔开，如果只设置属组，需使用‘:属组’的形式

-R：递归修改指定目录下所有文件，子目录的归属
```
sudo chown testUser a.txt
sudo chown testUser:group1 a.txt
chgrp 组名 文件|文件夹
```

### 网络

- 查看ip地址
    - ipconfig（wins） ifconfig（linux）

- ping 查看网络联通性
    - ping ip
    - ping 域名
    - ping -c n ip|域名  发送几次

- netstat
    - netstat -anp
         - -n 显示端口
         - -p 显示进程
         - -t tcp
         - -u udp
         - -a 显示所有

- ps 进程
     - 参数：
        - -a-e 显示所有进程
        - -u 显示指定用户的进程的详细信息
        - -x通常与a一起使用，列出较完整的信息
        - -r 正在运行的进程
```
ps -aux | grep ssh
```

- kill 杀死进程
  - kill 参数 进程号
      - kill -9 进程号

- top：性能分析工具，可查看资源使用情况
- free：系统内存的状态

### 压缩，打包

- 打包：将多个文件或者目录放在一起，形成一个总的包。这样便于保存和传输，但是大小是没有变化的。
- 压缩：是指将一个或者多个大文件或者目录通过压缩算法使文件的体积变小以达到压缩的目的，可以节省存储空间，在压缩的时候通常是先打包再压缩

#### tar

-z	是否同时具有gz属性，用gzip对包进行压缩
-j	是否同时具有bz2属性：用bzip对包进行压缩
-x	解压缩、提取打包的内容
-t	查看压缩包内容
-J	是否同时具有xz属性
-c	建立一个压缩，打包文档
-v	显示压缩或者打包的内容（view）
-f	使用文件名，在f后面要接压缩后的文件的名字，只要用到tar命令，-f选项是必须要用的，-f参数在使用的时候一定排在其他参数的后面，在最右边

-C	切换到指定目录，表示指定解压缩包的内容和打包的内容存放的目录
-p	保留备份数据的原本权限与属性，常用于备份（-c）重要的配置文件
-P	保留绝对路径

- 打包
  tar -cvf 打包后的文件名 文件|文件夹 # cvf c：create v：view f： filename
- 压缩
  - linux主要有三种压缩方式：
    - 1.gzip：是公认的压缩这速度最快，压缩大文件的时候与其他的压缩方式相比更加明显，历史最久，应用最广泛的压缩方式 tar -zcvf 打包后的文件名 文件|文件夹
    - 2.bzip：压缩形成的文件小，但是可用性不如gzip tar -jcvf 打包后的文件名 文件|文件夹
    - 3.xz：是最新的压缩方式，可以自动提供最佳的压缩率

参数|作用|命名方式|
-|-|-|
-z|gzip|文件名.tar.gz|
-j|bzip2|.tar.bz2|
-J|xz|.tar.xz|
  
- 解压
tar -xvf ：解包
tar -zxvf packagename -C 目录 被解压文件 ：解压到指定目录

#### zip，unzip

zip [参数] [压缩包名] [压缩的目录或者文件的路径]

-m	将文件压缩后，删除原文件
-o	将压缩文件内的所有文件的最新变动时间设为压缩的时间
-q	安静模式，在压缩的时候不显示指令执行的过程
-r	递归压缩，将自定目录下的所有子文件以及文件一起处理
-x	”文件列表“，压缩时排除文件列表中的文件

unzip [参数] [压缩文件]  （-d [目录]）  //如果不是用括号里面的内容，则解压文件在当前工作目录

-c	将解压缩的结果显示到屏幕上（显示每一个目录下的每一个文件的内容），同时对字符做适当的转换，但是并没有解压压缩包
-l	显示压缩文件内所包含的文件
-t	检查压缩文件是否正确
-v	执行时显示压缩文件的详细信息
-q	安静模式，执行时不显示任何信息
-d	指定文件解压后存储的目录
-x	指定不要处理压缩文件中的那些文件

#### gzip

gzip [-cdtv#] 文件名

　　-c 将输出写到标准输出上，并保留原有文件。
　　-d 将压缩文件解压。
　　-t 测试，检查压缩文件是否完整。

　　-v 对每一个压缩和解压的文件，显示文件名和压缩比。

    -# -9 或--best表示最高压缩方法（高压缩比）。系统缺省值为 6


备注：默认gzip 会删除源文件，并生成xx.gz文件，如果需要保留源文件的话可以使用：
gzip -c xxx文件 > xxx.gz
解压需要保留源文件的话使用：
gzip -cd  xx.gz > 文件名

### 包管理

#### dpkg
redhot：centos：rpm软件包管理
debian：ubuntu：dpkg软件包管理（debian package缩写）
安装、删除、构建和管理deb 格式的软件包。

使用 dpkg 命令安装软件时，可以使用 -i 选项并指定 deb 安装包的路径。和 Ubuntu 下的另一个包管理工具 apt-get（Advanced Package Tool）有所不同。
apt-get 命令并不直接操作 deb 安装包文件，而是从 /etc/apt/sources.list 配置文件中定义的软件镜像源里下载软件包并安装，使用时也只需指定软件的名称（或者也可以附加上版本号）

因此，dpkg 主要是用来安装已经下载到本地的 deb 软件包，或者对已经安装好的软件进行管理。而 apt-get 可以直接从远程的软件仓库里下载安装软件。

dpkg -l： 命令列出当前系统中已经安装的软件以及软件包的状态
dpkg -r： -r 选项只会移除指定的软件包而不对其配置文件产生影响，可以使用 -P 选项在删除软件包的同时清理配置文件
dpkg -P <package>
dpkg -L <package> 或 dpkg --list-files <package>： 查看软件包的安装位置
dpkg -i <.deb file name>： 安装软件

#### apt

apt = apt-get、apt-cache 和 apt-config 中最常用命令选项的集合。apt 可以看作 apt-get 和 apt-cache 命令的子集

apt|apt-cache|-|
-|-|-|
apt search|	apt-cache search	|搜索应用程序|
apt show|	apt-cache show|	显示安装细节|
apt install	|	apt-get install	|	安装软件包|	
apt remove|	apt-get remove	|移除软件包|
apt purge|	apt-get purge	|移除软件包及配置文件|

apt list： 列出包含条件的包（已安装，可升级等）
apt edit-sources：	编辑源列表

其他：
wget -c
yum
curl -O
apt

### 虚拟环境

pyenv：管理不同的python版本
virtualenv：管理不同的虚拟环境

#### virtualenv
1. 安装
```shell
apt install virtualenv
# 默认去找python2
```
2. 创建虚拟环境
```shell
whereis python3
# /usr/bin/python3.7
virtualenv -p /usr/bin/python3.7 myfirstvirtual
# 会生成一个文件夹myfirstvirtual
```
3. 激活虚拟环境
```shell
cd myfirstvirtual/bin
source activate
# (myfirstvirtual) $
```
4. 退出虚拟环境
```shell
deactivate
```

#### virtualenvwrapper

1.安装
```shell
sudo pip3 install virtualenvwrapper
# ~/.local/bin/virtualenvwrapper.sh
```
2.配置环境变量
.bashrc 
注意：等号左右不能有空格！！！
```shell
# Envs 是虚拟环境的存放目录
export WORK_ON=$HOME/Envs
export WIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.7
source /home/qpp/.local/bin/virtualenvwrapper.sh
```
save .bashrc
source .bashrc

3. 创建
```shell
mkvirtualenv mysecondvirtual --python=python3.7
# (mysecondvirtual)$
```

4 常用命令
```shell
# 切换，在虚拟环境上工作
workon mysecondvirtual
# 停止
deactivate
rmvirtualenv
lsvirtualenv    #列举所有的环境。

cdvirtualenv    #导航到当前激活的虚拟环境的目录中，比如说这样您就能够浏览它的 site-packages。

cdsitepackages   # 和上面的类似，但是是直接进入到 site-packages 目录中。

lssitepackages     #显示 site-packages 目录中的内容。

```
#### python3-venv
Python3.3以上的版本通过venv模块原生支持虚拟环境，可以代替之前的virtualenv。
```shell
sudo apt install python3-venv
# 创建
python3 -m venv venvname
# 激活
source venvname/bin/activate
# 退出
deactivate
```
#### pyenv

安装、卸载、编译、管理多个 python 版本，并随时将其中一个设置为工作环境

pyenv install -list
pyenv install 版本号：安装对应的版本号
pyenv versions ：查看安装的版本号
pyenv global 版本号：使用版本号
pyenv virtualenv 版本号 virtualname：使用pythonxxx版本设置虚拟环境
pyenv activate virtualname： 进入虚拟环境
pyenv deactivate virtualname：退出虚拟环境

pyenv只能管理使用pyenv下载的python版本，系统的需要用pyenv重新安装
使用pip安装第三方模块会安装到~.pyenv/versions/xxx 下。不会和系统模块发生冲突
使用pip安装模块后，可能需要执行pyenv rehash更新数据库

#### psm 镜像源
```shell
pip install psm
psm ls # 查看可以使用的镜像源
psm use xxx # 使用
psm show # 查看
```
