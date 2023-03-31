from selenium import webdriver
import time

driver = webdriver.Chrome() # or any other browser you prefer
driver.get("https://web.whatsapp.com/")

input("Scan the QR code and press Enter to continue...") # wait for the user to scan the QR code

number = "+52 1 55 1451 4194" # replace with the phone number of the recipient
message = "Hello, this is an automatic message!" # replace with the message you want to send

# search for the recipient's chat
search_box = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
search_box.send_keys(number + "\n")

time.sleep(2) # wait for the chat to load

# type and send the message
message_box = driver.find_element_by_xpath('//div[@class="_3uMse"][@contenteditable="true"][@data-tab="1"]')
message_box.send_keys(message + "\n")

time.sleep(2) # wait for the message to be sent

driver.quit() # close the browser window
