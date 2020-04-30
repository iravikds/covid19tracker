from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    source = requests.get('https://www.mohfw.gov.in/').text

    soup = BeautifulSoup(source, 'lxml')

    table = soup.find('table')
    table_rows = table.find_all('tr')
    table_list = []
    table_list.append(['S.No', 'State/UT','Confirmed', 'Recovered', 'Death'])

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        table_list.append(row)
    del table_list[1]
    table_list = table_list[:-4]
    context = {"table_list": table_list}

    return render(request, 'index.html', context)
