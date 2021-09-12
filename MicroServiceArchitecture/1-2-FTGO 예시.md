# FTGO 예시

## 모놀리식 구조
전형적인 자바 애플리케이션인 FTGO 의 전체 구조는 코어가 비지니스 로직으로 구성된 융각형 아키텍쳐이며 UI, 외부 시스템 통합을 위해 어댑터가 비지니스 로직을 감싼 모양새이다.  
![2-1](https://raw.githubusercontent.com/sanggi-wjg/my_study/main/MicroServicePattern/data/2-1.png)

#
## 마이크로 서비스 구조
FTGO 애플리케이션은 각 요청에 대해 서비스로 보내고 각자의 API 를 통해 서로 협동한다.
![2-2](https://raw.githubusercontent.com/sanggi-wjg/my_study/main/MicroServicePattern/data/2-2.png)

![2-3](https://raw.githubusercontent.com/sanggi-wjg/my_study/main/MicroServicePattern/data/2-3.PNG)

#
## 마이크로 서비스로 변경을 통해
### 장점
* 크고 복잡한 애플리케이션을 지속적인 전달/배포 
* 서비스 규모가 작아 관리 용이
* 서비스를 독립적으로 배포/확장 가능
* 서비스 팀별로 자율적인 업무 수행 가능
* 결함 격리가 쉬움
* 새로운 기술에 대해 도입 용이

### 단점
* 서비스를 찾기가 어려움
```
마이크로 서비스는 따로 정해진 규약이 없어 서비스 모듈을 잘 못 분해할 경우 분산 모놀리식이 구성 될 수도 있다.
```
* 분산 시스템이 복잡해 개발, 테스트, 배포가 어려움
```
서비스 통신간 에러, 지연시간 등에 대해서 처리하도록 설계가 필요 
DB가 서비스 별로 구성되어 트랜잭션 구현이 어렵다. 따라서 마이크로 서비스 도입시에는 SAGA 라는 기술로 데이터 일관성을 유지한다.

여러 서비스를 사용 해야 할 경우 테스트도 쉽지 않은 일이며 이런 경우 우수한 개발자가 필요하다. 

또한, 운영 복잡도도 증가한다. 배포 자동화 작업시에 아래 기술을 사용 해서 자동화를 고도화 한다.
(넷플릭스 Spinnaker, 파보탈 Cloud Foundry, 레드햇 PaaS, Docker Swarm, Kubernates)
```
* 여러 서비스에 걸친 기능은 배포 시기를 잘 조정 해야 함
* 도입 시점을 언제 해야 하는지 결정이 어려움
