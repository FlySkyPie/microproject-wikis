
有了程式碼檢查工具，你可以忘記程式碼格式化，專注於編寫業務邏輯。

[Ruff](https://github.com/astral-sh/ruff)是一個“速度極快”的新程式碼檢查工具，它替代了black、autoflake、isort，並支援600多個檢查規則。

使用pre-commit鉤子是一種流行的最佳實踐，但對我們來說，只使用指令碼就足夠了。

```bash
#!/bin/sh -e
set -x

ruff check --fix src
ruff format src
```