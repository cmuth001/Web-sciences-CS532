# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:45:20 2018

@author: cmuthyal
"""

import docclass
from subprocess import check_output

cl = docclass.naivebayes(docclass.getwords)
#remove previous db file
# check_output(["rm", "chandu.db"])

cl.setdb("SpamOrNot.db")
# docclass.spamTrain(cl)
# docclass.sampletrain(cl)
docclass.checkSpamOrNot(cl)
#classify text: "the banking dinner" as spam or not spam
output = {'tp':0, 'tn':0, 'fp':0, 'fn':0}
for i in range(1,11):
    with open('./testData/notSpam'+str(i)+'.txt') as f:
          txt = f.read()
          notSpamStatus = cl.classify(txt)
          if notSpamStatus == 'Not Spam':
          	output['tp']+=1
          	print("Not Spam ",i,": ",notSpamStatus)
          else:
          	output['fn']+=1
          	print("Not Spam ",i,": ",notSpamStatus)
          	print('check why not spam')
          print('\n')
          
          # print("Not_Spam ",x,": ",cl.classify(email), file=open('output.txt', 'a+'))

    with open('./testData/spam'+str(i)+'.txt') as f:
          txt = f.read()
          spamStatus = cl.classify(txt)
          if spamStatus == 'Spam':
          	output['tn']+=1
          else:
          	output['fp']+=1
          print("Spam ",i,": ",spamStatus)
print(output)