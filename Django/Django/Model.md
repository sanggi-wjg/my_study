## Django Model

### on_delete 옵션
* CASCADE : `ForeignKeyField`를 포함하는 모델 **인스턴스(row)도 같이 삭제**한다.
* PROTECT : 해당 요소가 **같이 삭제되지 않도록** `ProtectedError`를 발생시킨다.
* SET_NULL : `ForeignKeyField` 값을 `NULL`로 바꾼다. `null=True`일 때만 사용할 수 있다.
* SET_DEFAULT : `ForeignKeyField` 값을 `default` 값으로 변경한다. `default` **값이 있을 때만 사용할 수 있다.**
* 