import serial, pyautogui
ser = serial.Serial('com4',9600)
print('started')
while True:
    data = ser.read()
    if data:
        if data==b"l":
            pyautogui.hotkey('ctrl', 'win','right')
            print('window changed')
        else:
            pass

