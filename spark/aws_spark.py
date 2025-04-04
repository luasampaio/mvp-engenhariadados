from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

def main():
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session
    job = Job(glueContext)

    df = glueContext.create_dynamic_frame_from_rdd([{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}], "df")
    df.toDF().show()
    
if __name__ == '__main__':
    main()