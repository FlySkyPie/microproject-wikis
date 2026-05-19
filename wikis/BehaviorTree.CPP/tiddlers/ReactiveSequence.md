**ReactiveSequence** 專為持續檢查「條件」而設計。其特點在於即使子節點回傳 RUNNING，下一個 Tick 依然強制從第一個 Child 重新檢查。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | - |
| FAILURE | 是 | Root |
| RUNNING | 是 | Root |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | ? |
| FAILURE | 是 | Root |
| RUNNING | - | Root |