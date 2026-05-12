Parallel Nodes 是一種特殊的控制節點，允許所有子節點**並行 (Concurrently)** 執行。與序列節點不同，Parallel Nodes 是唯一可以讓多個子節點同時處於 `RUNNING` 狀態的節點類型。

雖然稱為「並行」，但這並不代表多線程執行。在行為樹的單次 Tick 中，所有子節點仍是在同一個線程中依序被 Tick。若需要真正的多線程，子節點本身必須是異步節點。

目前框架提供兩種類型：
- [Parallel](#Parallel)
- [ParallelAll](#ParallelAll)