`LCO-Embedding-Omni-7B-GGUF` 是由 [marksverdhei](#marksverdhei) 量化並上傳的多模態嵌入模型。

以 llama.cpp 運行[嵌入運算](#嵌入運算)伺服器時使用方式如下。

文字嵌入：

```shell
curl -s http://localhost:8080/embeddings \
  -d '{"content": "Your text here"}'
```

照片嵌入：

```shell
curl -s http://localhost:8080/embeddings \
  -d '{"content": [{"prompt_string": "<__media__>", "multimodal_data": ["<base64-image-data>"]}]}'
```

音訊 (WAV) 嵌入：

```shell
curl -s http://localhost:8080/embeddings \
  -d '{"content": [{"prompt_string": "<__media__>", "multimodal_data": ["<base64-audio-data>"]}]}'
```

注意：該 API 定義不兼容於 [OpenAI 嵌入 API](<#OpenAI 嵌入 API>)。