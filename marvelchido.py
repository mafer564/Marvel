#virtualenv - p python3 carpeta
#producthunt
import requests
import hashlib
class Marvel:
	ts='1'
	key= "49b00060252ec6df688a67b44b75cc0e"
	s_key=" d1eca4ab9b76596debb63de6f68be3e0e8bca898"
	h= hashlib.md5((ts+s_key+key).encode()).hexdigest()
	url="http://gateway.marvel.com/v1/public/"
	personaje= None
	@classmethod
	def getPersonaje(cls,personaje):
		try:
			response=requests.get(cls.url+"characters",
				params ={ 'apikey':cls.key,
				'ts':cls.ts,
				'hash':cls.h,
				'name': personaje}).json()
			print(response.keys())
			data = response ("data")
			print(data.keys())
			results= data ["results"]
			cls.personaje = results [0]
			return "Personaje {} agregado".format(personaje)
		except:
			return "algo salio mal." 