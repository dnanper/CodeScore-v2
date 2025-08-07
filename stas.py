import json
import numpy as np

input_path = "/home/tatan/CodeScore/results/ds1000_pass.jsonl"  # Thay đường dẫn file vào đây
output_path = "/home/tatan/CodeScore/results/ds1000_pass.txt"

# Tạo danh sách chứa các giá trị
scores = []
passed = []
pass_at_1 = []

# Đọc file jsonl
with open(input_path, 'r') as f:
    for line in f:
        item = json.loads(line)
        scores.append(item.get("predict_score", 0))
        passed.append(item.get("predict_passed", 0))
        pass_at_1.append(item.get("predict_pass_at_1", 0))

def summarize_field(name, values, thresholds=[0.9]):
    arr = np.array(values)
    summary = []
    summary.append(f"--- {name} ---")
    summary.append(f"Số lượng samples: {len(arr)}")

    # Percentiles
    percentiles = [10, 20, 30, 50, 70, 80, 90]
    summary.append("\nPhân vị (percentile):")
    for p in percentiles:
        val = np.percentile(arr, p)
        summary.append(f"{p}% samples <= {val:.6f}")
    summary.append("")
    for p in percentiles:
        val = np.percentile(arr, 100 - p)
        summary.append(f"{p}% samples >= {val:.6f}")

    # Đếm theo ngưỡng
    summary.append("\nThống kê theo ngưỡng:")
    for t in thresholds:
        gt = (arr > t).sum()
        le = (arr <= t).sum()
        summary.append(f"> {t}: {gt} samples")
        summary.append(f"<= {t}: {le} samples")

    summary.append("\n")
    return "\n".join(summary)

# Ghi ra file
with open(output_path, "w") as out:
    out.write(summarize_field("predict_score", scores))
    out.write(summarize_field("predict_passed", passed))
    out.write(summarize_field("predict_pass_at_1", pass_at_1))

print(f"Đã ghi thống kê vào {output_path}")
