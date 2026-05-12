**AsyncSequence** 的邏輯與標準 Sequence 相似，但處理子節點切換的方式不同。

- **Yields execution**：在每個子節點成功後，它會將執行權交還給樹，回傳 RUNNING 並發出喚醒信號。
- **可中斷性**：這使得序列在子節點之間是可中斷的，允許父節點（如 [ReactiveSequence](#ReactiveSequence)）在下一個子節點開始前重新評估條件。

這適用於需要在執行步驟間持續檢查環境變化的情境。