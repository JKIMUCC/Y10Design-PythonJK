import requests
import pprint
import os
import json


def writeHTML(data):
			hdata = str(data)
			myfile = open("main.html","w")

			html_s = """
			<!DOCTYPE html>
			<html>
			<head>
				<link href="https://fonts.googleapis.com/css?family=Fjalla+One" rel="stylesheet">
				<title>News API</title>
			</head>





			<body>


				<style>
			body {
			  height: 500px;
			  background: linear-gradient(141deg, #0fb8ad 0%, #1fc8db 51%, #2cb5e8 75%);
			}


			</style>

				<h1>Welcome to My News API</h1>
				<p>Go to <a href='https://newsapi.org/'>News API</a> for API Info.</p>
				<style>

				body {
					font-family: 'Fjalla One', sans-serif;
				}



				<style>
				body {
				  font-family: 'Fjalla One', sans-serif;
				  font-size: 20px;
				}

				#myBtn {
				  display: none;
				  position: fixed;
				  bottom: 20px;
				  right: 30px;
				  z-index: 99;
				  font-size: 18px;
				  border: none;
				  outline: none;
				  background-color: red;
				  color: white;
				  cursor: pointer;
				  padding: 15px;
				  border-radius: 4px;
				}

				#myBtn:hover {
				  background-color: #555;
				}
				</style>

				<style>
			body {
			  font-family: 'Fjalla One', sans-serif;
			}

			.sidebar {
			  height: 100%;
			  width: 0;
			  position: fixed;
			  z-index: 1;
			  top: 0;
			  left: 0;
			  background-color: #009500;
			  overflow-x: hidden;
			  transition: 0.5s;
			  padding-top: 60px;
			}

			.sidebar a {
			  padding: 8px 8px 8px 32px;
			  text-decoration: none;
			  font-size: 25px;
			  color: #111;
			  display: block;
			  transition: 0.3s;
			}

			.newsImage3{
				width: 398px;
				height: 250px;
				padding-left:20px;
				float: left;
				padding-top: 32px;
			}
			.card1 {
			  	box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
			  	transition: 0.3s;
			  	width: 400px;
				height: 250px;
				padding-left:90px;
				float: left;
				padding-top: 32px;
			}
			.card1:hover {
			  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
			}
			.card2 {
				box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
			  	transition: 0.3s;
			  	width: 400px;
				height: 250px;
				padding-left:20px;
				float: left;
				padding-top:32px;
			}
			.card2:hover {
			  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
			}
			.card3 {
				box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
			  	transition: 0.3s;
			  	width: 400px;
				height: 250px;
				padding-left:20px;
				float: left;
				padding-top:32px;
			}
			.card3:hover {
			  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
			}
			.container {
			  padding: 2px 16px;
			  background: white;
			  color:black;
			}
			.news{
				background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("bg2.jpg");
				height: 510px;
				width: fill;
			}
			.sidebar a:hover {
			  color: #f1f1f1;
			}

			.sidebar .closebtn {
			  position: absolute;
			  top: 0;
			  right: 25px;
			  font-size: 36px;
			  margin-left: 50px;
			}

			.openbtn {
			  font-size: 20px;
			  cursor: pointer;
			  background-color: #111;
			  color: white;
			  padding: 10px 15px;
			  border: none;
			}

			.openbtn:hover {
			  background-color: #444;
			}

			#main {
			  transition: margin-left .5s;
			  padding: 16px;
			}


			@media screen and (max-height: 450px) {
			  .sidebar {padding-top: 15px;}
			  .sidebar a {font-size: 18px;}
			}
			</style>
			</head>
			<body>

			<div id="mySidebar" class="sidebar">
			  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×</a>
			  <a href="main.html">Main</a>
			  <a href="list.html">List of News Sources</a>
			</div>


			  <button class="openbtn" onclick="openNav()">☰ Menu</button>

			<script>
			function openNav() {
			  document.getElementById("mySidebar").style.width = "250px";
			  document.getElementById("main").style.marginLeft = "250px";
			}

			function closeNav() {
			  document.getElementById("mySidebar").style.width = "0";
			  document.getElementById("main").style.marginLeft= "0";
			}
			</script>


			</head>
			"""

			myfile.write(html_s)
			myfile.write('<h1> Your Results: </h1>\n')
			myfile.write('<div class="news >')

			for i in range(3):
                myfile.write('	<a href="' + url[i] + '">\n')
                myfile.write('		<div class="card' + str(i+1) + '">\n')
                myfile.write('			<img src="' + iurl[i] + '"alt="Image1" style="width:100%; height: 105%">\n')
                myfile.write('			<div class="container">\n')
                myfile.write('		 		<h4><b>' + title[i] + '</b></h4> \n')
                myfile.write('		  	</div>\n')
                myfile.write('		</div>\n')
                myfile.write('	</a>\n')

            myfile.write('</div>\n')
			myfile.write('</body>\n')
			myfile.write('</html>')



secret = '8320ac2931434c4fb2dc3f02ed23d8ca'


print("Welcome to the News Search Engine")
print("1: Top Headlines")
print("2: Search by topic")
print("3: Search by date published")
print("4: Search by news source url")

while True:[]
	choice = int(input("What would you like to do? \n"))

	if choice == 1:
		

		def main():
			url = ('https://newsapi.org/v2/top-headlines?'
				'country=us&'
				'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')

			response = requests.get(url)
			response_json = response.json()
			p = pprint.pprint(response_json)
			writeHTML(p)
		main()
		break

	elif choice == 2:
		search = input("Enter your search word: \n")

		url = ('https://newsapi.org/v2/everything?'
			'q='+search+'&'
			'from=2019-10-22&'
			'to=2019-10-21&'
			'sortBy=popularity&'
			'lang=eng&'
			'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')

		response = requests.get(url)
		sjson = response.json()

		title = []
		url = []
		iurl = []

		for i in range(5):
			title.append(sjson['articles'][i]['title'])
			url.append(sjson['articles'][i]['url'])
			iurl.append(sjson['articles'][i]['urlToImage'])




		response_json = response.json()
		p = pprint.pprint(response_json)
		writeHTML(title[1])
		break

	elif choice == 3:
		print("please put in format: YYYY-MM-DD")
		search = input("Enter your search word: \n")

		url = ('https://newsapi.org/v2/top-headlines?'
			'from='+search+'&'
			'sortBy=popularity&'
			'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')

		response = requests.request("GET", url)
		response_json = response.json()
		p = pprint.pprint(response_json)
		writeHTML(p)
		break


	elif choice == 4:
		print("Enter the news")
		print("Please input a valid news source.")
		search = input("Enter your search word: \n")

		url = ('https://newsapi.org/v2/top-headlines?'
			'source='+search+''
			'sortBy=popularity&'
			'apiKey=8320ac2931434c4fb2dc3f02ed23d8ca')
	
		response = requests.request("GET", url)
		response_json = response.json()
		p = pprint.pprint(response_json)
		writeHTML(p)
		break

	else:
		choice = input("That is not an available choice, press enter to try again. \n")
		os.system("clear")

























