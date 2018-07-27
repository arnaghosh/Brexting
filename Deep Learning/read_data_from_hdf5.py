import h5py
import numpy as np

def loadHDF5file_to_np(filename):
	file = h5py.File(filename,'r');
	print(file.keys())

	data = file['home/TF']
	data = np.transpose(data,(2,1,0))
	labels = file['home/Y']
	return data,labels

if __name__ == "__main__":
	filename = '/media/arna/340fd3c9-2648-4333-9ec9-239babc34bb7/arna_data/BCI/AllTrials.h5' # put filename here
	data,labels = loadHDF5file_to_np(filename);
	print(data.shape)
	print(labels.shape)
