from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Beach:
    """ Stores the important information about the beaches

    Attributes
    ----------
    name : str
        stores the name of the beach
    location : str
        stores the location of the beach (city)
    direction : str
        stores direction of the beach
    report : str
        stores the metservice link for the beach

    Functions
    ---------
    on_shore   : checks the wind and returns whether it is on shore
    off_shore  : checks the wind and returns whether it is off shore
    cross_wind : checks the wind and returns wheather it is a cross wind
    """

    def __init__(self, name: str, location: str, direction: str, report: str):
        self.name = name
        self.location = location
        self.direction = direction
        self.report = report

    def __repr__(self):
        return f"The {self.name} is located in {self.location} and is facing {self.direction}"

    def on_shore(self, wind):
        """ Checks to see if wind is on shore """
        if self.direction == "W" and wind == "E":
            return True
        if self.direction == "E" and wind == "W":
            return True
        if self.direction == "N" and wind == "S":
            return True
        if self.direction == "S" and wind == "N":
            return True
        return False

    def off_shore(self, wind):
        """ Checks to see if wind is off shore """
        if self.direction == "W" and wind == "W":
            return True
        elif self.direction == "E" and wind == "E":
            return True
        elif self.direction == "N" and wind == "N":
            return True
        elif self.direction == "S" and wind == "S":
            return True
        return False

    def cross_wind(self, wind):
        """ Checks to see if there is a cross wind """
        if not self.off_shore(wind) and not self.on_shore(wind):
            return True
        return False

    def get_temp(self, driver: webdriver.Firefox):
        driver.get(self.report)
        time.sleep(2)
        return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/p/span").text

    def get_period(self, driver: webdriver.Firefox, time_of_day: str):
        if time_of_day == "early":
            driver.get(self.report)
            time.sleep(2)
            return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[7]/td[2]/small").text
        else:
            driver.get(self.report)
            time.sleep(2)
            return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[7]/td[3]/small").text

    def get_wave_height(self, driver: webdriver.Firefox, time_of_day: str):
        if time_of_day == "early":
            driver.get(self.report)
            time.sleep(2)
            return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/small").text
        else:
            driver.get(self.report)
            time.sleep(2)
            return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[9]/td[3]/small").text

    def get_wind_direction(self, driver: webdriver.Firefox, time_of_day: str):
        if time_of_day == "early":
            driver.get(self.report)
            time.sleep(2)
            return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[5]/td[2]/small").text
        else:
            driver.get(self.report)
            time.sleep(2)
            return driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[5]/td[3]/small").text
beaches = {
    "Wiakuku"  : Beach("Waikuku Beach", "Christchurch", "E", "https://www.metservice.com/marine/regions/christchurch/surf/locations/waikuku-beach-christchurch"),
    "Brighton" : Beach("New Brighton", "Christchurch", "E", "https://www.metservice.com/marine/regions/christchurch/surf/locations/new-brighton-beach")
}

def morning_conditions(beach, driver):
        temp = beach.get_temp(driver)
        period = beach.get_period(driver, "early")
        height = beach.get_wave_height(driver, "early")
        wind = beach.get_wind_direction(driver, "early")
        if beach.off_shore(wind):
            wind = "off shore"
        elif beach.on_shore(wind):
            wind = "on shore"
        elif beach.cross_wind(wind):
            wind = "cross shore"

        return f"{beach.name} is currently {temp}, with waves {height} metres high with a period of {period} seconds and has {wind} winds."

def afternoon_conditions(beach, driver):
        temp = beach.get_temp(driver)
        period = beach.get_period(driver, "late")
        height = beach.get_wave_height(driver, "late")
        wind = beach.get_wind_direction(driver, "late")
        if beach.off_shore(wind):
            wind = "off shore"
        elif beach.on_shore(wind):
            wind = "on shore"
        elif beach.cross_wind(wind):
            wind = "a cross"

        return f"{beach.name} will be {temp} this afternoon, with waves {height} metres high with a period of {period} seconds and has {wind} winds."

if __name__=="__main__":
    try:
        beach = beaches.get("Wiakuku")
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
