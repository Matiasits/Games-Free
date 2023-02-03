import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from urlEnum import UrlEnum
from headersEnum import HeadersEnum
from httpmetods import HttpMethods



class GamesClient():

	responseTrucha = {
		'freeGames' : {
			'current' : [{'title' : 'cs'}],
			'upcoming' : [{'title' : 'cod'}]
		}
	}

	url = UrlEnum.BASE_URL.value


	headers = {
		HeadersEnum.KEY_NAME.value : HeadersEnum.KEY_VALUE.value,
		HeadersEnum.HOST_NAME.value : HeadersEnum.HOST_VALUE.value
	}

#	response = requests.request(HttpMethods.GET.value, url, headers=headers)

	def get_freegames_response(self):
		#response = requests.request(HttpMethods.GET.value, self.url, headers=self.headers)
		#json = response.json()
		return self.responseTrucha['freeGames']
