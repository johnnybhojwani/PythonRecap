import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client


chapters=list(range(1,261))

random_chapter = random.choice(chapters)


webpage = 'https://online.recoveryversion.bible/BibleChapters.cfm?cid='+ str(random_chapter)

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')


#Get the name of the book of the Bible from the webpage
books = soup.findAll("span",class_="show-for-sr")

book = books[1].text.rstrip("Outline")


#Get the chapter of the book from the webpage
chapter = soup.find("h4",class_="chapter").text.lstrip("CHAPTER ")


all_verses = soup.findAll("p",class_="verses")
mychoice = random.choice(all_verses)

message = book+chapter+":"+mychoice.text.lstrip()

print(message)



#text my choice to my phone!
accountSID = 'ACd6351ff4800a312d3756d77307724047'

authToken = '4b146ee9261e04a21ad2736e8fa0e3ab'

client = Client(accountSID, authToken)

TwilioNumber = ""

myCellPhone = ""


#send text message
textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                                     body=message)



# to set it up to automatically run this program, set it up in task manager:
# create a .bat file that has the line:

# python "C:\Users\johnny_bhojwani\Box Sync\MIS 4V98 - PYTHON\Web Scaping\webscraping - Bible - Recovery Version - KEY.py
#(presuming you have python set up as an environmental variable

# create an automated task that will run it on whatever schedule you want.










