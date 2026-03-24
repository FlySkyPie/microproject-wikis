如果你必須使用一個庫與外部服務互動，並且它不是非同步的，那麼在外部工作執行緒中進行HTTP呼叫。

我們可以使用starlette中著名的`run_in_threadpool`。

```python
from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from my_sync_library import SyncAPIClient 

app = FastAPI()

@app.get("/")
async def call_my_sync_library():
    my_data = await service.get_my_data()

    client = SyncAPIClient()
    await run_in_threadpool(client.make_request, data=my_data)
```