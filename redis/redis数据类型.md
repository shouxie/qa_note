<!--
 * @Author: shouxie
 * @Date: 2020-03-11 15:31:13
 * @Description: 
 -->
#### Redis 数据类型
Redis支持五种数据类型：
- string（字符串）
> string 是 redis 最基本的类型，你可以理解成与 Memcached 一模一样的类型，一个 key 对应一个 value。
string 类型是二进制安全的。意思是 redis 的 string 可以包含任何数据。比如jpg图片或者序列化的对象。
string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。
```shell
set test 'hello'
get test
# hello
```
- hash（哈希）
> Redis hash 是一个键值(key=>value)对集合。
Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。
```shell
hmset test field1 'hello' field2 'world'
hget test field1
# hello
hget test field2
# world
```
- list（列表）
> Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
```shell
lpush test test1
lpush test test2
lpush test test3
lrange test 0 3
# "test1"
# "test2"
# "test3"
```
- set（集合）
> Redis 的 Set 是 string 类型的无序集合。
集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。
**sadd 命令**
添加一个 string 元素到 key 对应的 set 集合中，成功返回 1，如果元素已经在集合中返回 0。
```shell
sadd test test1
sadd test test2
smembers test
# "test1"
# "test2"
```
- zset(sorted set：有序集合)
> Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。
不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。
zset的成员是唯一的,但分数(score)却可以重复。
**zadd 命令**
添加元素到集合，元素在集合中存在则更新对应score
```shell
zadd test 0 test1
zadd test 1 test2
zadd test 0 test3
zrangebyscore test 0 10
# test1
# test3
# test2
```

#### Redis 命令
> Redis 命令用于在 redis 服务上执行操作。
要在 redis 服务上执行命令需要一个 redis 客户端
```shell
redis-cli
# 连接本地redis server
ping
#pong
# 连接远程
redis-cli -h host -p port -a password
```
- Redis 键(key)
> Redis 键命令用于管理 redis 的键。
command redis