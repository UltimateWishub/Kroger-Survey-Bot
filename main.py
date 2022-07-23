# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# gathering required info
date = input("what's the date on the receipt? (eg. 7, 21, 30) ")
hour = input("what's the hour on the receipt? (eg. 01, 12, 06) ")
minute = input("what's the minute on the receipt? (eg. 07, 21, 59) ")
meridian = input("what's the meridian on the receipt? AM or PM ONLY ").upper()
cn1 = input("1st group of numbers ")
cn2 = input("2nd group of numbers ")
cn3 = input("3rd group of numbers ")
cn4 = input("4th group of numbers ")
cn5 = input("5th group of numbers ")
cn6 = input("6th group of numbers ")

# driver
driver = webdriver.Edge(
    executable_path="C:/Users/David/Documents/bing-rewards-1.11/BingRewards/drivers/msedgedriver.exe")

# load the webpage
driver.get("https://www.krogerstoresfeedback.com/")

# fill in date
driver.find_element(by=By.CLASS_NAME, value="ui-datepicker-trigger").click()
driver.find_element(by=By.LINK_TEXT, value=date).click()

# fill in time
# hour
driver.find_element(By.ID, "InputHour").click()
Select(driver.find_element(By.ID, "InputHour")).select_by_visible_text(hour)

# minute
driver.find_element(By.ID, "InputMinute").click()
Select(driver.find_element(By.ID, "InputMinute")
       ).select_by_visible_text(minute)

# meridian or sum (AM or PM)
driver.find_element(By.ID, "InputMeridian").click()
Select(driver.find_element(By.ID, "InputMeridian")
       ).select_by_visible_text(meridian)

# fill in entry id
driver.find_element(By.ID, "CN1").send_keys(cn1)
driver.find_element(By.ID, "CN2").send_keys(cn2)
driver.find_element(By.ID, "CN3").send_keys(cn3)
driver.find_element(By.ID, "CN4").send_keys(cn4)
driver.find_element(By.ID, "CN5").send_keys(cn5)
driver.find_element(By.ID, "CN6").send_keys(cn6)
driver.find_element(By.ID, "NextButton").click()


driver.find_element(By.CSS_SELECTOR, ".Opt5 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()


driver.find_element(By.ID, "NextButton").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114002 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114003 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114014 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114007 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114010 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114005 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114012 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114026 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114006 > .Opt5 > .radioSimpleInput").click()
driver.find_element(
    By.CSS_SELECTOR, "#FNSR114008 > .Opt5 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()

driver.find_element(By.ID, "NextButton").click()

driver.find_element(
    By.CSS_SELECTOR, ".Opt9 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()

driver.find_element(
    By.CSS_SELECTOR, ".Opt2 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()
driver.find_element(By.ID, "NextButton").click()

driver.find_element(
    By.CSS_SELECTOR, "#FNSR115001 > .Opt5 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()


driver.find_element(
    By.CSS_SELECTOR, ".Opt10 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()


driver.find_element(
    By.CSS_SELECTOR, "#FNSR128001 .checkboxSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()

driver.find_element(
    By.CSS_SELECTOR, ".Opt10 > .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()

Select(driver.find_element(By.ID, "R002004")).select_by_visible_text("26")
driver.find_element(By.ID, "NextButton").click()

Select(driver.find_element(By.ID, "R002003")
       ).select_by_visible_text("Prefer not to answer")
driver.find_element(By.ID, "NextButton").click()

Select(driver.find_element(By.ID, "R002017")
       ).select_by_visible_text("Prefer not to answer")

Select(driver.find_element(By.ID, "R002018")
       ).select_by_visible_text("Prefer not to answer")
driver.find_element(By.ID, "NextButton").click()

Select(driver.find_element(By.ID, "R002005")
       ).select_by_visible_text("Prefer not to answer")

Select(driver.find_element(By.ID, "R002006")
       ).select_by_visible_text("Prefer not to answer")
driver.find_element(By.ID, "NextButton").click()

driver.find_element(By.ID, "NextButton").click()

driver.find_element(
    By.CSS_SELECTOR, ".Opt2 .radioSimpleInput").click()
driver.find_element(By.ID, "NextButton").click()

driver.find_element(By.ID, "S003009").send_keys("4693040716")
driver.find_element(By.ID, "R003010").send_keys("4693040716")
driver.find_element(By.ID, "NextButton").click()

if driver.title == "Kroger : Shop Groceries, Find Digital Coupons & Order Online ":
    driver.quit()
