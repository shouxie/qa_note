
JMeter

JMeter在Mac下的安装
1. 官网下载地址：http://jmeter.apache.org/download_jmeter.cgi
需要先安装jdk，并且配置环境变量
分两个版本：
Binaries：二进制版，即已经编译好、可直接执行；
Source：源代码版，需要自己编译

下载完成后，解压，可以通过Finder（访达）页面双击这个文件解压，也可以通过终端输入tar zxvf apache-jmeter-5.0.tgz解压
进入bin目录执行sh jmeter

现在，我们已经可以成功启动JMeter了，但是每次都需要打开终端、进入到JMeter的bin目录下，输入sh jmeter命令来启动，显得有点繁琐。
当我们对~/.bash_profile这个文件熟悉后，可以直接把JMeter配置到环境变量中。

还是通过vim .bash_profile进入到vim编辑器，输入以下命令：
```
export JMETER_HOME=/Users/stefan/MyProjects/apache-jmeter-5.0
export PATH=$JAVA_HOME/bin:$PATH:.:$JMETER_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JMETER_HOME/lib/ext/ApacheJMeter_core.jar:$JMETER_HOME/lib/jorphan.jar:$JMETER_HOME/lib/logkit-2.0.jar
```

完成：直接在终端（任意目录）输入jmeter，即可启动JMeter。

更改JMeter语言为中文： 
启动JMeter的GUI模式后，默认语言是英文，它也自带了几种语言，我们可以把JMeter切换成中文，从菜单栏中进行切换，方法如下图。Chinese（Simplified）的意思是中文（简体），Chinese（Traditional）的意思是中文（繁体）。
设置完成后，关闭JMeter，重新启动GUI模式，会发现，语言又变成英文了。所以如果要更改默认语言为中文，需要修改配置文件，即/Users/stefan/MyProjects/tool/apache-jmeter-5.0/bin/jmeter.properties这个文件。
用Sublime Text或者其他的文本编辑器打开这个文件，找到这块区域：
```
#Preferred GUI language. Comment out to use the JVM default locale's language.
#language=en
```
修改为：
```
#Preferred GUI language. Comment out to use the JVM default locale's language.
language=zh_CN
```
再次打开JMeter后，会发现默认语言变为中文

参考：https://www.jianshu.com/p/bce9077d883c
