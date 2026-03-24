Pydantic有豐富的功能來驗證和轉換資料。

除了常規功能（如帶有預設值的必填和非必填欄位），Pydantic還有內建的綜合資料處理工具，如正規表示式、列舉、字串操作、電子郵件驗證等。

```python
from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field

class MusicBand(str, Enum):
   AEROSMITH = "AEROSMITH"
   QUEEN = "QUEEN"
   ACDC = "AC/DC"

class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=128)
    username: str = Field(min_length=1, max_length=128, pattern="^[A-Za-z0-9-_]+$")
    email: EmailStr
    age: int = Field(ge=18, default=None)  # 必須大於或等於18
    favorite_band: MusicBand | None = None  # 只允許輸入"AEROSMITH"、"QUEEN"、"AC/DC"值
    website: AnyUrl | None = None
```