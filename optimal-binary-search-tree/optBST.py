class optBST:
	def __init__(self,rlist):
		self.treeValue={}
		self.num=len(rlist)
		self.treetable={}
		self.rootlist={}
		self.sequence=[]
		for key in range(1,self.num+1):
			self.treeValue[key]=rlist[key-1]
	def dynamic_pro(self):
		for diff in range(1,self.num):

			for start in range(1,self.num+1-diff):
				tem={}
				roots=sum([value for key,value in self.treeValue.items() if key in range(start,start+diff+1)])
				print 'roots',roots
				for root in range(start,start+diff+1):
					print start,root,start+diff

					temvalue=roots-self.treeValue.get(root,0)+self.treetable.get((start,root-1),0)+self.treetable.get((root+1,start+diff),0)
					print temvalue
					tem[temvalue]=root
				minvalue=min(tem)
				self.treetable[(start,start+diff)]=minvalue
				self.rootlist[(start,start+diff)]=tem[minvalue]
				#print tem
			print self.treetable
		print self.rootlist
		return self.treetable[(1,self.num)]
	def reconstruct(self,start,end):
		if start<end:
			temroot=self.rootlist[(start,end)]
			print temroot
			self.sequence.append((start,end,temroot))
		#temvalue=self.treetable[(start-1end)]
			self.reconstruct(start,temroot-1)
			self.reconstruct(temroot+1,end)
		else:return

a=optBST([0.05,0.4,0.08,0.04,0.1,0.1,0.23]) 
b=a.dynamic_pro()
print b
a.reconstruct(1,7)
print a.sequence


