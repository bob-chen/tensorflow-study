from PIL import Image
from numpy import *


def GetImage(filelist):
	# value=zeros([1,width,height,1])
	width=28
	height=28
	value=zeros([1,width,height,1])
	value[0,0,0,0]=-1
	label=zeros([1,10])
	label[0,0]=-1

	for filename in filelist:
		# print(filename)
		img=array(Image.open(filename).convert("L"))
		# print (shape(img))
		width,height=shape(img);
		index=0
		tmp_value=zeros([1,width,height,1])
		for i in range(width):
			for j in range(height):
				tmp_value[0,i,j,0]=img[i,j]
				index+=1
		# print(tmp_value)
		# tmp_value=img
		if(value[0,0,0,0]==-1):
			value=tmp_value
		else:
			value=concatenate((value,tmp_value))
			
		tmp_label=zeros([1,10])
		index=int(filename.strip().split('/')[2][0])
		print "input:",index
		tmp_label[0,index]=1
		if(label[0,0]==-1):
			label=tmp_label
		else:
			label=concatenate((label,tmp_label))
		# label=(label[0,0]==-1 and tmp_label) or [label,tmp_label]
		# print(shape(value))
	return array(value),array(label)


# img=array(Image.open("test/0.png"))
# print((img))
# testImg, testLabel = GetImage(["test/2.png"])
# print(testImg)
