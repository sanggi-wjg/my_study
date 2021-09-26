node {
  withCredentials([[$class: 'UsernamePasswordMultiBinding',
     credentialsId: 'nexus-docker-hub2',
     usernameVariable: 'DOCKER_USER_ID',
     passwordVariable: 'DOCKER_USER_PASSWORD'
    ]])
     {
        stage('Git Checkout')
        {
            git branch: 'main',
            url: 'https://github.com/sanggi-wjg/flask-jwt-demo.git'
        }
        stage('Build')
        {
            sh "docker build -t ${DOCKER_USER_ID}/flask-jwt ."
        }
        stage('Tag')
        {
            sh "docker login localhost:5000 -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
            //sh "docker tag ${DOCKER_USER_ID}/flask-jwt ${DOCKER_USER_ID}/flask-jwt:${BUILD_NUMBER}"
            sh "docker tag ${DOCKER_USER_ID}/flask-jwt localhost:5000/flask-jwt:${BUILD_NUMBER}"
        }
        stage('Push')
        {
            //sh "docker push ${DOCKER_USER_ID}/flask-jwt:${BUILD_NUMBER}"
            //sh "docker push ${DOCKER_USER_ID}/flask-jwt:latest"
            sh "docker push localhost:5000/flask-jwt:${BUILD_NUMBER}"
        }
        stage('Run') {
            sh "docker run -d -p 8085:8085 --name flask-jwt localhost:5000/flask-jwt:${BUILD_NUMBER}"
        }
    }
}