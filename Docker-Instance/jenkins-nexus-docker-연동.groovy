node {
  withCredentials([[$class: 'UsernamePasswordMultiBinding',
     credentialsId: 'nexus-docker-hub',
    ]])
     {
        stage('Git Checkout')
        {
            git branch: 'main',
            url: 'https://github.com/sanggi-wjg/flask-jwt-demo.git'
        }
        stage('Build')
        {
            sh "docker build -t flask-jwt ."
        }
        stage('Tag')
        {
            sh "docker tag ${DOCKER_USER_ID}/flask-jwt ${DOCKER_USER_ID}/flask-jwt:${BUILD_NUMBER}"
        }
        stage('Push')
        {
            sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
            sh "docker push ${DOCKER_USER_ID}/flask-jwt:${BUILD_NUMBER}"
            sh "docker push ${DOCKER_USER_ID}/flask-jwt:latest"
        }
        stage('Run') {
            sh "docker run -d -p 8085:8085 --name flask-jwt flask-jwt"
        }
    }
}