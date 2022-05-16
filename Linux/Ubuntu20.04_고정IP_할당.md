# Ubuntu 20.04 고정 IP 할당 방법

## 개요 
* DHCP 로 설치 했을 경우
* 네트워크 설정 yaml 파일 : /etc/netplan/xx.yaml 경로
  (이름은 상이할 수 있음)

### 변경 전
```yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens160:
      dhcp4: true
  version: 2
```

### 변경 후
* **이더넷 인터페이스 이름은 꼭 확인 필요**  
  (인터페이스 이름은 ifconfig 명령어로 확인 가능)
```yaml
network:
  ethernets:
    ens160: # 이더넷 인터페이스 이름 (확인 필요!)
      dhcp4: no
      dhcp6: no
      addresses: [192.168.10.86/24] # 원하는 IP 주소
      gateway4: 192.168.10.254      # 게이트 웨이
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4] # DNS 네임 서버
  version: 2
```
### 적용
```shell
$ netplan apply
```

### 확인
```shell
$ ifconfig
```