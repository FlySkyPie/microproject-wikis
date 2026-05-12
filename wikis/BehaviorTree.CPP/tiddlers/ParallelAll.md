[ParallelAll](<#ParallelAll>) 與 [Parallel](#Parallel) 的最大區別在於它**永遠會執行完所有的子節點**，不會提前中止任何子節點。這對於需要確保所有副作用（Side effects）都完成的場景非常有用。

## 關鍵參數
- `max_failures`: 允許子節點失敗的最大數量。
    - 如果失敗數量 **小於** `max_failures`，返回 `SUCCESS`。
    - 如果失敗數量 **等於或超過** `max_failures`，返回 `FAILURE`。

## 特殊配置
若將 `max_failures` 設為 `-1`（等同於子節點總數），則無論子節點結果如何，該節點都會返回 `SUCCESS`。