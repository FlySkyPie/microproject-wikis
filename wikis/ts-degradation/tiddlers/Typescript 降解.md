為了解決 [大型 Typescript 專案重構痛點](<#大型 Typescript 專案重構痛點>) 的解決方案之一。

## 目標

給定一 Typescript 檔案，輸出 tar 包含多個經過分解的單一職責程式碼。

## 子任務

- 辨識所有頂級 export
- 辨識所有 import
- 辨識所有未定義
- 根據頂級 export 拆分成多個段落
- 對每個段落進行未定義辨識
- 從已知的 import 解決未定義變數

## 技術

Typescript [AST](#AST)。

## 命名

「降解 (Degradation)」一詞原本用於有機分子的領域，這裡使用了與 [FlyPie 的生物學借鏡](<#FlyPie 的生物學借鏡>)相同的概念。