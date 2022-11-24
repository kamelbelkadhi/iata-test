# iata-test

How to run the code:
1. Setup the AWS CLI credentials (Make sure to have enough access to run all the required resources
2. Install SAM
2. Run in terminal (it will overwrite samconfig.toml): sam deploy --guided


The project is devided into three main parts:

** Lambda functions:
-loadData: This one loads data from the https endpoint as it is into S3 bucket
-inzipData: Unzip the loaded data from S3 bucket and put back to S3 as CSV
-fetchToParquet: Fetch data from dataframe to Parquets (key is Country) into S3

**Layers
-s3fs: It's needed as part of reading/writing data

**Configurations:
-template.yml: Have all the necessary resources
