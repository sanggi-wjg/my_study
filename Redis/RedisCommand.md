## redis-cli Command
* https://redis.io/docs/manual/cli/

```shell
# 접속
docker exec -it demo-redis redis-cli

# 모니터링 
docker exec -it demo-redis redis-cli monitor

# 기타
docker exec -it demo-redis redis-cli info
docker exec -it demo-redis redis-cli help
```

```shell
docker exec -it demo-redis redis-cli --bigkeys

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Biggest string found so far '"keyboard"' with 4 bytes

-------- summary -------

Sampled 1 keys in the keyspace!
Total key length in bytes is 8 (avg len 8.00)

Biggest string found '"keyboard"' has 4 bytes

1 strings with 4 bytes (100.00% of keys, avg size 4.00)
0 lists with 0 items (00.00% of keys, avg size 0.00)
0 hashs with 0 fields (00.00% of keys, avg size 0.00)
0 streams with 0 entries (00.00% of keys, avg size 0.00)
0 sets with 0 members (00.00% of keys, avg size 0.00)
0 zsets with 0 members (00.00% of keys, avg size 0.00)
```

```shell
docker exec -it demo-redis redis-cli --stat
------- data ------ --------------------- load -------------------- - child -
keys       mem      clients blocked requests            connections          
2          1.48M    3       0       208 (+0)            30          
2          1.46M    3       0       209 (+1)            30          
2          1.47M    3       0       210 (+1)            30          
2          1.47M    3       0       211 (+1)            30          
2          1.47M    3       0       212 (+1)            30          
2          1.47M    3       0       213 (+1)            30          
2          1.46M    3       0       214 (+1)            30          
2          1.47M    3       0       215 (+1)            30          
2          1.47M    3       0       216 (+1)            30          
4          1.49M    3       0       221 (+5)            30          
4          1.50M    3       0       224 (+3)            30          
4          1.49M    3       0       225 (+1)            30          
4          1.47M    3       0       226 (+1)            30          
4          1.47M    3       0       227 (+1)            30          
4          1.47M    3       0       228 (+1)            30          
4          1.47M    3       0       229 (+1)            30          
4          1.47M    3       0       230 (+1)            30          
4          1.47M    3       0       231 (+1)            30          
4          1.47M    3       0       232 (+1)            30          
4          1.47M    3       0       233 (+1)            30 
```

---
## CRUD Command
### Select All
```shell
127.0.0.1:6379> keys *
1) "accounts"
hgetall {key}
hget {key} {column}
```


### Get, Set key:value 
```shell
set key value
get key
```
```shell 
127.0.0.1:6379> set key value
OK
127.0.0.1:6379> get key
"value"
```


### Multiple Get, Set Key:Value
```shell
mset key value key value
mget key key
```
```shell
127.0.0.1:6379> mset keyboard abko mouse zowie-gear
OK
127.0.0.1:6379> get keyboard
"abko"
127.0.0.1:6379> get mouse
"zowie-gear"
127.0.0.1:6379> mget keyboard mouse
1) "abko"
2) "zowie-gear"
```


### Set Key:Value With Expire
시간은 초단위
```shell
setex key second value
```
```shell
127.0.0.1:6379> setex monitor 10 AOC
OK
127.0.0.1:6379> get monitor
"AOC"
127.0.0.1:6379> get monitor
(nil)
```


### Delete Key
```
del key
```
```shell
127.0.0.1:6379> keys *
1) "keyboard"
2) "accounts"
3) "mouse"
4) "key"

127.0.0.1:6379> del keyboard
(integer) 1
127.0.0.1:6379> del accounts
(integer) 1
127.0.0.1:6379> del mouse
(integer) 1
127.0.0.1:6379> del mouse key
(integer) 1
127.0.0.1:6379> keys *
(empty array)
```
Delete시 (integer) n이 출력 되는데, n은 삭제 개수이다.  
0개면 아무것도 삭제가 안된거고 1은 한개, 2는 두개...


### Get Time Remaining Until Expire
```shell
ttl key (second)
pttl key (milli second)
```
```shell
127.0.0.1:6379> setex speaker 60 britz
OK
127.0.0.1:6379> ttl speaker
(integer) 55
127.0.0.1:6379> ttl speaker
(integer) 54
127.0.0.1:6379> pttl speaker
(integer) 52048
127.0.0.1:6379> pttl speaker
(integer) 47266
```


### keys like 검색  
```shell
keys *k*
```
```shell
127.0.0.1:6379> mset keyboard abko mouse zowie-gear speaker britz
OK
127.0.0.1:6379> keys *k*
1) "speaker"
2) "keyboard"
127.0.0.1:6379> keys *m*
1) "mouse"
```


### Delete All
```shell
flushall
```
```shell
127.0.0.1:6379> flushall
OK
127.0.0.1:6379> keys *
(empty array)
```


### Exist 검색
```shell
exsits key
```
```shell
127.0.0.1:6379> set keyboard abko
OK
127.0.0.1:6379> exists keyboard
(integer) 1
127.0.0.1:6379> exists mouse
(integer) 0
```

### Length 검색
```shell
strlen key
```
```shell
127.0.0.1:6379> strlen keyboard
(integer) 4
```

### Get, Set Hash
```shell
hset key field value
```
```shell
127.0.0.1:6379> hset user-1 name Snow
(integer) 1
127.0.0.1:6379> hset user-1 age 10
(integer) 1

127.0.0.1:6379> hmget user-1 name age
1) "Snow"
2) "10"
```
