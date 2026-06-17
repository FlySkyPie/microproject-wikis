SketchbookECS 是 [SketchbookWar](#SketchbookWar) 的子專案或前置專案。目標是在盡可能少損失 [Sketchbook](#Sketchbook) 原生功能的前提下將程式碼從 OOP 風格重構成 [ECS](#ECS) 風格。

## 技術棧

- miniplex
  - 作為 Entity-Component 的框架，雖然不如其他 ECS 框架有實現高密度資料堆，主要依然使用 Object，但是原生支援 Typescript 且有良好的型別設計可以提高開發體驗，並且更適合和 Three.js 這種高度 OOP 封裝的函式庫使用，而無須從頭依照 ECS 的邏輯撰寫輪子。
- inversify
  - IoC 框架，作為統整 System 的組織層，除了作為 Legacy OOP 實例與 ECS 之間的兼容層，也有將原本 OOP 架構中巢狀的實例關係輾平的作用。
- rapier.js
  - 當原始實作已經完全遷移到 ECS 架構，用 rapier 取代 Cannon.js，預期獲得性能提昇。

## 重構策略

- [OOP-ECS 兼容策略](<#OOP-ECS 兼容策略>)