import json

# Danh sách 4 file đầu vào
input_files = [
    "/home/tatan/CodeScore/data/gpt-3.5-turbo-0613_failed.jsonl",
    "/home/tatan/CodeScore/data/gpt-4-0613_failed.jsonl",
    "/home/tatan/CodeScore/data/gpt-4-turbo-2024-04-09_failed.jsonl",
    "/home/tatan/CodeScore/data/gpt-4o-2024-08-06_failed.jsonl"
]

# File đầu ra
output_file = "ds1000_failed.jsonl"

with open(output_file, 'w') as fout:
    for file in input_files:
        with open(file, 'r') as fin:
            for line in fin:
                if line.strip():  # bỏ qua dòng trống
                    fout.write(line)

print(f"✅ Đã gộp và lưu vào {output_file}")



