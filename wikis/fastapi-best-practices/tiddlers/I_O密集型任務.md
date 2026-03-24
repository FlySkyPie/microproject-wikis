
在底層，FastAPI可以有效地處理非同步和同步I/O操作。

- FastAPI線上程池中運行同步路由，阻塞的I/O操作不會阻止事件循環執行任務。
- 如果路由定義為`async`，那麼它會通過`await`正常呼叫，FastAPI相信你只會執行非阻塞的I/O操作。

需要注意的是，如果你違反了這種信任，在非同步路由中執行阻塞操作，事件循環將無法在阻塞操作完成之前運行後續任務。

```python
import asyncio
import time

from fastapi import APIRouter

router = APIRouter()

@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10) # 10秒的I/O阻塞操作，整個處理程序都會被阻塞

    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(10) # 10秒的I/O阻塞操作，但在單獨的執行緒中運行整個`good_ping`路由

    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10) # 非阻塞I/O操作

    return {"pong": True}
```

**當我們呼叫時會發生什麼：**

1. `GET /terrible-ping`
    1. FastAPI伺服器接收請求並開始處理
    2. 伺服器的事件循環和佇列中的所有任務都將等待`time.sleep()`完成
        1. 伺服器認為`time.sleep()`不是I/O任務，所以會等待它完成
        2. 等待期間，伺服器不會接受任何新請求
    3. 伺服器返迴響應。
        1. 響應之後，伺服器開始接受新請求
2. `GET /good-ping`
    1. FastAPI伺服器接收請求並開始處理
    2. FastAPI將整個路由`good_ping`傳送到執行緒池，工作執行緒將在那裡運行該函數
    3. 在`good_ping`執行期間，事件循環從佇列中選擇下一個任務並處理它們（例如接受新請求、呼叫資料庫）
        - 獨立於主執行緒（即我們的FastAPI應用），工作執行緒將等待`time.sleep`完成。
        - 同步操作只阻塞子執行緒，而不是主執行緒。
    4. 當`good_ping`完成工作後，伺服器向客戶端返迴響應
3. `GET /perfect-ping`
    1. FastAPI伺服器接收請求並開始處理
    2. FastAPI等待`asyncio.sleep(10)`
    3. 事件循環從佇列中選擇下一個任務並處理它們（例如接受新請求、呼叫資料庫）
    4. 當`asyncio.sleep(10)`完成後，伺服器完成路由的執行並向客戶端返迴響應

> [!WARNING]
關於執行緒池的注意事項：
> 
> - 執行緒比協程需要更多資源，因此它們不像非同步I/O操作那樣輕量。
> - 執行緒池的執行緒數量是有限的，也就是說，你可能會耗盡執行緒，導致應用變慢。[瞭解更多](https://github.com/Kludex/fastapi-tips?tab=readme-ov-file#2-be-careful-with-non-async-functions)（外部連結）
