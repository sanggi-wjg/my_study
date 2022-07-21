# Git Commit Convention and Useful Commit Message


## 1. Commit Message Convention의 필요
* 협업에 용이
* 기록 확인 용이
* 과거 이슈 추적이나 이슈 진행사항 확인  


## 2. Commit Message 작성 방법
```
Type : Subject

Body

Footer
```

### 2.1 Type
* Feat : 기능 추가
* HotFix : 긴급 버그 수정
* Fix : 버그 수정
* Build : CI/CD 관련 수정
* Docs : 문서 추가, 수정, 삭제
* Refactor : 리팩토링
* Test : 테스트 코드 추가, 수정, 삭제
* ETC : 기타 사항

### 2.2 Subject
* 제목의 길이는 최소화하고 마침표 없이 끝냄
* 명령문으로 작성
* 제목과 본문은 한 줄 띄워서 작성

#### Type : Subject 작성 예시
```
Feat : EMS 송장 발급 API 연동
Build : CD shell_script 변경
```



### 2.3 Body
* 모든 Commit에 작성할 필요는 없음
  (가령 HotFix 같은 경우?, 간단한 경우?)
* 어떻게(How) 보다는 개발을 한 무엇을, 왜(What, Why)에 집중하여 작성

#### Body 작성 예시
```
Feat : EMS 송장 발급 API 연동

- 신규 운송업체 계약, 사업부 요청사항으로 송장 발급 API 연동 개발
- API 자동화 연동을 위해 예약 비지니스 로직 개발 
```


### 2.4 Footer
* Git Issue Handle을 위해서 사용

#### Git issue keyword
```
close #issueID
```
* close
* closes
* closed
* fix
* fixes
* fixed
* resolve
* resolves
* resolved

#### Git Commit 예시
```
Feat : EMS 송장 발급 API 연동

- 신규 운송업체 계약, 사업부 요청사항으로 송장 발급 API 연동 개발
- API 자동화 연동을 위해 예약 비지니스 로직 개발

close #11 
close #12
fixes #13
```
적용 시점은 feat - dev - master branch를 사용한다고 가정,  
feat branch에 올린 commit이 master branch에 merge 하는 시점에 종료



## Ref
* https://junhyunny.github.io/information/github/git-commit-message-rule/
* https://medium.com/innovation-incubator/how-to-write-a-useful-commit-message-a-git-guide-2c10570dc65f