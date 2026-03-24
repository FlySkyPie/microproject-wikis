你可能認為可以返回與路由的`response_model`匹配的Pydantic對象來進行一些最佳化，但你錯了。

FastAPI首先使用其`jsonable_encoder`將該pydantic對象轉換為字典，然後使用你的`response_model`驗證資料，最後才將你的對象序列化為JSON。

這意味著你的Pydantic模型對象會被建立兩次：

- 第一次，當你顯式建立它以從路由返回時。
- 第二次，FastAPI隱式建立它以根據response_model驗證響應資料。

```python
from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()

class ProfileResponse(BaseModel):
    @model_validator(mode="after")
    def debug_usage(self):
        print("created pydantic model")

        return self

@app.get("/", response_model=ProfileResponse)
async def root():
    return ProfileResponse()

```

**日誌輸出：**

```
[INFO] [2022-08-28 12:00:00.000000] created pydantic model
[INFO] [2022-08-28 12:00:00.000020] created pydantic model

```
