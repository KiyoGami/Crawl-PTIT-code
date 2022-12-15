from bs4 import BeautifulSoup as bs
import os
from requests import get, Session
from dotenv import load_dotenv
load_dotenv()

with Session() as s:
    site = s.get('https://code.ptit.edu.vn/login')
    soup = bs(site.content, 'html.parser')
    token = soup.find('input', {'name': '_token'})['value']
    login_data = {"username": os.environ.get('PTIT_username'),
                  "password": os.environ.get('PTIT_password'),
                  "_token": token}
    s.post('https://code.ptit.edu.vn/login', login_data)
    problem_html = s.get('https://code.ptit.edu.vn/student/question?course=326')
    problem_soup = bs(problem_html.content, 'html.parser')
    rows = problem_soup.find_all('tr', {'class': 'bg--10th'})
    links = [td.find('a')['href'] for td in rows]
    for link in links: print(link)
