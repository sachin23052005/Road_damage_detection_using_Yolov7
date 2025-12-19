# Road Damage Detection using YOLOv7

## 📌 Project Overview

This project focuses on **automatic road damage detection** using the **YOLOv7 object detection model**. The system is designed to identify and classify different types of road surface damages from images, which can help in infrastructure monitoring, maintenance planning, and smart city applications.

YOLOv7 is chosen due to its **high inference speed, improved accuracy, and better small-object detection** compared to earlier YOLO versions.

---

## 🧠 Model Overview (YOLOv7)

YOLOv7 is a state-of-the-art, one-stage object detection model. It processes an image through:

- **Backbone** – Extracts features from the input image  
- **Neck** – Combines and refines features  
- **Head** – Predicts bounding boxes, objectness scores, and class probabilities  

Compared to YOLOv5 and YOLOv6, YOLOv7 offers:

- Faster inference  
- Improved accuracy  
- Better small and thin object detection  
- More stable training  

---

## 📂 Dataset Information

- **Dataset Name:** Road Damage Detection  
- **Source:** Roboflow  
- **Dataset URL:** https://universe.roboflow.com/baka-1ravj/road-damage-det/dataset/4/download/yolov7pytorch  
- **Format:** YOLOv7 PyTorch TXT  
- **Total Images:** ~10,000  

### 🏷️ Classes (6 types of road damage)

1. Alligator cracking  
2. Edge cracking  
3. Longitudinal cracking  
4. Patching  
5. Rutting  
6. Transverse cracking


---

## ⚙️ Training Details

- **Epochs:** 20  
- **Batch Size:** 16  
- **Workers:** 4  
- **Hardware:** GPU  
- **Training Time:** ~1 to 1.15 hours (GPU)  

> ⚠️ Training on CPU was significantly slower (7–10 hours for 50 epochs), making GPU training highly recommended.

During training, YOLOv7 generated:

- Training batch images with bounding boxes  
- Epoch-wise results including loss, precision, recall, and mAP  
- Performance graphs such as precision, recall, F1-score, and confusion matrix  

---

## 📊 Validation & Evaluation

Validation was performed on unseen data to test the model’s generalization capability.

### 🔢 Final Evaluation Metrics

| Metric       | Value  |
|--------------|--------|
| Precision    | 0.6349 |
| Recall       | 0.6261 |
| F1-Score     | 0.6304 |
| mAP@0.5      | 0.6423 |
| mAP@0.5:0.95 | 0.3912 |

---

## 📉 Performance Analysis

- The model performs well on **alligator cracking, patching, and rutting**.  
- Thin crack types such as **edge, longitudinal, and transverse cracking** are harder to detect due to:
  - Low contrast  
  - Small size  
  - Similarity to shadows and road textures  
- Dataset imbalance and noise also affect performance.  
- Training for only **20 epochs** limits accuracy; YOLOv7 typically performs best with **50–150 epochs**.  

---

## ✅ Conclusion

The YOLOv7 model was successfully trained and evaluated for road damage detection using a Roboflow dataset. The results demonstrate that YOLOv7 is capable of detecting most types of road surface damage with reasonable accuracy.

Although detecting thin and irregular cracks remains challenging, the model shows strong potential for **real-time automated road inspection systems**.

---

## 🚀 Future Improvements

- Increase training epochs (50–150)  
- Balance dataset classes  
- Apply advanced data augmentation  
- Use higher-resolution inputs  
- Experiment with YOLOv7-X or YOLOv8  
- Deploy model in real-world road inspection systems  

---

## 📁 Results & Visualizations

All training results, graphs, and evaluation outputs (precision-recall curves, confusion matrix, F1 score, etc.) are available at the link below:

🔗 **Results Drive Link:**  
https://drive.google.com/file/d/1WNsIEMq5zALTBfdeW3qqcEvFDfVO51J_/view?usp=sharing  

---

## 🧑‍💻 Author

**Sachin**  
Project: *Road Damage Detection using YOLOv7*

---



