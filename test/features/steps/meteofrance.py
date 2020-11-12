from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_binary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('A web browser')
def web_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(2)

@when('I navigate to the meteofrance home page')
def nav_home(context):
    context.driver.get('https://meteofrance.com/')

@when('I fill the search text bar')
def fill_bar(context):
    context.driver.find_element_by_id("search_form_input").send_keys("Toulouse")

@when('I submit the form')
def fill_bar(context):
    context.driver.find_element_by_id("search_form_input").send_keys(Keys.ENTER)

@when("I click on Toulouse city")
def click_on_toulouse_search_result(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "search_result_poi_315550"))
    )
    time.sleep(0.5)
    context.driver.find_element_by_id("search_result_poi_315550").find_elements_by_tag_name("a")[0].click()

@then('A search text bar is displayed')
def search_bar_displayed(context):
    assert context.driver.find_element_by_id("search_form_input").is_displayed() is True

@then('The search result contains Toulouse city')
def check_toulouse_in_search(context):
    assert context.driver.find_element_by_id("search_result_poi_315550").is_displayed() is True

@then("Toulouse meteo is displayed")
def check_toulouse_weather(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "title-block"))
    )
    assert context.driver.find_element_by_id("title-block").text == "METEO TOULOUSE (31000)"
