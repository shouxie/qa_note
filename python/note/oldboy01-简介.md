<!--
 * @Author: shouxie
 * @Date: 2020-03-17 17:10:28
 * @Description: 
 -->

### python 简介
> python的创始⼈为吉多·范罗苏姆（Guido van Rossum）龟爷。1989年的圣诞节期间，吉多·
范罗苏姆为了在荷兰-阿姆斯特丹打发时间，决⼼开发⼀个新的脚本解释程序，作为ABC语⾔的⼀种继承。 
Python可以应⽤于众多领域，如：数据分析、组件集成、⽹络服务、图像处理、数值计算
和科学计算等众多领域。⽬前业内⼏乎所有⼤中型互联⽹企业都在使⽤Python，如：
Youtube、Dropbox、BT、Quora（中国知乎）、⾖瓣、知乎、Google、Yahoo!、
Facebook、NASA、百度、腾讯、汽⻋之家、美团等。
**⽬前Python主要应⽤领域：**
- 云计算: 云计算最⽕的语⾔， 典型应⽤OpenStack
- WEB开发: 众多优秀的WEB框架，众多⼤型⽹站均为Python开发，Youtube, Dropbox, ⾖瓣。。。， 典型WEB框架有Django
- 科学运算、⼈⼯智能: 典型库NumPy, SciPy, Matplotlib, Enthought librarys,pandas
- 系统运维: 运维⼈员必备语⾔
- ⾦融：量化交易，⾦融分析，在⾦融⼯程领域，Python不但在⽤，且⽤的最多，⽽且重要性逐年提⾼。原因：作为动态语⾔的Python，语⾔结构清晰简单，库丰富，成熟稳定，科学计算和统计分析都很⽜逼，⽣产效率远远⾼于c,c++,java,尤其擅⻓
策略回测
- 图形GUI: PyQT, WxPython,TkInter

> 编程语⾔主要从以下⼏个⻆度为进⾏分类:
编译型和解释型
静态语⾔和动态语⾔
强类型定义语⾔和弱类型定义语⾔
=======
#### 编译和解释的区别是什么？

编译器是把源程序的每⼀条语句都编译成机器语⾔,并保存成⼆进制⽂件,这样运⾏时计算机可以直接以机器语⾔来运⾏此程序,速度很快;
⽽解释器则是只在执⾏程序时,才⼀条⼀条的解释成机器语⾔给计算机来执⾏,所以运⾏速度是不如编译后的程序运⾏的快的.
这是因为计算机不能直接认识并执⾏我们写的语句,它只能认识机器语⾔(是⼆进制的形式)


编译型vs解释型
编译型
优点：编译器⼀般会有预编译的过程对代码进⾏优化。因为编译只做⼀次，运⾏时不需要编
译，所以编译型语⾔的程序执⾏效率⾼。可以脱离语⾔环境独立运⾏。
缺点：编译之后如果需要修改就需要整个模块重新编译。编译的时候根据对应的运⾏环境⽣
成机器码，不同的操作系统之间移植就会有问题，需要根据运⾏的操作系统环境编译不同的
可执⾏⽂件。
解释型
优点：有良好的平台兼容性，在任何环境中都可以运⾏，前提是安装了解释器（虚拟机）。
灵活，修改代码的时候直接修改就可以，可以快速部署，不⽤停机维护。
缺点：每次运⾏的时候都要解释⼀遍，性能上不如编译型语⾔。

#### python的优缺点
优点：
1. Python的定位是“优雅”、“明确”、“简单”，所以Python程序看上去总是简单易
懂，初学者学Python，不但⼊⻔容易，⽽且将来深⼊下去，可以编写那些⾮常⾮常
复杂的程序。
2. 开发效率⾮常⾼，Python有⾮常强⼤的第三⽅库，基本上你想通过计算机实现任何
功能，Python官⽅库⾥都有相应的模块进⾏⽀持，直接下载调⽤后，在基础库的基
础上再进⾏开发，⼤⼤降低开发周期，避免重复造轮⼦。
3. ⾼级语⾔————当你⽤Python语⾔编写程序的时候，你⽆需考虑诸如如何管理你
的程序使⽤的内存⼀类的底层细节
4. 可移植性————由于它的开源本质，Python已经被移植在许多平台上（经过改动
使它能够⼯ 作在不同平台上）。如果你⼩⼼地避免使⽤依赖于系统的特性，那么你
的所有Python程序⽆需修改就⼏乎可以在市场上所有的系统平台上运⾏
5. 可扩展性————如果你需要你的⼀段关键代码运⾏得更快或者希望某些算法不公
开，你可以把你的部分程序⽤C或C++编写，然后在你的Python程序中使⽤它们。
6. 可嵌⼊性————你可以把Python嵌⼊你的C/C++程序，从⽽向你的程序⽤户提供
脚本功能。
看缺点：
1. 速度慢，Python 的运⾏速度相⽐C语⾔确实慢很多，跟JAVA相⽐也要慢⼀些，因此
这也是很多所谓的⼤⽜不屑于使⽤Python的主要原因，但其实这⾥所指的运⾏速度
慢在⼤多数情况下⽤户是⽆法直接感知到的，必须借助测试⼯具才能体现出来，⽐如
你⽤C运⼀个程序花了0.01s,⽤Python是0.1s,这样C语⾔直接⽐Python快了10倍,
算是⾮常夸张了，但是你是⽆法直接通过⾁眼感知的，因为⼀个正常⼈所能感知的时
间最⼩单位是0.15-0.4s左右，哈哈。其实在⼤多数情况下Python已经完全可以满
⾜你对程序速度的要求，除⾮你要写对速度要求极⾼的搜索引擎等，这种情况下，当
然还是建议你⽤C去实现的。
2. 代码不能加密，因为PYTHON是解释性语⾔，它的源码都是以名⽂形式存放的，不过我不认为这算是⼀个缺点，如果你的项⽬要求源代码必须是加密的，那你⼀开始就
不应该⽤Python来去实现。
3. 线程不能利⽤多CPU问题，这是Python被⼈诟病最多的⼀个缺点，GIL即全局解释器锁（Global Interpreter Lock），是计算机程序设计语⾔解释器⽤于同步线程的⼯具，使得任何时刻仅有⼀个线程在执⾏，Python的线程是操作系统的原⽣线程。在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的执⾏。⼀个python解释器进程内有⼀条主线程，以及多条⽤户程序的执⾏线程。即使在多核CPU平台上，由于GIL的存在，所以禁⽌多线程的并⾏执⾏。关于这个问题的折衷解决⽅法，我们在以后线程和进程章节⾥再进⾏详细探讨。

当然，Python还有⼀些其它的⼩缺点，在这就不⼀⼀列举了，我想说的是，任何⼀⻔语⾔都不是完美的，都有擅⻓和不擅⻓做的事情，建议各位不要拿⼀个语⾔的劣势去跟另⼀个语⾔的优势来去⽐较，语⾔只是⼀个⼯具，是实现程序设计师思想的⼯具，就像我们之前中学学⼏何时，有的时候需要要圆规，有的时候需要⽤三⻆尺⼀样，拿相应的⼯具去做它最擅⻓的事才是正确的选择。之前很多⼈问我Shell和Python到底哪个好？我回答说Shell是个脚本语⾔，但Python不只是个脚本语⾔，能做的事情更多，然后⼜有钻⽜⻆尖的⼈说完全没必要学Python,Python能做的事情Shell都可以做，只要你⾜够⽜B,然后⼜举了⽤Shell可以写俄罗斯⽅块这样的游戏，对此我能说表达只能是，不要跟SB理论，SB会把你拉到跟他⼀样的⾼度，然后⽤充分的经验把你打倒。
#### python解释器
 > 当我们编写Python代码时，我们得到的是⼀个包含Python代码的以.py为扩展名的⽂本
⽂件。要运⾏代码，就需要Python解释器去执⾏.py⽂件。
由于整个Python语⾔从规范到解释器都是开源的，所以理论上，只要⽔平够⾼，任何⼈都
可以编写Python解释器来执⾏Python代码（当然难度很⼤）。事实上，确实存在多种
Python解释器。
- CPython
当我们从Python官⽅⽹站下载并安装好Python 2.7后，我们就直接获得了⼀个官⽅版
本的解释器：CPython。这个解释器是⽤C语⾔开发的，所以叫CPython。在命令⾏下运
⾏python就是启动CPython解释器。
CPython是使⽤最⼴的Python解释器。教程的所有代码也都在CPython下执⾏。
- IPython
 IPython是基于CPython之上的⼀个交互式解释器，也就是说，IPython只是在交互⽅
式上有所增强，但是执⾏Python代码的功能和CPython是完全⼀样的。好⽐很多国产浏览
器虽然外观不同，但内核其实都是调⽤了IE。
CPython⽤>>>作为提示符，⽽IPython⽤In [序号]:作为提示符。
- PyPy
 PyPy是另⼀个Python解释器，它的⽬标是执⾏速度。PyPy采⽤JIT技术，对Python代
码进⾏动态编译（注意不是解释），所以可以显著提⾼Python代码的执⾏速度。
绝⼤部分Python代码都可以在PyPy下运⾏，但是PyPy和CPython有⼀些是不同的，这就
导致相同的Python代码在两种解释器下执⾏可能会有不同的结果。如果你的代码要放到
PyPy下执⾏，就需要了解PyPy和CPython的不同点。
- Jython
 Jython是运⾏在Java平台上的Python解释器，可以直接把Python代码编译成Java字节
码执⾏。
- IronPython
 IronPython和Jython类似，只不过IronPython是运⾏在微软.Net平台上的Python解
释器，可以直接把Python代码编译成.Net的字节码。

python解释器+lib(内置库)+pip包管理器
可扩展性
#### pip包管理器
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
#### python发展史
- 1989年，为了打发圣诞节假期，Guido(⻳叔)开始写Python语⾔的编译器。
Python这个名字，来⾃Guido所挚爱的电视剧Monty Python’s Flying Circus。他
希望这个新的叫做Python的语⾔，能符合他的理想：创造⼀种C和shell之间，功能
全⾯，易学易⽤，可拓展的语⾔。
- 1991年，第⼀个Python编译器诞⽣。它是⽤C语⾔实现的，并能够调⽤C语⾔的库
⽂件。从⼀出⽣，Python已经具有了：类，函数，异常处理，包含表和词典在内的
核⼼数据类型，以及模块为基础的拓展系统。
Granddaddy of Python web frameworks, Zope 1 was released in 1999
- Python 1.0 - January 1994 增加了 lambda, map, filter and reduce.
- Python 2.0 - October 16, 2000，加⼊了内存回收机制，构成了现在Python语⾔
框架的基础
- Python 2.4 - November 30, 2004, 同年⽬前最流⾏的WEB框架Django 诞⽣
- Python 2.5 - September 19, 2006
- Python 2.6 - October 1, 2008
- Python 2.7 - July 3, 2010
In November 2014, it was announced that Python 2.7 would be
supported until 2020, and reaffirmed that there would be no 2.8 release
as users were expected to move to Python 3.4+ as soon as possible
- Python 3.0 - December 3, 2008
- Python 3.1 - June 27, 2009
- Python 3.2 - February 20, 2011
- Python 3.3 - September 29, 2012
- Python 3.4 - March 16, 2014
- Python 3.5 - September 13, 2015

--------
print(values,values,sep='',end='\n')
格式化输出：
%s:占位符 
print('.........%s......$s' %(str1,str2))
%d:占位符 
转义字符：
print('.........%d......$d' %(int1,int2))
\n \t 制表符 \' \r 回车 \\
字符串前面加r，表示原样输出字符串
格式化输出之 %d  %s  %f

代码:
知识点： 
有 + 连接符的使用
类型转换： str() , int()
格式化：%d  %f  的使用

name='赵飞'
print('姓名是:'+name)  # str + str

age=18 # str(int) ---> (int ->str)  强制类型的转换 
print('年龄是:'+str(age))  # 'aaa'  int --->str
print('年龄是:%s' % age)  # %s --> str 简写   底层：str(age) ---> '18'
isMarry=False  # 布尔： True， False
print('结婚否？回答: %s' % isMarry)  # str(False) ---> 'False'


```python
print('年龄是:%d' % age) # %d  digit  数字 # age= '18岁'  

# print('年龄是:%d' % age)  

age=18.5   # int(18.5)--->18  取整数
print('年龄是:%d' % age)  

year=2019
print('今年是：%02d' % year)  # 仍然是2019 但是%f就可设置位数


# %f float  小数点后面的位数 而且是四舍五入
salary=8899.32895
print('我的薪水是:%.2f' % salary)
# ticket 49.5                                                                 
# count 35   
# 方法1                                                                 
'''                                                                           
电影 XXX                                                                        
人数 xxx                                                                        
单价 xxx                                                                        
总票价 xxx                                                                       
'''                                                                           
movie = 'ttt'                                                                 
ticket = 79.9                                                                 
count = 35                                                                    
print('电影:%s\n人数:%d\n:单价:%.1f\n总票价%.1f' %(movie,count,ticket,count*ticket))   
# 方法2 
messgae = '''                
电影:%s                
人数:%d                
单价:%.1f              
总票价:%.1f             
'''%(movie,count,ticket,count
print(messgae)   
```
```python
name = 'qpp'                                                                      
age = 19                                                                          
salary='99.99'                                                                    
message = 'my name is {},age is {},my salary is {}'.format(name,age,salary)       
print(message)                                                                      
```
不合法的缩进：
IndentationError: unexpected indent


#### 变量
> 将运算的中间结果暂存到内存,以便后续程序调⽤.

变量的命名规则:
 1, 变量由字⺟, 数字,下划线搭配组合⽽成
 2, 不可以⽤数字开头,更不能是全数字
 3,不能是python的关键字, 这些符号和字⺟已经被python占⽤, 不可以更改
 4,不要⽤中⽂
 5,名字要有意义
 6,不要太⻓
 7, 区分⼤⼩写
推荐⼤家使⽤驼峰体或者下划线命名
驼峰体: 除⾸字⺟外的其他每个单词⾸字⺟⼤写
下划线: 每个单词之间⽤下划线分开
#### 常量
在python中不存在绝对的常量. 约定俗成, 所有字⺟⼤写就是常量
例如: PI = 3.141592653
 BIRTH_OF_SYLAR = 1990

#### 注释
 > 有时候我们写的东⻄不⼀定都是给⽤户看的. 或者不希望解释器执⾏. 那我们可以使⽤#来注释掉代码. 被注释的内容是不会执⾏的.可以⽅便后⾯的程序员来拜读你的代码
 单⾏注释: # 被注释的内容
 多⾏注释:''' 被注释的内容 ''', """这个也是多⾏注释"""

#### python的基本数据类型
type() 判断数据类型
int('1') # 转为int类型
str() 转为字符串
%d
多个变量赋值： a,b,c = 1,2,'hello'
python中数据类型可以分为：

- 内置类型
  - 数值类型：整型int，浮点型float，复数（complex） 3+5j
  - str:字符串
  - bool:布尔值【True，False】
  - None：空值，表示变量没有确定的值
  - list：列表
  - tuple：元组
  - dict：字典
  - set：集合
- 自定义类型
  - class ：类

##### 基础类型

- **数值类型**：
  - 整型（int）： python3中只有int一种，可以表示整数，例如：10，-5,10000

  - 浮点型（float）： 表示带小数点的实数，有两种表示法：
    - 小数表示： 1.9     .23
    - 科学计数法： 用e来表示10的指数，1e2就代表了100，注意e前面必须有数值，e后面必须为整数

  - 复数（complex）：表示数学上的无理数，形如：a+bj
----
Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。

Python math 模块提供了许多对浮点数的数学运算函数。

Python cmath 模块包含了一些用于复数运算的函数。

cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。

要使用 math 或 cmath 函数必须先导入：
import math
python3移除了cmp()函数

- **布尔型(bool)**：表示事务的两种状态，男女、阴晴、亮暗等，它只有两个值：True，False
long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。
- None：表示空对象，一般用于判断，不同于0和空字符

- **字符串（str）**：在python中，用引号（单引号、双引号、三引号）表示字符串

python的字串列表有2种取值顺序:

从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
'h e l l o'
 0 1 2 3 4
 -5 -4 -3 -2 -1
 如果你要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
Python 列表截取可以接收第三个参数，参数作用是截取的步长
  - 字符串的表示

    ```
    # 用单引号表示： 'hello'
    # 用双引号表示："我用python"
    # 用3个单引号表示：可以表示多行文本，例如：
    	'''伟大
    	   的
    	   祖国
    	 '''
    # 用3个双引号表示：可以表示多行文本，例如：
    	"""生死看淡，
    	不服就干"""
    ```

  - 转义字符：有些特殊字符无法从键盘输入，可以使用转义字符表示，另外，无论是单引号、双引号还是三引号字符串，其中引号是字符串界定符，引号并不是字符串的内容，那么如何在单引号字符串中表示一个单引号呢，这也可以使用转义字符表示。常见的转义字符

    | 转义字符   | 描述          | 转义字符 | 描述       |
    | ------ | ----------- | ---- | -------- |
    | `\'`   | 表示一个普通字符单引号 | \n   | 换行       |
    | `\"`   | 表示一个普通字符双引号 | \r   | 回车       |
    | `\'''` | 一个普通的三单引号   | `\\` | 一个普通的字符 |
    | `\"""` | 一个普通的三双引号   | \a   | 响铃       |
    | \t     | tab键        | \b   | 回删一个字符   |

  - 字符串编码：计算机只能识别二进制，那么字符串如何存储到计算机里呢
    ```
    计算机不能直接存储字符串，但我们可以将字符编码，例如用65表示大写字符A，66表示大写字符B....等这种表示方式就是美国类的ASCII码，只能表示127个字符，但对于美国人来说已经足够了。一但能用整数表示字符，我们可以很方便的把整数用二进制表示，那么字符串也就和容易存储到计算机了。
    但还有很多其他国家的语言是不能用ASCII表示的，所有ISO组织就推出了unicode码，用来表示任何一种语言的字符，unicode码也称之为万国码，通用码，可以表示任何一种语言的任何一个字符。unicdoe码有多中表示方式，例如：utf-8、utf-16、utf-32等。一般使用较多的是utf-8，utf-8是一种变长的编码，表示一个字符可能用一个字节，也可能是三个字节
    中文常用编码一般用GBK编码，用2个字节表示一个汉字
    ```
##### list：列表
 > 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾
加号 + 是列表连接运算符，星号 * 是重复操作
```python
list0 = ['hello', 'world', 1, 23, False]
print('list is ', list0[0:4:2])
print(list0*2)
print(list0+[1])
print(list0[-1:])
```
##### 元组
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
```python
tuple = (1, 'hello', 1.10, -10, True, 'world')
print(tuple[1:5])  # ('hello', 1.1, -10, True)
print(tuple[0])  # 1
print(tuple*3)  # (1, 'hello', 1.1, -10, True, 'world', 1, 'hello', 1.1, -10, True, 'world', 1, 'hello', 1.1, -10, True, 'world')
print(tuple + (1, 2, 3))  # (1, 'hello', 1.1, -10, True, 'world', 1, 2, 3)
print(tuple[0:4:2])  # (1, 1.1)
```
##### 字典
> 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成

##### Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
int(x [,base])

将x转换为一个整数

long(x [,base] )

将x转换为一个长整数

float(x)

将x转换到一个浮点数

complex(real [,imag])

创建一个复数

str(x)

将对象 x 转换为字符串

repr(x)

将对象 x 转换为表达式字符串

eval(str)

用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)

将序列 s 转换为一个元组

list(s)

将序列 s 转换为一个列表

set(s)

转换为可变集合

dict(d)

创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)

转换为不可变集合

chr(x)

将一个整数转换为一个字符

unichr(x)

将一个整数转换为Unicode字符

ord(x)

将一个字符转换为它的整数值

hex(x)

将一个整数转换为一个十六进制字符串

oct(x)

将一个整数转换为一个八进制字符串

##### 1.2 类型判断

我们可以使用type和isinstance来测试和判断数据类型

~~~
#type用法：
  type(obj)
  功能：返回obj的数据类型
  参数：obj是你要测试变量或数值
  示例：
    age = 10
    name = 'hello'
    print(type(name),type(age))
    
    #判断变量是否是指定类型
    if type(age) is int:
       print('是')
    else:
       print('否')

#isinstance用法：
  isinstance(obj,typename)
  功能：判断obj是否是指定类型，是返回True,否返回False
  参数： objobj是你要判断的变量或数值
        typename是指定数据类型,可以是int,float,str等。也可是一个
                 类型的元组,例如:(int,float)
  示例：
    age = 10
	name = 'hello'	
	print(isinstance(age,int))
	print(isinstance(name,(str,int)) #只要name是str或int的一种就返回True
	
	if isinstance(age,int):
	    print('是')
	else:
	    print('否')
	    
#type和isinstance的区别
type判断基本类型是没问题的，但无法判断子类对象是父类的一种
isinstance可以判断子类对象是父类的一种
class A:
    pass

class B(A):
    pass

objA = A()
objB = B()

#输出否
if type(objB) is A:
    print('是')
else:
    print('否')
    
print(isinstance(objB,A))  #True
~~~

结论：优先使用isinstance

##### 8.1 整数(int)
> 常⻅的数字都是int类型. ⽤于计算或者⼤⼩的比较
在32位机器上int的范围是: -2**31～2**31-1，即-2147483648～2147483647
在64位机器上int的范围是: -2**63～2**63-1，即-9223372036854775808～9223372036854775807
够你⽤了吧. 注意这些是整数. 

##### 8.2 字符串(str)
> 在Python中,凡是⽤引号引起来的,全是字符串.
字符串可以⽤单引号，双引号，或者三引号引起来，没有什么区别，只是⼀些特殊的格式需要不⽤的引号
⽐如：
```python
msg = "My name is Alex , I'm 22 years old!" 
# 这个就需要单双引号配合。
msg = """
今天我想写⾸⼩诗，
歌颂我的同桌，
你看他那乌⿊的短发，
好像⼀只炸⽑鸡。
"""
'''想多⾏赋值⼀个字符串，就需要三引号。
数字类型有 +-*/ 字符串有么？
字符串只有 + *。
'''
#字符串的拼接
s1 = 'a '
s2 = 'bc'
#print(s1 + s2)
#相乘 str*int 重复int次的字符串,float 类型的会报错
name = '坚强'
#print(name*8)
# print(s1+s2+1) 字符串拼接int类型会报错
```
''' 保证样式（格式）输出，换行空格等，作为注释使用

##### 8.3 布尔值(bool), 真或者假, True和False

#### ⽤户交互

使⽤input()函数,可以让我们和计算机互动起来
语法:
 内容 = input(提⽰信息)
这⾥可以直接获取到⽤户输入的内容
接收的永远都是字符串
'''python
'''
#### 运算符种类
- 赋值运算符
 = += -= *= /=
 id(var1) # 返回变量内存地址
- 算术运算符
加：+  减：- 乘：* 除：/ 幂：** 整除：// 取余：% 
'str'*n # n次str
```python
print(8**2) # 64
print('hello'*3) #hellohellohello
```
数学函数

|     函数名      |          函数的说明           | 示例                          |
| :----------: | :----------------------: | --------------------------- |
|     abs      |           取绝对值           | abs(-10)                    |
|   pow(x,y)   |          x的y次方           | pow(10,2)求10的平方             |
| round(x,[n]) |   浮点数的4舍5入， n代表保留小数的位数   | round(3.456)                |
|    max()     |        求给定参数的最大值         | max(21,43,65,75,86,32,3,45) |
|    min()     |        求给定参数的最小值         | min(21,43,65,75,86,32,3,45) |
| math.ceil()  | 需要导入import  math库   向上取整 | math.ceil(18.1) #19         |
| math.floor() | 需要导入import  math库   向下取整 | math.floor(18.1) #18        |
|  math.sqrt   | 需要导入import  math库   求平方根 | math.sqrt(100)              |


随机函数

获取随机数，需要引入random库。

import  random

|                函数名                |                   函数说明                   |
| :-------------------------------: | :--------------------------------------: |
| random.randrange(start,stop,step) | start 指定范围的起始值 包含本身，默认是0；stop 指定范围的结束值 不包含本身； step 步长，默认步长是1。该函数返回一个整数 |
|     random.randint(start,end)     |   返回[start  end]之间的一个随机整数，start必须小于end   |
|          random.random()          |           返回一个[0.0,1.0)之间的随机小数           |

##### 注意

 优先级：  ** >正负号 > // % * /  > + -
 从左向右算
 tip:!!!在幂运算和一元运算符联合计算时，从右向左算，例如： -1 ** 2 = -1

- 关系运算符
'''
源文件：一起解释编译复用内存
交互式：小整数复用 大整数，定义一个变量会重新开辟内存
'''
关系运算就是比较运算，如果表达式成立，返回True，否则返回False。关系运算的结果是布尔值。

| 运算符  | 示例       | 说明                             |
| ---- | -------- | ------------------------------ |
| ==   | a == b   | a和b值相等，结果是True，a和b值不相等结果为False |
| !=   | a != b   | a不等于b 结果为True，否则结果为True        |
| >    | a  > b   | a大于b结果为True，否则为False           |
| >=   | a  >=  b | a大于等于b结果为True，否则为False         |
| <    | a < b    | a小于b结果为True，否则为False           |
| <=   | a <= b   | a小于等于b结果为True，否则为False         |
is 对象比较
注意：

 优先级： 比较运算符优先级相同
 从左向右算
 可以这样算：`1 < a < 3`  等价于 a > 1  and  a < 3

- 逻辑运算符
逻辑运算符可以用于构造复杂条件。逻辑运算符包括：

 逻辑与 and  对应汉语的意思是“并且”  、 “同时”
 逻辑或  or   对应汉语意思为"或者"
 逻辑非 not  对应汉语意思为”相反“

在逻辑运算中，False、None、0、0.0、‘’（空字符串）被看做假（False），其它的看做真(True)

- 位运算符
bin() # 十进制转二进制 二进制表示：以0b开头
int() # 二进制转十进制
八进制表示：以0o开头
八进制转二进制 3610 -> 3 -> 011  6 -> 110   1 -> 001   0 -> 000 ===>  011110001
负数：
>正数的反码和补码都与原码相同。 
而负数的反码为对该数的原码除符号位外各位取反。 
负数的补码为对该数的原码除符号位外各位取反，然后在最后一位加1 
在计算机中，负数以原码的补码形式表达。 

bit byte 1byte=8bit 二进制表示其实有8位 如： 5 ---> 0000 0101
二进制负数计算：
5求负数：-x=!x+1
1. 先求5的二进制 0000 0101
2. 取反         1111 1010
3. 最后位数加1   1111 1011

bin(-5) # python 的bin方法，是直接求出5的二进制表示，再在前面加负号

十六进制 以0x开头，0-9 a-f
十六进制转二进制 3610 -> 3 -> 0011  6 -> 0110   1 -> 0001   0 -> 0000 ===>  0011011000010000

---
第一位是符号位，1为负数，0为正数
异或: 两个数上下对齐，相同为0，不同为1
##### 位运算 与：& 或：|  非：~ 异或：^ 左移：>> 右移：<<
&：
1 True 0 False
  0000 1010
& 0101 0011
——————————————
  0000 0010

```python
# -x=!x+1 在计算机中，负数以原码的补码形式表达。
print(~0b0101)  # 取反=> 1111 1010 减1-> 1111 1001      取反->0000 0110
print(~-4)  # -4 : 化二进制数：- 0000 0100 -> 1111 1011 +1 -> 1111 1100 取反==== 0000 0011 正数 不需要转换 为3
print(~5)  # 6: 0000 0101 -> 各位取反： 1111 1010 转为10进制数： ------> 1开头的为负数。转为： x=！（-x-1） 1111 1001 -》 0000 0110 -》 -6

```
左移：>> m>>n m*2的n次方
右移：<< m<<n m//2

#### 三目运算符
resultTrue if tiaojian else resultFalse

#### 运算符优先级
**
~
+ - (符号运算符)
* / // %
+ - (加减)
<< >>
&
^
|
== != < > <= >=
is is not
not
and
or

#### if语句
if 条件:
  条件成立执行的语句


if 条件:
  条件成立执行的语句
else:
  条件不成立执行的语句

if 条件:
  语句
elif 条件:
  语句
elif 条件:
  语句
else:
  语句
#### for语句

range(start=0,end,step) # 不包含end

- for i in []:
  语句

- for...else 适用于for正常执行完或者没有循环数据时需要做的事(break跳出来的循环不适用)
for i in []:
  语句
else:
  语句
```python
for i in range(5):
    print('my age is %d' %i)
else:
    print('my age is -0')
```
- pass 空语句
> 只要有锁进，锁进的内容还不确定的时候，此时为了保证语法完整性，可以使用pass占位，不会报语法错误
```python
```
- break 强制跳出for循环！for循环包含整个循环，包含for...else结构的部分
```python
for i in range(3):
    username = input('请输入用户名')
    password = input('请输入密码')
    if username == 'qpp' and password == '11':
        print('hello')
        break
    else:
        print('用户名或密码错误，只有三次机会请重新输入')
else:
    print('账户锁定')
```

#### while 循环
while 条件:
      语句体
else:
      语句体
```python
i = 1
while i <= 30:
    if not(i % 3):
        print('i:%d' % i)
    i += 1

```
Python continue 语句跳出本次循环，而break跳出整个循环。

continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

continue语句用在while和for循环中。

--------基础部分：从现在开始不看视频了，看菜鸟教程！！！
#### 循环嵌套

#### 字符串
in， not in 在。。。里
字符串格式化
r 保留原格式
print(r'\'111\'')  # \'111\'
print('\'111\'')  # '111'
hello[start:end:方向和步长] 负数表示反方向，倒叙
```python
hello = 'hello world'
#  逆序输出world 正序输出hello 逆序输出字符串 打印oll 打印llo wo
print(hello[-1:-6:-1])
print(hello[0:5])
print(hello[::-1])
print(hello[4:1:-1])
print(hello[2:8])
```
字符串内置函数
capitalize() # 将字符串第一个字母大写
upper() # 转大写
lower() # 转小写
title() # 每个单词的首字母转大写   istitle() # 判断每个单词的首字母是否是大写
```python
message = 'my name is hh'
msg = message.capitalize()
print(msg)  # My name is hh
msg = message.upper()
print(msg) # MY NAME IS HH
msg = message.lower()
print(msg) # my name is hh
msg = message.title()
print(msg) # My Name Is Hh

valityCode = 'Assfewoi23460jgjF8ib0jjgil2GYTLiKgbhO210'
import random
code = ''
for i in range(4):
    ran = random.randint(0, len(valityCode) - 1)
    code += valityCode[ran]
print(code.lower())

j,code1 = 0,''
while j < 4:
    ran = random.randint(0,len(valityCode)-1)
    code1 += valityCode[ran]
    j +=1
print(code1.lower())
```
find lfind rfind rindex lindex index replace
find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常.

rfind(str, beg=0,end=len(string))
类似于 find()函数，不过是从右边开始查找.

rindex( str, beg=0, end=len(string))
类似于 index()，不过是从右边开始.

replace(old, new [, max])
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
```python
str = 'hello wolrd'
print('x' in str) # False
print('o' in str) # True
print('x' not in str) # True
print(str.find('x'))
print(str.rfind('o'))
print(str.index('x'))
```
编码：
encode decode
```python
print('哈哈'.encode('utf-8')) # b'\xe5\x93\x88\xe5\x93\x88'
print('哈哈'.encode('utf-8').decode())
```
startswith endswith
startswith(substr, beg=0,end=len(string))
检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
```python
print(str.startswith('hell'))
print(str.endswith('d'))
your = input('请上传图片')
if your.endswith('jpg') or your.endswith('png') or your.endswith('gif'):
    print('yes')
else:
    print('no')
```
isalpha()
如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
isdigit()
如果字符串只包含数字则返回 True 否则返回 False..

```python
print(str.replace(' ','').isalpha())
str1 = '121'
print(str1.isdigit())

sum1 = 0
for i in range(3):
    inp = input('请输入数字')
    if inp.isdigit():
        sum1 += int(inp)
    else:
        print('error')
        break
else:
    print('sum %d' % sum1)
```
join lstrip rstrip strip
```python
print('-'.join('hello')) # h-e-l-l-o
list1 = ['h','e','1',0]
print(' '.join(list1)) # TypeError: sequence item 3: expected str instance, int found list包含数字，不能直接转化成字符串。
print(' '.join('%s' % id for id in list1)) # h e 1 0
```
count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
split(str="", num=string.count(str))
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
单词：
   Keyword :  关键字
   arguments  参数
Ignore  忽略
Join 加入
#### 列表
names = ['','','']
extend
append
del
max
min
sum
remove # list.remove(obj)  obj -- 列表中要移除的对象。
clear 清除列表所有元素
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.reverse() 反向列表中元素 会改变列表
list.count(obj) 统计某个元素在列表中出现的次数
list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序

cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。


排序，reverse=True 降序
sorted(ranList,reverse=True)
列表中的元素可以存放：列表。。。
类型转换：
list() # 转为列表,只能将可迭代的转为列表，整型不能转
int()
str()
print(list(range(0,5)))  # [0, 1, 2, 3, 4]
```python

list0 = ['1',2,3,'hello',4]
list0.append('world')
print(list0) # ['1', 2, 3, 'hello', 4, 'world']
list0.extend('hello')
print(list0) # ['1', 2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o']
list0.extend([3,4])
print(list0) # ['1', 2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4]
list0 = list0+[0]
print(list0) # ['1', 2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4, 0]
del list0[0]
print(list0) # [2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4, 0]
print(1 in list0) # False
list0.insert(1,'name')
print(list0) # [2, 'name', 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4, 0]


# 产生10个不同随机数放入列表中
import random
ranList,i = [],0
while i < 10:
    ran = random.randint(0,15)
    if (ran not in ranList):
        ranList.append(ran)
        i+=1
print(ranList)

# max min sum
maxVal = minVal = ranList[0]
sum1 = 0
for i in ranList:
    if i < minVal:
        minVal = i
    if i > maxVal:
        maxVal = i

    sum1 += i
print(maxVal,max(ranList),minVal,min(ranList),sum1,sum(ranList))

```

#### 元组 () tuple
元组中的元素不可修改
如果元组只有一个元素，需要加上逗号：(1,)
tuple()

下标和切片同列表
sum
min
max
len
tuple.count(obj) # obj存在的次数
tuple.index(obj) # obj的下标，不存在会报错
sorted() # 会返回成列表类型

##### 组包与解包

组包：python解释器自动将多个数据组装到一个容器中
解包：将容器中的多个数据拆出来
```python
#组包: 解释器把1,2,3自动组包成一个元组,然后赋值给a,a的类型就是元组类型的

　　a = 1,2,3 # 相当于 a = (1,2,3)
　　print(a) # (1, 2, 3)
　　print(type(a)) # <class 'tuple'>

#解包: 解释器会自动对元组(1,2)进行 解包,然后把1赋值给m,把2赋值给n，把3赋值给3
　　m,n,k = (1,2,3) # m=1,n=2,k=3
　　print(m) # 1
　　print(n) # 2
　　print(k) # 3 
```
变量个数与元组不一致：
*变量名： 表示未知个数，此变量为列表
```python
a,*b=(1,2,3)
print(a,b, *b, *[1,2,3,4]) # 1 [2, 3] 2 3 1 2 3 4
a,*b = (1,)
print(a,b) # 1 []
```

#### 字典(dictionary) {} dict
```python
# 元组只有成对出现才可以转字典
tuple3 = (('name', '123'),('age',12))
print(dict(tuple3)) # {'name': '123', 'age': 12}
tuple4 = [('name', '123', '456'),('age', 12,13)]
print(dict(tuple4)) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
```
增加：
字典不支持‘+’ # obj1+obj2 报错
dict.get(key, default=None):返回指定键的值，如果值不在字典中返回default值
dict.clear():删除字典内所有元素
dict.copy(): 返回一个字典的浅复制
dict.has_key(key):如果键在字典dict里返回true，否则返回false，py3已移除，改为__contains__
dict.fromkeys(seq[, val]): 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
dict.setdefault(key, default=None):**和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default**
dict.update(dict2):把字典dict2的键/值对更新到dict里,如果有相同的key，会替换成update的值
pop(key[,default]):删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem():返回并删除字典中的最后一对键和值。
```python
obj = {}
obj['name'] = 'zhangsan'
print(obj) # {'name': 'zhangsan'}
print(obj['name'])  # zhangsan # 取不到会报错

print(obj.get('age')) # 18 如果取不到不会报错

for i in obj:
    print(i) # 遍历出来的是key


obj.clear()
print(obj)
obj['name'] = 'zhangsan'
obj['age'] = 19
obj['ferght'] = 100
print(obj.copy())
print(obj.get('aaa',1), obj)  # 1 {'name': 'zhangsan', 'age': 19, 'ferght': 100}
print(obj.setdefault('aaa',1),obj) # 1 {'name': 'zhangsan', 'age': 19, 'ferght': 100, 'aaa': 1}
# print(obj.has_key('name')) # py3 remove
print(obj.__contains__('name'))  # True

obj1 = {'name': 'lisi', 'age':20,'hhh':'hello'}
obj1.update(obj)
print(obj1) # {'name': 'zhangsan', 'age': 19, 'hhh': 'hello', 'ferght': 100, 'aaa': 1}

print(obj2.fromkeys(tuple5)) # {'name': None, 'age': None}
print(obj2.fromkeys(tuple5, 10)) # {'name': 10, 'age': 10}
print(obj2.fromkeys(list1))
print(obj2.fromkeys(list1,10))
print(obj2) # {}
```
字典里面的函数：
items() values() keys()
```python
# 转为列表包含元组的形式
print(obj.items()) # dict_items([('name', 'zhangsan'), ('age', 18)])
# 取出字典中所有的值，保存到列表中
print(obj.values()) # dict_values(['zhangsan', 18])
# 取出字典中所有的key 保存到列表中
print(obj.keys()) # dict_keys(['name', 'age'])

for i in obj.items():
    print(i) 
    # ('name', 'zhangsan')   
    #  ('age', 18)
for key, value in obj.items():
    print(key,value)
    '''
    name zhangsan
    age 18
    '''
```
删除：
del dict[key]
内置函数：
dict.pop(key, default) # 返回删除的value，会改变dict.default为删除的时候找不到key，返回默认值
dict.popitem() # 一般从末尾删除元素
```
#### 集合 set
无序，不重复的集合
s1 = set() # 创建空集合只能用set()方式，因为 s1={} 声明一个字典
{元素1,元素2,元素3,...} 
```python
list1 = [1,2,2,3,4]
print(set(list1))
```
add
update
```python
s1 = set()
s1.add('hello')
s1.add('111')
s1.add(2)
print(s1) # {'111', 2, 'hello'}
s1.update((1,2))
print(s1) # {'111', 1, 2, 'hello'}
s1.add((1,2))
print(s1) # {1, 2, (1, 2), '111', 'hello'}
```

删除：
pop # 删除第一个
remove # 删除指定元素 删除不存在元素会报错
clear
dicard # 删除指定元素 删除不存在元素不报错

符号操作：
in
== ：判断两个集合中的内容是否相等 
-： 差集 difference
&： 交集 intersection
| ： 并集 union
^：对称差集 ----- 两个集合中不同的元素
不支持+ *
difference_update() # 加上update，就是会改变集合 s1.difference_update(s2)  将差集赋值给s1
```python
# 集合的交集，并集，差集合
s1 = {1,2,3,4}
s2 = {1,2,3,5,6,7}

s3 = s2 - s1
print(s3) # {5, 6, 7}
print(s2.difference(s1)) # {5, 6, 7}

s4 = s1 & s2
print(s1.intersection(s2)) # {1, 2, 3}
print(s4) # {1, 2, 3}

s5 = s1 | s2
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7}
print(s5) # {1, 2, 3, 4, 5, 6, 7}

 # 对称差集 ----- 两个集合中不同的元素
print(s1^s2) # {4, 5, 6, 7}
```

#### 可变 不可变
不可变： 对象所指的内存中的值是不可变的（int string float tuple）
可变: dict字典 list列表 set集合,  值改变
```python
# 变量的值改变，是重新指向了一个地址空间
str = 'hello'
print(id(str)) # 4335977392
str = 'hello1'
print(id(str)) # 4335985392

li = [1,2,3]
print(li, id(li)) # [1, 2, 3] 4519372928
li.pop()
print(li,id(li)) # [1, 2] 4519372928

s = {1,2,3}
print(s,id(s)) # {1, 2, 3} 4527199616
s.discard(1)
print(s,id(s)) # {2, 3} 4527199616
```
#### 类型转换
str
int
list
dict
set
tuple
```python
# str int tuple list set dict
s = 'hello'
sint = '9'
print(int(sint), type(sint)) # 9 <class 'str'>
print(list(s)) # ['h', 'e', 'l', 'l', 'o']
print(set(s)) # {'h', 'e', 'l', 'o'}
# print(tuple(s))
print(dict(s))  # 字典需要序列才能转
```


isinstance(var1, int) # True

enumerate
> 该函数在字面上是枚举、列举的意思，用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中，可同时得到数据对象的值及对应的索引值
```python
for i, index in enumerate({1,2,3}):
    print(i, index)
# 0 1
# 1 2
# 2 3
```