
import os
import signal
import subprocess
import time
import win32api, win32con

proc = subprocess.Popen(["C:\\All_Siva\\Softwares\\My_Quartus_16\\quartus\\bin64\\nios2-terminal.exe",""],stdout=subprocess.PIPE)
#print("ran program")
#flush 4 lines
r = proc.stdout.readline().strip()
r = proc.stdout.readline().strip()
r = proc.stdout.readline().strip()
r = proc.stdout.readline().strip()

#start timer
t1 = time.time()
t_lastAction = time.time()
while(1):
	out = int.from_bytes(proc.stdout.readline().strip(),byteorder='little')-48;
	#print (out)
	h_x,h_y = win32api.GetCursorPos();
	if (out==4):
		win32api.SetCursorPos((h_x,h_y-40));
		t_lastAction = time.time()
	elif (out==2):
		win32api.SetCursorPos((h_x-40,h_y));
		t_lastAction = time.time()
	elif (out==3):
		win32api.SetCursorPos((h_x+40,h_y));
		t_lastAction = time.time()
	elif (out==3):
		win32api.SetCursorPos((h_x,h_y+40));
		t_lastAction = time.time()
	t2 = time.time()
	if (t2-t_lastAction>2):
		h_x,h_y = win32api.GetCursorPos();
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,h_x,h_y,0,0);
		t_lastAction = time.time()
	if (t2-t1>1000): 
		break;

proc.kill()	
#os.killpg(os.getpid(proc.pid), signal.SIGTERM)
#out = subprocess.check_call(["C:\\All_Siva\\Softwares\\My_Quartus_16\\quartus\\bin64\\nios2-terminal.exe"],shell=True)
#print("prog out:",out)