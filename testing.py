#download file from internet
import urllib

# testfile = urllib.URLopener()
# testfile.retrieve("http://spark-public.s3.amazonaws.com/algo2/datasets/clustering_big.txt", "clustering_big.txt")

#computing simple numbers
hamm=[0]*15
k=0
for i in range(5):
    for j in range(i,5):
        mask=1 << i
        mask2 = 1 << j
        hamm[k]=mask|mask2
        k=k+1
        print(mask|mask2)

#function that computes neighbors for the given point
def neighbors(x):
    print("x", x)
    result = []
    for i in hamm:
        print('hamm', i)
        print("[x^i]",x, i, [x^i])
        if points[x^i] != 0:
            result.append(x^i)
            print("match", x^i, points[x^i])
    print("result",result)
    print()
    print()
    print()

    return result

#reading the data into arrays points and index
points = [0]*pow(2,5)
index=[]
from timeit import default_timer as timer
start=timer()

with open("clustering_big (copy).txt") as f:
    next(f)
    cluster=1
    for line in f:
        curindex=int(line.replace(' ',''), base = 2)
        index.append(curindex)
        points[curindex]=cluster
        # print("line", line)
        # print("curindex", curindex)
        # print("points", points)
        # print("index", index)
        cluster=cluster+1
    print("points", points)
    print("index", index)
readend=timer()
print("reading data:",readend-start)

#performing clustering
names=[0]
loopstart=timer()
for i in index:
    if points[i] in names:
        continue
    nclust = [i]
    while len(nclust) != 0:
        nnclust = []
        for dot in nclust:
            for ind in neighbors(dot):
                if points[ind] != points[i]:
                    nnclust.append(ind)
                    points[ind]=points[i]
        nclust = nnclust
    names.append(points[i])
end=timer()
print("loop time", end-loopstart)
print("total time", end-start)
print(points)
print(len(names)-1)