Fallback 是最基礎的同步控制節點。

* **執行邏輯**：在單次 Tree Tick 中嘗試所有子節點。當一個子節點失敗時，立即在同一次呼叫中 Tick 下一個子節點。
* **RUNNING 處理**：當子節點回傳 RUNNING 時，下次 Tick 會從該節點繼續執行（Tick Again），不會重新檢查已失敗的前序節點。
* **適用場景**：適用於需要立即嘗試多個備案的情況，例如嘗試多種開門方式。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| ---| ---| ---|
| SUCCESS | 否 | - |
| FAILURE | 否 | - |
| RUNNING | 是 | RUNNING Child |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| ---| ---| ---|
| SUCCESS | 否 | ? |
| FAILURE | 否 | ? |
| RUNNING | - | RUNNING Child |