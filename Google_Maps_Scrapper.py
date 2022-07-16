from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class GoogleMapsScraper:
    def __init__(self,headless=False,restaurants=True,hotels=True):
        self.headless=headless
        self.restaurants=restaurants
        self.hotels=hotels
        self.RestaurantData=[]
        self.HotelsData=[]
        options=Options()
        options.add_experimental_option("detach", True)
        if headless:
            options.headless=True
        else:
            options.headless=False

        self.driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        
    def SearchMaps(self,location):
     
        
        #first page
        self.driver.get("https://www.google.com/maps/search/"+str(location))
        
        

        try:
            #If google maps is unable to search the place
            NotFound=self.driver.find_element_by_xpath("//*[@class='IPum6b']")
            return "Search Not found"     #try improving your search keywords
        
        except:
            #if place is searched on google maps 
            try:
                #check if number of locations matching keyword is displayes on google maps or a single location is foud
                
                #if number of locations found select the first one
                FirstLocation=self.driver.find_element_by_xpath("//a[@class='hfpxzc']")
                FirstLocation.click()
                FirstLocationName=str((self.driver.find_element_by_xpath("//*[@class='hfpxzc']")).get_attribute("aria-label"))
                #open the location in google maps
                self.driver.get("https://www.google.com/maps/search/"+FirstLocationName)

            except:
                pass
            
            
            
                
            if self.restaurants:
                
                #wait till the restaurant button on maps load
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Restaurants']")))
                #click the restaurant button to get nearest restaurants 
                self.driver.find_element_by_xpath("//button[@aria-label='Restaurants']").click()
              
                #wait for restaurants data to load 
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='hfpxzc']")))
                
                #scroll 2 times to load first 12 restaurants. "initially data of only 4 is loaded"
                for i in range(0,2):
                    scroll=self.driver.find_elements_by_xpath("//a[@jsan='7.hfpxzc,0.aria-label,8.href,0.jsaction']")
                    scroll[-1].send_keys(Keys.END)
                    
                #fetch resturants data an store in rest
                fetched_restaurants=self.driver.find_elements_by_xpath("//*[@class='Nv2PK THOPZb CpccDe']")

                #iterate over all restaurants data and store its name and google maps link
                for res in fetched_restaurants:
                    self.RestaurantData.append({res.get_attribute("aria-label"):res.get_attribute("href")})
                        
            
            if self.hotels:
                #go back to first page
                self.driver.back()
                #wait till the hotels button on maps load
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Hotels']")))
                #click the restaurant button to get nearest Hotels 
                self.driver.find_element_by_xpath("//button[@aria-label='Hotels']").click()
                
                #wait for Hotels data to load 
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='hfpxzc']")))
                
                #scroll 2 times to load first 12 Hotels. "initially data of only 4 is loaded"
                for i in range(0,2):
                    scroll=self.driver.find_elements_by_xpath("//a[@jsan='7.hfpxzc,0.aria-label,8.href,0.jsaction']")
                    scroll[-1].send_keys(Keys.END)
                    
                #fetch resturants data an store in rest
                fetched_hotels=self.driver.find_elements_by_xpath("//a[@class='hfpxzc']")

                #iterate over all restaurants data and store its name and google maps link
                for hot in fetched_hotels:
                    self.HotelsData.append({hot.get_attribute("aria-label"):hot.get_attribute("href")})
                        
                print(len(self.RestaurantData))
                print(len(self.HotelsData))

                return (self.RestaurantData,self.HotelsData)
            
            
        
            
#main
gs=GoogleMapsScraper(restaurants=True,hotels=True)
p=gs.SearchMaps("wadi bani khalid")
print(p)