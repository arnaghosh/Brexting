#http://bnci-horizon-2020.eu/database/data-sets

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
from scipy.fftpack import fft
import csv
ofile=open('basicCxmX.csv', "wb")
writer=csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

import sys,math,os
sys.path.append('/Users/mac/git/sms-tools/software/models')
import utilFunctions as UF
#import stft as STFT
import dftModel as DFT

import scipy.io as sio

mat = sio.loadmat('A01E.mat');
A = mat['data'];


run1 = A[0][8];  # run1 is A[0][3], run2 is A[0][4] and so on till run6 is A[0][8].
fs = run1['fs'][0][0][0][0];
run1_x = run1['X'];
run1_x = run1_x[0][0];
run1_trial = run1['trial'];
run1_trial = run1_trial[0][0][:,0];
run1_y = run1['y'][0][0][:,0];

#removing average of all electrodes at each time point --> average referencing
r1 = run1_x[:,0:21]
m1 = np.mean(r1, axis = 1)
#plt.plot(m1)
#plt.show()
m1t = np.reshape(m1, ( np.size(run1_x[:,1]),1) )
m1t_matrix = m1t * np.ones((np.shape(run1_x)))
run1_x -= m1t_matrix

#run1_x_C3 = run1_x[:,7]; #C3 is electrode #8
#run1_x_C4 = run1_x[:,11]; #C4 is electrode #12
important_electrodes = [0,2,4,7,9,11,14,16,19]

# print(np.shape(run1_x_C3))
# print(np.shape(run1_x_C4))
# print(fs)


w_name = 'hamming'
M = fs/2
N = 512
H = M/8
maxFreq = 50.0

# M = 131072
# N = 131072
# H = 44100*4
final_save_arr = np.zeros((np.shape(run1_trial)[0]*42,np.shape(important_electrodes)[0],N/2+1));
final_save_labels = np.zeros((np.shape(run1_trial)[0]*42));
for t in range(np.shape(run1_trial)[0]):
	start_time = run1_trial[t];
	for electrodes in range(np.shape(important_electrodes)[0]):
		x3 = run1_x[start_time+750:start_time+1500,important_electrodes[electrodes]];
		#x4 = run1_x_C3[start_time+750:start_time+1500]
		#(fs, x) = scipy.io.wavfile.read('/Users/mac/git/sms-tools/sounds/basicCmaj.wav', mmap=False)

		w = get_window(w_name, M)

		# m, p = STFT.stftAnal(x, w, N, H)


		M = w.size                                      
		hM1 = int(math.floor((M+1)/2))                  
		hM2 = int(math.floor(M/2))                      
		#x = np.append(np.zeros(hM2),x)                  
		#x = np.append(x,np.zeros(hM2))                  
		pin = hM1                                            
		pend = x3.size-hM1                               
		w = w / sum(w)
		counter = 0;
		while pin<=pend:
			counter = counter+1;
			x1 = x3[pin-hM1:pin+hM2]   
			#x2 = x4[pin-hM1:pin+hM2]                     
			mX1, pX1 = DFT.dftAnal(x1, w, N)  
			#mX2, pX2 = DFT.dftAnal(x2, w, N)              
			if pin == hM1:                               
				xmX1 = np.array([mX1])
				xpX1 = np.array([pX1])

				#xmX2 = np.array([mX2])
				#xpX2 = np.array([pX2])
				#writer.writerow([xmX])
			else:                                        
				xmX1 = np.vstack((xmX1,np.array([mX1])))
				xpX1 = np.vstack((xpX1,np.array([pX1])))

				#xmX2 = np.vstack((xmX2,np.array([mX2])))
				#xpX2 = np.vstack((xpX2,np.array([pX2])))
				#writer.writerow([xmX])
			pin += H
			final_save_arr[t*42 + counter-1][electrodes] = mX1;

			# return mX, pX
		print(electrodes,counter)
	final_save_labels[t*42:t*42 + counter] = run1_y[t];

	print "Printing DFT:",t
	#print(np.shape(xmX1))
	#print np.sum(xmX1[17:25])
		#print np.sum(xmX2[17:25])
sio.savemat('Trial6.mat',{'TF':final_save_arr,'Y':final_save_labels}) # change filename here 
#print type(mX)
# print np.array([mX1])
# print np.array([mX2])
#np.savetxt("bciTestC3.txt",xmX1,delimiter=' ')
#np.savetxt("bciTestC4.txt",xmX2,delimiter=' ')

#print "Printing stacked frames:"
#print xmX
#plt.plot(np.arange(x.size)/float(fs), x)
#plt.plot(mX)
#plt.pcolormesh(np.transpose(xmX))

#plt.figure(1)

# numFrames = int(xmX1[:,0].size)
# frmTime = H*np.arange(numFrames)/float(fs)
# binFreq = fs*np.arange(N*maxFreq/fs)/N
# plt.pcolormesh(frmTime, binFreq, np.transpose(xmX1[:,:N*maxFreq/fs+1]))

# plt.figure(2)
# numFrames = int(xmX2[:,0].size)
# frmTime = H*np.arange(numFrames)/float(fs)
# binFreq = fs*np.arange(N*maxFreq/fs)/N
# plt.pcolormesh(frmTime, binFreq, np.transpose(xmX2[:,:N*maxFreq/fs+1]))

# plt.show()