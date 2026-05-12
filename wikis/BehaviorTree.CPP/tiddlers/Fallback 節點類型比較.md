這三種控制節點在處理子節點回傳 RUNNING 以及節點間過渡的差異如下表所示：

| 控制節點類型 | 子節點回傳 RUNNING 時 | 子節點間是否讓位 (Yield) |
| :--- | :---: | :---: |
| [Fallback](#Fallback) | Tick Again | 否 |
| [Async Fallback](<#Async Fallback>) | Tick Again | 是 |
| [Reactive Fallback](<#Reactive Fallback>) | Restart | 否 |



* **Tick Again**：下次 Tick 從同一個子節點開始，跳過已失敗的節點。
* **Restart**：下次 Tick 重新從第一個子節點開始評估。