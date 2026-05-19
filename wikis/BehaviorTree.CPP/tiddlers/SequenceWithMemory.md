**SequenceWithMemory** 用於不希望重複執行已經成功過的子節點的情況。其特點在於 FAILURE 時不會導致重頭開始，而是保留當前的執行進度。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | - |
| FAILURE | 是 | FAILURE Children |
| RUNNING | 是 | RUNNING Children |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | ? |
| FAILURE | 是 | FAILURE Children |
| RUNNING | - | RUNNING Children |