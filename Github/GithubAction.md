# Github Action

## Github Action 개요
Github action 은 github에서 공식적으로 제공하는 `work flow 자동화 툴`.  
github repo 안에서 `.github/workflows` 경로에 yml 파일 작성으로 생성.

## Github Action 구성
다음 6가지의 개념으로 구성 되어 있음
* Workflows
* Events
* Runners
* Jobs
* Steps
* Actions

### 워크 플로우(workflows)
자동화된 프로세스 단위.  
하나 이상의 `job`으로 이루어져 있으며 설정한 이벤트에 의해 실행된다.

### 이벤트(Events)
워크 플로우를 실행하는 특정 활동이나 규칙이다.   
커밋의 push, pull request가 생성 되었을 때뿐만 아니라 
Github 외부에서 발생하는 활동으로도 이벤트를 발생시킬 수도 있다.
```yaml
on:
  push:
    branches: [ master ]
  pull_request:
      branches: [ master ]
```

```yaml
on:
   schedule:
     - cron: '00 15 * * *' # default UST 
```

### 러너(runners)
Github에서 호스팅 하는 러너는 Ubuntu Linux, Windows, macOS 환경을 기반,  
워크 플로우의 각 작업은 새로운 가상 환경에서 실행된다. 
호스팅 하는 러너를 사용할 수도 있고 직접 호스팅 할 수도 있다
```yaml
runs-on: ubuntu-20.04
```

### 작업(jobs)
워크 플로우의 기본 단위.  
기본적으로 워크 플로우는 여러 작업을 병렬적으로 실행하며 순차적으로 실행하도록 설정할 수도 있다. 
예를 들어 빌드와 테스트 코드의 수행인 두 작업을 순차적으로 실행할 수도 있으며 
이 경우에는 빌드 작업이 실패하면 테스트 작업은 실행되지 않는다.
```yaml
jobs:
  build:
    runs-on: ubuntu-20.04
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
  ...
```

### 스텝(steps)
작업에서 커맨드를 실행하는 독립적인 단위.   
한 작업(job)의 각 스텝들은 동일한 러너에서 실행되므로 해당 작업의 액션들은 서로 데이터를 공유한다.
```yaml
steps:
  - uses: actions/checkout@v2
  - name: Set up Python 3.8
```

### 액션(actions)
워크 플로우의 가장 작은 요소로 직접 만들어 사용할 수도 있고 이미 만들어진 것을 가져와 사용할 수도 있다.
```yaml
uses: actions/checkout@v2
```

### 사용 용도
#### CI/CD
예를 들어서   
CI는   
파이썬 경우 flake Python lint 검사 하거나 pytest 나  
자바나 코틀린 경우 compile test, gradle(or maven) build test 나
Docker image build 테스트 나  
등등등

CD는 원격 서버 배포 
등등등

#### 기타 자동화
그냥 말그대로 기타 용도, 어떻게 쓰냐에 따라 많음  
어떤 자료 취합해서 이메일 보내거나  
예시처럼 스크랩 해서 웹 훅 보내거나 등등등

<hr>

## 방법

### 1. Github private repository 생성

### 2. Action 탭에서 action.yml 생성

![](data/1.png)

### 3. action.yml 작성 
```yaml
name: Send WTI Stock 

on:
   schedule:
     - cron: '00 15 * * *' # default UST 

jobs:
  build:
    runs-on: ubuntu-20.04
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: "3.8"
    - name: Install python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install selenium==4.1.0 requests pillow
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Install ubuntu package
      run: |
        wget https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip
        unzip ./chromedriver_linux64.zip  
    - name: Execute code
      run: |
        python3 ./send_wti_stock.py
```

### 4. 실행할 send_wti_stock.py Python file commit
```python
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def send_to_discord(filename):
    discord_webhook_url = "https://discord.com/api/webhooks/936272198639964180/IoA6kaWSxhcbDpSIV-xBZnNHTeZVx1hdTap8q1pGHPP8KHwbAINmXsMunFv5v43D80Zg"
    response = requests.post(
        url = discord_webhook_url,
        headers = { "Content-Disposition": "form-data" },
        files = { 'file': (filename, open(filename, 'rb')) }
    )
    # print(response.status_code)
    # print(response.text)


save_filename = "screenshot.png"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('./chromedriver', options = options)

try:
    driver.implicitly_wait(3)

    driver.get('https://www.google.com/search?q=wti+oil+stock')
    find = driver.find_element(by = By.CLASS_NAME, value = "webanswers-webanswers_table__webanswers-table")
    table = find.find_element(by = By.TAG_NAME, value = "table")

    file = table.screenshot(save_filename)
    send_to_discord(save_filename)

finally:
    driver.quit()

```

<hr>

## 장단점
### 장점
* Github 오픈 소스 만들때 다른 CI/CD 구축한 서버 없이도 CI/CD 로 충분히 활용 가능  
* CI/CD 외에 목적으로도 활용 가능 함.

### 단점
* 테스트 중에 예약 시간에 workflow가 작동을 안해서 구글에서 찾아보았는데 실행 시간이 불규칙 하다고 함.
> The schedule event can be delayed during periods of high loads of GitHub Actions workflow runs. 
> High load times include the start of every hour. To decrease the chance of delay, 
> schedule your workflow to run at a different time of the hour.
* 즉시 실행이 없음
* 다른 CI/CD 오픈 소스에 마켓 쉐어 밀려서 신경 덜 쓰는 느낌? 

#### 참고
https://zzsza.github.io/development/2020/06/06/github-action/