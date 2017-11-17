class huffman:
    def __init__(self,weightfile):
        weightlist =[]
        with open(weightfile,'r') as f:
            for line in f:
                weightlist.append(int(line.strip()))
        sorted_weightlist = sorted(weightlist,reverse=True)
        self.sorted_weightlist=[]
        maxtem={}
        maxtem[sorted_weightlist[0]]=['minflag'] #use 'minflag' and 'maxflag' denote the path of the maxword and minword
        self.sorted_weightlist.append(maxtem)
        for i in sorted_weightlist[1:-1]:
            tem={}
            tem[i]=['False']
            self.sorted_weightlist.append(tem)
        mintem={}
        mintem[sorted_weightlist[-1]]=['maxflag']
        self.sorted_weightlist.append(mintem)

        self.maxlength=0
        self.minlength=0
        self.queue=[] #use queue to save the new_formed metanodes

    def _left_or_right(self):
        if len((self.queue))>0 and len(self.sorted_weightlist)>0:
            if self.queue[0].keys()[0]<self.sorted_weightlist[-1].keys()[0]:
                p = self.queue.pop(0)
            else: p=self.sorted_weightlist.pop()
        elif len((self.queue))==0:p=self.sorted_weightlist.pop()
        else:p=self.queue.pop(0)
        return p

    def find(self):
        right_p=self._left_or_right()
        left_p=self._left_or_right()
        return left_p,right_p

    def _fuse(self,left,right):
        left_p=left.keys()[0]
        right_p=right.keys()[0]
        root={}
        root_p = right_p + left_p
        root[root_p]=[]
        if 'maxflag' in left.values()[0] or 'maxflag' in right.values()[0]:
            self.maxlength += 1
            root[root_p].append('maxflag')
        if  'minflag'in left.values()[0] or 'minflag' in right.values()[0]:
              self.minlength += 1
              root[root_p].append('minflag')
        if not root[root_p]:root[root_p].append('False')
        self.queue.append(root)


    def growth(self):
        left=self.sorted_weightlist.pop()
        right=self.sorted_weightlist.pop()
        self._fuse(left,right)
        while len(self.queue)+len(self.sorted_weightlist)>1 :
            left_p,right_p=self.find()
            self._fuse(left_p,right_p)
if __name__=="__main__":
       huffman=huffman('huffman.txt')
       huffman.growth()
       max,min=huffman.maxlength,huffman.minlength
       print max,min


       #answers are 19 and 9