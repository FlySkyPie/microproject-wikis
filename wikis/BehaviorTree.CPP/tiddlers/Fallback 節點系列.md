Fallback 節點系列在其他框架中常被稱為「Selector」或「Priority」。其核心目的在於依序嘗試不同的策略，直到找到一個可行的方案為止。

目前框架提供三種主要類型：
* [Fallback](#Fallback)
* [AsyncFallback](<#Async Fallback>)
* [ReactiveFallback](<#Reactive Fallback>)

這些節點共享以下基本規則：
* 在 Tick 第一個子節點前，節點狀態變更為 **RUNNING**。
* 若子節點回傳 **FAILURE**，則 Tick 下一個子節點。
* 若所有子節點皆回傳 **FAILURE**，則整體回傳 **FAILURE** 並停止所有子節點。
* 若任一子節點回傳 **SUCCESS**，則整體回傳 **SUCCESS** 並停止所有子節點。