ReactiveFallback 用於處理需要持續監測前序條件的異步場景。

* **重啟機制**：與前兩者不同，當子節點回傳 RUNNING 時，下次 Tick 會從第一個子節點「重新開始」（Restart）。
* **中斷邏輯**：若先前失敗的條件節點狀態從 FAILURE 變為 SUCCESS，它會立即中斷當前正在執行的異步子節點。
* **應用範例**：例如「睡覺」行為。如果「是否休息充足？」這個條件變為 SUCCESS，則會立即中斷「睡覺」節點。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| ---| ---| ---|
| SUCCESS | 否 | - |
| FAILURE | 否 | - |
| RUNNING | 是 | 第一個 Child |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| ---| ---| ---|
| SUCCESS | 否 | ? |
| FAILURE | 否 | ? |
| RUNNING | - | 第一個 Child |