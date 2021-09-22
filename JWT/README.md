# Json Web Token
JWT 는 요청자/응답자 간에 JSON 객체를 안전하게 전송할 수 있는 간결하고 자기 포함된 개방형 표준(RFC 7519)
정보는 디지털 서명되어 있어 신뢰할 수 있으며 Secret(HMAC 알고리즘), 
RSA나 ECDSA 를 이용한 public/private 키를 이용하여 서명할 수 있다.

## JWT 사용 하는 케이스
### Authorization
JWT를 사용하는 흔한 케이스.   
유저 로그인 후, 요청에 대해서 JWT가 포함 될 것이고 이를 통해서 route, service, resource 등
허용/비허용 제한할 수 있다. 

Single Sign On 은 도메인간에 쉽게 사용 가능하며 작은 자원을 사용해 최근 많이 사용 된다.

### Information Exchange
JWT는 요청/응답간 안전하게 자료 교환할 수 있는 방법이다. JWT는 서명화 되어 reciever 는 sender가 누군지 
확신할 수 있기 때문이다. 또 payload 와 header 를 통해 계산된 서명이라 위조에 대해서 덜하다.

## JWT 구성
JWT 는 세 파트로 이루어져 있다.
1. Header
2. Payload
3. Signature
![1](https://raw.githubusercontent.com/sanggi-wjg/my_study/main/JWT/data/1.png)

### 1. Header
Header 는 두 파트로 이루어져 있다. Base64Url 로 encode 될 JWT 의 첫번째 파트 이다.
1. 첫째는 JWT의 타입
1. 두번째는 서명 알고리즘(HMAC SHA256, RSA, ...)
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### 2. Payload
Payload 는 claims 가 포함되어 있다. claims는 세가지 타입이 있으며 
Base64Url 로 encode 될 JWT 의 두번째 파트 이다.

1. **Registered claims** : 선정의 된 claims 이며 필수는 아니지만 사용을 권장한다.  
iss (issuer), exp (expiration time), sub (subject), aud (audience), ...  
(https://datatracker.ietf.org/doc/html/rfc7519#section-4.1)

1. **Public claims** : JWT 사용시 마음대로 정의할 수 있으나 충돌에 주의해야 한다.
(https://www.iana.org/assignments/jwt/jwt.xhtml)  

1. **Private claims** : Registered/Public claims 이 아닌 요청/응답 당사자간 정보를 
공유하기 위해서 사용에 합의가 되어있는 custom claims 이다.
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```

### 3. Signature
signature 부분을 생성하기 위해서 encoded header 와 encoded payload, secret, 
header에 명시된 알고리즘이 필요하며 그걸 통해서 sign 한다.
Base64Url 로 encode 될 JWT 의 세번째 파트 이다.
```python
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

### 4. 최종
세개의 Base64Url 로 encode 된 string은 각각 점으로 구분하여 하나의 string으로 합친다.
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
![2](https://raw.githubusercontent.com/sanggi-wjg/my_study/main/JWT/data/2.png)

## JWT 작동 방법
인증 방법으로는 user 가 자신의 credentials 을 이용해 성공적으로 로그인 했다면 Json Web Token 이 return 
될 것이고 이후 Token은 보안적으로 중요하게 취급 되어야 한다.  
(예를 들어 오랜 기간동안 보관하거나 browser stroage에 보관한다는 등)

보호된 route, resource 에 접근시 항상 Authorization 헤더를 통해서 JWT 를 확인 하여야 한다.
```
Authorization: Bearer <token>
```
![3](https://raw.githubusercontent.com/sanggi-wjg/my_study/main/JWT/data/3.png)

## JWT 사용 장/단점

### 장점
JWT 사용시 사용자 인증에 대한 정보는 토큰에 포함하기 때문에 별도 인증 저장소가 필요 없어진다.  
따라서, MSA 환경에서 쉬운 인증 인가 방법을 제공한다.
* URL 파라미터와 헤더로 사용
* 수평 스케일 용이
* 디버깅 및 관리 용이
* 트래픽 부담이 낮음
* REST API 서비스 구현 가능
* 내장된 만료

### 단점
* 토큰은 Client에 저장되어 정보 변경시 정보 변경이 어려움
* 필드를 너무 많이 사용하면 토큰이 너무 커짐
* 거의 모든 요청에 전송되므로 트래픽 크기에 영향을 미침

## 참고
https://jwt.io/