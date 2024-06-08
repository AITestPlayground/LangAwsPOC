# LangAwsPOC

Steps

Create an S3 bucket with the documents that we want to have


Go to AWS Bedrock and create a knowldege base 

Setup the IAM permission to use knowledge base for the particular IAM user

Connect it to the S3 bucket instance and set any chunking details that you need.

You can add the documents manually to S3 bucket or add use the S3_Uploader class under the db_vectoriser. Now the documents are chunked and embedded into the db

Connect the knowledge base with the configured Opensearch or pgvector db

Add the id of the knowledgebase to the secretes

Call the model

