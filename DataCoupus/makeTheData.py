# -*- coding: utf8 -*-
__author__ = 'shin'
import re
import jieba
import random
import datetime
from list_document.namelist_question import namelist_question_cut
from list_document.namelist_answer import namelist_answer_cut
from list_document.countlist_question import countlist_question_cut
from list_document.countlist_answer import countlist_answer_cut
from list_document.departurelist_question import departurelist_question_cut
from list_document.departurelist_answer import departurelist_answer_cut
from list_document.destinationlist_question import destinationlist_question_cut
from list_document.destinationlist_answer import destinationlist_answer_cut
from list_document.timelist_question import timelist_question_cut
from list_document.timelist_answer import timelist_answer_cut
from list_document.idnumberlist_question import idnumberlist_question_cut
from list_document.idnumberlist_answer import idnumberlist_answer_cut
from list_document.phonelist_question import phonelist_question_cut
from list_document.phonelist_answer import phonelist_answer_cut



print 'name question:%d'%len(namelist_question_cut)
print 'name answer:%d\n'%len(namelist_answer_cut)
print 'count question:%d'%len(countlist_question_cut)
print 'count answer:%d\n'%len(countlist_answer_cut)
print 'departure question:%d'%len(departurelist_question_cut)
print 'departure answer:%d\n'%len(departurelist_answer_cut)
print 'destination question:%d'%len(destinationlist_question_cut)
print 'destination answer:%d\n'%len(destinationlist_answer_cut)
print 'idnumber question:%d'%len(idnumberlist_question_cut)
print 'idnumber answer:%d\n'%len(idnumberlist_answer_cut)
print 'time question:%d'%len(timelist_question_cut)
print 'time answer:%d\n'%len(timelist_answer_cut)
print 'phone question:%d'%len(phonelist_question_cut)
print 'phone answer:%d\n'%len(phonelist_answer_cut)

storyNumber=1000
fw=open('/home/shin/DeepLearning/MemoryNetwork/MemNN/DataCoupus/ticket_shin_test.txt','w')

familyName=['号','王','李','赵','周','吴','顾','郑','何','万','黄','周','吴','徐','孙','胡','朱','高',
           '林','何','郭','马','罗','梁','宋','谢','韩','唐','冯','于','董','萧','程','曹','袁','邓',
           '许','欧阳','太史','端木','上官','司马','东方','独孤','南宫','万俟','闻人','夏侯','诸葛','尉迟','公羊']

lastName=['舒敏','安邦','安福','安歌','安国','刚捷','刚毅','高昂','高岑','高畅','高超','高驰','高达','浩言','皓轩','和蔼','和安','和璧','和昶','和畅',
         '天','景','同','景曜','靖','琪','君昊','君浩','俊艾','俊拔','俊弼', '才','风','歌','光','和','平', '和洽','和惬','和顺','和硕','和颂',
         '佳','可嘉','可','心','琨瑶','琨瑜','兰','芳','兰蕙','梦','娜','若','英','月','兰泽','芝','岚翠','风','岚岚','蓝','尹']


countDict=['一张','二张','两张','三张','四张','五张','六张','七张','八张','九张','十张']

locationDict=['纽约','伦敦','东京','巴黎','香港','新加坡','悉尼','米兰','上海','北京','马德里','莫斯科','首尔','曼谷','多伦多','布鲁塞尔','芝加哥','吉隆坡','孟买',
              '华沙','圣保罗','苏黎世','阿姆斯特丹','墨西哥城','雅加达','都柏林','曼谷','台北','伊斯坦布尔','里斯本','罗马','法兰克福','斯德哥尔摩布拉格','维也纳',
              '布达佩斯','雅典','加拉加斯','洛杉矶','奥克兰','圣地亚哥','布宜诺斯艾利斯','华盛顿','墨尔本','约翰内斯堡','亚特兰大','巴塞罗那','旧金山','马尼拉',
              '波哥大á','特拉维夫','新德里','迪拜','布加勒斯特','奥斯陆','柏林','赫尔辛基','日内瓦','利雅得','哥本哈根','汉堡','开罗','卢森堡','班加罗尔',
              '达拉斯','科威特城','波士顿','慕尼黑','迈阿密','利马','基辅','休斯顿','广州','贝鲁特','卡拉奇','索菲亚','蒙得维的亚','里约热内卢','胡志明市',
              '蒙特利尔','内罗毕','巴拿马城','金奈','布里斯班','卡萨布兰卡','丹佛','基多','斯图加特','温哥华','麦纳麦','危地马拉市','开普敦',
              '圣何塞','西雅图','深圳','珀斯','加尔各答','安特卫普','费城','鹿特丹','拉各斯','波特兰','底特律','曼彻斯特','惠灵顿','里加',
              '爱丁堡','圣彼得堡.','圣迭戈','伊斯兰堡','伯明翰','多哈','阿拉木图','卡尔加里']

#dayDict=['一号','二号','两号','三号','四号','五号','六号','七号','八号','九号','十号','十一''''''''''''''''''''''''''''''''''''''''''''''''']

def namePart(f,ind):

    fullname=random.choice(familyName)+random.choice(lastName)

    #f.write('%d%s'%(ind+1,random.choice(namelist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,namelist_question_cut[0].encode('utf8')))
    ans_sent=random.choice(namelist_answer_cut).replace('[slot_name]',fullname.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\tnil\t%d\n'%(ind+3,ind+2))
    f.write('%d name ?\t%s\t%d\n'%(ind+4,fullname,ind+2))
    f.write('%d destination ?\tnil\t%d\n'%(ind+5,ind+2))
    f.write('%d departure ?\tnil\t%d\n'%(ind+6,ind+2))
    f.write('%d idnumber ?\tnil\t%d\n'%(ind+7,ind+2))
    f.write('%d time ?\tnil\t%d\n'%(ind+8,ind+2))
    f.write('%d phone ?\tnil\t%d\n'%(ind+9,ind+2))

    ind=ind+9
    return f,ind

def countPart(f,ind):

    #f.write('%d%s'%(ind+1,random.choice(countlist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,countlist_question_cut[0].encode('utf8')))

    rand_or_rule=random.randint(0,1)#0的时候规则，1的时候随机
    if rand_or_rule:
        fullcount=str(random.randint(0,66666))+'张'
    else :
        fullcount=random.choice(countDict)
    ans_sent=random.choice(countlist_answer_cut).replace('[slot_count]',fullcount.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\t%s\t%d\n'%(ind+3,fullcount,ind+2))
    f.write('%d name ?\tnil\t%d\n'%(ind+4,ind+2))
    f.write('%d destination ?\tnil\t%d\n'%(ind+5,ind+2))
    f.write('%d departure ?\tnil\t%d\n'%(ind+6,ind+2))
    f.write('%d idnumber ?\tnil\t%d\n'%(ind+7,ind+2))
    f.write('%d time ?\tnil\t%d\n'%(ind+8,ind+2))
    f.write('%d phone ?\tnil\t%d\n'%(ind+9,ind+2))

    ind=ind+9
    return f,ind


def departurePart(f,ind):

    #f.write('%d%s'%(ind+1,random.choice(departurelist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,departurelist_question_cut[0].encode('utf8')))

    rand_or_rule=random.randint(0,1)#0的时候规则，1的时候随机
    if rand_or_rule:
        fulldeparture='地方代号-'+str(random.randint(0,66666))
    else :
        fulldeparture=random.choice(locationDict)
    ans_sent=random.choice(departurelist_answer_cut).replace('[slot_departure]',fulldeparture.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\tnil\t%d\n'%(ind+3,ind+2))
    f.write('%d name ?\tnil\t%d\n'%(ind+4,ind+2))
    f.write('%d destination ?\tnil\t%d\n'%(ind+5,ind+2))
    f.write('%d departure ?\t%s\t%d\n'%(ind+6,fulldeparture,ind+2))
    f.write('%d idnumber ?\tnil\t%d\n'%(ind+7,ind+2))
    f.write('%d time ?\tnil\t%d\n'%(ind+8,ind+2))
    f.write('%d phone ?\tnil\t%d\n'%(ind+9,ind+2))

    ind=ind+9
    return f,ind    


def destinationPart(f,ind):

    #f.write('%d%s'%(ind+1,random.choice(destinationlist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,destinationlist_question_cut[0].encode('utf8')))

    rand_or_rule=random.randint(0,1)#0的时候规则，1的时候随机
    if rand_or_rule:
        fulldestination='地方代号-'+str(random.randint(0,66666))
    else :
        fulldestination=random.choice(locationDict)
    ans_sent=random.choice(destinationlist_answer_cut).replace('[slot_destination]',fulldestination.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\tnil\t%d\n'%(ind+3,ind+2))
    f.write('%d name ?\tnil\t%d\n'%(ind+4,ind+2))
    f.write('%d destination ?\t%s\t%d\n'%(ind+5,fulldestination,ind+2))
    f.write('%d departure ?\tnil\t%d\n'%(ind+6,ind+2))
    f.write('%d idnumber ?\tnil\t%d\n'%(ind+7,ind+2))
    f.write('%d time ?\tnil\t%d\n'%(ind+8,ind+2))
    f.write('%d phone ?\tnil\t%d\n'%(ind+9,ind+2))

    ind=ind+9
    return f,ind


def timePart(f,ind):

    #f.write('%d%s'%(ind+1,random.choice(timelist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,timelist_question_cut[0].encode('utf8')))

    delta=datetime.timedelta(days=random.randint(0,100), seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=random.randint(0,24), weeks=0)
    timetime=datetime.datetime.now()+delta
    fulltime=timetime.strftime('%Y年%m月%d日%H点%M分')

    ans_sent=random.choice(timelist_answer_cut).replace('[slot_time]',fulltime.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\tnil\t%d\n'%(ind+3,ind+2))
    f.write('%d name ?\tnil\t%d\n'%(ind+4,ind+2))
    f.write('%d destination ?\tnil\t%d\n'%(ind+5,ind+2))
    f.write('%d departure ?\tnil\t%d\n'%(ind+6,ind+2))
    f.write('%d idnumber ?\tnil\t%d\n'%(ind+7,ind+2))
    f.write('%d time ?\t%s\t%d\n'%(ind+8,fulltime,ind+2))
    f.write('%d phone ?\tnil\t%d\n'%(ind+9,ind+2))

    ind=ind+9
    return f,ind

def idnumberPart(f,ind):

    #f.write('%d%s'%(ind+1,random.choice(idnumberlist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,idnumberlist_question_cut[0].encode('utf8')))
    
    fullidnumber=str(random.randint(1000000000000000,9999999999999999))
    ans_sent=random.choice(idnumberlist_answer_cut).replace('[slot_idnumber]',fullidnumber.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\tnil\t%d\n'%(ind+3,ind+2))
    f.write('%d name ?\tnil\t%d\n'%(ind+4,ind+2))
    f.write('%d destination ?\tnil\t%d\n'%(ind+5,ind+2))
    f.write('%d departure ?\tnil\t%d\n'%(ind+6,ind+2))
    f.write('%d idnumber ?\t%s\t%d\n'%(ind+7,fullidnumber,ind+2))
    f.write('%d time ?\tnil\t%d\n'%(ind+8,ind+2))
    f.write('%d phone ?\tnil\t%d\n'%(ind+9,ind+2))

    ind=ind+9
    return f,ind

def phonePart(f,ind):

    #f.write('%d%s'%(ind+1,random.choice(phonelist_question_cut).encode('utf8')))
    f.write('%d%s'%(ind+1,phonelist_question_cut[0].encode('utf8')))
    
    fullphone=str(random.randint(10000000000,19999999999))
    ans_sent=random.choice(phonelist_answer_cut).replace('[slot_phone]',fullphone.decode('utf8'))
    f.write('%d%s'%(ind+2,ans_sent.encode('utf8')))

    f.write('%d count ?\tnil\t%d\n'%(ind+3,ind+2))
    f.write('%d name ?\tnil\t%d\n'%(ind+4,ind+2))
    f.write('%d destination ?\tnil\t%d\n'%(ind+5,ind+2))
    f.write('%d departure ?\tnil\t%d\n'%(ind+6,ind+2))
    f.write('%d idnumber ?\tnil\t%d\n'%(ind+7,ind+2))
    f.write('%d time ?\tnil\t%d\n'%(ind+8,ind+2))
    f.write('%d phone ?\t%s\t%d\n'%(ind+9,fullphone,ind+2))

    ind=ind+9
    return f,ind

orderlist=[0,1,2,3,4,5,6]


for story_ind in range(storyNumber):
    random.shuffle(orderlist)
    line_ind=1
    '''---------------greeting--------------'''

    fw.write('%d 您好 ， 机票 预订 中心 ， 需要 我 为 你 做些 什么 ？\n'%(line_ind))
    line_ind+=1
    fw.write('%d 我 想 预订 机票 。\n'%line_ind)
    fw.write('%d count ?	nil	%d\n'%(line_ind+1,line_ind))
    fw.write('%d name ?	nil	%d\n'%(line_ind+2,line_ind))
    fw.write('%d destination ?	nil	%d\n'%(line_ind+3,line_ind))
    fw.write('%d departure ?	nil	%d\n'%(line_ind+4,line_ind))
    fw.write('%d idnumber ?	nil	%d\n'%(line_ind+5,line_ind))
    fw.write('%d time ?	nil	%d\n'%(line_ind+6,line_ind))
    fw.write('%d phone ?	nil	%d\n'%(line_ind+7,line_ind))

    line_ind=9



    '''---------------greeting--------------'''

    for i in orderlist:
        if i==0:
            fw,line_ind=namePart(fw,line_ind)
            continue
        if i==1:
            fw,line_ind=countPart(fw,line_ind)
            continue
        if i==2:
            fw,line_ind=departurePart(fw,line_ind)
            continue
        if i==3:
            fw,line_ind=destinationPart(fw,line_ind)
            continue
        if i==4:
            fw,line_ind=timePart(fw,line_ind)
            continue
        if i==5:
            fw,line_ind=idnumberPart(fw,line_ind)
            continue
        if i==6:
            fw,line_ind=phonePart(fw,line_ind)
            continue


    fw.write('%d 已经 为 您 预订 完毕 。\n'%(line_ind+1))
    line_ind+=1
    fw.write('%d 非常 谢谢 。\n'%line_ind)
    fw.write('%d count ?	nil	%d\n'%(line_ind+2,line_ind))
    fw.write('%d name ?	nil	%d\n'%(line_ind+3,line_ind))
    fw.write('%d destination ?	nil	%d\n'%(line_ind+4,line_ind))
    fw.write('%d departure ?	nil	%d\n'%(line_ind+5,line_ind))
    fw.write('%d idnumber ?	nil	%d\n'%(line_ind+6,line_ind))
    fw.write('%d time ?	nil	%d\n'%(line_ind+7,line_ind))
    fw.write('%d phone ?	nil	%d\n'%(line_ind+8,line_ind))




fw.close()






