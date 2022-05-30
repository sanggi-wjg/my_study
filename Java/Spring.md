# Spring


## IoC 컨테이너와 Bean
### 스프링 IoC 컨테이너
Inversion of Control : 의존 관계 주입(Dependency Injection) 이라고도 하며,
어떤 객체가 사용하는 `의존객체를 직접만들어 사용하는게 아니라, 주입 받아서 사용하는 방법`을 말 함
* BeanFactory
* Application Component의 중앙 저장소
* Bean 설정 소스로부터 Bean 정의를 읽고, Bean을 구성하고 제공한다.

### Bean
* Spring IoC 컨테이너가 관리하는 객체
* 장점
  * 의존성 관리
  * 스코프
    * 싱글톤
    * 프로토 타입
  * 라이프 사이클 인터페이스

## Annotation

### Event 사용
* @EventListener 사용 예시
  * https://velog.io/@ljinsk3/Spring-Events

### @Component 와 @Bean 사용
#### @Component
* 개발자가 작성한 Class를 Bean으로 만드는 것
* Singletone을 생성
* 패키지 스캔 안에 "이 Class를 정의 했으니 Bean으로 등록하라" 는 뜻  
  (ComponentScan : @Component이 붙은 Class들을 검색)

#### @Bean
* 개발자가 작성한 Method를 Bean으로 만드는 것
* 주로 `@Configuration` 이 들어간 Spring 설정 Class 내에 Method에서 사용