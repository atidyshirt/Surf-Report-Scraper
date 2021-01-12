""" The helper classes and functions """

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

