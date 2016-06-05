import os

clustersCsv = "output/kmeans/clusterng5.csv"
data = "data/data1_pdfs"

projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

clustersCsvPath = os.path.join(projectPath, clustersCsv)
dataPath = os.path.join(projectPath, data)


allFields = os.listdir(dataPath)

allFiles = []

for field in allFields:
    files = os.listdir(os.path.join(dataPath,field))
    files = [os.path.splitext(x)[0].strip() for x in files]
    allFiles.append(files)

clusters = []
for line in open(clustersCsvPath).readlines():
    elements = line.split(",")[1:]
    cleanedElements = [x.replace("/","").strip() for x in elements]
    clusters.append(cleanedElements)

validatedCsvName = os.path.splitext(os.path.basename(clustersCsvPath))[0] + "validated.csv"
outputFile = open(os.path.join(os.path.dirname(clustersCsvPath),validatedCsvName),"w")

for k in range(0,len(clusters)):
    for element in clusters[k]:
        field = "none"
        for j in range(0,len(allFields)):
            if element in allFiles[j]:
                field = allFields[j]
        # print field
        outputFile.write(element+","+field+","+str(k+1)+"\n")
print "Check validated file"