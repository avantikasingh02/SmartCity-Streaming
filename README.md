**SMART CITY STREAMING PROJECT**

**PROJECT OVERVIEW**:

The goal of this project is to develop a thorough real-time data streaming pipeline for a Smart City project. It records and analyzes real-time data from a car on its way from London to Birmingham, including GPS data, camera footage, emergency incidents, weather, and vehicle data. To guarantee effective data ingestion, processing, storage, and visualization, the pipeline makes use of a combination of Internet of Things devices, Apache Kafka, Apache Spark, Docker, and AWS services.

**TECHNOLOGIES USED**:

- IoT Devices: For capturing real-time data.
- Apache Zookeeper: For managing and coordinating Kafka brokers.
- Apache Kafka: For real-time data ingestion into different topics.
- Apache Spark: For real-time data processing and streaming.
- Docker: For containerization and orchestration of Kafka and Spark.
- Python: For data processing scripts.
- AWS Cloud:
  - S3: For storing processed data as Parquet files.
  - Glue: For data extraction and cataloging.
  - Athena: For querying processed data.
  - IAM: For managing access and permissions.
  - Redshift: For data warehousing and analytics.
- Amazon QuickSight: For data visualization and dashboarding.

**PROJECT WORKFLOW**

1. DATA INGESTION:
   - IoT devices capture real-time data.
   - Data is ingested into Kafka topics configured in Docker using docker-compose.yml.
     
2. DATA PROCESSING:
   - Apache Spark reads data from Kafka topics.
   - Spark processes the data and writes it to AWS S3 as Parquet files.
   - Spark Streaming is used for real-time data processing with checkpointing to handle data issues.

3. DATA STORAGE:
   - Processed data is stored in AWS S3.
   - AWS Glue crawlers extract data from S3 and catalog it.

4. DATA QUERYING:
   - AWS Athena queries the processed and cataloged data from Glue.
     
5. DATA VISUALIZATION:
   - Amazon QuickSight visualizes the queried data with interactive dashboards.

**CONCLUSION**

This project demonstrates the power of modern data engineering tools to handle complex, real-time data streams and deliver actionable insights for Smart City initiatives. The use of AWS services ensures scalability, reliability, and ease of data management, making it an excellent example of an end-to-end data streaming pipeline.
