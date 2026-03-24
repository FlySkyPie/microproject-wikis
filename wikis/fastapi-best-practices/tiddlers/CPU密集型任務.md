
第二個需要注意的是，非阻塞的可等待對象或傳送到執行緒池的操作必須是I/O密集型任務（例如打開檔案、資料庫呼叫、外部API呼叫）。

- 等待CPU密集型任務（例如繁重的計算、資料處理、視訊轉碼）是沒有意義的，因為CPU必須工作才能完成這些任務，而I/O操作是外部的，伺服器在等待這些操作完成時什麼也不做，因此它可以處理下一個任務。
- 在其他執行緒中運行CPU密集型任務也不是有效的，因為[GIL（全域直譯器鎖）](https://realpython.com/python-gil/)的存在。簡而言之，GIL只允許一個執行緒同時工作，這使得它對CPU任務毫無用處。
- 如果你想最佳化CPU密集型任務，你應該將它們傳送到另一個處理程序中的工作節點。

**困惑使用者的相關StackOverflow問題**

1. [https://stackoverflow.com/questions/62976648/architecture-flask-vs-fastapi/70309597#70309597](https://stackoverflow.com/questions/62976648/architecture-flask-vs-fastapi/70309597#70309597)
    - 在這裡你也可以查看[我的回答](https://stackoverflow.com/a/70309597/6927498)
2. [https://stackoverflow.com/questions/65342833/fastapi-uploadfile-is-slow-compared-to-flask](https://stackoverflow.com/questions/65342833/fastapi-uploadfile-is-slow-compared-to-flask)
3. [https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion](https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion)
