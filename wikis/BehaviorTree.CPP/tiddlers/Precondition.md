Precondition 節點在 Tick 子節點前會先評估腳本條件。

- **if**：要評估的腳本條件。
- **else**：當條件為 false 時回傳的狀態（預設為 FAILURE）。
- **特性**：一旦子節點進入 RUNNING 狀態，除非設定 `else="RUNNING"` 來實現逐 Tick 評估，否則在子節點完成前不會重新評估條件。