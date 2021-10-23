# Airflow
#### Concepts
Airflow 는 프로그래밍을 통해서 workflows를 작성하고 스케쥴링 하고 모니터링 하는 플랫폼 이다.

Airflow 는 Directed Acyclic Graphs(DAGs)을 통해서 workflows를 작성하며
Airflow 스케줄러는 지정된 종속에 따라서 array of workers를 이용하여 Task를 실행 한다.

DAG은 tasks 사이에 종속성과 실행될 순서, 재시도를 명시 해야하며, 
Taks는 무엇을 할지 작성하여야 한다.
![airflow-1](https://github.com/sanggi-wjg/my_study/blob/main/Airflow/data/airflow-1.png?raw=true)

#### Strength points
Airflow는 Python 기반으로 쉽게 작성 가능하며 콘솔을 통해서 Task 작업 확인과 bottleneck을 찾을때도 유용하다.

## Install
#### Requirements
적어도 4Gb 이상의 메모리 이상이여야 작업이 적절하게 실행 될 것.(이상은 8Gb)
docker-compose 버전이 1.29.1 이상이여야 docker-compose.yaml 이 지원한다.

### Docker
```shell script
# fetch
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.0/docker-compose.yaml'
```
#### file contents
* **airflow-scheduler** : 모든 tasks, DAGs의 모니터링과 종속성 완료시 task instance를 trigger.
* **airflow-webserver** : http://localhost:8080
* **airflow-worker** : Scheduler가 전달한 tasks 를 실행하는 worker.
* **airflow-init** : Initialization service.
* **flower** : Flower는 환경 모니터링 앱이다. http://localhost:5555
* **postgre** : Database
* **Redis** : Scheduler에서 worker로 메시지 전달 브로커 
![airflow-2](https://github.com/sanggi-wjg/my_study/blob/main/Airflow/data/airflow-2.png?raw=true)