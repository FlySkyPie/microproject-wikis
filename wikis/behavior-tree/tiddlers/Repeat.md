Repeat 是一個 [Decorator](#Decorator)，行為如下： 

- 子節點回傳 SUCCEEDED 則：
  - 結束 Cycle，計數器加一
    - 計數器未達上限則：設定下一個 Cycle 為子節點。
- 子節點回傳 FAILED 則：
  - 結束 Cycle，設定下一個 Cycle 為 Root。