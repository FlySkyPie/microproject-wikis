Timeout 節點用於監控子節點的執行時間。

- **行為**：如果子節點處於 RUNNING 狀態的時間超過了 `msec` 設定的時長，該子節點會被中止 (Halt) 並且 Timeout 節點會回傳 FAILURE。
- **應用**：常與 [RetryUntilSuccessful](#RetryUntilSuccessful) 組合，形成「具備超時機制的重試模式」。