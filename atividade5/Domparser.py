import urllib.request
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html_head = "<html lang='br-pt'><head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edg'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Document</title></head><body>"
strr = ""
with open ("seeds.txt","r") as file:
  for line in file:
    try:
      page = urllib.request.urlopen(line)
      html = str(page.read().decode('utf-8'))
      soup = bs(html, 'lxml')
      
      print("Título:", soup.title.string)
      print("src: ",soup.find('img').get("src") if soup.find('img') else "Não possui imagem")
      if soup.find('img'):
        if soup.find('img').get("src")[:5] == "https":
          linkImage = soup.find('img').get('src')
          strr = strr + f"<h2>{soup.title.string}</h2>" + "<img src=" + linkImage + "/>"
        else:
              linkImage = line.replace("\n", "") +soup.find('img').get('src')
              strr = strr + f"<h2>{soup.title.string}</h2>" + "<img src=" + linkImage + "/>"
      else:
        strr = strr + f"<h2>{soup.title.string}</h2> <p> Imagem não fornecida </p>"
    except  Exception as e:
      print("Ocorreu um erro nessa requisição: ", e)

with open("result.html","w") as resultHTML:
  resultHTML.write(strr)




