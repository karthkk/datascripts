import sys
from functools import partial

class Fl:
	def __init__(self, sep, l):
		file_name = l[0]
		idx = int(l[1])
		lns = open(file_name).readlines()
		self.dictdata = dict(map(lambda x: (x.strip().split(sep)[idx],x.strip()),lns))
		l = len(self.dictdata.values()[0].split(sep))
		self.empty = sep.join(['' for i in range(l)])
	
	def lookup(self,key):
		return self.dictdata.get(key,self.empty)


file_sep = sys.argv[1]
files_idxes = sys.argv[2:]
flname_idx_pairs = zip(*(iter(files_idxes),) * 2)
fl_data= map(lambda x: Fl(file_sep,x),flname_idx_pairs)
all_keys = []
for p in fl_data:
	all_keys+=p.dictdata.keys()
filteredkeys = {}.fromkeys(all_keys).keys()
for f in filteredkeys:
	print ','.join(map(lambda x: x.lookup(f),fl_data))

