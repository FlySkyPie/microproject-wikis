[Qwen3-TTS ONNX 移植先行者](<#已知 Qwen3-TTS ONNX 先行者>)之一，專案結構：

```
├── README.md                       # This file
├── onnx_inference.py               # Core inference engine (library)
├── generate_cache.py               # Step 1: Generate global embedding cache
├── create_speaker.py               # Step 2: Create speaker profile
├── synthesize.py                   # Step 3: Synthesize speech
├── requirements.txt                # Python dependencies
├── voice_clone_config.json         # Model config (voice clone)
├── voice_design_config.json        # Model config (voice design)
├── dual_model_config.json          # Combined model config
├── tokenizer/                      # Tokenizer files
│   ├── tokenizer.json              # Rust tokenizer (recommended, fast)
│   ├── vocab.json                  # BPE vocabulary
│   ├── merges.txt                  # BPE merge rules
│   └── tokenizer_config.json       # Tokenizer config
├── fp16/                           # FP16 ONNX models (recommended)
│   ├── shared/                     # Shared models (speaker encoder, speech tokenizer)
│   │   ├── speaker_encoder.onnx
│   │   ├── speech_tokenizer_encoder.onnx
│   │   └── speech_tokenizer_decoder.onnx
│   ├── voice_clone/                # Voice Clone talker models + cache
│   │   ├── talker_decode.onnx
│   │   ├── code_predictor.onnx
│   │   ├── code_predictor_kv.onnx
│   │   ├── text_embedding.onnx
│   │   ├── codec_embedding.onnx
│   │   ├── code_predictor_embed_g*.onnx
│   │   ├── model_cache.npz         # Pre-computed global cache
│   │   └── *.weight                # External data files for ONNX models
│   └── voice_design/               # Voice Design talker models + cache
│       ├── talker_decode.onnx
│       ├── code_predictor.onnx
│       ├── code_predictor_kv.onnx
│       ├── text_embedding.onnx
│       ├── codec_embedding.onnx
│       ├── code_predictor_embed_g*.onnx
│       ├── model_cache.npz
│       └── *.weight
└── onnx/                           # FP32 ONNX models (alternative)
    └── (same structure as fp16/)
```

專案問題：

- DLL 是針對 Windows 建構的，無法在 Linux 下使用。
- 專案本身沒有附上開源許可證。
- 模型與 SDK 未拆分。
- 模型拆分的方式很瑣碎，疑似一層一個檔案。
- SDK 封裝差勁，需要一些額外的預建置步驟。

專案連結：[https://huggingface.co/xkos/Qwen3-TTS-12Hz-1.7B-ONNX](https://huggingface.co/xkos/Qwen3-TTS-12Hz-1.7B-ONNX)