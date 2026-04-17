Qwen3-TTS-12Hz-1.7B-Base 是 [Qwen3-TTS](#Qwen3-TTS) 系列中的模型之一，它的主要功能為語音複製，例如，給定一語音作為樣本，並進行 TTS：

```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

ref_audio = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/clone.wav"
ref_text  = "Okay. Yeah. I resent you. I love you. I respect you. But you know what? You blew it! And thanks to you."

wavs, sr = model.generate_voice_clone(
    text="I am solving the equation: x = [-b ± √(b²-4ac)] / 2a? Nobody can — it's a disaster (◍•͈⌔•͈◍), very sad!",
    language="English",
    ref_audio=ref_audio,
    ref_text=ref_text,
)
sf.write("output_voice_clone.wav", wavs[0], sr)
```

又如，給定一語音嵌入向量作為語音特徵，並進行 TTS：

```python
prompt = VoiceClonePromptItem(
    ref_code=None,
    ref_spk_embedding=embedding,
    x_vector_only_mode=True,
    icl_mode=False,
)

# 3. Load the TTS model
from qwen_tts import Qwen3TTSModel

tts = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base", device_map="cuda:0",
)

# 4. Generate speech — reusable across any text
wavs, sr = tts.generate_voice_clone(
    text="Hello from a stored embedding!",
    language="English",
    voice_clone_prompt=prompt,
)
sf.write("output.wav", wavs[0], sr)
```