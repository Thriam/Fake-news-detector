import requests
from bs4 import BeautifulSoup
search=input("Input the news to be searched: ")
url="https://www.google.com/search?q="+search
res=requests.get(url)
html_page=res.content
soup=BeautifulSoup(html_page, 'html.parser')
text=soup.find_all(text=True)
output=''
removed=['[document]']
for t in text:
    if t.parent.name not in removed:
        output+='{} '.format(t)
list1=output.split()
output=",".join(list1)
list2=search.split()
search=",".join(list2)
count=output.count(search)
if count>=2:
    print("\nThe news is true\n")
else:
    print("\nThe news is false\n")
