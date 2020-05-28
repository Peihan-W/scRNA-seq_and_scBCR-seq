import csv 
from collections import defaultdict
import operator


def recalc_frequency(in_file, out_file1, out_file2):
	sample = in_file.split('\\')[4].split('-')[0]
	f = open(in_file, 'r')
	anno = csv.reader(f)
	next(anno)
	IGH_dict = defaultdict(list)
	IGL_dict = defaultdict(list)
	IGK_dict = defaultdict(list)
	for row in anno:
		if row[10] == 'True' and row[11] == 'True':
			ig_type = row[5]
			v = row[6]
			d = row[7]
			j  = row[8]
			c = row[9]
			seq = row[12]
			clono = row[16]
			umi = int(row[15])
			info_list = [clono, v, d, j, c, umi]
			if ig_type == 'IGH':
				IGH_dict[seq].append(info_list)
			elif ig_type == 'IGL':
				IGL_dict[seq].append(info_list)
			elif ig_type == 'IGK':
				IGK_dict[seq].append(info_list)
	f.close()

	IGH_list = []
	for key in IGH_dict.keys():
		clono = []
		v = []
		d = []
		j  = []
		c = []
		total_freq = 0
		total_umi = 0
		for i in range(len(IGH_dict[key])):
			temp = IGH_dict[key][i]
			clono.append(temp[0])
			v.append(temp[1])
			d.append(temp[2])
			j.append(temp[3])
			c.append(temp[4])
			total_freq += 1
			total_umi += temp[5]
			# print(total_umi)
		clono = list(set(clono))
		v = list(set(v))
		d = list(set(d))
		j  = list(set(j))
		c = list(set(c))
		clono = '_'.join(clono)
		v = '_'.join(v)
		d = '_'.join(d)
		j  = '_'.join(j)
		c = '_'.join(c)
		avg_umi = round(total_umi/total_freq, 2)
		# print(avg_umi)
		info_list = [key, clono, v, d, j, c, total_freq, avg_umi]
		IGH_list.append(info_list)

	IGH_list = sorted(IGH_list, key=operator.itemgetter(-1), reverse=True)
	
	n = 0
	for sublist in IGH_list:
		if sublist[-2] >= 2: # at least 2 clones
			n+=1
			sublist[-1] = str(sublist[-1])
			sublist[-2] = str(sublist[-2])
			info = '\t'.join(sublist)
			fw2.write(sample + '_' + str(n) + '\t')
			fw2.write(info + '\n')
	n = 0
	for sublist in IGH_list:
		n+=1
		sublist[-1] = str(sublist[-1])
		sublist[-2] = str(sublist[-2])
		info = '\t'.join(sublist)
		fw1.write(sample + '_' + str(n) + '\t' + sample + '\t')
		fw1.write(info + '\n')


N1 = 'sample\\N1-QCS-B-10XBCR\\outs\\filtered_contig_annotations.csv'
N2 = 'sample\\N2-LJ-B-10XBCR\\outs\\filtered_contig_annotations.csv'
N3 = 'sample\\N3-WPH-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S1 = 'sample\\S1-SQZ-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S2 = 'sample\\S2-HSH-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S3 = 'sample\\S3-SQ-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S4 = 'sample\\S4-SX-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S5 = 'sample\\S5-ZYC-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S6 = 'sample\\S6-ZJX-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S7 = 'sample\\S7-SJC-B-10XBCR\\outs\\filtered_contig_annotations.csv'
S8 = 'sample\\S8-WMH-B-10XBCR\\outs\\filtered_contig_annotations.csv'

out_file1 = 'D:\\project5_covid19\\序列\\all_heavy_cdr3\\all_IGH_cdr3_annotations.txt'
fw1 = open(out_file1, 'w')
out_file2 = 'D:\\project5_covid19\\序列\\高频\\enriched_IGH_cdr3_annotations_2.txt'
fw2 = open(out_file2, 'w')

file_list = [N1, N2, N3, S1, S2, S3, S4, S5, S6, S7, S8]
for file in file_list:
	recalc_frequency(file, out_file1, out_file2)