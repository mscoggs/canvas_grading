from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import numpy as np

url = "https://wwu.instructure.com/courses/1413421/gradebook/speed_grader?assignment_id=5780523&student_id=3995242"
driver = webdriver.Chrome("chromedriver")

QUESTION_NUMBER = 5
TOTAL_STUDENTS = 350

driver.get(url)

time.sleep(2)
driver.find_element_by_id("i0116").send_keys("scoggim@wwu.edu")
driver.find_element_by_id("idSIButton9").click()

time.sleep(3)


driver.find_element_by_id("i0118").send_keys("who_farted_69")
driver.find_element_by_id("idSIButton9").click()

time.sleep(2)

driver.find_element_by_id("idSIButton9").click()

time.sleep(8)

#
# #driver.find_element_by_name("FA20 MATH 112: Functions and Algebraic Methods 202040").click()
# #driver.find_element_by_class_name("ic-DashboardCard__header").click()
# driver.find_element_by_css_selector("[aria-label='FA20 MATH 112: Functions and Algebraic Methods 202040']").click()
#
# time.sleep(2)
#
# driver.find_element_by_class_name("quizzes").click()
#
# time.sleep(2)

#elems = driver.find_elements_by_xpath("//a[@href]")

# elems = driver.find_elements_by_xpath("//div[@class='quiz_sortable question_holder']")
#
# doc = driver.page_source
# print(re.findall(r'https://wwu.instructure.com/files/+[(0-9)*]+/download', doc))

time.sleep(2)
#driver.find_element_by_id("next-student-button").click()
#time.sleep(2)



driver.find_element_by_class_name("question_input").send_keys("2")

















print(elems)
print(np.size(elems))
for elem in elems:
    link = elem.get_attribute("href")
    print(link)


quit()
links = driver.find_elements_by_xpath("//*[contains(text(), 'Question 5')]")

for link in links:
    print(link.get_attribute("href"))


print(links)

quit()
driver.find_elements_by_xpath("//*[contains(text(), 'Question 5')]").click()

continue_link = driver.find_element_by_link_text('Question 5').click()

#driver.find_element_by_xpath("//button[contains(text(), 'Question 5')]").click()
src1 = driver.find_element_by_class_name('_3nY-4HH-_rvFvLd7JbWW4j')

fraction = 0.5
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight*"+str(fraction), src1)

doc = driver.page_source
print(re.findall(r'https://wwu.instructure.com/files/+[0-9*]+/download', doc))








driver.find_element_by_xpath("//button[contains(text(), 'Students')]").click()
time.sleep(3)

src1 = driver.find_element_by_class_name('_3nY-4HH-_rvFvLd7JbWW4j')

total_clicks = 0
old_height = 0

while(True):

    try: driver.find_element_by_class_name("_2ExN4wVEDxBobXoyy9V5aD").click()
    except: break
    time.sleep(2)
    new_height = driver.execute_script("return arguments[0].scrollHeight", src1)
    print(new_height)
    if(new_height == old_height): break
    total_clicks += 1
    old_height = new_height

    #if(total_clicks == 4): break


driver.execute_script("arguments[0].scrollTop = 0", src1)



contacts_file = open("mycontacts_august.txt", "w")
emails = []

scrolls_per_block = 6

for x in range(total_clicks):
    for y in range(scrolls_per_block):
        doc = driver.page_source
        re.findall(r'[\w\]+@wwu.edu+', doc)
        emails = np.append(np.unique(emails), re.findall(r'[\w\]+@wwu.edu+', doc))
        fraction = str((scrolls_per_block*x+y)/(scrolls_per_block*total_clicks))
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight*"+fraction, src1)
        time.sleep(2)
        emails = np.unique(emails)
        print(np.size(emails))
        time.sleep(1)
    if(np.size(emails) > 800):
        write_list = emails[0:500]
        emails = emails[500:np.size(emails)]
        for email in write_list:
            print("writing ", email)
            contacts_file.write(email + "\n")

for email in emails:
    print("writing ", email)
    contacts_file.write(email + "\n")
