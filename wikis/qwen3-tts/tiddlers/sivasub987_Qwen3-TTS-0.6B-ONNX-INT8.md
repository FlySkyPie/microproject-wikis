[Qwen3-TTS ONNX 移植先行者](<#已知 Qwen3-TTS ONNX 先行者>)之一，模型拆分方式：

| Model | Original | Quantized | Compression |
| --- | --- | --- | --- |
| talker_prefill | 1.69 GB | 448 MB | 75% |
| talker_decode | 1.69 GB | 448 MB | 75% |
| text_project | 1.21 GB | 317 MB | 75% |
| tokenizer12hz_decode | 436 MB | 221 MB | 52% |
| code_predictor | 420 MB | 111 MB | 75% |
| tokenizer12hz_encode | 184 MB | 76 MB | 61% |
| code_predictor_embed | 120 MB | 31 MB | 75% |
| speaker_encoder | 34 MB | 9.3 MB | 73% |
| codec_embed | 12 MB | 3.1 MB | 75% |
| **Total** | **6.1 GB** | **1.6 GB** | **73%** |

專案問題：

- 僅處理 0.6B，我要的是 1.7B。
- 已經經過量化，具有推論品質下降之風險。
- 專案本身沒有附上開源許可證。
- 模型與 SDK 未拆分。


專案連結：[https://huggingface.co/sivasub987/Qwen3-TTS-0.6B-ONNX-INT8](https://huggingface.co/sivasub987/Qwen3-TTS-0.6B-ONNX-INT8)
