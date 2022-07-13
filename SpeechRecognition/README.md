# Python Speech Recognition 방법
파이썬에서 음성 인식 하는 방법.

음성 인식을 기술을 활용하여 이미 아마존 알렉사, 카카오 미니 등 다양한 제품들이 현재 집에서 서비스를 하고 있다.
그럼 음성인식이란 어떤것이고 어떻게 작동을하고 간단한 개요를 확인하고 파이썬에서 음성인식과 TTS를 활용하여 간단한 데모를 구현 해보자


## 1. 음성인식 개요
음성인식은 1950년대 Bell Labs에서 연구의 기초를 둔다.
처음에는 한명의 말과 수십개 정도의 단어 정도에서 였지만 
현재는 수많은 사람의 말과 수많은 언어의 단어를 인식 한다.

### 작동 방법
→ Physical Sound with Microphone  
→ Electrical Signal  
→ Digital Data with Analog-to-Digital Converter  
→ Digitized Data는 몇가지 모델을 이용하여 Text로 변환된다.

현대의 많이 사용되는 음성인식 모델은 HMM(Hidden Markov Model)로
milli second 단위로 기반해 Speech Signal을 가정해낸다.  
→ Speech Signal을 10 milli second 조각으로 분할  
→ 각 조각의 스펙트럼을(frequency 등) 중심계수(Ceptral Coefficient)로 알려진 실수 벡터로 매핑  
(벡터의 Dimension은 보통 작게 나오는데 32 이상이여 정확하다고 한다.)  
(https://en.wikipedia.org/wiki/Cepstrum)  
→ 벡터 그룹을 output으로   
→ 텍스트로 디코드 하기위해 벡터 그룹을 하나 이상의 음소(Phonemes)와 매칭  
 (https://en.wikipedia.org/wiki/Phoneme)  
→ 음소는 사람마다 다양하기 때문에 훈련이 필요  
→ 알고리즘을 통해 가장 비슷한 음소를 결정하여 음소의 순열을 생성



## 2. Python에서 사용 가능한 음성인식 패키지
```shell
apiai
assemblyai
google-cloud-speech
pocketsphinx
SpeechRecognition
watson-developer-cloud
wit
```
이후 데모 구현으로는 `SpeechRecognition` 선택  
https://github.com/Uberi/speech_recognition

## 3. SpeechRecognition 설치
```shell
pip install SpeechRecognition

[Python 3.6 이하]
pip install pyaudio

[Python 3.7 이상]
pip install pipwin
pipwin install pyaudio

(혹시 pyaudio 에러가 난다면 아래 링크 참조)
https://stackoverflow.com/questions/61348555/error-pyaudio-0-2-11-cp38-cp38-win-amd64-whl-is-not-a-supported-wheel-on-this-p
```


```python
import speech_recognition as sr

print(sr.__version__)
# output
# 3.8.1
```


```python
recognizer = sr.Recognizer()
```
`Recognizer`는 다양한 API를 제공하며, `sphinx` 는 Offline에서 사용 가능하며 이외는 Online에서만 가능하다.
(소스를 따라가 보면 API를 사용하기 위해 HTTP Request를 사용한다.)  
* recognize_bing(): Microsoft Bing Speech
* recognize_google(): Google Web Speech API
* recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
* recognize_houndify(): Houndify by SoundHound
* recognize_ibm(): IBM Speech to Text
* recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
* recognize_wit(): Wit.ai

## 4. Audio file을 통한 데모 구현
* audio 파일 샘플  
* https://cpham.perso.univ-pau.fr/SmartSantanderSample/Audio_sample.html
* http://www.voiptroubleshooter.com/open_speech/index.html

```python
import speech_recognition as sr

r = sr.Recognizer()

file = sr.AudioFile('OSR_us_000_0010_8k.wav')
with file as source:
    audio = r.record(source)

result = r.recognize_google(audio)
print(result)

# output
# Birch canoe slid on the smooth plank glue the sea to a dark blue background it is easy to tell the depth of the well these days a chicken leg of a variegated price is often served in Randall's the juice of lemons makes find the boxes on the side the pump truck the ha grimstead top corn and garbage for hours of City Works in a large size and stockings and hard to sell
```

## 5. Microphone을 통한 데모 구현
```python
import speech_recognition as sr

names = sr.Microphone.list_microphone_names()
print(names)

# output
# ['Microsoft Sound Mapper - Input', '마이크(USB Audio Device)', ...]
```
시스템이 라즈베리 파이가 아닌 이상 default microphone 설정이 안되어 있다고 한다.
`sr.Microphone.list_microphone_names()`를 통해서 사용 가능한 Microphone의 Index를 확인

```python
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone(device_index = 1)
with mic as source:
    audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

result = r.recognize_google(audio, language = "ko-KR")
print(result)

# output
# 안녕하세요
```
`listen()`의 argument로 timeout과 phrase_time_limit과
`recognize_google()` argument로 language를 설정해준다.

주변 소음을 제어하기 위해서 `adjust_for_ambient_noise()`를 제공해주고 있다.  
```python
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout = 5, phrase_time_limit = 5)
```

어떤 소리는 음성인식 API를 통해 나타내는 것이 굉장히 어려울 수 있음을 감안하여
try-except 처리를 해준다.
```python
import speech_recognition
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone(device_index = 1)
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

try:
    result = r.recognize_google(audio, language = "ko-KR")
    print(result)
except speech_recognition.UnknownValueError:
    print("음성 인식 실패")
except speech_recognition.RequestError:
    print("HTTP Request Error 발생")
except speech_recognition.WaitTimeoutError:
    print("WaitTimeout Error 발생 ㅠㅠ")
```