# Python venv 설치

https://github.com/pyenv

## pyenv 패키지 설치
```shell
curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile

exec "$SHELL"
```

## 설치
```shell
# 설치 가능 버전 상위 리스트
pyenv install --list | grep -v - |tail

# 3.10.4 버전 설치
pyenv install 3.10.4

# 설치 확인
pyenv versions
```

## 사용
```shell
# 전역 사용
pyenv global 3.10.4

# 디렉토리에서만 사용
pyenv local 3.10.4
```

## virtualenv
```shell
pip install virtualenv
```