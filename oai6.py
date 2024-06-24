from openai import OpenAI
 
client = OpenAI()

file = client.beta.vector_stores.files.create_and_poll(
  vector_store_id="vs_DU2aEFK3rx5FpYc2fmmVzV56",
  file_id="file-m3kfCO6jd1tF3fYvgcuKVmOj"
)

print(file.status)
