from django.core.management.base import BaseCommand

import csv
from juries.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        file = open('results.csv','w')
        
        fieldnames = ['mturk', 'group_id', 'group_round1', 'group_round2', 'group_round3', 'case1', 'case2', 'case3', 'chat_username',
                      'age', 'gender','education','political','political_engagement','confidence','moral0','moral1','moral2','moral3','moral4','moral5',
                      'control_difficulty', 'control_time','control_satisfaction','control0','control1','control2','control3','control4','control5',
                      'scaleable_vote','scaleable_content_unlist','scaleable_content_delete','scaleable_content_report','scaleable_user_warn',
                      'scaleable_user_ban','scaleable_user_permaban','scaleable_justification','scaleable_difficulty','scaleable_time','scaleable_satisfaction',
                      'scaleable0','scaleable1','scaleable2','scaleable3','scaleable4','scaleable5','immersive_vote','immersive_content_unlist',
                      'immersive_content_delete','immersive_content_report','immersive_user_warn','immersive_user_ban','immersive_user_permaban',
                      'immersive_justification','immersive_difficulty','immersive_time','immersive_satisfaction','immersive_convo','immersive_trust',
                      'immersive0','immersive1','immersive2','immersive3','immersive4','immersive5','complete_pref','complete_prefwhy','complete_nonpref',
                      'complete_nonprefwhy','complete_participate0','complete_participate1','complete_participate2','complete_participate3',
                      'complete_participate4','complete_enf_rec','complete_enf_enf','complete_enf_why','complete3','complete_confidence',
                      'complete_familiarity','complete_comments','email', 'num_chat_messages','num_chat_words']
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        
        u = UserInfo.objects.all()
        
        for i in u:
            d = {}
            d['mturk'] = i.mturk_user.username
            d['group_id'] = i.groupinfo.id
            d['group_round1'] = i.groupinfo.round1
            d['group_round2'] = i.groupinfo.round2
            d['group_round3'] = i.groupinfo.round3
            d['case1'] = i.groupinfo.case1
            d['case2'] = i.groupinfo.case2
            d['case3'] = i.groupinfo.case3
            d['chat_username'] = i.chat_username
            d['age'] = i.age_range
            d['gender'] = i.gender
            d['education'] = i.education
            d['political'] = i.political
            d['political_engagement'] = i.political_engage
            d['confidence'] = i.confidence
            d['moral0'] = i.moral0
            d['moral1'] = i.moral1
            d['moral2'] = i.moral2
            d['moral3'] = i.moral3
            d['moral4'] = i.moral4
            d['moral5'] = i.moral5
            d['control_difficulty'] = i.control_difficulty
            d['control_time'] = i.control_time
            d['control_satisfaction'] = i.control_satisfaction
            d['control0'] = i.control0
            d['control1'] = i.control1
            d['control2'] = i.control2
            d['control3'] = i.control3
            d['control4'] = i.control4
            d['control5'] = i.control5
            d['scaleable_vote'] = i.scaleable_vote
            d['scaleable_content_unlist'] = i.scaleable_content_unlist
            d['scaleable_content_delete'] = i.scaleable_content_delete
            d['scaleable_content_report'] = i.scaleable_content_report
            d['scaleable_user_warn'] = i.scaleable_user_warn
            d['scaleable_user_ban'] = i.scaleable_user_ban
            d['scaleable_user_permaban'] = i.scaleable_user_permaban
            d['scaleable_justification'] = i.scaleable_justification
            d['scaleable_difficulty'] = i.scaleable_difficulty
            d['scaleable_time'] = i.scaleable_time
            d['scaleable_satisfaction'] = i.scaleable_satisfaction
            d['scaleable0'] = i.scaleable0
            d['scaleable1'] = i.scaleable1
            d['scaleable2'] = i.scaleable2
            d['scaleable3'] = i.scaleable3
            d['scaleable4'] = i.scaleable4
            d['scaleable5'] = i.scaleable5
            
            d['immersive_vote'] = i.immersive_vote
            d['immersive_content_unlist'] = i.immersive_content_unlist
            d['immersive_content_delete'] = i.immersive_content_delete
            d['immersive_content_report'] = i.immersive_content_report
            d['immersive_user_warn'] = i.immersive_user_warn
            d['immersive_user_ban'] = i.immersive_user_ban
            d['immersive_user_permaban'] = i.immersive_user_permaban
            d['immersive_justification'] = i.immersive_justification
            d['immersive_difficulty'] = i.immersive_difficulty
            d['immersive_time'] = i.immersive_time
            d['immersive_satisfaction'] = i.immersive_satisfaction
            d['immersive_convo'] = i.immersive_convo
            d['immersive_trust'] = i.immersive_trust
            d['immersive0'] = i.immersive0
            d['immersive1'] = i.immersive1
            d['immersive2'] = i.immersive2
            d['immersive3'] = i.immersive3
            d['immersive4'] = i.immersive4
            d['immersive5'] = i.immersive5
            
            d['complete_pref'] = i.complete_pref
            d['complete_prefwhy'] = i.complete_prefwhy
            d['complete_nonpref'] = i.complete_nonpref
            d['complete_nonprefwhy'] = i.complete_nonprefwhy
            
            d['complete_participate0'] = i.complete_participate0
            d['complete_participate1'] = i.complete_participate1
            d['complete_participate2'] = i.complete_participate2
            d['complete_participate3'] = i.complete_participate3
            d['complete_participate4'] = i.complete_participate4
            
            d['complete_enf_rec'] = i.complete_enf_rec
            d['complete_enf_enf'] = i.complete_enf_enf
            d['complete_enf_why'] = i.complete_enf_why
            d['complete3'] = i.complete3
            d['complete_confidence'] = i.complete_confidence
            d['complete_familiarity'] = i.complete_familiarity
            d['complete_comments'] = i.complete_comments
            d['email'] = i.email
            
            comments = ChatMessage.objects.filter(user=i, group=i.groupinfo)
            word_count = 0
            for c in comments:
                word_count += len(c.text.split())
            
            d['num_chat_messages'] = comments.count()
            d['num_chat_words'] = word_count
            
            writer.writerow(d)
            
          
        
        
        


























