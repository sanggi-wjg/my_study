## docker compose

```shell script
cd /home
git clone https://github.com/sanggi-wjg/flask-jwt-demo.git

cd /flask-jwt-demo
docker build -t flask-jwt .
#docker run -d -p 8085:8085 --name flask-jwt flask-jwt
```