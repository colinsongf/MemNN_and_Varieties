# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

namelist_answer=[]
'''
namelist_answer.append('[slot_name]。')
namelist_answer.append('叫[slot_name]。')
namelist_answer.append('姓名是[slot_name]。')
namelist_answer.append('我是[slot_name]。')
namelist_answer.append('您好，我叫[slot_name]。')
namelist_answer.append('[slot_name]')
namelist_answer.append('我的名字是[slot_name]。')
namelist_answer.append('我大名唤作[slot_name]。')
namelist_answer.append('哦，我的名字就是[slot_name]啊。')
namelist_answer.append('名叫[slot_name]。')
namelist_answer.append('叫[slot_name]。')
namelist_answer.append('没问题，我叫[slot_name]。')
namelist_answer.append('好的，名字是[slot_name]。')
namelist_answer.append('我的全名就是[slot_name]。')
namelist_answer.append('姓名是[slot_name]。')
namelist_answer.append('[slot_name]是我的名字。')
namelist_answer.append('我名叫[slot_name]。')
namelist_answer.append('我是[slot_name]啊。')
'''
namelist_answer.append('周杰伦。')
namelist_answer.append('叫周杰伦。')
namelist_answer.append('姓名是周杰伦。')
namelist_answer.append('我是周杰伦。')
namelist_answer.append('您好，我叫周杰伦。')
namelist_answer.append('周杰伦')
namelist_answer.append('我的名字是周杰伦。')
namelist_answer.append('我大名唤作周杰伦。')
namelist_answer.append('哦，我的名字就是周杰伦啊。')
namelist_answer.append('名叫周杰伦。')
namelist_answer.append('叫周杰伦。')
namelist_answer.append('没问题，我叫周杰伦。')
namelist_answer.append('好的，名字是周杰伦。')
namelist_answer.append('我的全名就是周杰伦。')
namelist_answer.append('姓名是周杰伦。')
namelist_answer.append('周杰伦是我的名字。')
namelist_answer.append('我名叫周杰伦。')
namelist_answer.append('我是周杰伦啊。')

namelist_answer_cut=[]
for ans in namelist_answer:
    w_sent=''
    sent=jieba._lcut(ans)
    for word in (sent):
        w_sent +=' '
        w_sent +=word
    w_sent += '\n'
    w_sent=w_sent.replace('周杰伦'.decode('utf8'),'[slot_name]')
    namelist_answer_cut.append(w_sent)
pass