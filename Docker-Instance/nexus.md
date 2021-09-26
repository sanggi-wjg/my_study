### Nexus
```shell script
https://hub.docker.com/r/sonatype/nexus3/
https://velog.io/@king/private-docker-registry

sudo docker pull sonatype/nexus3:3.34.1
sudo docker run -d -p 8081:8081 -p 5000:5000 --name demo-nexus sonatype/nexus3:3.34.1
sudo docker exec -it demo-nexus bash
> cat /nexus-data/admin.password

# password
admin / wpdlwl
```

### Nexus 세팅
#### docker-hosted, docker-hub 추가
![nexus-1](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/nexus-1.png?raw=true)

##### repo-docker-hosted 추가
![nexus-2](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/nexus-2.png?raw=true)
![nexus-3](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/nexus-3.png?raw=true)

##### docker-hub 추가
![nexus-4](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/nexus-4.png?raw=true)
![nexus-5](https://github.com/sanggi-wjg/my_study/blob/main/Docker-Instance/data/nexus-5.png?raw=true)

### nexus 연동
```shell script
# docker http
sudo vi /etc/docker/daemon.json
{
    "insecure-registries" : ["localhost:5000"]
}

```

### nexus docker hub 테스트
```shell script
# docker hub login
docker login localhost:5000

# docker hub push
docker images
REPOSITORY        TAG         IMAGE ID       CREATED       SIZE
sonatype/nexus3   3.34.1      8a9245af1b06   2 days ago    655MB
redis             latest      02c7f2054405   3 weeks ago   105MB
jenkins/jenkins   lts-jdk11   619aabbe0502   4 weeks ago   441MB

# docker tag
docker tag 619aabbe0502 localhost:5000/jenkins/jenkins:20210925

docker images
REPOSITORY                       TAG         IMAGE ID       CREATED       SIZE
sonatype/nexus3                  3.34.1      8a9245af1b06   2 days ago    655MB
redis                            latest      02c7f2054405   3 weeks ago   105MB
jenkins/jenkins                  lts-jdk11   619aabbe0502   4 weeks ago   441MB
localhost:5000/jenkins/jenkins   20210925    619aabbe0502   4 weeks ago   441MB

docker push localhost:5000/jenkins/jenkins:20210925

# docker hub pull
docker pull localhost:5000/jenkins/jenkins:20210925
``` 