
FastAPI同時支援同步和非同步依賴項，當你不需要等待任何東西時，很容易會想使用同步依賴項，但這可能不是最佳選擇。

與路由一樣，同步依賴項線上程池中運行。這裡的執行緒也有代價和限制，如果只是進行小的非I/O操作，這些代價和限制是多餘的。

[瞭解更多](https://github.com/Kludex/fastapi-tips?tab=readme-ov-file#9-your-dependencies-may-be-running-on-threads)（外部連結）
