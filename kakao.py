import requests
import json

"""
인가코드 받기
url = 'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=988d454a59ac0d8161c9864eb3fd6abe&redirect_uri=https://localhost.com'

"""
url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "988d454a59ac0d8161c9864eb3fd6abe",
    "redirect_uri" : "https://localhost.com",
    "code"         : 'GXJLwJ0Jh9jsdPTkLncOsC9l1-rok8aKzHe09sLiYBwUrOWlHxfEATd1sUUH8sXH_HQ6rworDKgAAAF49-wofQ'
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)