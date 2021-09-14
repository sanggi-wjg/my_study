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
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/factory.py) |
 
### Abstract Factory Pattern
Client 코드에서 특정 클래스 선언 없이도 연계된 객체들을 생성할 수 있음.
|구분|내용|
|----|:----|
|목적|클래스(명사)를 묶어서 메소드(동사) 들을 수행할 때 사용|
|예시|딱히 안써봄 |
|장점|클라이언트 서비스 코드에서 호출을 할 때 응집도, 종속도를 낮춰주며 추상화를 통해서 확장을 쉽게 해 줌 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/abstract_factory.py) |
 
### Builder Pattern
복잡한 객체들을 단계별로 구성할 수 있고 패턴을 사용해서 다양한 기능을 구현 할 수 있다. 
|구분|내용|
|----|:----|
|목적|객체들을 조합하기 위해서 사용함. 추상 팩토리와 비슷함|
|예시|HTTP API 부분 사용함 |
|장점|캡슐화, 클라이언트로 부터 객체 분리 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/builder.py) / [Example Code 2](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/builder_2.py)|

### Prototype Pattern
기존 개체 복사
|구분|내용|
|----|:----|
|목적|서비스 코드에서 계산된 값을 가진 객체를 여러번 생성 하면 비효율적임. 따라서 복사를 해야 함|
|예시|대용량 데이터 처리하는 정산 같은 곳에서 되있긴 한데... 딱히 안써 봄... ORM 들이 이런식으로 하긴 함... lazy load긴 한데...|
|장점| |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/prototype.py) |

### Singleton Pattern
Special One.
|구분|내용|
|----|:----|
|목적|천상천하! 유아독존! |
|예시|로그 등 단일 객체로 돌아가야 하는 것에서 사용 |
|장점|쉬움 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/singleton.py) |

#
## Structural Patterns
### Adapter Pattern
호환되지 않는 기능에 대해 클래스로 wrapping 으로 공동 모듈을 할 수 있도록 도와 줌
|구분|내용|
|----|:----|
|목적|같은 목적을 가진 다수의 클래스(명사)의 메소드(동사)들이 똑같은 순서와 의미를 가지는데, 사용 중 소수의 클래스의 메소드(동사) 의미가 변경점 생기면 사용 |
|예시|개발에서 출고요청 기능에서 사업부에 대해 wrapping 함 |
|장점| 유지보수시 소스의 흐름(?)에 영향을 미치는 점이 적으며 확장이 쉬움 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/adapter.py) |

### Bridge Pattern
대규모 클래스나 관련된 클래스를 서로 독립적으로 개별 계층으로 분할 할 수 있음
이 패턴은 몰라도 객체지향 언어를 사용한다면 이런식으로 개발한 부분이 있을 것이다.
|구분|내용|
|----|:----|
|목적| 개인적으로 다형성과 추상화의 꽃이라고 생각함|
|예시| 많이 씀 |
|장점| 확장에 좋음 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/bridge.py) | 

### Composite Pattern
트리 구조로 객체안에 어떻게 구현 되어 있는지 상관 없이 공통 메소드로 동일하게 처리할 수 있음 
|구분|내용|
|----|:----|
|목적| |
|예시| 안 써봄 |
|장점|  |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/composite.py) | 

### Decorator Pattern
사용 목적에서 Builder pattern 이랑 비슷함
개인적으로 느끼기에는 별로 안좋다고 느낌  
쓴다고 하면 다른 패턴이나 같이 응용해서 구현하거나 상황에 맞게 변조해서 구현 해야하는 부분이 많다고 느낌
|구분|내용|
|----|:----|
|목적| |
|예시| 안 써봄, 굳이 쓴다면 피킹리스트에서 쓸 수 있을거 같음, 근데 구현 한다면 이걸로 안하고 Builder 로 구현할 듯 |
|장점|  |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/decorator.py) | 

### Facade Pattern
프로젝트에서 나만의 라이브러리(패키지, 등등) 처럼 객체들을 모아모아 구현 하는 것
|구분|내용|
|----|:----|
|목적| |
|예시| 많이 씀, 개발에서 출고에서 씀 |
|장점| 소스 흐름이 간단(?)해지고 객체들로 다양한 구현을 할 수 있음, 확장성도 좋음 |
|단점| 객체 초기화나 의존성을 가지고 있어서 확장은 상관 없지만 변경 등에 어려움 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/facade.py) / [Example Code 2](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/facade_2.py) | 

### Flyweight Pattern
여러 객체들간에 사용할 공통 데이터들에 대해서 공유를 통해서 가용 메모리를 효율적으로 사용할 수 있도록 해줌 
|구분|내용|
|----|:----|
|목적| 생성시에 큰 자원이 들어가고 자주 사용하는 객체들에 대해서 효율적으로 사용하기 위해서 미리 생성을 해놓는다.  |
|예시| 안써봄 |
|장점| 메모리 효율적 사용 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/facade.py) / [Example Code 2](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/flyweight.py) | 

### Proxy Pattern
패턴을 통해 원래 객체 요청에 대해서 액세스 제어 등을 전이나 후에 수행할 수 있다.
|구분|내용|
|----|:----|
|목적|  |
|예시| 프레임워크에 기본적으로 기능이 있음 |
|장점|  |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/facade.py) / [Example Code 2](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/proxy.py) | 

#
## Behavioral Patterns

### Chain of Responsibility Pattern

### Iterator Pattern

### Memento Pattern

### State Pattern

### Template Method Pattern
이 패턴은 몰라도 이런식으로 개발한 부분이 있을 것이다.
|구분|내용|
|----|:----|
|목적| 클래스 메인 로직에 대부분 공통 메소드인데 중간에 몇개가 추가되거나 변경 사항이 생겼을때나 메소드안에 메소드가 추가 되는 같은 상황에서 사용 |
|예시| 진짜 개 많이 씀 |
|장점| 쉬움 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/template_method.py) | 

### Command Pattern
요청에 대한 독립 객체로 만들어 줌. 커맨드 패턴은 요청의 대한 정보를 전달하고, 연기, 취소 등을 구현할 수 있음
|구분|내용|
|----|:----|
|목적|  |
|예시| 개발에서 linux shell cli 관련 모듈에서 씀 |
|장점| 쉬움 |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/command.py) | 

### Mediator Pattern

### Observer Pattern

### Strategy Pattern
 
|구분|내용|
|----|:----|
|목적| |
|예시| 안 써봄 |
|장점|  |
|예제|[Example Code](https://github.com/sanggi-wjg/my_study/blob/main/DesignPattern/code_example/strategy.py) |

### Visitor Pattern
