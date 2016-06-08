# Steps to use this course

1) Crawl Resumes
    From crawling-scripts folder run file.py to get all the links
    From crawling-scripts folder run wgett.py to download the resumes
    Copy the downloaded resumes to HDFS
2) Run Kmeans
    In cloudera VM run 4 steps of Kmeansmahout script which is mentioned in scripts folder
    Put kmeans output file in output folder and run validatekmeans script
    Above step creates clusters
3) Run LDA
    On each cluster obtained above run 5 stesps ldamahout script
    The above step creates topics on each cluster
4) Index Raw data and clustered results to elasticsearch
    Run indexToEs.py on raw data obtained from step 1
    Run indexToEsWithTopics.py with ouputs generated in step 2 and step 3


Mapreducescripts were not used as Mahout is used. 