import requests
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
