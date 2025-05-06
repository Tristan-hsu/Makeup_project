# Makeup Project

一個基於深度學習的虛擬化妝系統，能自動偵測臉部特徵並套用化妝效果。

## 📌 專案介紹

本專案利用 Autoencoder 與 DenseNet 等深度學習技術，實現臉部圖像的自動上妝處理。主要功能包括臉部特徵區域偵測、AI 化妝效果合成、眼部細節強化與背景細節處理。

## 🗂️ 專案結構

- `256img_lst/`：訓練圖像資料集
- `eye_feature_model/`：眼部特徵偵測模型
- `pymatting_ex/`：圖像分割處理
- `saved_model/`：儲存的模型檔案
- `train_model_code/`：模型訓練程式
- `trimap/`：圖像分割輔助圖
- `data_preprocessing.ipynb`：資料預處理程式
- `put_color_on_face.ipynb`：化妝效果應用程式
- `requirement.txt`：依賴套件
- `test.jpg`、`outcome.jpg`：範例輸入與輸出圖像

## 🛠️ 技術與套件

- Python 3
- PyTorch
- OpenCV
- PyMatting
- Jupyter Notebook

## 🚀 安裝與使用

1. 複製這個專案：
   ```bash
   git clone https://github.com/Tristan-hsu/Makeup_project.git
   cd Makeup_project
   ```

2. 安裝所需套件：
```bash
pip install -r requirement.txt
```
3. 執行預處理與化妝效果應用：
```bash
jupyter notebook data_preprocessing.ipynb
jupyter notebook put_color_on_face.ipynb
```
## 🚀 模型訓練
執行
`train_model_code/`裡的程式
Autoencoder 和 DenseNet的訓練碼

📈 訓練流程
預處理資料以便訓練
使用 Autoencoder 和 DenseNet 進行模型訓練
將訓練結果儲存於 saved_model/
套用訓練完成的模型產生化妝效果圖

🎨 範例成果
輸入：test.jpg
輸出：outcome.jpg（已套用化妝效果）
