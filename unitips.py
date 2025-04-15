import requests
from bs4 import BeautifulSoup 

loginurl = "https://www.unitips.mx/accounts/login/"
userurl = "https://www.unitips.mx/cursos-admision/user/"

session = requests.Session()
login_page = session.get(loginurl)
soup = BeautifulSoup(login_page.text, 'html.parser')
token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

payload = {
'login': 'antonio.gomez@aotlook.com',
'password': 'cesar123', 
'csrfmiddlewaretoken': token, 
'mixpanel_id': 'antonio.gomez@outlook.com',
}

headers = {
    'Referer': loginurl,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

response = session.post(loginurl, data=payload, headers=headers)

if response.status_code != 302:
	print("no fue recibido el log in")

contenido = session.get(userurl)
print(contenido.text)