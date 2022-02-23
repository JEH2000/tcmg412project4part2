
import re

requeststotaled = 0
requestforyear = 0
failedrequest = 0
redirects = 0

days = {}
weeks = {}
months = {}
filenames = {}
FILE = 'http_access_log.txt'  
lastyear = '/1995'
with open("http_access_log.txt") as GG:
    variable = GG.readlines()
    for line in variable:
        requeststotaled += 1
        if lastyear in line:
            requestforyear += 1
            if '302 -' in line:
                redirects += 1
            if '403 -' in line or '404 -' in line:
                failedrequest += 1 
        splitter = re.split('.+ \[(.+) .+\] "[A-Z]{3,5} (.+) HTTP/1.0" ([0-9]{3})', line)
        if len(splitter) == 5:
            date = splitter[1]
            file = splitter[2]
            date = date.split(':')
            if date[0] in days:
                days[date[0]] += 1
            else:
                days[date[0]] = 1   
            date[0] = date[0].split('/')
            if date[0][1] + " " + date[0][2] in months:
                months[date[0][1] + " " + date[0][2]] += 1
            else:
                months[date[0][1] + " " + date[0][2]] = 1
            if file in filenames:
                filenames[file] += 1
            else:
                filenames[file] = 1   
print("Total lines in file---" + str(requestforyear))
print("Request total in entire file --- " + str(requeststotaled))
print("Failed requests: " + str(failedrequest) + " Percent: " + str(round((failedrequest / requeststotaled) * 100, 2)) + "% of requests")
print("Redirected requests --- " + str(redirects) + " Percent: " + str(round((redirects / requeststotaled) * 100, 2)) + "% of requests")
print("Most requested file --- " + str(list(filenames.keys())[0]))
print("Least requested file--- " + str(list(filenames.keys())[-1]))
print("Requests each month --- ")
for key, value in months.items():
    print(str(key) + " - Freq: " + str(value))
print("**************************************************************************")
print("requests a day ")
for key, value in days.items():
    print(str(key) + " - Freq: " + str(value))

ii = open('http_access_log.txt', "r")
janmonth = open("January1995log.txt", "w")
febmonth = open("Febuary1995log.txt", "w")
marmonth = open("March1995log.txt", "w")
aprmonth = open("April1995log.txt", "w")
maymonth = open("May1995log.txt", "w")
Junmonth = open("June1995log.txt", "w")
julmonth = open("July1995log.txt", "w")
augmonth = open("August1995log.txt", "w")
sepmonth = open("September1995log.txt", "w")
octmonth1994 = open("October1994log.txt", "w")
octmonth1995 = open("October1995log.txt", "w")
novmonth1994 = open("November1994log.txt", "w")
decmonth1994 = open("December1994log.txt", "w")


for line in ii:
	if "/Jan/" in line:
		janmonth.write(line)
	elif "/Feb/" in line:
		febmonth.write(line)
	elif "/Mar/" in line:
		marmonth.write(line)
	elif "/Apr/" in line:
		aprmonth.write(line)
	elif "/May/" in line:
		maymonth.write(line)
	elif "/Jun/" in line:
		Junmonth.write(line)
	elif "/Jul/" in line:
		julmonth.write(line)
	elif "/Aug/" in line:
		augmonth.write(line)
	elif "/Sep/" in line:
		sepmonth.write(line)
	elif "/Oct/1994" in line:
		octmonth1994.write(line)
	elif "/Nov/1994" in line:
		novmonth1994.write(line)
	elif "/Dec/1994" in line:
		decmonth1994.write(line)
	elif "/Oct/1995" in line:
         octmonth1995.write(line)

ii.close()
janmonth.close()
febmonth.close()
marmonth.close()
aprmonth.close()
maymonth.close()
Junmonth.close()
julmonth.close()
augmonth.close()
sepmonth.close()
octmonth1994.close()
novmonth1994.close()
decmonth1994.close()
octmonth1995.close()




#with open('http_access_log.txt') as fo:
#    op=''
#    start=0
#    cntr = 1
#    for x in fo.read().split("\n"):
#        if (x=='/Jan/'):
#            if (start==1):
#                with open(str(cntr) + '.txt','w') as opf:
#                    opf.write(op)
#                    opf.close()
                    #op=''
                    #cntr+=1
 #           else:
                #start = 1
        #else:
#                op= op + '\n' + x
        
    
#    fo.close()


#with open("http_access_log.txt",'r') as file:
#    for line in file:
#        grade_data = line.strip().split('/')

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