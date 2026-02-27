相較於 [Fork 遊戲方案](<#Fork 遊戲方案>)，[FlyPie](#FlyPie) 在其之上有著額外的立場：理解與改動的成本。

以 Martin 提到的事情為例：

> SuperTuxKart 是用 C++ 寫的，Code 很難。

Fork 現成的開源專案有「改不改得動」的問題，因此 [FlyPie](#FlyPie) 只考慮基於 Web, Javascript, Three.js...之類的方案，這些是 [FlyPie](#FlyPie) 比較熟悉的技術棧。

目前潛在的遊戲方案有：

- [https://github.com/mattbradley/dash](https://github.com/mattbradley/dash)
  - 314 ⭐
  - 非常陽春的平面實做，但是有基本的道路繪圖、自動駕駛...等實作可供參考。
- [https://github.com/RobertTBS/OLD-OLD-OLD-slowroads-OLD-OLD-OLD](https://github.com/RobertTBS/OLD-OLD-OLD-slowroads-OLD-OLD-OLD)
  - Slow Roads 是一個有在 Steam 上架的遊戲。
  - 它有一個網頁 Demo: https://slowroads.io/
  - Slow Roads 實做了大地圖動態生成與載入，是其跟其他駕駛類 Three.js 實作最大的差異，也是最有參考價值的一點
  - OLD-OLD-OLD-slowroads-OLD-OLD-OLD 是網頁 Demo 的快取
  - 它不是 source code，想要使用的話必須要逆向工程