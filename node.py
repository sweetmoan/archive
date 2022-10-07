import serial , time , pyautogui,requests
from colorama import Fore ,init , Style
init(autoreset=True)
colr_grn=Style.BRIGHT+Fore.GREEN
colr_red=Style.BRIGHT+Fore.RED

def getcom_set():
    cprt=input('Com port:')
    try:
        getcom_set.ser = serial.Serial(f'COM{cprt}',9600)
        print(colr_grn+f'COM{cprt} connected')
    except:
        print(colr_red+'hardware not found')
        return

def jumper():
    getcom_set()
    print('running..')
    while True:
        data = getcom_set.ser.read()
        if data:
            #getcom_set.ser.flushInput()
            print(data)
            if data=='a_j':
                #pyautogui.hotkey('ctrl', 'win','right')
                print(colr_grn+'window changed')
            elif data=='b_u':
                
                
                
            else:
                pass

def nadlier():
    pass

def telegram_bot_sendtext(bot_message):
    bot_token = '5494265803:AAGXS8wjfgVcckIGexQ_lhdQtqzV1S-em0o'
    bot_chatID = '5448992299'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='+bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


#telegram_bot_sendtext('testing message')




def serialtest():
    cprt=input('Com port:')
    try:
        ser = serial.Serial(f'COM{cprt}',9600)
        print(colr_grn+f'COM{prt} connected')
    except:
        print(colr_red+'hardware not found')
        
    print('opt{q} to quit')
    while True:
        i = input("Enter Input: ").strip()
        
        if i == "q":
            print('quiting..')
            break
        
        ser.write(i.encode())
        time.sleep(0.5)
        print(ser.readline().decode('ascii'))
    ser.close()
    
menu=True
while menu:

    print('''
opt[s] for serial test
[c] jumper
[w] nadlier
''')

    main=input('>> ')
    if main == 's':
        serialtest()
    elif main == 'c':
        jumper()
    elif main == 'w':
        nadlier()
    else:
        print('invalid input')
        input()

