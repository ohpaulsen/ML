from matplotlib.pyplot import *
import numpy as np

class values:
    label = 'nolabel'
    X = [];
    Y = [];
    xmin,xmax,ymin,ymax,mean = 0,0,0,0,0

    def fillvalues(self):
        self.xmax = max(self.X)
        self.xmin = min(self.X)
        self.ymin = min(self.Y)
        self.ymax = max(self.Y)

class DTree:
    X,Y,Z = None,None,None
    X2,Y2 = '',''
    labelarray = []
    testarray = []

    def __init__(self):
        self.checkInput()
        self.testData()
#        self.createTree()
        self.getLabel()
        self.trainData()
        self.ClassTestData()

    def checkInput(self):
        try:
            DTree.X,DTree.Y,DTree.Z = np.genfromtxt(r'test.txt', unpack=True)
            if(len(DTree.X) == 0):
                print "Training data is empty"
            else:
                print "Training data read OK"
        except Exception as e:
            print str(e)

    def trainData(self):
        for lab in DTree.labelarray:
            tX,tY = [],[]
            for i in range(0,len(DTree.X)):
                if(lab.label == DTree.Z[i]):
                    tX.append(DTree.X[i])
                    tY.append(DTree.Y[i])
            if(len(tX) != 0):
                lab.X,lab.Y = tX, tY
                lab.fillvalues()

    def testData(self):
        try:
            DTree.X2,DTree.Y2 = np.genfromtxt(r'test2.txt', unpack=True)
            if(len(DTree.X2) == 0):
                print "Test data is empty"
            else:
                print "Test data read OK"
        except Exception as e:
            print str(e)

    def ClassTestData(self):
        for l in DTree.labelarray:
            for t in range(0,len(DTree.X2)):
                   Xc = DTree.X2[t]
                   Yc = DTree.Y2[t]
                   if(Xc <= l.xmax and Xc >= l.xmin and Yc <= l.ymax and Yc >= l.ymin):
                       v = values()
                       v.X = DTree.X2[t]
                       v.Y = DTree.Y2[t]
                       v.label = l.label
                       DTree.testarray.append(v)

    def getLabel(self):
        labels = sorted(set(DTree.Z))
        for l in labels:
            v = values()
            v.label = l
            DTree.labelarray.append(v)

if __name__ == "__main__":
    x = DTree()
