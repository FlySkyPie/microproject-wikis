即便該設計不同於數個已知「多模態嵌入」API 的設計，但是盡可能使用各種現有規範。

```shell
# Note: "input" also supports batch processing with arrays: ["text1", "text2", "text3"]
curl https://openrouter.ai/api/v1/embeddings \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "marksverdhei/Qwen3-Voice-Embedding-12Hz-1.7B",
    "input": "data:audio/mpeg;base64, iVBORw0KGgoAAAANSUhEUgAAAAUA
    AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO
        9TXL0Y4OHwAAAABJRU5ErkJggg==",
    "encoding_format": "float"
  }'
```

透過引入 RFC 2397 與 RFC 3003 並同時遵守 [OpenAI API](<#OpenAI API>) 的設計哲學並兼容 [OpenAI 嵌入 API](<#OpenAI 嵌入 API>)，同時擴增支援多模態的能力。

