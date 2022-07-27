from pyspark.sql import SparkSession


spark = SparkSession.builder \
         .master('yarn') \
         .appName("testing") \
         .getOrCreate()


#spark-submit "file_path"
#--master
#Learn about cluster Manager --> yarn mesos kubernetes local local[k]
#deploy-mode 

#Cluster  and client 

# 
#
#
#
#

