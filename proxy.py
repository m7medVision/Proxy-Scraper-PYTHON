import requests
from colorama import Fore
try:
    f=open('LIST.txt','a')
    proxyweb=requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text
    f.write(proxyweb+ '\n')
    f.close()
    print('DONE link 1')
    f=open('LIST.txt','a')
    proxyweb2=requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text
    f.write(proxyweb2+ '\n')
    f.close()
    print('DONE link 2')
    f=open('LIST.txt','a')
    proxyweb3=requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
    f.write(proxyweb2+ '\n')
    f.close()
    print('DONE link 3')
    f=open('LIST.txt','a')
    proxyweb3=requests.get("https://majhcc.pw/api/proxies.php").text
    f.write(proxyweb2+ '\n')
    f.close()
    print('DONE link 4')
except:
    print ("ERROR")


r = requests.Session()

def check(prox):
	link = 'http://instagram.com/'
	r.proxies = {
	'http':'http://{}'.format(prox),
	'https':'http://{}'.format(prox),
    'http' : 'socks5://{}'.format(prox),
    'http' : 'socks4://{}'.format(prox),
	}
	try:
		req = r.get(link,timeout=100)
		if req.status_code == 200:
			print(Fore.LIGHTGREEN_EX+"Proxy Work [{}]".format(prox))
			with open('working.txt','a') as wr:
				wr.write(prox+'\n')
		else:
				print(Fore.YELLOW +"blocked proxy [{}]".format(prox))
	except:
		print(Fore.LIGHTRED_EX+"Bad Proxy [{}]".format(prox))

proxies=open('LIST.txt', 'r').read().splitlines()
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(500)
results = pool.map(check, proxies)