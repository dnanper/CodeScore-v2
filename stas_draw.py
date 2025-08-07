import json
import numpy as np
import matplotlib.pyplot as plt

input_path = "/home/tatan/CodeScore/results/ds1000_pass.jsonl"  # Đường dẫn file jsonl
output_prefix = "/home/tatan/CodeScore/results/ds1000_pass"  # Tên prefix cho file ảnh đầu ra

# Đọc dữ liệu
scores = []
passed = []
pass_at_1 = []

with open(input_path, 'r') as f:
    for line in f:
        item = json.loads(line)
        scores.append(item.get("predict_score", 0))
        passed.append(item.get("predict_passed", 0))
        pass_at_1.append(item.get("predict_pass_at_1", 0))

def plot_distribution(values, title, filename, bins=100):
    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=bins, color="skyblue", edgecolor="black")
    plt.title(f"Phổ giá trị: {title}")
    plt.xlabel("Giá trị")
    plt.ylabel("Số lượng mẫu")
    plt.grid(True, linestyle="--", alpha=0.5)
    min_val = min(values)
    max_val = max(values)
    plt.xticks(np.arange(round(min_val, 1), round(max_val + 0.1, 1), 0.1))
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Vẽ phổ
plot_distribution(scores, "predict_score", f"{output_prefix}_score.png")
plot_distribution(passed, "predict_passed", f"{output_prefix}_passed.png")
plot_distribution(pass_at_1, "predict_pass_at_1", f"{output_prefix}_pass_at_1.png")

print("Đã vẽ phổ giá trị và lưu thành file PNG.")
