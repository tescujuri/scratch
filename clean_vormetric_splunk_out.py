INPUT_FILE = "./data.in"
OUTPUT_FILE = "./data.out"
cleaned = []
output = ""   

def write_file(data):
   with open(OUTPUT_FILE, 'w') as data_out:
      data_out.write(data)
      data_out.close()
      
def clean_data(data):
   return data.replace('.bilatu.com', '').replace('.bilatu.net', '').replace('.dev', '').strip()
      
with open(INPUT_FILE, 'r') as data:
   lines = data.readlines()
   for line in lines:
      cleaned_data = clean_data(line)
      if cleaned_data not in cleaned:
         cleaned.append(cleaned_data)
   for clean in cleaned:
      output += clean.strip('"') + "\n"
   data.close()
   
write_file(output)
