#audiobook created by kunsh manghwani
import pyttsx3
import PyPDF2
name = input("Enter the name of your pdf file to read:-  ")
book = open(name,'rb')

pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print( "your book has "+ str(pages)+" pages")
speaker = pyttsx3.init()
i=0
speaker.say('hello you are welcome to the audiobook created by K star')
while True:
    page = pdfreader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    i=i+1
