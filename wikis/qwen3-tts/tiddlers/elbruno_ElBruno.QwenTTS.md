[Qwen3-TTS ONNX 移植先行者](<#已知 Qwen3-TTS ONNX 先行者>)之一。

SDK 程式碼：[https://github.com/elbruno/ElBruno.QwenTTS](https://github.com/elbruno/ElBruno.QwenTTS)

模型頁面：[https://huggingface.co/elbruno/Qwen3-TTS-12Hz-0.6B-Base-ONNX](https://huggingface.co/elbruno/Qwen3-TTS-12Hz-0.6B-Base-ONNX)

模型拆分方式：

| File | Description | Size |
| --- | --- | --- |
| `speaker_encoder.onnx` + `.data` | ECAPA-TDNN speaker encoder | ~34 MB |
| `talker_prefill.onnx` + `.data` | Talker LM prefill (28 layers) | ~1.7 GB |
| `talker_decode.onnx` + `.data` | Talker LM single-step decode | ~1.7 GB |
| `code_predictor.onnx` | Code Predictor (5 layers, 15 groups) | ~440 MB |
| `vocoder.onnx` | Vocoder decoder (24kHz output) | ~2.7 MB |
| `embeddings/` | Text/codec embeddings as .npy + config | ~1.4 GB |
| `tokenizer/` | BPE tokenizer (vocab.json, merges.txt) | ~4 MB |

專案問題：

- SDK 為 C#，需要的是 Python。
- 僅移植 `Qwen3-TTS-12Hz-0.6B-Base` 而沒有移植 `Qwen3-TTS-12Hz-1.7B-Base`。