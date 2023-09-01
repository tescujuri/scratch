import re

INPUT_FILE = "./data.in"
OUTPUT_FILE = "./data.out"
cleaned = []
output = ""

def write_file(data_in):
    with open(OUTPUT_FILE, 'w') as data_out:
        data_out.write(data_in)
        data_out.close()

def clean_data(data_in):
    prefix_clean = re.sub(r".*: ", '', data_in)
    cleaned_out = prefix_clean.replace('.bilatu.com', '').replace('.bilatu.net', '').replace('.dev', '').replace('..', ".").replace('"', '').replace("^ ", "")
    return cleaned_out

with open(INPUT_FILE, 'r') as data:
    lines = data.readlines()
    for line in lines:
        cleaned_data = clean_data(line)
        if cleaned_data not in cleaned:
            cleaned.append(cleaned_data)
    for clean in cleaned:
        output += clean.strip('"')

    data.close()

write_file(output)
