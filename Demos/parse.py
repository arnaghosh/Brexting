
import os
import signal
import subprocess
import time
import win32api, win32con
import threading

mutex = threading.Lock();
class TimerThread(threading.Thread):
        def __init__(self,threadID,name):
                threading.Thread.__init__(self);
                print "Timer thread starting";
                self.threadID = threadID;
                self.name = name;
                self.started = 0;
                self.t0 = 0;
                self.t1 = 0;
                self.exit = 0;
                
        def run(self):
                mutex.acquire();
                self.t0 = time.time();
                mutex.release();
                while(1):
                        if self.exit == 1:
                               break;
                        self.t1 = time.time();
                        #print(self.t1 - self.t0)
                        mutex.acquire()
                        if (self.started and self.t1 - self.t0 >2):
                                self.t0 = time.time();
                                h_x,h_y = win32api.GetCursorPos();
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,h_x,h_y,0,0);
                                time.sleep(0.001);
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,h_x,h_y,0,0);
                        mutex.release()
                print "Time thread closing";

        def close(self,TaskThread):
                self.exit = 1;
                mutex.acquire()
                TaskThread.exit = 1;
                mutex.release()

class TaskThread():
        def __init__(self,threadID,name):
                print "Task thread starting";
                self.threadID = threadID;
                self.name = name;
                self.exit = 0;

        def run(self,timeThread):
                proc = subprocess.Popen(["C:\\altera_lite\\16.0\\quartus\\bin64\\nios2-terminal.exe",""],stdout=subprocess.PIPE)
                #print("ran program")
                #flush 4 lines
                r = proc.stdout.readline().strip()
                r = proc.stdout.readline().strip()
                r = proc.stdout.readline().strip()
                r = proc.stdout.readline().strip()

                s_cmd = '"C:\\altera_lite\\16.0\\nios2eds\\Nios II Command Shell.bat" nios2-download -g C:/Users/arnat/Desktop/temp/Demonstrations/SoC_FPGA/Nios_Access_DDR3/software/p1_t1/p1_t1.elf'
                os.system(s_cmd);
                #start timer
                mutex.acquire();
                timeThread.t0 = time.time();
                mutex.release();
                while(1):
                        try:
                                #out = int.from_bytes(proc.stdout.readline().strip(),byteorder='little')-48;
                                s = proc.stdout.readline().strip()
                                mutex.acquire()
                                timeThread.started = 1;
                                mutex.release();
                                out = int(s);
                                print ("arna",out)
                                h_x,h_y = win32api.GetCursorPos();
                                if (out==4):
                                        win32api.SetCursorPos((h_x,h_y-30));
                                        mutex.acquire();
                                        timeThread.t0 = time.time();
                                        mutex.release();
                                elif (out==1):
                                        win32api.SetCursorPos((h_x-30,h_y));
                                        mutex.acquire();
                                        timeThread.t0 = time.time();
                                        mutex.release();
                                elif (out==2):
                                        win32api.SetCursorPos((h_x+30,h_y));
                                        mutex.acquire();
                                        timeThread.t0 = time.time();
                                        mutex.release();
                                elif (out==3):
                                        win32api.SetCursorPos((h_x,h_y+30));
                                        mutex.acquire();
                                        timeThread.t0 = time.time();
                                        mutex.release();
                                else:
                                        self.exit = 1;
                                if (self.exit==1):
                                        mutex.acquire()
                                        timeThread.exit = 1;
                                        mutex.release()
                                        break;
                        except (RuntimeError, TypeError, ValueError, NameError):
                                print("Seems like program ended!!");
                                break;                

                proc.kill()	
                print("Task thread closing");

        def close(self):
                self.exit = 1;
if __name__ == '__main__':
        timer = TimerThread(1,"timer");
        task = TaskThread(2,"task");
        timer.start();
        task.run(timer);
        timer.close(task);
        task.close();
