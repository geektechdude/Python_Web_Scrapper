# geektechstuff
# web scrapper

# libraries to import
from urllib.request import urlopen
from bs4 import BeautifulSoup

def show_html(URL_input):
    # shows the HTML unparsed
    html = urlopen(URL_input)
    return(html.read())

def soupy(URL_INPUT):
    # uses Beautiful Soup to show HTML with parser
    bs=BeautifulSoup(show_html(URL_INPUT),'html.parser')
    return(bs)

def find_div_text(URL_INPUT):
    # finds all the div tags in the HTML and returns their text
    bs=BeautifulSoup(show_html(URL_INPUT),'html.parser')
    for div in bs.find_all('div'):
        return(div.get_text())

def find_divs(URL_INPUT):
    # finds the div tags in the HTML
    bs=BeautifulSoup(show_html(URL_INPUT),'html.parser')
    for div in bs.find_all('div'):
        return(div)

def find_links(URL_INPUT):
    # returns all the hyperlink destinations on a page
    list_of_urls = []
    html = urlopen(URL_INPUT)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a'):
        list_of_urls.append((link.attrs['href']))
    return(list_of_urls)


def find_pictures(URL_INPUT):
    # returns all the pictures on a page and list picture source
    list_of_pic_urls = []
    html = urlopen(URL_INPUT)
    bs = BeautifulSoup(html, 'html.parser')
    for img in bs.find_all('img'):
        list_of_pic_urls.append(img.attrs['src'])
    return(list_pic_urls)

def links_of_links(URL_INPUT):
        lots_of_links = find_links(URL_INPUT)
        print(lots_of_links)
        for item in lots_of_links:
                try: 
                        print("Visiting",item)
                        print("Found links:")
                        print(find_links(item))
                        print("Finished on",item)
                except:
                        print('error') 

print(links_of_links("https://www.geektechstuff.com"))