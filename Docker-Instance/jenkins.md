### Jenkins
```shell script
https://hub.docker.com/r/jenkins/jenkins

sudo docker pull jenkins/jenkins:lts-jdk11
sudo docker run --name demo-jenkins -p 8080:8080 -p 50000:50000 -d jenkins/jenkins:lts-jdk11
sudo docker start demo-jenkins 
sudo docker exec -it demo-jenkins bash
> cat /var/jenkins_home/secrets/initialAdminPassword

# password
root / wpdlwl 
```