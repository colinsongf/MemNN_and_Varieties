# encoding:utf-8
'''
Created on 2015-11-18

@author: dell
'''

import sys
import ConfigParser

reload(sys)
sys.setdefaultencoding("utf8")

import matlab.engine
import jieba

jieba.initialize()
from TimeRecognition import *

regexFilePath = '/home/shin/DeepLearning/MemoryNetwork/QA/Interface/date.regex'

TimeR = TimeRecognition(regexFilePath)

# different working space console=False / eclipse=True
workSpace_working = False

# get Config
cf = ConfigParser.ConfigParser()
cf.read("FieldDialog.conf")
MatlabPath = cf.get('PathConfig', 'MatlabPath')
StoryPath = cf.get('PathConfig', 'StoryPath')
ResultPath = cf.get('PathConfig', 'ResultPath')
ErrorPath = cf.get('PathConfig', 'ErrorPath')
Field = cf.get('OtherConfig', 'Field')
CurrentSlotString = cf.get('PropertyConfig', '%sSlot' % (Field))
MachineName = cf.get('OtherConfig', 'MachineName')
UserName = cf.get('OtherConfig', 'UserName')

ErrorPath = '%s_%s' % (ErrorPath, Field)

# get FieldSlot
Slot = []
for value in CurrentSlotString.split(','):
    Slot.append(value)
CurrentSlot = set(Slot)

# read regex rules
regexFilePath = 'date.regex'
regexFid = open(regexFilePath, 'r')
regexRules = {}
for line in regexFid.readlines():
    [rules, tag] = line.strip().split('\t')
    regexRules[rules] = tag

# start Matlab Engine
eng = matlab.engine.start_matlab()
eng.eval('cd %s;' % (MatlabPath), nargout=0)

# read machine request
requestTemplatePath = '/home/shin/DeepLearning/MemoryNetwork/QA/Interface/OnlineTest/RequestTemplate/%sRequestTemplate.txt' % (Field)


def readTemplate(requestTemplatePath):
    requestFid = open(requestTemplatePath, 'r')
    lines = requestFid.readlines()
    queryDict = {}
    for line in lines:
        [tag, query] = line.strip().split('=')

        queryDict[tag] = query

    return queryDict


queryDict = readTemplate(requestTemplatePath)


def getQueryType(TicketSlot, SlotValueDict):
    EmptySlot = TicketSlot - set(SlotValueDict.keys())
    return 0 if len(EmptySlot) == 0 else list(EmptySlot)


def saveStory(StoryPath, storyList, TicketSlot, UserFirstResponse, writeMode='w'):
    StoryFid = open(StoryPath, '%s' % (writeMode))
    for i, sentence in enumerate(storyList):
        # print sentence
        StoryFid.write('%d %s\n' % (i + 1, sentence))
    queryTypes = getQueryType(TicketSlot, SlotValueDict)

    if UserFirstResponse:
        for queryType in queryTypes:
            StoryFid.write("%d %s\t%s\t%d\n" % (len(storyList) + 1, queryType + ' ?', 'nil', len(storyList)))
        UserFirstResponse = False
    else:
        StoryFid.write("%d %s\t%s\t%d\n" % (len(storyList) + 1, queryTypes[0] + ' ?', 'nil', len(storyList)))


def copyStory(StoryPath, ErrorPath):
    srcFid = open(StoryPath, 'r')
    dstFid = open(ErrorPath, 'a')
    for line in srcFid.readlines():
        dstFid.write(line)
    srcFid.close()
    dstFid.close()
    print 'Save Error Success!'


def AllSlotFilled(Slot, SlotDict):
    EmptySlot = Slot - set(SlotDict.keys())
    return 1 if len(EmptySlot) == 0 else 0


# start interface
DialogCounter = 1
while 1:
    FinishFlag = 0
    storyList = []
    UserFirstResponse = True

    SlotValueDict = {}
    print('\n\n\n\n\n\n\n\n--------------------Start Dialog %d----------------------------------') % (DialogCounter)
    DialogCounter += 1

    greeting = "%s:%s" % (MachineName, queryDict['greeting'])
    greeting = greeting if workSpace_working else greeting.decode('utf-8').encode('utf-8')
    print '%s\n' % (greeting)
    storyList.append(' '.join(jieba.cut(greeting[len(MachineName) + 1:])))

    while FinishFlag == 0:
        input_a = raw_input('%s: ' % (UserName))
        input_a = str(input_a)
        if input_a.lower() == 'save':
            copyStory(StoryPath, ErrorPath)
        else:
            UserInput = ' '.join(jieba.cut(input_a))
            UserInput = TimeR.process(UserInput)

            storyList.append(UserInput)
            # print storyList
            saveStory(StoryPath, storyList, CurrentSlot, UserFirstResponse)
            UserFirstResponse = False

            # execute matlab
            #eng.eval('OnlineTest_shin(\'%s\')' % (Field), nargout=0)
            eng.eval("OnlineTest_shin('hhh',6)")

            # get result
            ResultFid = open(ResultPath, 'r')
            lines = ResultFid.readlines()
            for line in lines:
                [tag, result] = line.strip().split('=')
                if tag in CurrentSlot and result != 'nil':
                    SlotValueDict[tag] = result
            currentStatment = []
            for k, v in SlotValueDict.iteritems():
                currentStatment += '%s=%s,' % (k, v.decode('utf-8').encode('utf8'))
            print ('                                    SlotStatus---(%s)') % (''.join(currentStatment))

            # judeg Ticket get all slot info
            if AllSlotFilled(CurrentSlot, SlotValueDict):
                FinishFlag = 1
                FinishGreeting = ('%s' % (queryDict['end']))
                FinishGreeting = FinishGreeting if workSpace_working else FinishGreeting.decode('utf-8').encode('gbk')
                print '%s:%s\n' % (MachineName, FinishGreeting)
                print 'Does the Response Right(y/n)'
                input_a = str(raw_input(' '))
                if input_a.lower() == 'n':  copyStory(StoryPath, ErrorPath)

            # new request for slot info
            queryType = getQueryType(CurrentSlot, SlotValueDict)
            if queryType > 0:
                query = queryDict[queryType[0]].decode('utf-8').encode('utf8')
                print '%s:%s\n' % (MachineName, query)
                storyList.append('%s' % (' '.join(jieba.cut(query))))
'''
1 您好 ， 很 高兴 为您服务
2 你好 ， 小美女 。
3 请问 您 要 订 几张 机票
4 我要 八张 机票 。
5 请问 您 要 订 几张 机票
6 从 石家庄 到 昆明 的 机票 。
7 请问 您 要 订 几张 机票
8 我 的 名字 是 周杰伦 。
9 count ?	nil	8
10 name ?	nil	8
11 destination ?	nil	8
12 departure ?	nil	8
13 idnumber ?	nil	8
14 time ?	nil	8
'''