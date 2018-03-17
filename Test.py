from selenium import webdriver
import os

cwd = os.getcwd()

driver = webdriver.Firefox()

driver.get("file://" + cwd + "/../Exercises/ExerciseJunior.html")

title = driver.title
driver.find_element_by_id("answer1").send_keys(title)

name = driver.find_element_by_xpath("//span[@id='ok_2']/../b").text
driver.find_element_by_id("name").send_keys(name)

ocupation = driver.find_element_by_xpath("//span[@id='ok_3']/../b").text
driver.find_element_by_id("occupation").send_keys(ocupation)

black_boxs = len(driver.find_elements_by_class_name("blackbox"))
driver.find_element_by_id("answer4").send_keys(str(black_boxs))

driver.find_element_by_xpath("//a[@onclick='link_clicked();return false']").click()

red_box_class = driver.find_element_by_id("redbox").get_attribute("class")
driver.find_element_by_id("answer6").send_keys(red_box_class)

driver.find_element_by_id("submitbutton").click()

driver.find_element_by_id("checkresults").click()

solutions = driver.find_elements_by_xpath("//li/span")

for solution in solutions:
    text_solution = solution.text
    print(text_solution)
    assert text_solution == "OK", "Something went wrong at question" + solution.get_attribute("id")




