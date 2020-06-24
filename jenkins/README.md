<!--
 * @Author: shouxie
 * @Date: 2020-02-26 15:28:10
 * @Description: 
 -->
##### 1.下载jmeter
Binaries：二进制版，即已经编译好、可直接执行；
Source：源代码版，需要自己编译；

##### 2.下载完成后，解压，可以通过Finder（访达）页面双击这个文件解压，也可以通过终端输入tar zxvf apache-jmeter-5.0.tgz解压。

##### 3.配置环境变量：
open .bash_profile
```shell
export JMETER_HOME=/Users/qpp/apache-jmeter-5.2.1
export PATH=$JAVA_HOME/bin:$PATH:.:$JMETER_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JMETER_HOME/lib/ext/ApacheJMeter_core.jar:$JMETER_HOME/lib/jorphan.jar:$JMETER_HOME/lib/logkit-2.0.jar
```
保存，source .bash_profile
shell下 执行 jmeter

##### 4.更改JMeter语言为中文:
启动JMeter的GUI模式后，默认语言是英文，它也自带了几种语言，我们可以把JMeter切换成中文，从菜单栏中进行切换，方法options->choose language-> Chinese（Simplified）。Chinese（Simplified）的意思是中文（简体），Chinese（Traditional）的意思是中文（繁体）

设置完成后，关闭JMeter，重新启动GUI模式，会发现，语言又变成英文了。所以如果要更改默认语言为中文，需要修改配置文件，即/Users/qpp/apache-jmeter-5.2.1/bin/jmeter.properties这个文件。
```shell
#Preferred GUI language. Comment out to use the JVM default locale's language.
#language=en
# 修改为：
#Preferred GUI language. Comment out to use the JVM default locale's language.
language=zh_CN
```
重新打开jmeter

参考：https://www.jianshu.com/p/bce9077d883c

