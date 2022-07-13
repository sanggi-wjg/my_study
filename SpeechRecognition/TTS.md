# Python TTS 방법

TTS(Text to Speech) 기술은 유튜브, 트위치 등 인터넷 방송 뿐만 아니라
네이버, 구글 번역 사이트 등 발음 기능 등으로 웹 서비스로도 많이 사용 되는데
TTS는 어떻게 작동 되는지 한번 알아보자.


## 1. TTS 개요
TTS는 머신 러닝 등을 이용하여 텍스트에서 인간의 발언으로 구현해주는 것이다.
TTS를 이용하여 메뉴얼 녹음이라든지 회사 비지니스 관점에서 시간이나 돈 등을 절약할 수 있는데

https://github.com/pndurette/gTTS


### TTS 구현 방법
#### 연결 (Concatenative) 방식
녹음된 오디오의 조각을 이어 붙이는 방식으로 
매우 고품질을 제공하지만 머신 러닝을 위해서 많은 데이터가 필요하다.

#### 매개변수 (Parametric) 방식
주어진 텍스트에 대한 Digital Signal을 확률 모델을 구성하는 방식으로
실제 사람과 비슷한 품질을 제공한다. 

#### 1. 문자을 단어로 변환  
머신 러닝 알고리즘을 위해서 텍스트를 읽기 가능한 포맷으로 변경 해야하는데
단어 뿐만 아니라 숫자, 약어, 등에서 도전이 생긴다.

위에 도전들은 반드시 변환이 되어야 하고 알고리즘을 통해 별개의 문구로 
머신 러닝이 읽기 가능하도록 적절하게 변환한다. 

#### 2. 완벽한 발음 표기
각 문장은 감정이나 의미등에 따라서 다르게 발음이 될수 있다.
정확한 발음을 위해서 적절한 사전을 사용해야 한다.

만약 없는 단어라면 알고리즘은 일반적인 룰을 따르거나
알고리즘은 녹음된 것을 체크해야한다.

그 후 컴파일된 25 milli second 조각들의 개수를 계산(음소 처리) 한 후
각 조각들에 대해서 구문과 문장의 적절한 억양을 재현한다.

#### 3. 표기를 발언으로 변환
처리된 텍스트를 읽기 위해 모델을 사용하고 
적절한 억양과 소리, 음소 사이에 머신 러닝을 사용하여 연결을 한 후
Sound wave Generator로 vocal sound를 생성한다.



## 2. Python에서 사용 가능한 TTS 패키지
```shell
TTS
gTTS
```
이후 데모 구현으로는 `gTTS` 선택  
https://github.com/pndurette/gTTS



## 3. gTTS 설치
```shell
pip install gTTS
```

```shell
from gtts import gTTS

def gtts_test(text: str) -> None:
    tts = gTTS(text)
    tts.save(f"{text}.mp3")


test_text = "안녕하세요"
gtts_test(test_text)
```

file byte 형태로도 사용할 수 있다.
```shell
from io import BytesIO
from gtts import gTTS

def gtts_to_fp(text: str) -> None:
    fp = BytesIO()
    try:
        gTTS(text).write_to_fp(fp)
    finally:
        fp.close()


test_text = "안녕하세요"
gtts_to_fp(test_text)
```