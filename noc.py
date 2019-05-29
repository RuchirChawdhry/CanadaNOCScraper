from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/find-national-occupation-code.html"
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
table = soup.find('table')
df = pd.read_html(str(table))[0]
display(df)
df.to_csv('noc.csv')
