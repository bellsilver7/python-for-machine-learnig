# 1장 크롤링과 스크레이핑

### 1-1 데이터 다운로드하기

urllib로 웹 사이트에서 데이터를 읽어 들이고 파일로 저장하는 방법

```python
# download-png2.py
....
with open(save_name, mode='wb') as f:
    ...
```

open() 함수에서 mode는 "wb"를 사용했다.

- "w"는 쓰기 모드
- "b"는 바이너리 모드

<br/>

클라이언트 접속 정보 출력

```shell
# download-ip.py 출력
[ip]
API_URI=http://api.aoikujira.com/ip/get.php
REMOTE_ADDR=xxx.xxx.xxx.xxx
REMOTE_HOST=xxx.xxx.xxx.xxx
REMOTE_PORT=35720
HTTP_HOST=api.aoikujira.com
HTTP_USER_AGENT=Python-urllib/3.9
HTTP_ACCEPT_LANGUAGE=
HTTP_ACCEPT_CHARSET=
SERVER_PORT=80
FORMAT=ini
```

<br/>

매개변수 인코딩

```python
# download-forecast.py
...
values = {
    'stnId': '108'
}
params = urllib.parse.urlencode(values)
...
```

<br/>

별칭

```python
import urllib.request as req
import urllib.parse as parse
```

<br/>

명령줄 매개변수

```python
import sys

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]
```

<br/>

셔뱅(shebang)

```python
#!/usr/bin/env python3
```

download-forecast-argv.py 파일의 첫 번째 줄에 있는 것을 셔뱅이라고 부른다.
Linux/macOS에서는 실행 권한이 있을 때 python 명령어를 따로 지정하지 않아도 프로그램이 실행되게 할 수 있다.