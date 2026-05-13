Selector 是一個[組合節點](#組合節點)，在某些框架中亦被稱作 Fallback，行為如下：

- 循序遍歷子節點。
- 當下 Cycle 子節點回傳 Failure，則在當下 Cycle 遍歷下一個子節點。
- 當下 Cycle 子節點回傳 Success，則在當下讓父節點繼續遍歷。
- 當下 Cycle 子節點回傳 Running，則中止當下 Cycle，下個 Cycle 從 Running 的子節點開始。