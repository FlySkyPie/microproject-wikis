Python 單例可以透過以下方式實現：

```python
class AwesomeService:
    _instance = None

    def __new__(cls) -> Self:
        """
        Create Singleton
        """
        if cls._instance is None:
            cls._instance = super(AwesomeService, cls).__new__(cls)
            cls._instance._initialize_singleton()

        return cls._instance
      
def get_foo() -> AwesomeService:
    foo = AwesomeService()
    return foo
```

使用場合：

- 使用用戶端-伺服器架構（Client-server model）時，使 Client 端的 Socket 資源持續存在。