import urllib
import re

print "\nThis is a Release Scraper for NDC  \nBy: @ZWeed4U"
print "\n"


#TO DO NEXT: Get date scraped  <-lulz

i=0



print "#################  RECENT/UPCOMING RELEASES  #################\n"

try:    
    while i< 64: #<-  random number
        
            htmlfile = urllib.urlopen("http://help-en-us.nike.com/app/answers/detail/a_id/41986/p/3897")
            htmltext = htmlfile.read()

            regex = '<h3>(.+?)</h3>'    #'<h3><a href="[^.]*" target="[^.]*">(.+?)</a></h3>'
            regex2 = '</h3>(.+?)<br>(.+?)</td>'

            pattern = re.compile(regex)
            pattern2 = re.compile(regex2)

            name = re.findall(pattern,htmltext)
            info = re.findall(pattern2,htmltext)
               
            if '<a href' in name[i]:
                print str(name[i].split('>')[1][:-3]) + " - " + str(info[i]) + "\n"

            else: 
                print str(name[i])+ " - " + str(info[i])+ "\n"

            i+=1

except:
    print "\n"
    print "Error - most likely out of bounds (<64 release news items)"

 

