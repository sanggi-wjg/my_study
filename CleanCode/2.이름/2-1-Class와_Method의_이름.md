## Class 이름
### Class와 Object의 이름은 **명사**가 적합하다.  
[Good] Customer, WikiPage, Account, AddressParser  
[Bad] Manager, Processor, Data, Info 

## Method 이름
### Method와 Function의 이름은 **동사**가 적합하다.  
[Good] postPayment, deletePage, save

javabean 표준에 따라서
Accessor(접근자), Mutator(변경자), Predictate(조건자)는 앞에
get, set, is 를 붙인다.
  
# 
## 이름을 혼용하지마라
여러 Class에 add() 함수의 역할과 Paramerter와 Return 이 동일하다면 계속 사용해도 되지만 기존과 다른 성격을 지닌다면 insert() 나 append()등의 이름을 사용해라.

#
## 의미있는 맥락을 추가해라
name, street, houseNumber, city, state 보다는  
addr 이라는 접두사를 사용해서   
addrName, addrStreet, addrHouseNumber, addrCity, addrState 변경해서 사용하면 의미가 명확해진다.

#
## 이름의 길이는 상관없다
한 가지의 역할만 하는 함수가 작고 짧은 좋은 이름을 가진 다면 좋겠지만,  
이름이 길어져도 상관없다. 짧고 무슨 역할을 하는지 모르겠을 이름보다 길고 무슨 역할인지 명확한 이름이 더 좋다.  
