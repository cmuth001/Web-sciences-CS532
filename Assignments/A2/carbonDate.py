
import requests
import json
import csv
from datetime import datetime
import errno
totalUrls=0
noMementoCount = 0
noEst = 0
def carbonDateAgeCalculation(url):
    print('--------------------------')
    global ageAndMementos
    global noMementoCount
    global noEst
    global totalUrls
    totalUrls = totalUrls+1
    try:
        cdUrl = 'http://cd.cs.odu.edu/cd/'+url
        memUrl = 'http://memgator.cs.odu.edu/timemap/json/'+url
        cdres = requests.get(cdUrl)
        memres =requests.get(memUrl, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
        print('cdredst:',cdres.status_code,'memst:',memres.status_code)
        data = cdres.json()
        memcount = memres.headers['X-Memento-Count']
        estDate = data['estimated-creation-date']

        if estDate=="":
            noEst = noEst+1
        if memcount=='0':
            noMementoCount = noMementoCount+1
        print('noMementoCount: ', noMementoCount)
        print('noEst: ', noEst)
        if cdres.status_code==200 and memres.status_code==200:
            estDate = datetime.strptime(estDate, '%Y-%m-%dT%X')
            age = datetime.now() - estDate
            print('age: ', age.days, 'Memento: ',memcount)

            print('-------------------------')
            return([age.days,memcount])
    except KeyboardInterrupt:
        exit()
    except:
        pass
    return('fail')

with open('finalurls.txt') as fp:
    with open('ageAndMementos.csv','w') as csvfile:
        fieldsnames = ['age','mementos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldsnames)
        writer.writeheader()
        for line in fp:
            values = carbonDateAgeCalculation(line.strip())
            if values!='fail':
                writer.writerow({'age': values[0], 'mementos': values[1]})
            else:
                print(values)

print('totalUrls: ', totalUrls)
print('no mementos: ', noMementoCount)
print('no date estimate: ', noEst)

'''
('totalUrls: ', 1001)
('no mementos: ', 851)
('no date estimate: ', 139)


'''