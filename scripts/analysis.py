
import csv

file = open('results_new_combined.csv','r')

csvfile = csv.DictReader(file)

users = {}

avg_time_spent = []

immersive = {'immersive_difficulty': [],
           'immersive_time': [],
           'immersive_satisfaction': [],
             'immersive0': [],
             'immersive1': [],
             'immersive2': [],
             'immersive3': [],
             'immersive4': [],
             'immersive5': [],
             }
scaleable = {'scaleable_difficulty': [],
           'scaleable_time': [],
           'scaleable_satisfaction': [],
             'scaleable0': [],
             'scaleable1': [],
             'scaleable2': [],
             'scaleable3': [],
             'scaleable4': [],
             'scaleable5': [],
             }
control = {'control_difficulty': [],
           'control_time': [],
           'control_satisfaction': [],
           'control0': [],
           'control1': [],
           'control2': [],
           'control3': [],
           'control4': [],
           'control5': [],
           }

enforcement = []
recommendation = []

pref = {'control': 0,
        'scaleable': 0,
        'immersive': 0}
nonpref = {'control': 0,
        'scaleable': 0,
        'immersive': 0}


for row in csvfile:
#     if row['status'] == "OK":
        
    users[row['mturk']] = row
#         t = row['time_spent']
#         avg_time_spend.append()

    
    if 'Blind Voting' in row['complete_pref']:
        pref['scaleable'] += 1
    elif 'No Jury' in row['complete_pref']:
        pref['control'] += 1
    elif 'Deliberating' in row['complete_pref']:
        pref['immersive'] += 1

    if 'Blind Voting' in row['complete_nonpref']:
        nonpref['scaleable'] += 1
    elif 'No Jury' in row['complete_nonpref']:
        nonpref['control'] += 1
    elif 'Deliberating' in row['complete_nonpref']:
        nonpref['immersive'] += 1

    try:
        enforcement.append(float(row['scaleable_vote']))
        recommendation.append(float(row['immersive_vote']))
    except Exception, e:
        pass
    
    if row['immersive_difficulty'].strip() != '0':
        immersive['immersive_difficulty'].append(int(row['immersive_difficulty']))
    if row['immersive_time'].strip() != '0':
        immersive['immersive_time'].append(int(row['immersive_time']))
    if row['immersive_satisfaction'].strip() != '0':
        immersive['immersive_satisfaction'].append(int(row['immersive_satisfaction']))
    if row['immersive0'].strip() != '0':
        immersive['immersive0'].append(int(row['immersive0']))
    if row['immersive1'].strip() != '0':
        immersive['immersive1'].append(int(row['immersive1']))
    if row['immersive3'].strip() != '0':
        immersive['immersive2'].append(int(row['immersive2']))
    if row['immersive3'].strip() != '0':
        immersive['immersive3'].append(int(row['immersive3']))
    if row['immersive4'].strip() != '0':
        immersive['immersive4'].append(int(row['immersive4']))
    if row['immersive5'].strip() != '0':
        immersive['immersive5'].append(int(row['immersive5']))

    if row['scaleable_difficulty'].strip() != '0':
        scaleable['scaleable_difficulty'].append(int(row['scaleable_difficulty']))
    if row['scaleable_time'].strip() != '0':
        scaleable['scaleable_time'].append(int(row['scaleable_time']))
    if row['scaleable_satisfaction'].strip() != '0':
        scaleable['scaleable_satisfaction'].append(int(row['scaleable_satisfaction']))
    if row['scaleable0'].strip() != '0':
        scaleable['scaleable0'].append(int(row['scaleable0']))
    if row['scaleable1'].strip() != '0':
        scaleable['scaleable1'].append(int(row['scaleable1']))
    if row['scaleable2'].strip() != '0':
        scaleable['scaleable2'].append(int(row['scaleable2']))
    if row['scaleable3'].strip() != '0':
        scaleable['scaleable3'].append(int(row['scaleable3']))
    if row['scaleable4'].strip() != '0':
        scaleable['scaleable4'].append(int(row['scaleable4']))
    if row['scaleable5'].strip() != '0':
        scaleable['scaleable5'].append(int(row['scaleable5']))
    
    if row['control_difficulty'].strip() != '0':
        control['control_difficulty'].append(int(row['control_difficulty']))
    if row['control_time'].strip() != '0':
        control['control_time'].append(int(row['control_time']))
    if row['control_satisfaction'].strip() != '0':
        control['control_satisfaction'].append(int(row['control_satisfaction']))
    if row['control0'].strip() != '0':
        control['control0'].append(int(row['control0']))
    if row['control1'].strip() != '0':
        control['control1'].append(int(row['control1']))
    if row['control2'].strip() != '0':
        control['control2'].append(int(row['control2']))
    if row['control3'].strip() != '0':
        control['control3'].append(int(row['control3']))
    if row['control4'].strip() != '0':
        control['control4'].append(int(row['control4']))
    if row['control5'].strip() != '0':
        control['control5'].append(int(row['control5']))
    
#     f.write()

print len(users)

import scipy.stats

print scipy.stats.ttest_ind(enforcement, recommendation)

import numpy as np

N = 3

im_mean = []
im_std = []
 
sc_mean = []
sc_std = []
 
ct_mean = []
ct_std = []
 
# 
for c in immersive:
    immersive[c] = filter(lambda a: a != 0, immersive[c])

for c in scaleable:
    scaleable[c] = filter(lambda a: a != 0, scaleable[c])

for c in control:
    control[c] = filter(lambda a: a != 0, control[c])

c = []
s = []
i = []
 
for x in sorted(immersive)[6:]:
    print immersive[x]
    print len(immersive[x])
    im_mean.append(np.mean(immersive[x]))
    im_std.append(np.std(immersive[x])/2.0)
    i.append(immersive[x])
     
for x in sorted(scaleable)[6:]:
    print scaleable[x]
    print len(scaleable[x])
    sc_mean.append(np.mean(scaleable[x]))
    sc_std.append(np.std(scaleable[x])/2.0)
    s.append(scaleable[x])
     
for x in sorted(control)[6:]:
    print control[x]
    print len(control[x])
    ct_mean.append(np.mean(control[x]))
    ct_std.append(np.std(control[x])/2.0)
    c.append(control[x])


import matplotlib.pyplot as plt



def set_box_color(bp, color, fill):
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['caps'], color='black')
    plt.setp(bp['medians'], color='red')
    
    for patch in bp['boxes']:
        patch.set(facecolor=fill)       


plt.figure(figsize=(7,4))



bpl = plt.boxplot(c, positions=np.array(xrange(len(c)))*0.8+0.20, sym='', widths=0.15, vert=False, patch_artist=True)
bpr = plt.boxplot(s, positions=np.array(xrange(len(s)))*0.8+0.0, sym='', widths=0.15, vert=False, patch_artist=True)
bpt = plt.boxplot(i, positions=np.array(xrange(len(i)))*0.8-0.20, sym='', widths=0.15, vert=False, patch_artist=True)
set_box_color(bpl, 'orange', 'orange') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#af8dc3', '#af8dc3')
set_box_color(bpt, '#91bfdb', '#91bfdb')
 
 
# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='orange', label='Control')
plt.plot([], c='#af8dc3', label='Scaleable')
plt.plot([], c='#91bfdb', label='Immersive')
plt.legend()

ticks = ['Did you have\nany difficulties\nmaking a\ndecision for\nthis case?', 
                    'How satisfied\nare you with\nthe decision?', 
                    'Did you feel\n any time\nconstraints\nwith this\nprocess?']

plt.yticks([0,0.8,1.6], ticks)
plt.ylim(-0.4, 2.0)
plt.xlim(0.5, 5.5)
plt.tick_params(labelsize=8)
plt.tight_layout()
plt.savefig("foo.pdf", bbox_inches='tight')






c = []
s = []
i = []
 
for x in sorted(immersive)[:6]:
    print immersive[x]
    print len(immersive[x])
    im_mean.append(np.mean(immersive[x]))
    im_std.append(np.std(immersive[x])/2.0)
    i.append(immersive[x])
     
for x in sorted(scaleable)[:6]:
    print scaleable[x]
    print len(scaleable[x])
    sc_mean.append(np.mean(scaleable[x]))
    sc_std.append(np.std(scaleable[x])/2.0)
    s.append(scaleable[x])
     
for x in sorted(control)[:6]:
    print control[x]
    print len(control[x])
    ct_mean.append(np.mean(control[x]))
    ct_std.append(np.std(control[x])/2.0)
    c.append(control[x])


import matplotlib.pyplot as plt



def set_box_color(bp, color, fill):
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='#BEBEBE')
    plt.setp(bp['caps'], color='#BEBEBE')
    plt.setp(bp['medians'], color='red')
    
    for patch in bp['boxes']:
        patch.set(facecolor=fill)       


plt.figure(figsize=(8,5))


plt.plot([], c='orange', label='Control')
plt.plot([], c='#af8dc3', label='Scaleable')
plt.plot([], c='#91bfdb', label='Immersive')
l = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


bpl = plt.boxplot(c, positions=np.array(xrange(len(c)))*1.2+0.30, sym='', widths=0.2, vert=False, patch_artist=True)
bpr = plt.boxplot(s, positions=np.array(xrange(len(s)))*1.2+0.0, sym='', widths=0.2, vert=False, patch_artist=True)
bpt = plt.boxplot(i, positions=np.array(xrange(len(i)))*1.2-0.30, sym='', widths=0.2, vert=False, patch_artist=True)
set_box_color(bpl, 'orange', 'orange') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#af8dc3', '#af8dc3')
set_box_color(bpt, '#91bfdb', '#91bfdb')
 
 


ticks = ['This process is\nan effective way\nto protect users\nfrom unwanted or\ntoxic content.',
         'This process\ncares about my\npreferences.',
         'This process\nis fair.',
         'This process\nvalues individual\nvoices equally.',
         'This process\nimproves my trust\nin how content\nmoderation\ndecisions are made.',
         'This process feels\nlike a legitimate\nexercise of the social\nmedia platform\'s power.']


plt.yticks([0,1.2,2.4,3.6,4.8,6,7.2], ticks)
plt.ylim(-0.8, 6.8)
plt.xlim(0.5, 5.5)
plt.tick_params(labelsize=7)
plt.tight_layout()
plt.savefig("foo2.pdf", bbox_inches='tight')




N = 2
# plot
 
import matplotlib.pyplot as plt
  
fig, ax = plt.subplots()
  
ind = np.arange(N)    # the x locations for the groups
width = 0.25         # the width of the bars
p1 = ax.bar(ind, [pref['control'],nonpref['control']], width-0.03, color='orange',edgecolor='black')
p2 = ax.bar(ind + width, [pref['scaleable'],nonpref['scaleable']], width-0.03,
            color='#af8dc3',edgecolor='black')
p3 = ax.bar(ind + width+width, [pref['immersive'],nonpref['immersive']], width-0.03,
            color='#91bfdb',edgecolor='black')
  
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels((
#                     'protect', 'preferences', 'fair', 'equal voices', 'trust', 'legitimate', 
                    'Most Preferable',
                    'Least Preferable'))
  
ax.tick_params(labelsize=9)
ax.legend((p1[0], p2[0], p3[0]), ('Control', 'Scaleable', 'Immersive'))
# ax.yaxis.set_units(inch)
ax.autoscale_view()
 
plt.ylim(0, 60)
  
plt.savefig("foo3.pdf", bbox_inches='tight')



