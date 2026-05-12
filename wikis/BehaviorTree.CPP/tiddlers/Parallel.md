[Parallel](<#Parallel>) 節點在達到指定的成功或失敗閾值時就會結束執行。

## 關鍵特性
- **早期停止**：一旦滿足 `success_count` 或 `failure_count`，節點會立即停止其餘仍在 `RUNNING` 狀態的子節點。
- **閾值配置**：
    - `success_count`: 成功子節點數達到此值則返回 `SUCCESS`。
    - `failure_count`: 失敗子節點數達到此值則返回 `FAILURE`。
- **負數索引**：支援 Python 風格，`-1` 代表子節點總數。

## 預設行為
預設情況下（`success_count="-1"`, `failure_count="1"`），所有子節點都必須成功才會返回 `SUCCESS`；只要有一個失敗，整個節點就返回 `FAILURE`。