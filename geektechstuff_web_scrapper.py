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
    return(list_of_pic_urls)

def links_of_links(URL_INPUT):
        # prints the links of the links that find_links finds -use carefully!
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

def wiki_login():
        # import selenium webdriver
        from selenium import webdriver
        import time
        # set browser / browser options
        browser = webdriver.safari.webdriver.WebDriver(quiet=False)
        # get page
        browser.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
        # web page IDs that handle log in
        username = browser.find_element_by_id('wpName1')
        password = browser.find_element_by_id('wpPassword1')
        login = browser.find_element_by_id('wpLoginAttempt')
        # send details to log in IDs
        username.send_keys("USERNAME_HERE")
        password.send_keys("PASSWORD_HERE")
        login.click()
        time.sleep(5)
        
        
def wordpress_login():
        # import selenium webdriver
        from selenium import webdriver
        import time
         # logon details
        username_wp = "USERNAME_HERE"
        password_wp = "PASSWORD_HERE"
        # set browser / browser options
        browser = webdriver.safari.webdriver.WebDriver(quiet=False)
        # if using Chrome it needs a path!
        #browser = webdriver.Chrome()
        # get page
        browser.get("https://wordpress.com/log-in")
        # delay to give page chance to load
        time.sleep(5)
        # Fields by ID for username page
        username_field = browser.find_element_by_id('usernameOrEmail')
        username_field.send_keys(username_wp)
        # element by XPath
        login_button = browser.find_element_by_xpath("//button[text()='Continue']")
        login_button.click()
        time.sleep(5)
        password_field = browser.find_element_by_id("password")
        password_field.send_keys(password_wp)
        login_button.click()
        time.sleep(5)
        wp_hub = browser.find_element_by_xpath("//*[@id='header']/a[1]")
        wp_hub.click()
        time.sleep(5)
        # looking for visitors stats
        # element by CSS selector
        stat = browser.find_element_by_css_selector("#my-stats-content > div.card.stats-module.is-chart-tabs > ul > li:nth-child(2) > a > span.value")
        stat_value = stat.text
        time.sleep(5)
        print("Total number of visitors so far today =", stat_value)
        browser.quit()
