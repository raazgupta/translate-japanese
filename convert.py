import sys
import mechanize
from BeautifulSoup import BeautifulSoup

#This section takes an image and converts it to Japanse text
response = mechanize.urlopen("http://maggie.ocrgrid.org/nhocr/")
forms = mechanize.ParseResponse(response, backwards_compat=False)
form = forms[0]
print form 

#Adding file to the form
form.add_file(open("image2.pgm"),"image/x-pgm","image.pgm")

jText = mechanize.urlopen(form.click()).read()

print 
print jText

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

#responseJapanese = br.open("http://translate.google.com/")
#formsJapanese = mechanize.ParseResponse(responseJapanese, backwards_compat=False)
#formJapanese = formsJapanese[0]
#print formJapanese

##adding japanese text to the google translate form
#formJapanese["text"] = jText
#formJapanese["sl"] = ["ja"]
#formJapanese["tl"] = ["en"]
#webText = br.open(formJapanese.submit()).read()

#FILE = open("test.html", "w")
#FILE.writelines(webText)
#FILE.close()

soup = BeautifulSoup(''.join(webText))
rBox = soup.find('span', id="result_box")
print rBox.contents[0].contents[0].string





