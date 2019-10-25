import requests
import pprint
import os






secret = '8320ac2931434c4fb2dc3f02ed23d8ca'


print("Welcome to the News Search Engine")
print("1: Top Headlines")
print("2: Search by topic")
print("3: Search by date published")
print("4: Search by news source url")

while True:
	choice = int(input("What would you like to do? \n"))

	if choice == 1:
		url = ('https://newsapi.org/v2/top-headlines?'
	       'country=us&'
	       'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')

		response = requests.get(url)
		response_json = response.json()
		pprint.pprint(response_json)
		break

	elif choice == 2:
		search = input("Enter your search word: \n")

		url = ('https://newsapi.org/v2/everything?'
			'q='+search+'&'
			'from=2019-10-22&'
			'sortBy=popularity&'
			'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')
		parameters = {
		'q': 'big data',
		'pageSize': 20,  
		'apiKey': secret 
		}

		response = requests.get(url, params=parameters)
		response_json = response.json()
		pprint.pprint(response_json)
		break

	elif choice == 3:
		print("please put in format: YYYY-MM-DD")
		search = input("Enter your search word: \n")

		url = ('https://newsapi.org/v2/top-headlines?'
			'from='+search+'&'
			'sortBy=popularity&'
			'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')
		parameters = {
		'q': 'big data',
		'pageSize': 20,  
		'apiKey': secret 
		}

		response = requests.get(url, params=parameters)
		response_json = response.json()
		pprint.pprint(response_json)
		break


	elif choice == 4:
		print("Enter the news")
		print("Please input a valid news source.")
		search = input("Enter your search word: \n")

		url = ('https://newsapi.org/v2/top-headlines?'
			'source='+search+''
			'sortBy=popularity&'
			'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')
		parameters = {
		'q': 'big data',
		'pageSize': 20,  
		'apiKey': secret 
		}

		response = requests.get(url, params=parameters)
		response_json = response.json()
		pprint.pprint(response_json)
		break

	else:
		choice = input("That is not an available choice, press enter to try again. \n")
		os.system("clear")

























