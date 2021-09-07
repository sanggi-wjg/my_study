# 디자인 패턴
맨날 뭐였지? 하고 까먹어서 이번 기회에 정리 한다.  
내가 볼거 내가 정리.

#
## Creational Patterns
### Factory Pattern
|구분|내용|
|----|:----|
|목적|클래스 메소드 동사 의미는 같지만 동사가 수행할 과정은 다를 때 사용|
|예시|WMS 개발에서 프린트 출력 생성이나 피킹리스트에서 사용 함|
|장점|클라이언트 서비스 코드에서 호출을 할 때 응집도, 종속도를 낮춰주며 추상화를 통해서 확장을 쉽게 해 줌 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/factory.py) |
 
### Abstract Factory Pattern
|구분|내용|
|----|:----|
|목적|클래스(명사)를 묶어서 메소드(동사) 들을 수행할 때 사용|
|예시| |
|장점|클라이언트 서비스 코드에서 호출을 할 때 응집도, 종속도를 낮춰주며 추상화를 통해서 확장을 쉽게 해 줌 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/abstract_factory.py) |
 
### Builder Pattern
|구분|내용|
|----|:----|
|목적|객체들을 조합하기 위해서 사용함. 추상 팩토리와 비슷함|
|예시| |
|장점|캡슐화, 클라이언트로 부터 객체 분리 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8%20%ED%8C%A8%ED%84%B4/code_example/builder.py) / [Example Code 2](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8%20%ED%8C%A8%ED%84%B4/code_example/builder_2.py)|

### Prototype Pattern
### Singleton Pattern

#
## Structural Patterns
### Adapter Pattern
### Bridge Pattern
### Composite Pattern
### Decorator Pattern
### Facade Pattern
### Flyweight Pattern
### Proxy Pattern

#
## Behavioral Patterns
### Chain of Responsibility Pattern
### Iterator Pattern
### Memento Pattern
### State Pattern
### Template Method Pattern
### Command Pattern
### Mediator Pattern
### Observer Pattern
### Strategy Pattern
### Visitor Pattern