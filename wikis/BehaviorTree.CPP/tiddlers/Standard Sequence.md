Standard 是最基本的序列節點，在同一個 Tick 內會盡可能向後執行。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | - |
| FAILURE | 是 | Root |
| RUNNING | 是 | RUNNING Children |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | ? |
| FAILURE | 是 | Root |
| RUNNING | - | RUNNING Children |