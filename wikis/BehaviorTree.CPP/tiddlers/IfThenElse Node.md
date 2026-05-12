`IfThenElse` 是一種**非響應式 (Non-reactive)** 的條件節點。
- **執行邏輯**：
    - 第 1 個子節點：條件 (If)。
    - 第 2 個子節點：條件回傳 SUCCESS 時執行 (Then)。
    - 第 3 個子節點（可選）：條件回傳 FAILURE 時執行 (Else)。
- **行為特性**：
    - 條件僅在開始時**評估一次**。
    - 若後續子節點進入 RUNNING 狀態，條件不會在後續的 Tick 中重新評估。
    - 若無第三子節點且條件失敗，則整體回傳 FAILURE。
- 關聯：對比動態監控的 [WhileDoElse](<#WhileDoElse Node>)。