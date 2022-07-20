## DRF Validators



### 
`Model`에 `unique=True` 추가 시에 `Serializer`에서 `validators`를 생성한다.
```python
class Board(models.Model):
    board_name = models.CharField(max_length=100, unique=True)
```
```python
>>> from boards.serializers import *
>>> s = BoardSerializer()
>>> print(repr(s))
BoardSerializer():
    id = IntegerField(label='ID', read_only=True)
    board_name = CharField(max_length=100, validators=[<UniqueValidator(queryset=Board.objects.all())>])
```