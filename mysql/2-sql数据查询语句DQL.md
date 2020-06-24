
SELECT column_name FROM table_name WHERE column_name 运算符 value
运算符|描述|
-|-|
=|等于|
<> 或 !=|不等于|
>|大于|
<|小于|
>=|大于等于|
<=|小于等于|
between and |选取介于两个值之间的数据范围；在MySQL中，相当于>=并且<=|
在where子句中，使用and、or可以把两个或多个过滤条件结合起来。
and、or运算符语法
SELECT column_name FROM table_name WHERE condition1 AND condition2 OR condition3
and：表示左右两边的条件同时成立
or：表示左右两边只要有一个条件成立
- 运算符in的使用
>运算符 IN 允许我们在 WHERE 子句中过滤某个字段的多个值。
```sql
#where子句使用in语法
SELECT column_name FROM table_name WHERE column_name IN(value1, value2, …)
```
- 运算符like的使用
在where子句中，有时候我们需要查询包含xxx 字符串的所有记录，这时就需要用到运算符like。
```sql
#where子句使用like语法
SELECT column_name FROM table_name WHERE column_name LIKE ‘%value%’
```
说明：
1、LIKE子句中的%类似于正则表达式中的*，匹配任意0个或多个字符
2、LIKE子句中的_匹配任意单个字符
3、LIKE子句中如果没有%和_，就相当于运算符=的效果

#### 数据查询语言DQL-MySQL常用函数讲解
>MySQL函数指的是MySQL数据库提供的内置函数，包括数学函数、字符串函数、日
期和时间函数、聚合函数、条件判断函数等，这些内置函数可以帮助用户更方便地处理表中的数据，
简化用户的操作。

函数|描述|
-|-|
数学函数|abs、sort、mod、sin、cos、tan、cot等|
字符串函数|如length、lower、upper、trim、substring等|
日期和时间函数|now、curdate、curtime、sysdate、date_format、year、month、week等|
聚合函数|count、sum、avg、min、max|
条件判断函数|IF、IFNULL、CASE WHEN等|
系统信息函数|VERSION、DATABASE、USER等|
加密函数|MD5、SHA1、SHA2等|

```sql
select md5('qpp');
select user();
select abs(-10);
```

- 函数now()用于返回当前的日期和时间
```sql
select now();
```
- 函数date_format()用于以指定的格式显示日期/时间。
```sql
select name, date_format(birthday, '%Y/%m/%d') from user;
```
- 聚合函数是对一组值进行计算，并返回单个值。
count: 返回符合条件的记录总数
sum: 返回指定列的总和，忽略空值
avg: 返回指定列的平均值，忽略空值
min: 返回指定列的最小值，忽略空值
max: 返回指定列的最大值，忽略空值
```sql
select count(*) from user;
select sum(salary) from user;
select avg(salary) from user;
...
```
- 函数ifnull()用于处理NULL值。
ifnull(v1,v2)，如果 v1 的值不为 NULL，则返回 v1，否则返回 v2。
- case when是流程控制语句，可以在SQL语句中使用case when来获取更加准确和直接的结果。
SQL中的case when类似于编程语言中的if else或者switch。
```sql
#case when的语法有2种
CASE [col_name] WHEN [value1] THEN [result1]…ELSE [default] END
CASE WHEN [expr] THEN [result1]…ELSE [default] END
select name, case sex
when 1 then '男'
when 2 then '女'
else ''
end as sex from user;
```

#### order by    
```sql
select * from employee order by salary;
# asc升序 desc降序 默认asc
```
#### limit

```sql
select * from employee limit 5;
# limit 偏移量, 最大分页数
select * from employee limit 0, 5；
```

####数据查询语言DQL-GROUP BY与HAVING的使用
>group by表示根据某种规则对数据进行分组，它必须配合聚合函数进行使用，对数
据进行分组后可以进行count、sum、avg、max和min等运算。
```sql
#group by语法
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name
select dept, count(*) from employee group by dept;
select dept, max(salary) from employee group by dept;
```
说明：
1. aggregate_function表示聚合函数。
2. group by可以对一列或多列进行分组。

>在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数一起使用。HAVING 子句可
以对分组后的各组数据进行筛选。
```sql
#having语法
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
HAVING aggregate_function(column_name) operator value
# 查询部门人数小于10的部门
select dept, count(*) from employee group by dept having count(*) < 10;
# 查询部门最高工资最高的部门
select dept, max(salary) from employee group by dept having max(salary);
```

#### group_concat
>配合group by一起使用，用于将某一列的值按指定的分隔符进行拼接，MySQL默认
的分隔符为逗号。
```sql
#group_concat语法
group_concat([distinct] column_name [order by column_name asc/desc ] [separator '分隔符'])
select dept, count(*), group_concat(name) from employee group by dept;
select dept, count(*), group_concat(name order by name separator ';') from employee group by dept;
```
#### distinct的使用
>distinct用于在查询中返回列的唯一不同值（去重复），支持单列或多列。在实际的应用中，表中的
某一列含有重复值是很常见的，如employ表的dept列。如果在查询数据时，希望得到某列的所有
不同值，可以使用distinct。
```sql
#distinct语法
SELECT DISTINCT column_name, column_name
FROM table_name;
```

#### 数据查询语言DQL-表连接（内连接、外连接、自连接）
>表连接（JOIN）是在多个表之间通过一定的连接条件，使表之间发生关联，进而能从多个表之间获
取数据。
```sql
#表连接语法
SELECT table1.column, table2.column
FROM table1, table2
WHERE table1.column1 = table2.column2;
```
内连接 join 或 inner join
外连接 左外连接，left join 右外连接，right join 全外连接，full join
自连接 同一张表内的连接

连接类型|定义|图示|例子|
-|-|-|-|
内连接|只连接匹配的行|-|select A.c1, B.c2 from A join B on A.c3 = B.c3|
左连接|包含左表的全部行（不管右表是否存在与之匹配的行），以及右表中全部匹配的行|-|select A.c1, B.c2 from A left join B on A.c3 = B.c3|
右连接|包含右表的全部行（不管左表是否存在与之匹配的行），以及左表中全部匹配的行|-|select A.c1, B.c2 from A right join B on A.c3 = B.c3|
全连接|包含左右两个表的全部行（不管在另一个表中是否存在与之匹配的行）|-|select A.c1, B.c2 from A full join B on A.c3 = B.c3|

交叉连接（cross join）：没有用where子句的交叉连接将产生笛卡尔积，第一个表的行数乘以第二个表的行数等于笛卡尔积
和结果集的大小。

```sql
# 内连接
select A.stu_no, A.stu_name, B.course, B.grade from stu A join sc B on A.stu_no = B.stu_no;
select A.stu_no, A.stu_name, B.course, B.grade from stu A, sc B where A.stu_no = B.stu_no;
select A.stu, A.stu_name, B.course, B.grade from stu A inner join sc B on A.stu_no = B.stu_no;
# 左连接
select A.stu_no, A.stu_name, B.course, B.grade from stu A left sc B on A.stu_no = B.stu_no;
```

#### 自连接查询
>自连接是一种特殊的表连接，它是指相互连接的表在物理上同为一张表，但是逻辑上是多张表。自
连接通常用于表中的数据有层次结构，如区域表、菜单表、商品分类表等。
```sql
#自连接语法
SELECT A.column, B.column
FROM table A, table B
WHERE A.column = B.column

create table area(
  id int not null auto_increment primary key,
  pid int not null,
  name varchar(30)
);
insert into area(id, pid, name) values(1,0,'河南省'), (2,1,'郑州市');
select A.id,A.name,B.name as provinceName from area A, area B where A.pid = B.id;
```

#### 子查询in
>它允许我们在 WHERE 子句中过滤某个字段的多个值。
```sql
#where子句使用in语法
SELECT column_name FROM table_name WHERE column_name IN(value1, value2, …)
```
>如果运算符 in 后面的值是来源于某个查询结果，并非是指定的几个值，这时就需要用到子查询。子
查询又称为内部查询或嵌套查询，即在 SQL 查询的 WHERE 子句中嵌入查询语句。
```sql
#子查询in语法
SELECT column_name FROM table_name
WHERE column_name IN(
 SELECT column_name FROM table_name [WHERE]
);
select A.stu_no, A.stu_name from stu A where A.stu_no in (select B.stu_no from sc B);
```

#### 子查询exists
>EXISTS是子查询中用于测试内部查询是否返回任何行的布尔运算符。将主查询的数据放到子查询中
做条件验证，根据验证结果（TRUE 或 FALSE）来决定主查询的数据结果是否保留。
```sql
#where子句使用exists语法
SELECT column_name1
FROM table_name1
WHERE EXISTS (SELECT * FROM table_name2 WHERE condition);
select A.stu_no,A.stu_name from stu A where A.stu_no exists(select B.stu_no where sc B where A.stu_no = B.stu_no);
```