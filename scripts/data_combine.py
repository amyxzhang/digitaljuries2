

import csv

file1 = open('results_new.csv','r')
lines = file1.readlines()

file2 = open('time_spent.csv','r')
lines2 = file2.readlines()

file3 = open('user_notes2.csv','r')
lines3 = file3.readlines()

time_dict = {}

for line in lines2[1:]:
    vals = line.split(',')
    time_dict[vals[0].strip()] = vals[2]

status_dict = {}
notes_dict = {}

for line in lines3[1:]:
    vals = line.split(',')
    status_dict[vals[1].strip()] = vals[4]
    notes_dict[vals[1].strip()] = ','.join(vals[5:])
        
file4 = open('results_new_combined.csv','w')
 
sp = lines[0].split(',')
 
file4.write(sp[0] + ',time_spent,notes,' + ','.join(sp[1:]))
  
for line in lines[1:]:
    val = line.split(',')
    user = val[0].strip()
    if status_dict[user].strip() == 'OK':
        strr = user + ',' + time_dict[user] + ',' + notes_dict[user].strip()  + ',' + ','.join(val[1:])
        print strr
        file4.write(strr)
     

