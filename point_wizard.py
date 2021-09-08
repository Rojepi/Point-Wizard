import numpy as np
import cv2, time, ctypes, datetime, os, sys
from mss import base, mss
import pyautogui as pog
from PIL import Image
os.system('mode con: cols=70 lines=45')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def point_wizard():

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    #base_canvas_size = screensize[1],screensize[0] # H W : 1080,1920

    pog.FAILSAFE = False

    version_num = 'v 0.1'
    ui_line_length = 70
    left_side_pad = 5
    ui_delay = 1


    #bbox = {'top':1010,'left':1670,'width':1,'height':1}
    bbox = {'top':0,'left':0,'width':screensize[0],'height':screensize[1]}
    #bbox = {'top':980,'left':1660,'width':screensize[1],'height':screensize[0]}

    point_button_img = resource_path('point_button.jpg')
    point_button_img = cv2.imread(point_button_img)


    print('='*ui_line_length+'\n'+'='*ui_line_length)

    bar = [
        " [=     ]",
        " [ =    ]",
        " [  =   ]",
        " [   =  ]",
        " [    = ]",
        " [     =]",
        " [    = ]",
        " [   =  ]",
        " [  =   ]",
        " [ =    ]",
    ]
    bar_idx = 0

    name_file_0 = resource_path('point_wizard_name_0.txt')
    name_file_1 = resource_path('point_wizard_name_1.txt')

    name_file_0 = open(name_file_0).readlines()
    name_file_1 = open(name_file_1).readlines()

    for index,line in enumerate(name_file_0):
        if (index+1 != len(name_file_0)):
            print(line.replace('\n',''))
        else:
            print(line.replace('\n','')+'   '+version_num)

    for index,line in enumerate(name_file_1):
        if (index+1 != len(name_file_1)):
            print(line.replace('\n',''))
        else:
            print(line.replace('\n',''))

    print('\n\n\n'+' '*left_side_pad+'Welcome to Point Wizard! It will automatically collect bonus\n'+' '*left_side_pad+'Twitch channel points for you, Enjoy!\n\n')
    print(' '*left_side_pad+'Make sure Twitch is on your Main monitor. This program will\n'+' '*left_side_pad+'use your mouse every 15 minutes.\n'+' '*left_side_pad+'If you have any questions or problems, don\'t let me know.\n\n')
    start = input('                    - Press ENTER to Start -\n\n')

    time.sleep(ui_delay)
    print('  >  Starting Point Wizard')
    time.sleep(ui_delay)
    print('  >  Locating Point Dispensor')
    time.sleep(ui_delay)
    print('  >  Asking Twitch For Points')
    time.sleep(ui_delay)
    print('  >  Point Wizard is Running!\n')

    num_clicks = 0


    def get_point_button(img_to_search,img_to_look_for):
        im_search_gray = cv2.cvtColor(img_to_search, cv2.COLOR_BGR2GRAY)
        im_look_gray = cv2.cvtColor(img_to_look_for, cv2.COLOR_BGR2GRAY)

        w, h = img_to_look_for.shape[0],img_to_look_for.shape[1]
        res = cv2.matchTemplate(im_search_gray.astype(np.uint8),im_look_gray.astype(np.uint8),cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            #print(pt[0],pt[0]+w,pt[1],pt[1]+h)
            ##plt.imshow(im_search_gray[pt[1]:pt[1]+h,pt[0]:pt[0]+w])
            #plt.show()
            return pt[0],pt[0]+w,pt[1],pt[1]+h

    sct = mss()
    while True:
        sct_img = sct.grab(bbox)
        #print(np.array(sct_img)[0][0])
        #im = Image.fromarray(np.array(sct_img))
        #im.show()
        button_box = get_point_button(np.array(sct_img),point_button_img)
        if (button_box != None):
            pog.click(button_box[0],button_box[2])
            num_clicks += 1
            time.sleep(3)

        #print(' > POINTS COLLECTED  |  TOTAL: '+ str(num_clicks*50) + ' PTS  |  TIME ELAPSED: '+str(datetime.timedelta(minutes=(num_clicks-1)*15)))
        print(' > TOTAL POINTS COLLECTED: '+ str(num_clicks*50) + ' PTS  '+bar[bar_idx % len(bar)], end="\r")
        time.sleep(0.2)
        bar_idx += 1
        

        #time.sleep(10)

if __name__ == "__main__":
    point_wizard()
