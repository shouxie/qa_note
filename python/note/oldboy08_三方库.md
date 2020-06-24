<!--
 * @Author: shouxie
 * @Date: 2020-04-27 18:09:38
 * @Description: 
 -->
### pip包管理器
mac里面python自带easy_install的，最快的应该就是在terminal里面sudo easy_install pip
pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。
```shell
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
$ sudo python get-pip.py    # 运行安装脚本
```
注意：用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：
```shell
$ sudo python3 get-pip.py    # 运行安装脚本。
一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x。
```
pip install
pip list
pip uninstall
升级包 pip install --upgrade SomePackage
升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。
卸载包 pip uninstall SomePackage
搜索包 pip search SomePackage
显示安装包信息 pip show 
查看可升级的包 pip list -o
注意事项
如果 Python2 和 Python3 同时有 pip，则使用方法如下：
 Python2：
 python2 -m pip install XXX
 Python3:
 python3 -m pip install XXX

pip freeze > requirements.txt // 将项目依赖的包输出到指定的requirements.txt
pip install -r requirements.txt // 使用pip安装requirements中 的包
python -m pip install upgrade pip // 升级pip