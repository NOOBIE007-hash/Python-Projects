from bs4 import BeautifulSoup   # line 1 and 2 libraries are used for web scraping
from urllib.request import  urlopen
import smtplib                 # line 3 to 7 libraries are used for the updated file as sending mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# web scraping part

filename="covid_status.csv"
f=open(filename,"w")
headers="State,Confirmed Cases,Active Cases,Rcovered Cases,Dead Cases"
f.write(headers+"\n")
source = urlopen("https://www.mygov.in/covid-19/")
source_content = source.read()
html = BeautifulSoup(source_content,'html.parser')

table_html = html.find("div",{"class":"state_record"})

fulL_info1 = table_html.table
full_info2 = fulL_info1.tbody
all_states = full_info2.find_all("tr")

for state in all_states:
    all_data = state.find_all("td")
    f.write(state.td.text + "," + all_data[1].text + "," + all_data[2].text+ "," + all_data[3].text+ "," +all_data[4].text+"\n")

f.close()

# Sending email part and reference from geeksforgeeks
msg = MIMEMultipart()
msg['From']="madhavaprashath669@gmail.com"
msg['To']="dwarakaprasath569@gmail.com"
msg['Subject']="Sample Test Case"
body="Simple sample Test case is provided in file attached"
msg.attach(MIMEText(body,'plain'))
file_name="covid_status.csv"
attachment=open("covid_status.csv","rb")
p=MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',"attachment;filename= %s" %file_name)
msg.attach(p)
s=smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
'''
Important thing to note here is, this works only when the "Less Secure Apps" mode is TURNED ON in senders gmail 
settings. Else gmail considers this as a spam mail and code fails to run,
'''
s.login("madhavaprashath669@gmail.com", "god123219")
text=msg.as_string()
s.sendmail("madhavaprashath669@gmail.com", "dwarakaprasath569@gmail.com",text)
s.quit()