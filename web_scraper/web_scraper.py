import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(url):
    response  = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    result=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
   
    return f'{len(result)} citations needed'
    

def get_citations_needed_report(url):

    arr=[]
    response  = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    result=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    [arr.append(i.parent.text) for i in result ]
    return (('\n').join(arr))



domain ='https://en.wikipedia.org/wiki/History_of_Mexico'
# print(get_citations_needed_count(domain))
print(get_citations_needed_report(domain))
