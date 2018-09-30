import cv2
import numpy as np
import win32api
import os
import subprocess

def ManhattanDist(x1,y1,x2=0,y2=0):
	return np.abs(x2-x1)+np.abs(y2-y1);

def writeToFile(filename,arr):
        f = open(filename,'w');
        s = 'static const int movement['+str(len(arr)+1)+']={';
        for i in range(len(arr)-1):
                s = s+str(int(arr[i]))+',';
        s = s+str(int(arr[len(arr)-1]))+',-1};';
        print(s);
        f.write(s);

def drawOnCanvas(step):
	background = np.zeros((600,600,3),np.uint8)

	cv2.namedWindow('Canvas1',cv2.WINDOW_AUTOSIZE)
	cv2.imshow('Canvas1',background)
	draw = 0;
	img = background;
	cv2.waitKey(0);
	x_0,y_0 = win32api.GetCursorPos();
	prev_x,prev_y=-1,-1;
	hinge_x,hinge_y=-1,-1;
	all_hinge_x,all_hinge_y = np.array([]),np.array([])
	movement_dirs = np.array([]);
	while(1):
		a = cv2.waitKey(5)
		if a==27:
			break;
		elif a==13:
			draw=1-draw;
			x,y = win32api.GetCursorPos()
			if prev_x==-1:
				prev_x,prev_y = x-x_0,y-y_0;
			if hinge_x==-1:
				hinge_x,hinge_y = prev_x,prev_y;
				img = cv2.circle(img,(hinge_x,hinge_y),2,(255,0,0),-1);
				all_hinge_x = np.append(all_hinge_x,hinge_x);
				all_hinge_y = np.append(all_hinge_y,hinge_y);
		if draw==1:
			x,y = win32api.GetCursorPos()
			img = cv2.line(img,(prev_x,prev_y),(x-x_0,y-y_0),(255,255,255),5);
			prev_x,prev_y = x-x_0,y-y_0;
			if ManhattanDist(prev_x,prev_y,hinge_x,hinge_y)>step:
				if np.abs(prev_x-hinge_x)>np.abs(prev_y-hinge_y):
                                        movement_dirs = np.append(movement_dirs,1.5+np.sign(prev_x-hinge_x)*0.5);
					hinge_x = hinge_x+np.sign(prev_x-hinge_x)*step;
				else:
                                        movement_dirs = np.append(movement_dirs,3.5-np.sign(prev_y-hinge_y)*0.5);
					hinge_y = hinge_y+np.sign(prev_y-hinge_y)*step;
				img = cv2.circle(img,(hinge_x,hinge_y),2,(255,0,0),-1);
				all_hinge_x = np.append(all_hinge_x,hinge_x);
				all_hinge_y = np.append(all_hinge_y,hinge_y);
				
		cv2.imshow('Canvas1',img);
	writeToFile('C:/Users/arnat/Desktop/temp/Nios_Access_DDR3/software/brexting/movement_figure.h',movement_dirs);
	return img,all_hinge_x,all_hinge_y,x_0,y_0;

def mimicDrawing(image,step,x_0,y_0):
        proc = subprocess.Popen(["C:\\altera_lite\\16.0\\quartus\\bin64\\nios2-terminal.exe",""],stdout=subprocess.PIPE)
        #print("ran program")
        #flush 4 lines
        r = proc.stdout.readline().strip()
        r = proc.stdout.readline().strip()
        r = proc.stdout.readline().strip()
        r = proc.stdout.readline().strip()

        s_cmd = '"C:\\altera_lite\\16.0\\nios2eds\\Nios II Command Shell.bat" nios2-download -g C:/Users/arnat/Desktop/temp/Nios_Access_DDR3/software/brexting/brexting.elf'
        os.system(s_cmd);
        while(1):
                try:
                        #out = int.from_bytes(proc.stdout.readline().strip(),byteorder='little')-48;
                        s = proc.stdout.readline().strip()
                        out = int(s);
                        print(out)
                        h_x,h_y = win32api.GetCursorPos();
                        if (out==4):
                                win32api.SetCursorPos((h_x,h_y-step));
                                image = cv2.line(image,(h_x-x_0,h_y-y_0),(h_x-x_0,h_y-step-y_0),(0,0,255),2);
                        elif (out==1):
                                win32api.SetCursorPos((h_x-step,h_y));
                                image = cv2.line(image,(h_x-x_0,h_y-y_0),(h_x-step-x_0,h_y-y_0),(0,0,255),2);
                        elif (out==2):
                                win32api.SetCursorPos((h_x+step,h_y));
                                image = cv2.line(image,(h_x-x_0,h_y-y_0),(h_x+step-x_0,h_y-y_0),(0,0,255),2);
                        elif (out==3):
                                win32api.SetCursorPos((h_x,h_y+step));
                                image = cv2.line(image,(h_x-x_0,h_y-y_0),(h_x-x_0,h_y+step-y_0),(0,0,255),2);
                        else:
                                break;
                        cv2.imshow('Canvas1',image);
                        cv2.waitKey(5);
                except (RuntimeError, TypeError, ValueError, NameError):
                        print("Seems like program ended!!");
                        break;                

        proc.kill()
        return image;



if __name__ == "__main__":
	current_canvas,all_hinge_x,all_hinge_y,x_0,y_0 = drawOnCanvas(7);
	all_hinge_x = all_hinge_x.astype(int)
	all_hinge_y = all_hinge_y.astype(int)
	# draw blue lines (GT) here
	#for i in range(1,len(all_hinge_x)):
	#	current_canvas = cv2.line(current_canvas,(all_hinge_x[i-1],all_hinge_y[i-1]),(all_hinge_x[i],all_hinge_y[i]),(255,0,0),3);

	cv2.imshow('Canvas1',current_canvas);
	cv2.waitKey(0);
	currWD = os.getcwd();
	os.chdir("C:\\Users\\arnat\\Desktop\\temp\\Nios_Access_DDR3\\software\\brexting");
	s_cmd = '"C:\\altera_lite\\16.0\\nios2eds\\Nios II Command Shell.bat" make all';
	os.system(s_cmd);
	os.chdir(currWD);
        current_canvas = mimicDrawing(current_canvas,7,x_0,y_0);
        cv2.imshow('Canvas1',current_canvas);
	cv2.waitKey(0);	
	cv2.destroyAllWindows()	

