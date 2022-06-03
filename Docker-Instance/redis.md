### Redis
```shell script
sudo docker pull redis:6.2.5
sudo docker run --name demo-redis -p 6379:6379 -d redis:6.2.5 redis-server --appendonly yes
sudo docker exec -it demo-redis bash
```

### Command
```shell
docker exec -it demo-redis redis-cli

keys *
get {key}
hgetall {key}
hget {key} {column}

```