# Go

## 개요
2007년 구글에서 개발을 시작하여 2012년 GO 버젼 1.0을 완성. (현재 1.17 까지 realase)  

디자인은 로버트 그리즈머, 롭 파이크, 케네스 톰슨 (대학교 책에 나오는 사람, C언어 만든 사람) 이 진행

### 특징
* 컴파일, 정적 타이핑 언어
* 일차적 개발 목적은 시스템 프로그래밍

### 개발적 관점에서 특징
* Go 는 문법이 매우 간단  
  - 문법은 C++, Java, Python 장단점 모두 모아 놓은 느낌
* 동시성 기능 구현 쉬움 
* 다른 컴파일 언어에 비해 빠른 컴파일
* 다양한 라이브러리
  - Go 로 신규 개발하거나 이전한 천조국 회사님들의 오픈 소스 기여로   
  large scale 에 적합한 오픈 소스가 많음        
  - 개인적으로는 똑같은 목적에 오픈 소스여도 다른 언어에 비해 기능이 적은 경우도 겪었고  
  인구 Pool 자체가 적어 오픈 소스에 관한 내용이 인터넷 자체에 적고 책이나 강의 자체도 별로 없는게 힘듬


### Using at
![](data/1.png)

### Use cases
https://go.dev/solutions/#case-studies


## 코드
Go 언어가 다른 최신 언어들과 차별 되는 점  
4가지만 알면 다 아는 것 

### Public? Private?
첫 글자가  
대문자는 Public  
소문자는 Private
```go
var db *database
var DB *database

func somethingMethod()
func SomethingMethod()

type Something struct{}
type something struct{}

func (s *Something) SomethingMethod()
func (s *Something) somethingMethod()
```


### Go Error
Go 는 try-catch 가 없다 대신에 error 를 return 하여 체크
```go
func somethingMethod(mustTrue bool) (string, error) {
	if mustTrue {
		return "yes! It's true", nil
	}
	return "", errors.New("error : It's not true")
}

func showResult(res string, err error) {
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(res)
	}
}

func main() {
	res, err := somethingMethod(true)
	showResult(res, err)

	res, err = somethingMethod(false)
	showResult(res, err)
}

## output ##
yes! It's true
error : It's not true
```


### Go Routine (일명 Coroutine)
Go 에서는 Goroutine(고루틴)이라는 Async 기법 제공을 하는데   
병렬화된 고루틴의 동기화 문제는 프로그래머가 다뤄야 하며  
동기화를 무시할 경우 프로그램이 비정상 종료 되는데 해결하기 매우 쉬움

멀티스레드 메커니즘이지만 자체적인 스케줄러에 의해 관리되는 경량 스레드이며 
OS에서 관리하는 경량 스레드보다 더 경량

```go
func show(i int, c chan bool) {
	fmt.Println(i)
	c <- true
}

func main() {
	var result []bool
	channel := make(chan bool)

	for i := 0; i <= 10; i++ {
		go show(i, channel)
	}
	for i := 0; i <= 10; i++ {
		result = append(result, <-channel)
	}
	fmt.Println(result)
}

# output
1
10
2
6
7
8
9
3
5
0
4
[true true true true true true true true true true true]
```

### 구조체 struct
```go
type mySample struct {
	name string
	data map[int]string
}

func newMySample(name string) *mySample {
	m := mySample{name: name}
	m.data = map[int]string{}
	return &m
}

func (m *mySample) setData(data map[int]string) {
	m.data = data
}

func (m *mySample) getData() map[int]string {
	return m.data
}

func main() {
	sample := newMySample("SampleOne")
	d := map[int]string{0: "DataOne", 1: "DataTwo"}
	sample.setData(d)

	fmt.Println(sample.name)
	fmt.Println(sample.getData())
}

# output
SampleOne
map[0:DataOne 1:DataTwo]
```