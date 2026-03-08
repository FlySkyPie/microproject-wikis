在 [五層理論](<#FlyPie 的軟體工程五層理論>)基礎之上，[FlyPie](#FlyPie) 建立一套從上而下的重用策略。了解到解決問題最好的方法可能不是寫程式（開發軟體），面對需求時先問一個問題：

> 這個需求是否已經被解決過了？

## E2E 解決方案

市場或生態系上是否已經存在完整的 E2E 解決方案？例如：

- 電子商務 -> Shopify 或其他類似方案。
- CMS (content management system) -> WordPress 或其他類似方案。
- 試算表軟體 -> LibreOffice 或其他類似方案。
- 專案管理 -> OpenProject 或其他類似方案。
- etc.

## 軟體解決方案

市場或生態系上是否已經存在解決部份問題的軟體（E2E 以下；函式庫以上）？例如：

- RDBMS (relational database management system) -> MySQL 或其他類似軟體。
- NoSQL 資料庫 -> MongoDB 或其他類似軟體。
- Authentication -> Keyclock 或其他類似軟體。
- Authorization -> OpenFGA 或其他類似軟體。
- 影音編解碼 -> FFmpeg 或其他類似軟體。
- etc.

## 函式庫解決方案

市場或生態系上是否已經存在程式碼實作？例如：

- Material Design -> `mui/material-ui` 或其他類似函式庫。
- 影音編解碼 -> GStreamer
- WebGL 抽象化 -> Three.js
- etc.

## 部份引用

即便不直接使用上述解決方案，依然可以參考該解決方案的已經存在的：

- 領域模型
- 程式碼
- 界面設計
- 軟體架構
- 程式碼架構

---

最後一步才是自己動手實做。