# Micro Service Pattern

```
마이크로 서비스 패턴
저. 크리스 리처드슨
```

## MSA 사용 기술 스택

#### 배포 
```
# Repository
github or gitlab

# CI/CD
Jenkins

# 배포 자동화
Netflix Spinnaker
Pivotal Cloud Foundry
RedHat PaaS
Docker Swarm
Kubernates
```

#### Database
```
SAGA (일관성 유지)
CQRS (Command Query Responsiblity Segregation, 커맨드 쿼리 책임 분리)
```

#### 서비스 디스커버리
```
Netflix Eureka
Apahce zookeeper
etcd
HashiCorp consul
```

#### 보안
```
JWT
OAuth2.0
```

#### 통신 패턴 (RPI 패턴) - REST API 대체
```
GraphQL
Netflix Falcor(팔코)
gRPC

# 통신 실패에 대한 대처 패턴
Netflix Hystrix(히스트릭스)

# 메시징 큐, 브로커 (비동기)
RabbitMQ
ActiveMQ
ZeroMQ
Apache Kafka
Celery
AWS Kinesis
AWS SQS
```
