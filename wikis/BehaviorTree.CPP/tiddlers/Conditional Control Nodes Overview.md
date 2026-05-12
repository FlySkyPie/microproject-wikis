這些控制節點根據條件子節點（第一個子節點）的結果來選擇執行哪一個後續子節點。框架目前提供兩種主要類型：[IfThenElse](<#IfThenElse Node>) 與 [WhileDoElse](<#WhileDoElse Node>)。
- 限制：必須擁有恰好 2 個或 3 個子節點。
- 核心邏輯：第一子節點永遠是條件判斷。