# 라이브러리 읽어 들이기
import urllib.request

# url과 저장 경로 지정하기
url = "https://uta.pw/shodou/img/28/214.png"
save_name = "test.png"

# 다운로드
urllib.request.urlretrieve(url, save_name)
print("저장되었습니다...!")
