**Sequence** 是最基礎的順序節點。它在單次樹的 Tick（週期）中執行子節點。

當一個子節點回傳 SUCCESS 時，下一個子節點會**立即**在同一個呼叫中被執行。如果子節點回傳 FAILURE，序列會「[Restart](<#Sequence Control Rules>)」（從第一個子節點重新開始）。