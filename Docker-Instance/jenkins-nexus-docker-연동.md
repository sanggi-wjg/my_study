## 연동

https://jungeeyou.github.io/docker-5-post/

### Docker 테스트
```shell script
cd /home
git clone https://github.com/sanggi-wjg/flask-jwt-demo.git

cd /flask-jwt-demo
docker build -t flask-jwt .
#docker run -d -p 8085:8085 --name flask-jwt flask-jwt
```

#### jenkins nexus docker hub credential 추가
![jenkins-1](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/jenkins-1.png?raw=true)

```
production, alpha 등 환경에서는 소스 커밋이나 머지시에 한개 파이프라인에서 빌드해서 
nexus에 push 하고 다른 파이프라인에서는 nexus에서 pull 받아서 배포하고 그런식으로 하면 될듯?
```

## 배포 결과
![jenkins-2](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/jenkins-2.png?raw=true)
![jenkins-3](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/jenkins-3.png?raw=true)
![jenkins-4](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/jenkins-4.png?raw=true)