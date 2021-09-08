# 디자인 패턴
맨날 뭐였지? 하고 까먹어서 이번 기회에 정리 한다.  
내가 볼거 내가 정리.

#
## Creational Patterns
### Factory Pattern
Client 코드에서 특정 클래스 선없 없이 객체를 생성하기 위한 인터페이스를 제공한다.
(Client 코드에서는 main 로직에서 객체가 무엇을 하는지 몰라야 한다.)
|구분|내용|
|----|:----|
|목적|클래스 메소드 동사 의미는 같지만 동사가 수행할 과정은 다를 때 사용|
|예시|프린트 출력 생성이나 출고 피킹리스트에서 사용 함|
|장점|클라이언트 서비스 코드에서 호출을 할 때 응집도, 종속도를 낮춰주며 추상화를 통해서 확장을 쉽게 해 줌 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/factory.py) |
 
### Abstract Factory Pattern
Client 코드에서 특정 클래스 선언 없이도 연계된 객체들을 생성할 수 있음.
|구분|내용|
|----|:----|
|목적|클래스(명사)를 묶어서 메소드(동사) 들을 수행할 때 사용|
|예시|딱히 안써봄 |
|장점|클라이언트 서비스 코드에서 호출을 할 때 응집도, 종속도를 낮춰주며 추상화를 통해서 확장을 쉽게 해 줌 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/abstract_factory.py) |
 
### Builder Pattern
복잡한 객체들을 단계별로 구성할 수 있고 패턴을 사용해서 다양한 기능을 구현 할 수 있다. 
|구분|내용|
|----|:----|
|목적|객체들을 조합하기 위해서 사용함. 추상 팩토리와 비슷함|
|예시|HTTP API 부분 사용함 |
|장점|캡슐화, 클라이언트로 부터 객체 분리 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/builder.py) / [Example Code 2](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/builder_2.py)|

### Prototype Pattern
기존 개체 복사
|구분|내용|
|----|:----|
|목적|서비스 코드에서 계산된 값을 가진 객체를 여러번 생성 하면 비효율적임. 따라서 복사를 해야 함|
|예시|대용량 데이터 처리하는 정산 같은 곳에서 되있긴 한데... 딱히 안써 봄... ORM 들이 이런식으로 하긴 함... lazy load긴 한데...|
|장점| |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/prototype.py) |

### Singleton Pattern
Special One.
|구분|내용|
|----|:----|
|목적|천상천하! 유아독존! |
|예시|로그 등 단일 객체로 돌아가야 하는 것에서 사용 |
|장점|쉬움 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/singleton.py) |

#
## Structural Patterns
### Adapter Pattern
호환되지 않는 기능에 대해 클래스로 wrapping 으로 공동 모듈을 할 수 있도록 도와 줌
|구분|내용|
|----|:----|
|목적|같은 목적을 가진 다수의 클래스(명사)의 메소드(동사)들이 똑같은 순서와 의미를 가지는데, 사용 중 소수의 클래스의 메소드(동사) 의미가 변경점 생기면 사용 |
|예시|개발에서 출고요청 기능에서 사업부에 대해 wrapping 함 |
|장점| 유지보수시 소스의 흐름(?)에 영향을 미치는 점이 적으며 확장이 쉬움 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/adapter.py) |

### Bridge Pattern
대규모 클래스나 관련된 클래스를 서로 독립적으로 개별 계층으로 분할 할 수 있음
이 패턴은 몰라도 객체지향 언어를 사용한다면 이런식으로 개발한 부분이 있을 것이다.
|구분|내용|
|----|:----|
|목적| 개인적으로 다형성과 추상화의 꽃이라고 생각함|
|예시| 많이 씀 |
|장점| 확장에 좋음 |
|예제|[Example Code](https://github.com/sanggi-wjg/clean_code_study/blob/main/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4/code_example/bridge.py) | 

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
