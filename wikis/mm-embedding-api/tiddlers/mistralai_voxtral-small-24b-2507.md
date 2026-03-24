Voxtral Small 是 Mistral Small 3 的增強版，它融合了最先進的音訊輸入功能，同時保持了同類最佳的文字處理性能。它在語音轉錄、翻譯和音訊理解方面表現出色。音訊輸入的價格為每百萬秒 100 美元。

使用方式如下：

```shell
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
  "model": "mistralai/voxtral-small-24b-2507",
  "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this audio?"
          },
          {
            "type": "input_audio",
            "input_audio": {
              "data": "UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB",
              "format": "wav"
            }
          }
        ]
      }
    ]
  
}'
```