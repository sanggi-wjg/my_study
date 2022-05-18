### MySQL
```
docker pull mysql:5.7.34

docker run -d -p 33061:3306 -e MYSQL_ROOT_PASSWORD=wpdlwl --name mysql_1 mysql:5.7.34
docker run -d -p 33062:3306 -e MYSQL_ROOT_PASSWORD=wpdlwl --name mysql_2 mysql:5.7.34
docker run -d -p 33063:3306 -e MYSQL_ROOT_PASSWORD=wpdlwl --name mysql_3 mysql:5.7.34
```