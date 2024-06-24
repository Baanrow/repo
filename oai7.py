from openai import OpenAI
 
client = OpenAI()

vector_store_id="vs_DU2aEFK3rx5FpYc2fmmVzV56"

file_list = client.beta.vector_stores.files.list(vector_store_id=vector_store_id)

file_ids = file_list.data

for file in file_ids:
    print(f"Name: {file.id}")

print() 

print(file_list)

print()

print(client.beta.vector_stores.files.list(vector_store_id=vector_store_id))