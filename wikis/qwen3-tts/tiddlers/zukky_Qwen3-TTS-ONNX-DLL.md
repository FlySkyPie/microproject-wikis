[Qwen3-TTS ONNX 移植先行者](<#已知 Qwen3-TTS ONNX 先行者>)之一，專案結構：

```
├── qwen3_tts_rust.dll
├── qwen3_tts.h
├── README_dll_release.txt
├── README.md
├── onnx_kv/                      # 1.7B ONNX, embedded weights
├── onnx_kv_06b/                  # 0.6B ONNX, embedded weights (optional)
├── models/
│   ├── Qwen3-TTS-12Hz-1.7B-Base/
│   │   ├── config.json
│   │   ├── vocab.json
│   │   ├── merges.txt
│   │   └── tokenizer_config.json
│   └── Qwen3-TTS-12Hz-0.6B-Base/
│       ├── config.json
│       ├── vocab.json
│       ├── merges.txt
│       └── tokenizer_config.json
└── examples/python_dll_call/
    └── run_pipeline.py
```

`onnx_kv/` 內容：

| 檔案名稱 | 檔案大小 |
| :--- | :--- |
| `code_predictor.onnx` | 449 MB |
| `code_predictor_embed.onnx` | 252 MB |
| `codec_embed.onnx` | 25.2 MB |
| `speaker_encoder.onnx` | 48.2 MB |
| `talker_decode.onnx` | 5.67 GB |
| `talker_prefill.onnx` | 5.67 GB |
| `text_project.onnx` | 1.28 GB |
| `tokenizer12hz_decode.onnx` | 457 MB |
| `tokenizer12hz_encode.onnx` | 193MB |

專案問題：

- DLL 是針對 Windows 建構的，無法在 Linux 下使用。
- 專案本身沒有附上開源許可證。
- 模型與 SDK 未拆分。

專案連結：[https://huggingface.co/zukky/Qwen3-TTS-ONNX-DLL](https://huggingface.co/zukky/Qwen3-TTS-ONNX-DLL)