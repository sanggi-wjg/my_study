
## 설치 및 세팅

### 환경
```shell
Neuxs 설치 서버 : xxx.146.5.51
클라이언트 서버  : xxx.146.5.52
```

### Install Nexus
```shell
# docker image
https://hub.docker.com/r/sonatype/nexus3/

sudo docker pull sonatype/nexus3:3.34.1
sudo docker run -d -p 8081:8081 -p 5000:5000 --name demo-nexus sonatype/nexus3:3.34.1
sudo docker exec -it demo-nexus bash

# IP:port 접속 -> 로그인 시도 -> 밑에서 비밀번호 확인 
> cat /nexus-data/admin.password
```

### Nexus 세팅
Nexus Repo 세팅은 아래 확인
```shell
https://velog.io/@king/private-docker-registry
```

### Nexus 서버와 사용할 Client 서버에 아래 파일 추가
```shell
vi /etc/docker/daemon.json
{
    "insecure-registries" : ["xxx.146.5.51:5000"]
}

service docker restart
# Nexus 서버
docker restart demo-nexus
```

### Docker hub 로그인
```shell
docker login xxx.146.5.51:5000

Username: admin
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store
```

## Docker Image build

```shell
git clone https://github.com/sanggi-wjg/flask-docker-template.git

cd flask-docker-template
docker build -t demo-flask .
docker run -d -p 9001:5000 --name demo-flask demo-flask

# 접속 테스트
xxx.146.5.52:9001
```

```shell
docker tag 4ccf18e96b28 xxx.146.5.51:5000/demo-flask
# docker tag [IMAGE_ID] [DOCKER_HUB]/[IMAGE_NAME]

docker push xxx.146.5.51:5000/demo-flask

# pull 은 아래처럼 하면 됨
# docker pull xxx.146.5.51:5000/demo-flask
```