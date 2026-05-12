`WhileDoElse` 是 `IfThenElse` 的**響應式 (Reactive)** 變體，會在每個 Tick 重新評估條件。
- **執行邏輯**：
    - 第 1 個子節點：條件 (While)，每 Tick 評估一次。
    - 第 2 個子節點：條件為 SUCCESS 時持續執行 (Do)。
    - 第 3 個子節點（可選）：條件為 FAILURE 時持續執行 (Else)。
- **中斷機制**：若執行中的子節點（2或3）處於 RUNNING 狀態但條件結果發生改變，該子節點會被**中止 (Halted)** 並切換分支。
- 關聯：比較兩者的差異 [Comparison of Conditional Nodes](<#Comparison of Conditional Nodes>)。