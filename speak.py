'''First you need to install pyttsx3 
for windows goto command prompt and enter the following without quotations & hit enter
'pip install pyttsx3'
'''
import PyPDF2
import pyttsx3

file = open('watchdog.pdf','rb')
file_read = PyPDF2.PdfFileReader(file)
file_data = ''
for page in range(file_read.numPages):
	page_data = file_read.getPage(page)
	file_data += page_data.extractText()
file.close()

engine = pyttsx3.init()
engine.say(file_data)
engine.runAndWait()