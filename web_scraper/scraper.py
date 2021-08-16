import requests
from bs4 import BeautifulSoup


URL='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):
    pages=requests.get(URL)
    soup=BeautifulSoup(pages.content,'html.parser')
    result=soup.find_all(class_="mw-parser-output" )
    print(f"{len(result)}  number of citations")
    
    return len(result)
get_citations_needed_count(URL)



def get_citations_needed_report(URL):
    pages=requests.get(URL)
    soup=BeautifulSoup(pages.content,'html.parser')
    datas=soup.find_all(class_="mw-parser-output")
   
    result = ''
    for data  in datas:
        result = result + f'{data.parent.text.strip()}'

    f = open("citation.txt", "w")
    f.write(result)
    f.close()
    return result
print(get_citations_needed_report(URL))
get_citations_needed_report(URL)