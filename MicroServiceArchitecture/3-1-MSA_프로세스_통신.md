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
RPI는 Client가 요청을 보내면 서비스가 처리후 응답을 회신하는 통신 방법.  

### RPI 작동 원리
Client 비지니스 로직 호출 -> RPI 프록시 인터페이스 호출 -> RPI 서버 어댑터 접수 -> 서비스 비지니스 로직  
이후 순서대로 응답 반환

### 동기 RPI 패턴 : REST API
대표적인 API. 이하 내용 생략

##### REST API 의 성숙도 모델
* 레벨 0 : 서비스별로 URL에 POST 요청을 하여 서비스 호출. 호출시 어떤 비지니스 로직을 호출할지와 매개변수 전달.
* 레벨 1 : 비지니스 로직이 나뉘어 있고 각 매개변수가 지정 되어있는 URL POST 요청.
* 레벨 2 : HTTP Method 를 활용해 GET, POST, PUT 등을 서비스 별로 용도에 맞게 사용.
* 레벨 3 : 서비스를 HATEOAS 기반으로 설계. HATEOAS는 요청 응답 값에 해당 리소스가 할 수 있는 URL 을 반환 하는 것.
(https://en.wikipedia.org/wiki/HATEOAS)
> Hypermedia as the Engine of Application State (HATEOAS) is a constraint of the REST application architecture that distinguishes it from other network application architectures.  
> HATEOAS 는 다른 네트워크 애플리케이션 아키텍쳐로부터 구별하는 REST 애플리케이션 아키텍쳐의 규약
```json
[REQUEST]
GET /accounts/12345 HTTP/1.1
Host: bank.example.com

[RESPONSE]
HTTP/1.1 200 OK

{
    "account": {
        "account_number": 12345,
        "balance": {
            "currency": "usd",
            "value": 100.00
        },
        "links": {
            "deposits": "/accounts/12345/deposits",
            "withdrawals": "/accounts/12345/withdrawals",
            "transfers": "/accounts/12345/transfers",
            "close-requests": "/accounts/12345/close-requests"
        }
    }
}
```

##### REST API 한계에 대한 해결책
REST API는 비지니스 객체 중심이다. 예를 들어 주문과 소비자의 정보를 가져오기 위해서는 각각 1번씩 총 2번의 요청이 필요하다.  
이런 한계를 해결하기 위한 2가지의 방법이 있다.
1. 애플리케이션 규약을 정해서 서비스에서 연관 서비스도 호출하도록 하는 것  
(GET https://order.host.com/orders/order-id-1?expand=consumer)  
이 방법은 시간이 지나서 규모가 방대해질 수록 비효율적이고 개발이 힘들어지는 단점이 있다.
2. `GraphQL 이나 Netflix Falcor(팔코), gRPC` 를 사용 하는 것이다.

#
### 동기 RPI 패턴 : gRPC
(https://grpc.io/)  
gRPC는 다양한 언어로 Client/Server를 구현할 수있는 이진 메시지 기반 프로토콜의 프레임 워크이며
하나 이상의 서비스와 요청/응답 메시지 정의로 구성.

##### Install GO package
```
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
```
TODO: Go 로 gRPC demo 를 구현 하자
```

```