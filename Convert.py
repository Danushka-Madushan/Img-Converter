from PIL import Image
import sys
import os
import re

try:
	dire = os.listdir()
	imgdir = []
	if len(sys.argv) == 3:
		f_type = sys.argv[1].strip()
		if len(f_type) == 0:
			sys.exit()
		for a in dire:
			x = re.findall(rf'.+.{f_type}',a)
			if x:
				imgdir.append(x)

		print(f"\n $ {len(imgdir)} Files Were Found Under [ {f_type} ] Extension")
		converter = sys.argv[2].strip()
		if len(converter) == 0:
			sys.exit()
		index = 1
		store_val = 0
		input_val = 0
		for i in imgdir:
			for k in i:
				print(f" $ Converting... ", end="")
				im = Image.open(k)
				rgb_im = im.convert('RGB')
				n = re.findall(rf'(.+).{f_type}',k)
				for l in n:
					rgb_im.save(f'{l}.{converter}')
					store_val += int(os.path.getsize(f'{l}.{converter}'))
					input_val += int(os.path.getsize(k))
					os.remove(k)
					print(f"[ Processed : {index} ]", end="\r")
					index += 1
		print(f"\n $ [ Size  : {round(input_val/1024/1024)}MB > {round(store_val/1024/1024)}MB ]")
	else:
		print("\n $ Usage : Convert {Format} {Format}")
		sys.exit()

except Exception as ExecutionError:
	print(f"\n Oops! This Happend : {ExecutionError}")
