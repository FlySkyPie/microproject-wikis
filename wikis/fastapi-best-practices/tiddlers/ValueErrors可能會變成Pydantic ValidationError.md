
如果你在直接面向客戶端的Pydantic模式中引發`ValueError`，它將向使用者返回一個詳細的響應。

```python
# src.profiles.schemas
from pydantic import BaseModel, field_validator

class ProfileCreate(BaseModel):
    username: str
    
    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: str) -> str:
        if not re.match(STRONG_PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password

# src.profiles.routes
from fastapi import APIRouter

router = APIRouter()

@router.post("/profiles")
async def get_creator_posts(profile_data: ProfileCreate):
   pass
```

**響應示例：**

<img src="images/value_error_response.png" width="400" height="auto">
