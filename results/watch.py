import json
import pandas as pd

fail = "/home/tatan/CodeBleu/failed_all.jsonl"
pas = "/home/tatan/CodeBleu/passed_all.jsonl"

# Đọc và thêm label = 0 cho fail
with open(fail, "r") as f:
    failed = [dict(**json.loads(line), label=0) for line in f if line.strip()]

# Đọc và thêm label = 1 cho pass
with open(pas, "r") as f:
    passed = [dict(**json.loads(line), label=1) for line in f if line.strip()]

# Gộp lại
merged = failed + passed

# Chuyển sang DataFrame
df = pd.DataFrame(merged)

# Chỉ giữ lại các cột cần thiết
df = df[["codebleu", "label"]]

# Ghi ra file CSV
df.to_csv("ds1000_merged_2.csv", index=False)
