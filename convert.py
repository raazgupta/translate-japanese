import sys
import mechanize
from BeautifulSoup import BeautifulSoup

#Get file location from user
fileLoc = raw_input("Enter file location:")

#This section takes an image and converts it to Japanse text
response = mechanize.urlopen("http://maggie.ocrgrid.org/nhocr/")
forms = mechanize.ParseResponse(response, backwards_compat=False)
form = forms[0]
print "Processing..."

#Adding file to the form
form.add_file(open(fileLoc),"image/x-jpg","image.jpg")

jText = mechanize.urlopen(form.click()).read()
print
print "Japanese Text: " + jText

#This section takes the japanese text and converts it to English
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')]
br.open("http://translate.google.com/")
br.select_form(name="text_form")
br["text"] = jText
br["sl"] = ["ja"]
br["tl"] = ["en"]
responseEnglish = br.submit()
webText = responseEnglish.read()

soup = BeautifulSoup(''.join(webText))
#Print the romaji
romaji = soup.find('div', id="src-translit")
print
print "Romaji: " + romaji.contents[0].string 

#Print the english translation
englishTranslation = soup.find('span', id="result_box")
print
print "English Text: " + englishTranslation.contents[0].contents[0].string





