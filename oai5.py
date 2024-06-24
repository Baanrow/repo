from openai import OpenAI
 
client = OpenAI()
 
 
# Ready the files for upload to OpenAI
file_paths = ["vector/known_issues.pdf"]
file_streams = [open(path, "rb") for path in file_paths]
 
# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id="vs_DU2aEFK3rx5FpYc2fmmVzV56", files=file_streams
)
 
# You can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)

