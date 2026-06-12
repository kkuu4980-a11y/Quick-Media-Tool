# Quick Media Tool 

一個使用 Python 編寫的輕量化、跨平台命令列工具。讓你無需開啟沉重的影音剪輯軟體，就能秒速完成影音分離（MP4 轉 MP3）與精確的影片片段裁剪。支援雙語互動選單，完全在本機端處理，不依賴任何外部託管空間。

---

## Features / 專案特點

* **雙語互動選單**: 內建支援繁體中文與英文互動式命令列選單。
* **智慧影片偵測**: 自動掃描當前資料夾下的影片檔案（`.mp4`、`.mkv`、`.avi`、`.mov`）並提供編號供用戶選擇。
* **秒速音訊提取**: 直接抽離影片中的音軌，並以高音質 `.mp3` 格式單獨儲存。
* **精確影片裁剪**: 輸入精確的開始與結束秒數（支援小數點），即可迅速切出影片精華片段。
* **完全本機運行**: 基於 `moviepy` 函式庫完全在本機運算，不佔用任何雲端主機與硬碟空間。

---

## Prerequisites / 系統需求

* Python 3.x
* MoviePy 函式庫

### Installation / 安裝依賴

Before running the script, install the required dependency using pip:

在執行腳本之前，請先透過 pip 安裝所需的依賴套件：

```bash
pip install moviepy
```
