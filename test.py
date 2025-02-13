from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("TestSpark") \
        .master("local[*]") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .getOrCreate()

    data = spark.range(0, 10).collect()
    print(data)

    spark.stop()

if __name__ == "__main__":
    main()
