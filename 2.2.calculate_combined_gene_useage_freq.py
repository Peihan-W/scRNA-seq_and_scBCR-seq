import pandas as pd
import numpy as np
from collections import defaultdict

N1 = 'sample\\N1-B-10XBCR\\outs\\vloupe-clonotypes.csv'
N2 = 'sample\\N2-B-10XBCR\\outs\\vloupe-clonotypes.csv'
N3 = 'sample\\N3-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S1 = 'sample\\S1-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S2 = 'sample\\S2-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S3 = 'sample\\S3-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S4 = 'sample\\S4-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S5 = 'sample\\S5-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S6 = 'sample\\S6-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S7 = 'sample\\S7-B-10XBCR\\outs\\vloupe-clonotypes.csv'
S8 = 'sample\\S8-B-10XBCR\\outs\\vloupe-clonotypes.csv'

file_list = ['N1', 'N2', 'N3']
# file_list = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']


type_dict = defaultdict(int)
total= 0
for i in range(len(file_list)):
	f = open(eval(file_list[i]))
	f.readline()
	for line in f.readlines():
		line = line.strip().split(',')
		freq = line[2]
		IGHV = line[6].split(';')
		IGHJ = line[8].split(';')
		IGLV = line[12].split(';')
		IGLJ = line[14].split(';')
		IGKV = line[18].split(';')
		IGKJ = line[20].split(';')
		if IGHV[0] != '' and IGHJ[0] != '' and len(IGHV) == 1 and len(IGHJ) == 1:
			if IGLV[0] != '' and IGLJ[0] != '' and len(IGLV) == 1 and len(IGLJ) == 1:
				type_list = [IGHV[0], IGHJ[0], IGLV[0], IGLJ[0]]
			elif IGKV[0] != '' and IGKJ[0] != '' and len(IGKV) == 1 and len(IGKJ) == 1:
				type_list = [IGHV[0], IGHJ[0], IGKV[0], IGKJ[0]]
			type_key = ';'.join(type_list)
			type_dict[type_key] += int(freq)
			total += int(freq)


# print(type_dict)
print(total)

outf = open('sankey_data_N.csv', 'w')
outf.write('IGHV,IGHJ,IGLV,IGLJ,freq\n')
for key in type_dict:
	freq = type_dict[key]
	key = key.split(';')
	key.append(str(freq))
	key = ','.join(key)
	outf.write(key + '\n')

