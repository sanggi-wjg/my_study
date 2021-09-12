# 시스템

## Concern (관심사)
시작 단계는 모든 앱이 풀어야하는 관심사(Concern) 이다.
관심사 분리는 오래된 가장 중요한 기법이다.

대다수의 앱은 시작 단계라는 관심사를 분리 하지 않고 준비 과정 코드를 주먹구구로 구현하고 심지어 런타임 로직하고도 섞인다.

다음은 대표적인 예다.
```python
class SomethingMain(object):
    ...
    
    def get_service() -> Service:
        if not self._service:
            self._service =  MyService()
        return self._service
    
    def main():
        ...
        service = self.get_service()
        ...

    ...
```
위는 초기화 지연 (Lazy Initialization) 혹은 계산 지연 (Laze Evalutation) 이라는 기법이다.

장점은 우선, 실제로 필요할 때까지 객체를 생성하지 않아 자원을 적게하며 앱의 실행 시간이 그만큼 빨라진다. 그리고 절대 Null을 Retrun 하지 않는다.

단점은 get_service 가 MyService 에 의존하고 있다는 것이며 컴파일 언어에 경우 MyService 가 선언되어 있지 않다면 컴파일조차 안 될 것이다.

또한, 테스트도 문제이다. MyService 가 무거운 객체라면 단위 테스트에서는 가벼운 테스트 전용 객체를 service 에 할당 해야 한다.
게다가 If문으로 두가지의 책임을 가지므로 단일 책임 원칙에도 위반한다.


해결 방법은 몇가지가 있다.  
main 함수에서 시스템에 필요한 객체를 생성하고 앱에 넘긴다.
```
main   →   애플리케이션
↓               ↓
구축자  →    설정 객체
```
앱은 main이나 생성과정 등에 대해 몰라도 된다는 뜻이다.

이런건가?
```
Web Framework 에서 구동하는 main 하고 service 를 별도로 처리하라는 뜻이다.
Java swing 이나 Python GUI 개발한다고 하면 app main에서 위처럼 소스코드를 작성하지 말라는 뜻

Java swing 으로 똥피하기 같은 게임을 만든다고 하면 앱 구동과 함께 객체 쓰레드를 생성할 필요는 없다는 것이겠지.
```

팩토리 패턴도 피할수 있도록 도와준다.
팩토리 패턴은 쉬우니까 패스.