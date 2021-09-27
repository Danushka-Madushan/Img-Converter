from PIL import Image
import os 
import re

dire = os.listdir()
imgdir = []
f_type = input(" Extension : ")
for a in dire:
	x = re.findall(rf'.+.{f_type}',a)
	if x:
		imgdir.append(x)

print(f" {len(imgdir)} Images Were Found Under [ {f_type} ] Extension")
converter = input(" Convert to : ")
index = 1

for i in imgdir:
	for k in i:
		im = Image.open(k)
		rgb_im = im.convert('RGB')
		n = re.findall(rf'(.+).{f_type}',k)
		for l in n:
			rgb_im.save(f'{l}.{converter}')
			os.remove(k)
			print(f" Processing... [ Processed : {index} ]", end="\r")
			index += 1

