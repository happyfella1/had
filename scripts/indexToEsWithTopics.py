import os
from elasticsearch import Elasticsearch

projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

clustersCsv = "output/kmeans/clusterng5validated.csv"
topicsCsv = "output/ldaTopics/clustering6.csv"
topicsLines = open(os.path.join(projectPath,topicsCsv)).readlines()
topics = []
for line in topicsLines:
    topics.append(line.split(",")[1:])
data = "data/data1_docs"
indexName = "resumes-clustered"
typeName = "resume"

es = Elasticsearch()
fields = os.listdir(os.path.join(projectPath,data))
for i in range(0,len(fields)):
    fieldPath = os.path.join(projectPath,data,fields[i])
    files = os.listdir(fieldPath)
    for file in files:
        print "Indexing "+ file
        text = open(os.path.join(fieldPath,file)).read()
        es.index(index=indexName, doc_type=typeName, id=file, body={"topics":topics[i],"text": text})