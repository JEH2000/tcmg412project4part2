import re

from pyparsing import line

f = open('http_access_log.txt', "r")
counter = 0
content = f.read()
colist = content.split("\n")
for i in colist:
    if i:
        counter += 1
        
print ("number of lines in total")
print(counter)

def reader(filename):
    with open(filename) as m:
        log = m.read()
        digital = 0
        regexp = r'\d./(Oct)/(1995)|\d./(Sep)/(1995)|\d./(Aug)/(1995)|\d./(Jul)/(1995)|\d./(Jun)/(1995)|\d./(May)/(1995)|\b(1[1-9]|[3-6][0-9]|3[0-5])/(Apr)/(1995)'
        
        date_list = re.findall(regexp, log)
        
        digital = 0
        for g in date_list:
            if g:
                
                digital += 1
    print("total occurences in the past 6 months", digital)

if __name__ == '__main__':
    reader('http_access_log.txt')  

#reggie = r'/\O../1995'
#regexp = re.findall(reggie, f)
#for q in regexp:
 #   if q:        
      #  digital += 1
#print("number of lines in the past 6 months")
#print(digital)

#\d./Oct/1995|\d./Sep/1995|\d./Aug/1995|\d./Jul/1995|\d./Jun/1995|\d./May/1995|\d./Apr/1995


#from datetime import datetime

#my_date = '11/Oct/1995:14:07:30'

#datetime_object = datetime.strptime(my_date, '%d/%b/%Y:%I:%M:%S')
#^(3[01]|[12][0-9]|[1-9])$
#^(1[0-2]|[1-9])$
#\d./Oct/1995|\d./Sep/1995|\d./Aug/1995|\d./Jul/1995|\d./Jun/1995|\d./May/1995|\b(1[1-9]|[3-6][0-9]|7[0-5])/Apr/1995
#\d./Oct/1995|\d./Sep/1995|\d./Aug/1995|\d./Jul/1995|\d./Jun/1995|\d./May/1995|\d[11-30]/Apr/1995