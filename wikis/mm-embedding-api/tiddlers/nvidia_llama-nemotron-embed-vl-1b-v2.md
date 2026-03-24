Llama Nemotron Embed VL 1B V2 嵌入模型針對多模態問答檢索進行了最佳化。該模型可以[嵌入](#嵌入運算)圖像、文字或圖文組合形式的「文件」。使用者可以透過文字形式的查詢來檢索文件。此模型支援包含文字、表格、圖表和資訊圖表的圖像。

該模型是 OpenRouter 上目前 (2026-03-24) 唯一支援文字以外輸入的[嵌入](#嵌入運算)模型。

使用方式如下：

```shell
curl https://openrouter.ai/api/v1/embeddings \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nvidia/llama-nemotron-embed-vl-1b-v2:free",
    "input": [
      {
        "content": [
          {"type": "text", "text": "What is in this image?"},
          {"type": "image_url", "image_url": {"url": "https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg"}}
        ]
      }
    ],
    "encoding_format": "float"
  }'
```

注意：該 API 定義不兼容於 [OpenAI 嵌入 API](<#OpenAI 嵌入 API>)。