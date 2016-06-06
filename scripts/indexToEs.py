import os
from elasticsearch import Elasticsearch

clustersCsv = "output/kmeans/clusterng5validated.csv"
data = "data/data1_docs"
indexName = "resumes-raw"
typeName = "resume"

projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

es = Elasticsearch()
fields = os.listdir(os.path.join(projectPath,data))
for field in fields:
    fieldPath = os.path.join(projectPath,data,field)
    files = os.listdir(fieldPath)
    for file in files:
        print "Indexing "+ file
        text = open(os.path.join(fieldPath,file)).read()
        es.index(index=indexName, doc_type=typeName, id=file, body={"text": text})

