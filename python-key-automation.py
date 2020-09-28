import winput
import time
import random
from datetime import datetime
import mouse
import keyboard

global userchoice
userchoice = 0

global sessionname
sessionname = 'Unknown-session'

global previoustimestamp
global firsttime
firsttime = 0


global status
status = False

global counter1
counter1 = 0

global counter2
counter2 = 0

global counter3
counter3 = 0

global counter4
counter4 = 0

global previousvk
previousvk = '0231231'


##mouuse is a bit inconsistent
##def mouse_callback( event ):
##
##    this line not in code#if str(event.action) == '513':
##        if event.action == winput.WM_LBUTTONDOWN:
##                now = datetime.now()
##                eventpos = str(event.position)
##                date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
##                print("LMB press at {}".format( eventpos ))
##                SendKeyPressData('LMB',eventpos,date_time)
##                print('')
##                hooknunhookmouse()
##
##
##        if event.action == winput.WM_RBUTTONDOWN:
##                now = datetime.now()
##                eventpos = str(event.position)
##                date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
##                print("RMB press at {}".format( eventpos ))
##                SendKeyPressData('RMB',eventpos,date_time)
##                print('')
##                hooknunhookmouse()



##def hooknunhookmouse():
##    winput.unhook_mouse()
##    winput.hook_mouse( mouse_callback )
##    #winput.wait_messages()



def keyboard_callback( event ):
    global counter3
    global counter4
    global previousvk

    if str(event.action) == '256' and event.vkCode != winput.VK_F1 and event.vkCode != winput.VK_F2 and event.vkCode != winput.VK_SHIFT and event.vkCode != winput.VK_TAB and event.vkCode != winput.VK_MENU and event.vkCode != winput.VK_CONTROL  and event.vkCode != winput.VK_CAPITAL:

        eventvk = str(event.vkCode)
        print(str(event.vkCode))
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        SendKeyPressData(str(event.vkCode),'',date_time)




    if event.vkCode == winput.VK_F1:
            if counter4 == 0:
                print('F1 was pressed the application will pause')
                counter4 = 1
                winput.unhook_mouse()
                winput.unhook_keyboard()
                input('To continue press the enter key..')
                #winput.hook_mouse( mouse_callback )
                winput.hook_keyboard( keyboard_callback )

        # enter message loop
                winput.wait_messages()


            elif counter4 == 1:
                  counter4 = 0

    #to stop keyshare press F2 Key
    if event.vkCode == winput.VK_F2 : # quit on pressing Numlock. make it later in a way that it can be switched back on
        print('F2 key was pressed. Pythonmation has stopped')
        winput.stop()




def SendKeyPressData(keyname,position,timestamp):
    #write in a log file
    global filename
    global previoustimestamp
    global firsttime
    global sessionname
    global firsttimezerostamp
    global d1

    #firsttimezerostamp = datetime.now()
    #firsttimezerostamp = firsttimezerostamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    #d1 = firsttimezerostamp.strptime(str(firsttimezerostamp), "%Y-%m-%d %H:%M:%S.%f")
    #d1 = datetime.strptime(previoustimestamp, "%Y-%m-%d %H:%M:%S.%f")



    if firsttime == 0:
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y, %Hh%Mm%Ss")

        filename = 'Pythonmation - ' + sessionname + ' - ' + date_time + '.txt'
        with open(filename,"w") as f:
            f.write(str(keyname) + ',' + position + ',' + timestamp + ',' + '0:00:00.00'  + ',' + '\n')
            firsttimezerostamp = datetime.now()
            #firsttimezerostamp = firsttimezerostamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            d1 = firsttimezerostamp.strptime(str(firsttimezerostamp), "%Y-%m-%d %H:%M:%S.%f")
            firsttime = 1
            print('0:00:00.00')
            print('')
            f.close()
        previoustimestamp = timestamp

    elif firsttime == 1:


        with open(filename,"a") as f:


            d2 = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")

            timediff = (d2 - d1)
            print(str(timediff))
            print('')
            timediff = str(timediff)
            f.write(str(keyname) + ',' + position + ',' + timestamp + ',' + timediff + ',' +'\n')
            f.close()
        previoustimestamp = timestamp







def Mousemovement():
    position = winput.get_mouse_pos()
    return [position[0],position[1]]



def GetInput():
    global userchoice
    global sessionname
    sessionname = 'Unknown-session'
    userchoice = 0
    print('Welcome to pythonmation. here you can automate you mouse and keyboard activity and replay them!')
    while(int(userchoice) == 0):
        print('To play a previous recording type 1. To make a new recording Type 2')
        userchoice = input('')
        userchoice = int(userchoice)
        if(userchoice != 1):
            if(userchoice != 2):
                userchoice = 0

    if userchoice == 1:
        return 1

    elif userchoice == 2:
        print('Type the session name')
        sessionname = input('')
        return 2





def countdown(seconds):

    if seconds == 10:
        secs = ['10','9','8','7','6','5','4','3','2','1','Replay started..']
        for i in secs:
            print(i)
            time.sleep(1)

    elif seconds == 5:
        secs = ['5','4','3','2','1','Replay started..']
        for i in secs:
            print(i)
            time.sleep(1)

    elif seconds == '5rec':
        secs = ['5','4','3','2','1','Recording started..']
        for i in secs:
            print(i)
            time.sleep(1)

    elif seconds == 3:
        secs = ['3','2','1','Replay started..']
        for i in secs:
            print(i)
            time.sleep(1)





def Replayrecording(recordingname,numberoftimes):
    global status
    global line
    line = ''


    for i in range(int(numberoftimes)):
        print('')
        print('Replay number ' + str(i + 1))
        print('')

        if i == 0:
            countdown(10)
        else:
            countdown(3)



        with open(recordingname,"r") as f:
                starttime = datetime.now()

                line = f.readline()
                print('')
                while line != '':
                    keyboard.press_and_release('shift')

                    linesplit = line.split(',')
                    if(('LMB' or 'RMB') in linesplit[0]):


                        if('0:00:00.00' in linesplit[4]):
                                print(linesplit[4])
                                print(linesplit[0])

                                tbposx = linesplit[1].split(',')
                                posx = tbposx[0][1:]
                                posy = linesplit[2][1:-1]

                                winput.set_mouse_pos(int(posx), int(posy))

                                mousebtn = ''
                                if 'LMB' in linesplit[0]:
                                    mouse.click(button='left')
                                if 'RMB' in linesplit[0]:
                                    mouse.click(button='right')


                                previoustime = datetime.now()
                                line = f.readline()


                        else:
                            currenttime = datetime.now()
                            while (str(currenttime - starttime)[0:8]) not in linesplit[4]:
                                    currenttime = datetime.now()
                                    #print('not exactly the same' + str(currenttime - previoustime))
                                #out of while loop


                            print(linesplit[4])
                            print(linesplit[0])

                            tbposx = linesplit[1].split(',')
                            posx = tbposx[0][1:]



                            posy = linesplit[2][1:-1]
                            winput.set_mouse_pos(int(posx), int(posy))



                            mousebtn = ''
                            if 'LMB' in linesplit[0]:
                                mousebtn = 'left'
                            elif 'RMB' in linesplit[0]:
                                mousebtn = 'right'

                            #winput.press_mouse_button(mousebtn)
                            mouse.click(button=mousebtn)


                            previoustime = datetime.now()
                            line = f.readline()

                    #not mouse click
                    else:
                         previoustime = datetime.now()
                            #currenttime = datetime.now()
                         if('0:00:00.00' in linesplit[3]):
                                print(linesplit[3])
                                print(linesplit[0])
                                winput.press_key(int(linesplit[0]))
                                previoustime = datetime.now()
                                line = f.readline()



                         else:
                                currenttime = datetime.now()
                                while (str(currenttime - starttime)[0:8]) not in linesplit[3]:
                                    currenttime = datetime.now()
                                    #print('not exactly the same' + str(currenttime - previoustime))




                                print(linesplit[3])
                                print(linesplit[0])
                                winput.press_key(int(linesplit[0]))
                                previoustime = datetime.now()
                                line = f.readline()


                f.close()
                endtime = datetime.now()
                #print(str(endtime-starttime))

def StartApp():
    try:
        thechoice = GetInput()

        if thechoice == 2:
            print('')
            countdown('5rec')
            print("Press F1 to pause. Press F2 to quit")

            # hook input
            ##winput.hook_mouse( mouse_callback )
            winput.hook_keyboard( keyboard_callback )

            # enter message loop
            winput.wait_messages()

            # remove input hook
            ##winput.unhook_mouse()
            winput.unhook_keyboard()

        elif thechoice == 1:
            print('Enter the full name of the recording file to replay, or choose one from the list below by typing the number (example Num0)')
            linecounter = 0
            with open("replayhistory.txt","r") as f:
                for line in f:
                    if line != '':
                        print('Num' + str(linecounter) + ': ' +  line[:-1])
                        linecounter = int(linecounter)
                        linecounter = linecounter + 1

                f.close()


            isshortcut = False
            recordingname = input('')
            recordingnum = '-1'
            historyfilelines = ''
            if(('Num' in recordingname) or ('num' in recordingname)):
                recordingnum = recordingname.replace('Num','')
                recordingnum = recordingname.replace('num','')
                isshortcut = True


            if recordingnum != '-1':
                with open("replayhistory.txt","r") as f:
                    historyfilelines = f.readlines()
                    f.close()

                recordingname = historyfilelines[int(recordingnum)][:-1]




            if isshortcut == False:
                with open("replayhistory.txt","a") as f:
                    f.write(recordingname + '\n')
                    f.close()

            print('How many times do you want to replay')
            nrofreplays = input('')
            nrofreplays = int(nrofreplays)
            Replayrecording(recordingname,nrofreplays)
            ##winput.unhook_mouse()
            winput.unhook_keyboard()

    except Exception as e:
        print('Exception was thrown. ' + str(e))
        ##winput.unhook_mouse()
        winput.unhook_keyboard()




#Program
StartApp()