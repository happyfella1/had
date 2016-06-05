import os

clustersCsv = "output/kmeans/clusterng5validated.csv"
data = "data/data1_docs"


projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

clustersCsvPath = os.path.join(projectPath, clustersCsv)
dataPath = os.path.join(projectPath, data)
clustersFolder = os.path.splitext(os.path.basename(clustersCsvPath))[0]
clustersFolderPath = os.path.join(os.path.dirname(clustersCsvPath),clustersFolder)


def makeDirectory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
makeDirectory(clustersFolderPath)

for line in open(clustersCsvPath).readlines():
    elems = line.strip().split(",")
    i = open(os.path.join(dataPath,elems[1],elems[0])).read()
    clusterFolder = "cluster" + str(elems[2])
    outFolder = os.path.join(clustersFolderPath,clusterFolder)
    makeDirectory(outFolder)
    outPath = os.path.join(outFolder,elems[0])
    open(outPath,'w').write(i)


