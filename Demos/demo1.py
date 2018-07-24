import cv2
import numpy as np
import win32api

def ManhattanDist(x1,y1,x2=0,y2=0):
	return np.abs(x2-x1)+np.abs(y2-y1);

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
					hinge_x = hinge_x+np.sign(prev_x-hinge_x)*step;
				else:
					hinge_y = hinge_y+np.sign(prev_y-hinge_y)*step;
				img = cv2.circle(img,(hinge_x,hinge_y),2,(255,0,0),-1);
				all_hinge_x = np.append(all_hinge_x,hinge_x);
				all_hinge_y = np.append(all_hinge_y,hinge_y);
				
		cv2.imshow('Canvas1',img);
	return img,all_hinge_x,all_hinge_y;

if __name__ == "__main__":
	current_canvas,all_hinge_x,all_hinge_y = drawOnCanvas(20);
	all_hinge_x = all_hinge_x.astype(int)
	all_hinge_y = all_hinge_y.astype(int)
	for i in range(1,len(all_hinge_x)):
		current_canvas = cv2.line(current_canvas,(all_hinge_x[i-1],all_hinge_y[i-1]),(all_hinge_x[i],all_hinge_y[i]),(255,0,0),3);

	cv2.imshow('Canvas1',current_canvas);
	cv2.waitKey(0);
	cv2.destroyAllWindows()	

