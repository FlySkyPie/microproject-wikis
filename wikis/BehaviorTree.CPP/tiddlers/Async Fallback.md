AsyncFallback 與 Fallback 邏輯相似，但在子節點切換間具備「讓位」特性。

* **讓位機制**：當子節點失敗時，它會向樹回傳 RUNNING 並發出喚醒信號，將執行權交還。
* **可中斷性**：這種延遲 Tick 下一個子節點的特性，使其在子節點轉換間可以被中斷。
* **協作應用**：常用於 [ReactiveSequence](<#Async Fallback>) 之下。例如在尋找食物的過程中，每次嘗試失敗後都會重新評估「機器人是否還餓」的條件。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| ---| ---| ---|
| SUCCESS | 否 | - |
| FAILURE | 是 | 下一個 Child |
| RUNNING | 是 | RUNNING Child |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| ---| ---| ---|
| SUCCESS | 否 | ? |
| FAILURE | 否 | ? |
| RUNNING | - | RUNNING Child |