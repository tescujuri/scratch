
INPUT_FILE = 'data.in'
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
      data1 = line.replace('.wellsfargo.com', '')
      data2 = data1.replace('.wellsfargo.net', '')
      data3 = data2.replace('.infra', '')
      data4 = data3.replace('.wellsfargo.org', '')
      cleaned.append(data3)
         
   for clean in cleaned:
      output += clean.strip('"') + "\n"
   data.close()
   
write_file(output)


