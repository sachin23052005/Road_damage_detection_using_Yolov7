import subprocess
import re
import csv

# Paths (edit if needed)
weights = r"C:\Users\sachi\TCS_PROJECT_FINAL_ROAD_CONDITIONS\Yolov7_model\runs\train\yolov7_rd_superfast\weights\best.pt"
data = r"C:\Users\sachi\TCS_PROJECT_FINAL_ROAD_CONDITIONS\Yolov7_model\datasets\RoadDamage\data.yaml"
img_size = "640"
csv_output = "yolov7_evaluation_results.csv"

# Run YOLOv7 evaluation
process = subprocess.Popen(
    [
        "python", r"C:\Users\sachi\TCS_PROJECT_FINAL_ROAD_CONDITIONS\Yolov7_model\test.py",
        "--weights", weights,
        "--data", data,
        "--img", img_size,
        "--conf", "0.001",
        "--iou", "0.65"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

output_lines = process.stdout.readlines()

# Regex to capture metrics
pattern = re.compile(
    r"all\s+\d+\s+\d+\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)"
)

metrics = None
for line in output_lines:
    match = pattern.search(line)
    if match:
        precision, recall, map50, map5095 = match.groups()
        metrics = {
            "Precision": precision,
            "Recall": recall,
            "mAP@0.5": map50,
            "mAP@0.5:0.95": map5095
        }
        break

if metrics is None:
    raise RuntimeError("Could not extract metrics. Check YOLOv7 output format.")

# Save to CSV
with open(csv_output, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(metrics.keys())
    writer.writerow(metrics.values())

print("Evaluation complete")
print("Results saved to:", csv_output)
print(metrics)