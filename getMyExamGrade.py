from selenium import webdriver
from getpass import getpass
import re
import smtplib, ssl
import time
import os
from twilio.rest import Client
from selenium.webdriver.chrome.options import Options

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

usr = 'acc421'
pwd = 'Neocuber123'
CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
CHROMEDRIVER_PATH = 'C:/Users/MuhamadIqbal/AppData/Local/Programs/Python/Python37/Tools/chromedriver/chromedriver.exe'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options
                         ) 
driver.get('https://stisys.haw-hamburg.de/')

username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('login_link')
login_btn.submit()

driver.get('https://stisys.haw-hamburg.de/viewExaminationData.do')

ts = time.localtime()
readable = "Current time: " + time.strftime("%Y-%m-%d %H:%M:%S", ts)
print(readable)


with open("C:/Users/MuhamadIqbal/Desktop/getMyExamGrade/page_source_new.html", "w") as f:
    f.write(driver.page_source)

driver.quit()      
    
diff = "NEW:"
with open('page_source_new.html') as file1, open('page_source_original.html') as file2:
    for file1Line, file2Line in zip(file1, file2):
        if file1Line != file2Line:
            if not(bool(re.search('<div class="autoLogMessage">.*', file1Line)) or bool(re.search('<div class="autoLogMessage">.*', file2Line))):
                if file1Line.strip() == '</tr>':
                    break
                
                cleantxt = cleanhtml(file1Line).strip()
                
                if cleantxt != "":
                   diff = diff + '\n' + cleantxt 
                #diff = diff + 'OLD:' +  file2Line + '\n'
                
 

if diff != "NEW:":
   print('we spot the difference!') 
   os.remove("page_source_original.html") 
   os.rename('page_source_new.html','page_source_original.html')
   

   
   #client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
   client = Client('AC5feaff7948a64e99e3f9b83f0790f465','530a1cda40368fc79e8cdc0355db509b')

   # this is the Twilio sandbox testing number
   from_whatsapp_number='whatsapp:+14155238886'
   # replace this number with your own WhatsApp Messaging number
   to_whatsapp_number='whatsapp:+4915736367003'
   
   greeting = 'Hey, your grade is online!\n'
   closing = 'check this out for details:\n https://stisys.haw-hamburg.de/'
   message = greeting + closing

   client.messages.create(body= message,
                          from_=from_whatsapp_number,
                          to=to_whatsapp_number)
   time.sleep(1)                      
   client.messages.create(body= diff,
                          from_=from_whatsapp_number,
                          to=to_whatsapp_number)
   
   # port = 465  # For SSL
   # password = 'Black251096'

   # Create a secure SSL context
   # context = ssl.create_default_context()
   # smptp_server = "smtp.gmail.com"
   # sender_email = "myfancyreporter@gmail.com"
   # receiver_email = "miqbal.anshori@yahoo.com"
   # print("We spot the difference!")
   # message = """\
     

     # We spot the difference:
     
     # """
   # message = message + diff
   # message.encode('utf-8')
   # with smtplib.SMTP_SSL(smptp_server, port, context=context) as server:
     # server.login(sender_email, password)
     # server.sendmail(sender_email, receiver_email,message.encode('utf-8').strip())
     
   
   


    
   


