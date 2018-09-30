import cv2
import numpy as np
import win32api, win32gui, win32con
import os
import subprocess
import time
import clipboard, re
import keyboard
import threading

mutex = threading.Lock()
def ManhattanDist(x1,y1,x2=0,y2=0):
	return np.abs(x2-x1)+np.abs(y2-y1);

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

'''
clipboard.copy("abc");
for i in range(3):
        w = WindowMgr()
        w.find_window_wildcard(".*nios2-terminal*")
        w.set_foreground()
        h_x,h_y = win32api.GetCursorPos();
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,h_x,h_y,0,0);
        time.sleep(0.001);
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,h_x,h_y,0,0);
        time.sleep(3);
'''
'''
out_f = open("outFile.txt","wb");
proc = subprocess.Popen(["C:\\altera_lite\\16.0\\quartus\\bin64\\nios2-terminal.exe"],stdin=subprocess.PIPE, stdout = out_f, bufsize = 4096, shell = False)
#proc = subprocess.Popen(["python","demo3_test.py"],stdin=subprocess.PIPE, stdout = subprocess.PIPE, bufsize = 4096, shell = True)
print(proc.poll())
#flush 4 lines
#r = proc.stdout.readline().strip()
#r = proc.stdout.readline().strip()
#r = proc.stdout.readline().strip()
#r = proc.stdout.readline().strip()
#sprint(r);
s_cmd = '"C:\\altera_lite\\16.0\\nios2eds\\Nios II Command Shell.bat" nios2-download -g C:/Users/arnat/Desktop/temp/Nios_Access_DDR3-Final_Demo/software/brexting_finalDemo/brexting_finalDemo.elf'
os.system(s_cmd);
#print(proc.stdout.readline().strip())
text = "a\n";
print('text',text);
result,err = proc.communicate(text);
print(result)
proc.wait()
if proc.poll()==None:
        proc.kill()
out_f.close()
'''
class read_user_input(threading.Thread):
        def __init__(self,threadID,name):
                threading.Thread.__init__(self);
                print "User input thread starting";
                self.threadID = threadID;
                self.name = name;
                self.started = 0;
                self.t0 = 0;
                self.t1 = 0;
                self.exit = 0;
                self.s_user = ''
                self.s_bci = ''

        def run(self):                
                while True:
                        char = '';
                        try:
                                if keyboard.is_pressed('escape'):
                                        self.exit = 1;
                                        break;
                                elif keyboard.is_pressed('a'):
                                        print('a printed');
                                        char = 'a';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('b'):
                                        print('b printed');
                                        char = 'b';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('c'):
                                        print('c printed');
                                        char = 'c';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('d'):
                                        print('d printed');
                                        char = 'd';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('e'):
                                        print('e printed');
                                        char = 'e';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('f'):
                                        print('f printed');
                                        char = 'f';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('g'):
                                        print('g printed');
                                        char = 'g';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('h'):
                                        print('h printed');
                                        char = 'h';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('i'):
                                        print('i printed');
                                        char = 'i';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('j'):
                                        print('j printed');
                                        char = 'j';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('k'):
                                        print('k printed');
                                        char = 'k';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('l'):
                                        print('l printed');
                                        char = 'l';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('m'):
                                        print('m printed');
                                        char = 'm';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('n'):
                                        print('n printed');
                                        char = 'n';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('o'):
                                        print('o printed');
                                        char = 'o';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('p'):
                                        print('p printed');
                                        char = 'p';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('q'):
                                        print('q printed');
                                        char = 'q';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('r'):
                                        print('r printed');
                                        char = 'r';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('s'):
                                        print('s printed');
                                        char = 's';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('t'):
                                        print('t printed');
                                        char = 't';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('u'):
                                        print('u printed');
                                        char = 'u';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('v'):
                                        print('v printed');
                                        char = 'v';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('w'):
                                        print('w printed');
                                        char = 'w';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('x'):
                                        print('x printed');
                                        char = 'x';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('y'):
                                        print('y printed');
                                        char = 'y';
                                        time.sleep(0.2);
                                elif keyboard.is_pressed('z'):
                                        print('z printed');
                                        char = 'z';
                                        time.sleep(0.2);                        
                                else:
                                        pass;
                        except:
                                print('something else');
                        mutex.acquire()
                        self.s_user = self.s_user+char;
                        self.s_bci = self.s_bci + char;
                        mutex.release()


        def close(self):
                print("User input thread closing");
                self.exit = 1;

class display():
        def __init__(self,img):
                cv2.namedWindow('Canvas2',cv2.WINDOW_AUTOSIZE)
                cv2.imshow('Canvas2',img);

        def run(self,img,BCI_obj):
                while(1):
                        img = cv2.putText(img,"User Input: "+BCI_obj.User_inp.s_user,(15,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
                        img = cv2.putText(img,"BCI Output: "+BCI_obj.s_done,(15,160),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
                        cv2.imshow('Canvas2',img);
                        c = cv2.waitKey(5);
                        #print(c)
                        if c==27:
                                break;
                        elif c==13:
                                img = cv2.imread('keyboard_bg.png',1);
                                mutex.acquire()
                                User_inp.s_user = ''
                                mutex.release()

class bci(threading.Thread):
        def __init__(self,threadID,name):
                threading.Thread.__init__(self);
                self.threadID = threadID;
                self.name = name;
                print("SET ZERO FIRST");
                #set zero coord
                cv2.waitKey(0);
                self.x_0,self.y_0 = win32api.GetCursorPos();
                self.step = 20;
                self.char_pos = ((40,599),(425,675),(275,675),(194,599),(194,521),(272,599),(352,599),(432,599),(579,521),(500,599),(578,599),(656,599),(580,675),(502,675),(662,521),(730,521),(40,521),(270,521),(114,599),(351,521),(506,521),(351,675),(118,521),(198,675),(423,521),(118,675));
                self.s_done = ''
                self.User_inp = read_user_input(2,"userInpThread");
                self.User_inp.start()
                self.w = WindowMgr()

        def run(self):
                print('BCI started');
                while self.User_inp.exit==0:
                        while self.User_inp.s_bci!='':
                                target = self.User_inp.s_bci[0];
                                target_pos = self.char_pos[ord(target)-97];
                                x_1,y_1 = win32api.GetCursorPos();
                                x_1 = x_1 - self.x_0;
                                y_1 = y_1 - self.y_0;
                                while ManhattanDist(x_1,y_1,target_pos[0],target_pos[1])>=2*self.step:
                                        target_movement_array = np.array([]); # 1- left, 2 - right, 3 - down, 4 - up
                                        if abs(target_pos[0]-x_1)>self.step:
                                                target_movement_array = np.append(target_movement_array,(1.5+np.sign(target_pos[0]-x_1)*0.5)*np.ones(int(np.floor(np.abs(target_pos[0]-x_1)/self.step)),));
                                        if abs(target_pos[1]-y_1)>self.step:
                                                target_movement_array = np.append(target_movement_array,(3.5-np.sign(target_pos[1]-y_1)*0.5)*np.ones(int(np.floor(np.abs(target_pos[1]-y_1)/self.step)),));
                                        target_movement_str =  np.array_str(target_movement_array).replace(" ","").replace("[","").replace("]","").replace(".","")
                                        print(target_movement_str)
                                        clipboard.copy(target_movement_str);
                                        self.w.find_window_wildcard(".*nios2-terminal*")
                                        self.w.set_foreground()
                                        rect = win32gui.GetWindowRect(self.w._handle)
                                        m_x, m_y = (rect[0]+rect[2])/2, (rect[1]+rect[3])/2
                                        print(m_x,m_y)
                                        curr_x,curr_y = win32api.GetCursorPos();
                                        win32api.SetCursorPos((m_x,m_y));
                                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,m_x,m_y,0,0);
                                        time.sleep(0.0001);
                                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,m_x,m_y,0,0);
                                        win32api.SetCursorPos((curr_x,curr_y));
                                        self.w.find_window_wildcard(".*Canvas2*")
                                        self.w.set_foreground()
                                        time.sleep(0.75);
                                        for i in range(len(target_movement_array)):
                                                out = target_movement_array[i];
                                                h_x,h_y = win32api.GetCursorPos();
                                                if (out==4):
                                                        win32api.SetCursorPos((h_x,h_y-self.step));
                                                elif (out==1):
                                                        win32api.SetCursorPos((h_x-self.step,h_y));
                                                elif (out==2):
                                                        win32api.SetCursorPos((h_x+self.step,h_y));
                                                elif (out==3):
                                                        win32api.SetCursorPos((h_x,h_y+self.step));
                                                time.sleep(0.25);
                                        x_1,y_1 = win32api.GetCursorPos();
                                        x_1 = x_1 - self.x_0;
                                        y_1 = y_1 - self.y_0;
                                        
                                time.sleep(2);
                                temp_str = list(self.User_inp.s_bci);
                                del temp_str[0];
                                mutex.acquire();
                                self.s_done = self.s_done + self.User_inp.s_bci[0]
                                self.User_inp.s_bci = ''.join(temp_str);
                                mutex.release();
                                print(self.User_inp.s_bci)

        def close(self):
                self.User_inp.close();

if __name__=="__main__":
        img = cv2.imread('keyboard_bg.png',1);
        Disp = display(img);
        BCI_out = bci(1,"BciThread");
        BCI_out.start()
        Disp.run(img,BCI_out);
        BCI_out.close()
