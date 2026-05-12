Repeat 節點會重複執行子節點 N 次，前提是子節點必須持續回傳 SUCCESS。

- **參數**：`num_cycles` (整數，-1 代表無限循環)。
- **成功條件**：完成所有 N 次重複後回傳 SUCCESS。
- **中斷條件**：若子節點回傳 FAILURE，則立即回傳 FAILURE 並中斷循環。
- **狀態處理**：子節點為 RUNNING 時不增加計數器；為 SKIPPED 時重置子節點但不計數。