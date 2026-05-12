這兩種並行節點在處理策略上有明顯差異：

| 功能 | [Parallel](#Parallel) | [ParallelAll](#ParallelAll) |
| :--- | :--- | :--- |
| **早期終止** | 是（會停止剩餘子節點） | 否（執行所有子節點至結束） |
| **成功門檻** | 可配置的 `success_count` | 所有未失敗的子節點 |
| **失敗門檻** | 可配置的 `failure_count` | 可配置的 `max_failures` |
| **適用場景** | 競賽條件、N 取 M 成功 | 必須嘗試完成所有任務 |