在行為樹框架中，**Sequence**（順序節點）是一種控制節點。只要其子節點回傳 SUCCESS，它就會持續執行下一個子節點。一旦任何子節點回傳 FAILURE，整個序列就會中斷。

目前框架提供四種主要的 Sequence 類型：
- [Sequence](<#Standard Sequence>)
- [AsyncSequence](#AsyncSequence)
- [SequenceWithMemory](#SequenceWithMemory)
- [ReactiveSequence](#ReactiveSequence)

這些節點共有一些基本規則：
1. 在執行第一個子節點前，節點狀態變更為 **RUNNING**。
2. 若最後一個子節點也回傳 SUCCESS，則序列完成並回傳 **SUCCESS**。