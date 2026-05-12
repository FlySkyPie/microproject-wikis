Switch Node 透過輸入埠（Input Ports）來定義判斷邏輯：

| 埠名稱 | 類型 | 描述 |
| :--- | :--- | :--- |
| `variable` | InputPort\<string\> | 要進行比較判斷的黑板變數。 |
| `case_1` | InputPort\<string\> | 第一個子節點的匹配值。 |
| `case_2` | InputPort\<string\> | 第二個子節點的匹配值。 |
| `case_N` | InputPort\<string\> | 依此類推，直到第 N 個案例。 |

比較邏輯支援字串、整數、倍精度浮點數（Double）以及透過 `ScriptingEnumsRegistry` 註冊的列舉值。