為了區分不同 Sequence 的行為，框架定義了以下幾種反應模式：

| 類型 | 子節點回傳 FAILURE | 子節點回傳 RUNNING | 在子節點間 Yield |
| :--- | :--- | :--- | :--- |
| [Sequence](<#Standard Sequence>) | Restart | Tick again | No |
| [AsyncSequence](#AsyncSequence) | Restart | Tick again | Yes |
| [ReactiveSequence](#ReactiveSequence) | Restart | Restart | No |
| [SequenceWithMemory](#SequenceWithMemory) | Tick again | Tick again | No |

- **Restart**：整個序列從第一個子節點重新開始執行。
- **Tick again**：下次 Tick 時，直接執行同一個子節點，跳過先前已成功的兄弟節點。