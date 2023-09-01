INPUT_FILE = 'data.in.csv'
OUTPUT_FILE = 'data.out.csv'

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
      data1 = line.replace('.abc.com', '')
      data2 = data1.replace('.abc.net', '')
      data3 = data2.replace('.infra', '')
      cleaned.append(data3)
   for clean in cleaned:
      output += clean.strip('"') + "\n"
   data.close()
   
write_file(output)
