```
Qwen3TTSForConditionalGeneration(
  (talker): Qwen3TTSTalkerForConditionalGeneration(
    (model): Qwen3TTSTalkerModel(
      (layers): ModuleList(
        (0-27): 28 x Qwen3TTSTalkerDecoderLayer(
          (self_attn): Qwen3TTSTalkerAttention(
            (q_proj): Linear(in_features=2048, out_features=2048, bias=False)
            (k_proj): Linear(in_features=2048, out_features=1024, bias=False)
            (v_proj): Linear(in_features=2048, out_features=1024, bias=False)
            (o_proj): Linear(in_features=2048, out_features=2048, bias=False)
            (q_norm): Qwen3TTSRMSNorm((128,), eps=1e-06)
            (k_norm): Qwen3TTSRMSNorm((128,), eps=1e-06)
          )
          (mlp): Qwen3TTSTalkerTextMLP(
            (gate_proj): Linear(in_features=2048, out_features=6144, bias=False)
            (up_proj): Linear(in_features=2048, out_features=6144, bias=False)
            (down_proj): Linear(in_features=6144, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (input_layernorm): Qwen3TTSRMSNorm((2048,), eps=1e-06)
          (post_attention_layernorm): Qwen3TTSRMSNorm((2048,), eps=1e-06)
        )
      )
      (norm): Qwen3TTSRMSNorm((2048,), eps=1e-06)
      (rotary_emb): Qwen3TTSTalkerRotaryEmbedding()
      (codec_embedding): Embedding(3072, 2048)
      (text_embedding): Embedding(151936, 2048)
    )
    (text_projection): Qwen3TTSTalkerResizeMLP(
      (linear_fc1): Linear(in_features=2048, out_features=2048, bias=True)
      (linear_fc2): Linear(in_features=2048, out_features=2048, bias=True)
      (act_fn): SiLUActivation()
    )
    (codec_head): Linear(in_features=2048, out_features=3072, bias=False)
    (code_predictor): Qwen3TTSTalkerCodePredictorModelForConditionalGeneration(
      (model): Qwen3TTSTalkerCodePredictorModel(
        (layers): ModuleList(
          (0-4): 5 x Qwen3TTSDecoderLayer(
            (self_attn): Qwen3TTSAttention(
              (q_proj): Linear(in_features=1024, out_features=2048, bias=False)
              (k_proj): Linear(in_features=1024, out_features=1024, bias=False)
              (v_proj): Linear(in_features=1024, out_features=1024, bias=False)
              (o_proj): Linear(in_features=2048, out_features=1024, bias=False)
              (q_norm): Qwen3TTSRMSNorm((128,), eps=1e-06)
              (k_norm): Qwen3TTSRMSNorm((128,), eps=1e-06)
            )
            (mlp): Qwen3TTSTalkerTextMLP(
              (gate_proj): Linear(in_features=1024, out_features=3072, bias=False)
              (up_proj): Linear(in_features=1024, out_features=3072, bias=False)
              (down_proj): Linear(in_features=3072, out_features=1024, bias=False)
              (act_fn): SiLUActivation()
            )
            (input_layernorm): Qwen3TTSRMSNorm((1024,), eps=1e-06)
            (post_attention_layernorm): Qwen3TTSRMSNorm((1024,), eps=1e-06)
          )
        )
        (norm): Qwen3TTSRMSNorm((1024,), eps=1e-06)
        (rotary_emb): Qwen3TTSRotaryEmbedding()
        (codec_embedding): ModuleList(
          (0-14): 15 x Embedding(2048, 2048)
        )
      )
      (lm_head): ModuleList(
        (0-14): 15 x Linear(in_features=1024, out_features=2048, bias=False)
      )
      (small_to_mtp_projection): Linear(in_features=2048, out_features=1024, bias=True)
    )
  )
  (speaker_encoder): Qwen3TTSSpeakerEncoder(
    (blocks): ModuleList(
      (0): TimeDelayNetBlock(
        (conv): Conv1d(128, 512, kernel_size=(5,), stride=(1,), padding=same, padding_mode=reflect)
        (activation): ReLU()
      )
      (1): SqueezeExcitationRes2NetBlock(
        (tdnn1): TimeDelayNetBlock(
          (conv): Conv1d(512, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (activation): ReLU()
        )
        (res2net_block): Res2NetBlock(
          (blocks): ModuleList(
            (0-6): 7 x TimeDelayNetBlock(
              (conv): Conv1d(64, 64, kernel_size=(3,), stride=(1,), padding=same, dilation=(2,), padding_mode=reflect)
              (activation): ReLU()
            )
          )
        )
        (tdnn2): TimeDelayNetBlock(
          (conv): Conv1d(512, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (activation): ReLU()
        )
        (se_block): SqueezeExcitationBlock(
          (conv1): Conv1d(512, 128, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (relu): ReLU(inplace=True)
          (conv2): Conv1d(128, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (sigmoid): Sigmoid()
        )
      )
      (2): SqueezeExcitationRes2NetBlock(
        (tdnn1): TimeDelayNetBlock(
          (conv): Conv1d(512, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (activation): ReLU()
        )
        (res2net_block): Res2NetBlock(
          (blocks): ModuleList(
            (0-6): 7 x TimeDelayNetBlock(
              (conv): Conv1d(64, 64, kernel_size=(3,), stride=(1,), padding=same, dilation=(3,), padding_mode=reflect)
              (activation): ReLU()
            )
          )
        )
        (tdnn2): TimeDelayNetBlock(
          (conv): Conv1d(512, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (activation): ReLU()
        )
        (se_block): SqueezeExcitationBlock(
          (conv1): Conv1d(512, 128, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (relu): ReLU(inplace=True)
          (conv2): Conv1d(128, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (sigmoid): Sigmoid()
        )
      )
      (3): SqueezeExcitationRes2NetBlock(
        (tdnn1): TimeDelayNetBlock(
          (conv): Conv1d(512, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (activation): ReLU()
        )
        (res2net_block): Res2NetBlock(
          (blocks): ModuleList(
            (0-6): 7 x TimeDelayNetBlock(
              (conv): Conv1d(64, 64, kernel_size=(3,), stride=(1,), padding=same, dilation=(4,), padding_mode=reflect)
              (activation): ReLU()
            )
          )
        )
        (tdnn2): TimeDelayNetBlock(
          (conv): Conv1d(512, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (activation): ReLU()
        )
        (se_block): SqueezeExcitationBlock(
          (conv1): Conv1d(512, 128, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (relu): ReLU(inplace=True)
          (conv2): Conv1d(128, 512, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
          (sigmoid): Sigmoid()
        )
      )
    )
    (mfa): TimeDelayNetBlock(
      (conv): Conv1d(1536, 1536, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
      (activation): ReLU()
    )
    (asp): AttentiveStatisticsPooling(
      (tdnn): TimeDelayNetBlock(
        (conv): Conv1d(4608, 128, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
        (activation): ReLU()
      )
      (tanh): Tanh()
      (conv): Conv1d(128, 1536, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
    )
    (fc): Conv1d(3072, 2048, kernel_size=(1,), stride=(1,), padding=same, padding_mode=reflect)
  )
)
```