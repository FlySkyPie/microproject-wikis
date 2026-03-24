[OpenAI 嵌入 API](<#OpenAI 嵌入 API>) 設計上只能處理「文字→向量」的[嵌入運算](#嵌入運算)，從官方的規格書可以看到：

![](#CreateEmbeddingRequest.webp)

輸入必然為字串，原因是 OpenAI 提供的嵌入模型僅有：`text-embedding-3-small`、`text-embedding-3-large` 和 `text-embedding-ada-002` 這幾款文字嵌入模型，因此無法處理多模態問題；嵌入音訊、影像、圖像。