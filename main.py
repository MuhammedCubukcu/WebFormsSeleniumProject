import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import ElementList.HtmlElements as item

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Select item functions
def select_item(id, className):
    global select
    if id == 'id':
        select = driver.find_element(By.ID, className)
    if id == 'name':
        select = driver.find_element(By.NAME, className)
    if id == 'css':
        select = driver.find_element(By.CSS_SELECTOR,className)
    return select


#select item input text
selected_html_element_input_text = select_item(item.input_text[0], item.input_text[1])
selected_html_element_input_text.send_keys("Muhammed CBKC")

# select item input password
selected_html_element_input_pass = select_item(item.input_password[0], item.input_password[1])
selected_html_element_input_pass.send_keys('muhammed')

# select text area
selected_html_element_text_area = select_item(item.text_area[0], item.text_area[1])
selected_html_element_text_area.send_keys("I'am Software Engieener")

#Select dropdown
selected_html_element_dropdown = select_item(item.dropdown[0], item.dropdown[1])
selected_html_element_dropdown.click()
selected_html_element_dropdown.send_keys('two')


#dropdown data-list
selected_html_element_data_list = select_item(item.dropdown_data_list[0], item.dropdown_data_list[1])
selected_html_element_data_list.send_keys('New York')

#file upload
pdf_path = os.path.abspath('/home/mhmmd/Downloads/muhammedcubukcu_resume.pdf')
selected_html_element_upload_file = select_item(item.upload_file[0], item.upload_file[1])
selected_html_element_upload_file.send_keys(pdf_path)

#check-box
selected_html_element_checkbox = select_item(item.checkbox[0], item.checkbox[1])
selected_html_element_checkbox.click()

#color picker
"""selected_html_element_color_picker = select_item(item.color_picker[0],item.color_picker[1])
selected_html_element_color_picker.click()"""

#date picker
selected_html_element_date = select_item(item.date_picker[0], item.date_picker[1])
selected_html_element_date.click()
selected_html_element_date.send_keys('07/18/1998')

#form range
selected_html_element_form_range = select_item(item.form_range[0], item.form_range[1])
value = selected_html_element_form_range.get_attribute('value')
def set_range(el, val):
    minval = float(el.get_attribute("min") or 0)
    maxval = float(el.get_attribute("max") or 100)
    v = max(0, min(80, (float(val) - minval) / (maxval - minval)))
    width = el.size["width"]
    target = float(width) * v
    ac = ActionChains(driver)
    ac.move_to_element_with_offset(el, target, 1)
    ac.click()
    ac.perform()
set_range(selected_html_element_form_range,value)

#Submit button
selected_html_element_btn = select_item(item.submit_btn[0],item.submit_btn[1])
selected_html_element_btn.click()
