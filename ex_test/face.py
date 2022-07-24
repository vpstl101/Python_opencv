import requests
from io import BytesIO
from PIL import Image
import time

# 다운받을 이미지 url
url = "url=https://ibb.co/Hhj5yk4"

# time check
start = time.time()

# request.get 요청
res = requests.get(url)

# 이미지 다운로드 시간 체크
print(time.time() - start)

#Img open
request_get_img = Image.open(BytesIO(res.content))