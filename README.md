# GridWorld Value Iteration (DRL HW1)

🚀 **線上展演 (Live Demo) 立即體驗**： [https://drl-hw-1-lilac.vercel.app/](https://drl-hw-1-lilac.vercel.app/)

這是一個基於 Flask 與強化學習 (Reinforcement Learning) 的互動式網格地圖尋路專案。使用者可以自訂地圖大小、起點、終點以及障礙物，系統將使用 **價值迭代 (Value Iteration)** 演算法來推導出最佳政策 (Optimal Policy) 與狀態價值 (State Value Function)。

## ✨ 主要功能

- **動態網格生成**：支援 $5 \times 5$ 至 $9 \times 9$ 大小的自訂網格。
- **高互動性介面**：透過滑鼠點擊依序設定：
  - 🟢 1 個起點
  - 🔴 1 個終點
  - 🪨 $n-2$ 個障礙物
- **最佳政策推導**：後端實作嚴謹的 Value Iteration 演算法，計算並動態逼近收斂的 $V(s)$ 與最佳行動。
- **最佳行動視覺化**：於使用者介面中動態渲染每個網格的狀態價值及最佳尋路箭頭 ($\uparrow, \downarrow, \leftarrow, \rightarrow$)。
- **現代化設計 (Modern UI)**：具玻璃擬態 (Glassmorphism) 特效的互動面板和平滑的 CSS 過渡動效設計。

## 🚀 專案技術棧

- **後端**：Python, Flask
- **前端**：HTML5, CSS3, JavaScript, FontAwesome
- **佈署**：Vercel Serverless Function 即插即用支援

## 🛠 本地端運行

1. 安裝依賴套件 (或虛擬環境)：
   ```bash
   pip install -r requirements.txt
   ```
2. 啟動本機伺服器：
   ```bash
   python app.py
   ```
3. 在瀏覽器打開：[http://127.0.0.1:5000](http://127.0.0.1:5000)

## ☁️ 雲端佈署 (Vercel)

本專案已完全兼容 Vercel Serverless 函式，您可經由以下步驟輕易上雲：
1. 將本儲存庫 Fork 或 Push 至您個人的 GitHub。
2. 登入至 [Vercel](https://vercel.com/)。
3. 點擊 **"Add New Project"** 並匯入該 Repository。
4. 無需特殊 Build Config，直接點擊 **"Deploy"** 即可完成！

---
📌 **備註**：本專案為深度強化學習課程 (DRL) 之作業一 (HW1) 提交項目。
