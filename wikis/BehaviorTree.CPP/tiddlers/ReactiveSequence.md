**ReactiveSequence** 專為持續檢查「條件」而設計。

與一般 Sequence 不同，當子節點回傳 RUNNING 時，ReactiveSequence 下次會選擇「[Restart](<#Sequence Control Rules>)」而非僅僅「Tick again」。這意味著它每一週期都會重新從第一個子節點開始檢查。

**範例**：
若使用 ReactiveSequence 檢查「敵人是否可見」並執行「靠近敵人」，一旦敵人消失（條件回傳 FAILURE），「靠近敵人」的動作會立即被中斷。