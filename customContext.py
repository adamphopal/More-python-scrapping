from contextlib import contextmanager


@contextmanager
def CustomLog(*args):
	try:
		myfile = open(*args)
		myfile.write('This is coming from class!\n')
		
		yield myfile		
	finally:
		myfile.write('This is coming the second class!\n')
		myfile.close()


with CustomLog('index.txt','a') as customfile:
	customfile.write('THis is going to fail!\n')
	


