INPUT_FILE = "./data.in"
OUTPUT_FILE = "./data.out"

def write_file(data):
   with open(OUTPUT_FILE, 'w') as data_out:
      data_out.write(data)
      data_out.close()

cleaned = []
output = ""
with open(INPUT_FILE, 'r') as data:
   lines = data.readlines()
   for line in lines:
      line = line.strip()
      cleaned_data = line.replace('.wellsfargo.com', '').replace('.wellsfargo.net', '').replace('.infra', '')
      cleaned.append(cleaned_data)
   for clean in cleaned:
      output += clean.strip('"') + "\n"
   data.close()
   
write_file(output)
