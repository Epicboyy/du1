from duckpy import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from thrift import transport, protocol, server
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime, timedelta, date
from random import randint
from multiprocessing import Pool, Process
from io import StringIO
import selenium.webdriver as webdriver
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as pesan
import time, random, sys, pafy, json, null, codecs, html5lib ,shutil ,threading, glob, re, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
loop = asyncio.get_event_loop()
#======================================================================================
botStart = time.time()
#======================================================================================
fluk = LINE("yelqbxg@nextemail.net","iydgiot8iy")
fluk.log("Auth Token : " + str(fluk.authToken))
Poll = OEPoll(fluk)
Profile = fluk.getProfile()
Mid = fluk.getProfile().mid
bot = [Mid]
oepoll = OEPoll(fluk)
Family=["ud6ddda058a443da152d03a1030ebf14b",Mid]
admin=['ud6ddda058a443da152d03a1030ebf14b',Mid]
wblacklist = []
protectjoin = []
protectinvite = []
kcn = {"autojoin": False,"Members":10,}
#====================================================================================------------------------------------------------------
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        fluk.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
tagall2 = {
    "Api": True,
    "detectMention": True,
    "tag1": True,
    "autotag":"พิม.. ตั้งแทค: \n และใสข้อความที่จะตั้งครับ",
    "server": "VPS",
}
spduck = {
    "autowelcome":"ควยคับควย",
    "welcome": False,
    "autoleave":"ไปตายรึไอสัสสส",
    "leave": False,
}
du1 = {
    "autoJoin": True,
    'autoCancel':{"on":True,"members":10},	
    "wblacklist": False,
    "wblack": False,
    "winvite": False,
    "no": False,
    "leaveRoom": False,
    "dblacklist": False,
    "commentBlack":{},
    "dblack": False,
    "blacklist":{},
    "autoAdd": False,
    "autoJoinTicket": False,
    "autoBlock": False,
    "autoJoin": True,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "Nk": False,
    "Api": False,
    "Aip": False,
    "autoLeave": True,
    "kick":"AUTO NK BY PHU",
    "bye":"AUTO LV BY PHU", 
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ของผู้สร้าง",
    "Post":"ไม่ออกความเห็น@",
    "addPesan": "🙏สวัสดีครับ🙏เพื่อนใหม่\n👉สนใจทำเซลบอท แก้ไฟลเซล เพิ่มไฟลเซล สอนทำเซล กด1\n👉สนใจทำปก ทำดิส กด2\n👉สนใจสั่งตั๋วสิริ ลงบอทสิริ บอทapi กด3\n👉สนใจเช่าเซิฟ Vps กด4\n👉สนใจสั่งซื้อสติ๊กเกอร์ ทีมไลน์ กด5\n👉แอดมาเก็บคท กด6\n👉แอดแล้วไม่พูดไม่ทัก กดบล็อค\n👉แต่ถ้าทักแล้วไม่ตอบ. หรือตอบช้า โทรมาเบอร์นี้เลยคับ 061 631 0513 @!",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " ว่าไง? ที่รัก􀄃􀈻",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "52002736",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "leaveSticker": {
                "STKID": "51626494",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "51626530",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "readerSticker": {
                "STKID": "13188540",
                "STKPKGID": "1327110",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "33158349",
                "STKPKGID": "10788",
                "STKVER": "1"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "22832841",
                "STKPKGID": "1705396",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    }
}	  
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
    "autoBlock": False,
}
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
settings = {
    "restartPoint": "cc5706614d126a6d8c8699e9d96ce940e",
    "join": False,
    "userAgent": [
      "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
      "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
      "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
      "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
      "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
      "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
      "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
      "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
],
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
contact = fluk.getProfile()
backup = fluk.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
TEXT = {"tx":{},"txx":{}}
start_runtime = datetime.now()
#----------------------------------------------------------------------------------------------------
def sendTemplate(to,data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = fluk.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def flex(to,flex):
    data={"type": "flex","altText": str(flex),"contents": { "type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "{}".format(flex)}]}}}
    sendTemplate(to,data)         
def footer(to,text):
    data= {"type": "text","text": str(text),"sentBy": {"label": fluk.getProfile().displayName,"iconUrl": "https://obs.line-scdn.net/" + fluk.getContact(Mid).pictureStatus,"linkUrl": "line://ti/p/~fluk001122"}}
    sendTemplate(to,data)         

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def Rapid1Say(mtosay):
    fluk.sendText(Rapid1To,mtosay)
def duc(to,duc):
    data={"type": "flex","altText": str(duc),"contents": { "type": "bubble","styles": {"header": {"backgroundColor": "#FFFFCC"}},"header": {"type": "box","layout": "vertical","contents": [{"type": "text","size": 'sm',"align": "center","weight": "bold","color": "#000000","text": "💖   "+"{}".format(duc)+"   💖"}]}}}
    sendTemplate(to,data)                 
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + fluk.profile.userid
                        fluk.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+fluk.getContact(Mid).pictureStatus, fluk.getContact(Mid).displayName)
                    except Exception as error:
                        logError(error)    
def logError(text):
    fluk.log("[ ข้อผิดพลาด ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       fluk.sendMessage(msg)
    except Exception as error:
       print(error)  
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMessageWithMention(to, Mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(Mid)+'}'
        text_ = '@x '
        fluk.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)              
#----------------------------------------------------------------------------------------------------
def lineBot(op):
  try:
        timeis = time.localtime()
        a = time.strftime('%H:%M:%S', timeis)
        if op.type == 0:
            return       

#=====================================================================
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            if msg.toType == 0:
               if sender != fluk.profile.mid:
                  to = sender
               else:
                  to = receiver
            else:
              to = receiver
            if msg.contentType == 0:
               if text is None:
                  return    
#----------------------------------------------------------------------------------------------------  
               elif text.lower() == 'คทเรา':
                    fluk.sendReplyMessage(msg.id,to,text=None, contentMetadata={'mid': Mid}, contentType=13)       

               elif msg.text in ["/เปิดแสกน"]:
                   try:
                       del RfuCctv['point'][msg.to]
                       del RfuCctv['sidermem'][msg.to]
                       del RfuCctv['cyduk'][msg.to]
                   except:
                       pass
                   RfuCctv['point'][msg.to] = msg.id
                   RfuCctv['sidermem'][msg.to] = ""
                   RfuCctv['cyduk'][msg.to]=True
                   fluk.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")
               elif msg.text in ["/ปิดแสกน"]:
                   if msg.to in RfuCctv['point']:
                       RfuCctv['cyduk'][msg.to]=False
                       fluk.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                   else:
                       fluk.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")
                    
#----------------------------------------------------------------------------------------------------  
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = fluk.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰"
                            pref=['จ๊ะเอ๋','รู้นะว่าแอบอยู่','เล่นซ่อนแอบกันเหรอ','คิดว่าเป็นนินจารึไง','ว่าไง','อ่านอย่างเดียวเลยนะ','ออกมาคุยหน่อย','ออกมาเดี๋ยวนี้']
                            sendMessageWithMention(op.param1, op.param2)
                            duc(op.param1,str(random.choice(pref)))
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = fluk.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 1:
                            	duc(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print (" [ PHU SELF BOT]  ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
  except Exception as error:
    logError(error)
#----------------------------------------------------------------------------------------------------          
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
#----------------------------------------------------------------------------------------------------          
