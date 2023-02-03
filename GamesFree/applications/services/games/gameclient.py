import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from urlEnum import UrlEnum
from headersEnum import HeadersEnum
from httpmetods import HttpMethods

url = UrlEnum.BASE_URL.value


headers = {
	HeadersEnum.KEY_NAME.value : HeadersEnum.KEY_VALUE.value,
	HeadersEnum.HOST_NAME.value : HeadersEnum.HOST_VALUE.value
}

response = requests.request(HttpMethods.GET.value, url, headers=headers)

print(response.text)