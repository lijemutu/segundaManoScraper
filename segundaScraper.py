import random,time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("--log-level=3")
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs",{
    "profile.default_content_setting_value.notifications":1
})

DRIVER_PATH = 'C:/Users/Erick/projects/segundaManoScraper/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.segundamano.mx/anuncios/estado-de-mexico/toluca/venta-inmuebles")
#print(driver.page_source)

#driver.save_screenshot('screenshot.png')

urls = driver.find_elements_by_xpath('//div[@class="card grid"]/a')
links = []
for url in urls:
    links.append(url.get_attribute('href'))

for url in links:
    time.sleep(random.uniform(8.0,10.0))

    driver.get(url)
    try:
        shop = driver.find_element_by_xpath('//div[@class="av-AdReply_UserData-txt"]/a')
        shop = shop.get_attribute('href')
        continue
    except:
        pass
    contactInfo = driver.find_element_by_xpath('//*[@class="av-AdReply_UserData-txt"]').text
    contactInfo = contactInfo.split("\n")
    contactName = contactInfo[0]
    contactPhone = contactInfo[3]

    location = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[3]/div/div[1]/div[1]/div[1]').text
    location = location.split("\n")

    print("El nombre es ",contactName, " y su número es ",contactPhone," con casa en ",location[1])


driver.quit()






""" contactInfo = driver.find_element_by_xpath('//*[@id="av-Sidebar"]/div[3]/div/div[1]/div[1]').text
contactInfo = contactInfo.split("\n")
contactName = contactInfo[0]
contactPhone = contactInfo[3]

location = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[3]/div/div[1]/div[1]/div[1]').text
location = location.split("\n")

print("El nombre es ",contactName, " y su número es ",contactPhone," con casa en ",location[1])

 """




""" HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
r = requests.get("https://www.segundamano.mx/anuncios/estado-de-mexico/toluca/venta-inmuebles/casa-en-venta-fraccionamiento-las-misiones-toluca-933225667?nav=true"\
    ,headers=HEADERS)
soup = BeautifulSoup(r.content, features="lxml")
tree = html.fromstring(r.content)
print(r.content)
try:
    phone = tree.xpath('//*[@id="av-Sidebar"]/div[3]/div/div[1]/div[1]/div[5]')
except:
    phone = ''

print(phone) """