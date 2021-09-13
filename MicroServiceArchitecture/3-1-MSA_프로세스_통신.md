# MSA 프로세스 통신

## IPC 개요
### 통신 상호작용 기준  
**첫번째**
* 일대일: Client의 요청은 한개의 서비스가 처리
* 일대다: Client의 요철을 여러개의 서비스가 처리

**두번째**
* 동기: Client가 서비스에게 요청하고 응답 대기를 하며 블로킹도 할 수 있음
* 비동기: Client가 블로킹 하지 않으며 응답은 바로 하지 않아도 됨 

### 통신 상호작용 종류
* 요청/응답 : Client는 서비스에 요청을 하고 응답 대기. 강한 결합의 상호작용 스타일
* 비동기 요청/응답 : Client는 서비스에 요청을 하고 서비스는 비동기적으로 응답
* 단방향 알림 : Client는 요청만 하고 서비스는 응답을 하지 않음

### API 설계
API 기능 추가/변경/삭제 등을 통해서 충분히 변경될 수 있다. 따라서 이런 문제를 해결하기 위해서 
프로젝트 전략을 만들어야 한다.

* 시멘틱 버저닝 : API 버전 번호를 MAJOR, MINOR, PATCH 세 파트로 구성하고 규칙에 따라 증가
```
MAJOR : 하위 호환 되지 않는 변경을 API에 적용
MINOR : 하위 호환 되는 변경을 API에 적용
PATH : 하휘 호환 되는 오류/버그 수정
```
```
MAJOR 같이 변경이 클 경우에 REST API의 경우 두가지 방법이 있다.
1. Request URL에 버전을 포함 
- https://host.com/v1/service 
- https://host.com/v2/service

2. Request Header에 버전을 포함
- Accept: application/xml; version=1
- Accept: application/json; version=2
``` 

# 
## 동기 RPI 패턴 응용 통신
