# 라이브러리 읽어 들이기
import urllib.request

# url과 저장 경로 지정하기
url = "https://uta.pw/shodou/img/28/214.png"
save_name = "test.png"

# 메모리에 담기
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기
with open(save_name, mode='wb') as f:
    f.write(mem)
    print("저장되었습니다...!")
