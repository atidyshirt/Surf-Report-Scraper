from selenium import webdriver
from utils import morning_conditions, afternoon_conditions
from list_of_beaches import all_beaches

def main():
    try:
        beach = all_beaches.get("Wiakuku")
        options = webdriver.FirefoxOptions();
        options.set_headless()
        driver = webdriver.Firefox(firefox_options=options)
        print(morning_conditions(beach, driver))
        print(afternoon_conditions(beach, driver))
    finally:
        try:
            driver.close()
        except:
            pass

if __name__=="__main__":
    main()
