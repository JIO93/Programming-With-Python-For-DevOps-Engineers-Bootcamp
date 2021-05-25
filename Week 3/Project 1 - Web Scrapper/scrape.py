#Requests is a library that you can use to make API calls.
import requests
from bs4 import BeautifulSoup

#This line creats the get request
page = requests.get('https://michaellevan.net')

#This line pulls all of the content form the entire website. 
soup = BeautifulSoup(page.content, 'html.parser')

#This line gets the title of the page in text format.S
page_title = soup.title.text
#This line gets the header of the page.
page_head = soup.head

#These two lines pull the h1 headers in text format.
first_h1 = soup.select('h1')[0].text
second_h1 = soup.select('h1')[1].text

#These two lines print the first two headers in text format by calling the variable.
print(first_h1)
print(second_h1)