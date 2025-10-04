# 📈 AutoDeployLR - 線性回歸互動視覺化應用

一個基於 [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) 流程建構的線性回歸應用，使用者可即時調整資料參數，觀察模型擬合行為。此應用使用 Python + Streamlit 開發，並已部署至 Web 平台供互動使用。

---

## 📌 專案目標（Business Understanding）

- 教學演示：協助初學者理解簡單線性回歸原理
- 模型視覺化：觀察不同參數如何影響模型行為
- 自動部署：實作可快速發布的資料科學應用

---

## 📊 資料來源（Data Understanding & Preparation）

本專案資料為合成數據（synthetic data），遵循以下公式產生：

\[
y = ax + b + \text{noise}
\]

使用者可控制：
- `a`（真實斜率）
- `noise`（隨機誤差）
- `num_points`（資料點數量）

---

## 🧮 模型建立（Modeling）

- 使用 `scikit-learn` 的 `LinearRegression` 進行模型擬合
- 訓練後取得：
  - 模型斜率（學到的 a）
  - 截距（學到的 b）
- 即時畫出預測線與原始資料點

---

## 📈 模型評估（Evaluation）

- 顯示模型斜率 / 截距與原始設定值對比
- 使用 `matplotlib` 視覺化資料點與迴歸線
- 使用者透過互動參數觀察變化影響

---

## 🚀 部署（Deployment）

本應用已部署至 **Streamlit Cloud** 平台：

▶️ [線上使用網址](https://5114056018hw1.streamlit.app)

本機測試：

```bash
# 安裝套件
pip install -r requirements.txt

# 執行應用
streamlit run app.py
