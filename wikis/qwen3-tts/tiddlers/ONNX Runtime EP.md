![](#onnx-architecture.webp)

ONNX Runtime Execution Provider 是 [ONNX Runtime](<#ONNX Runtime>) 架構下的一種抽象，用於將機器學習運算與底層硬體解偶，透過這樣的架構允許在不修改上層程式碼的前提下抽換底層運算加速的實作，如：CUDA、WebGPU、CPU、XPU、FPGA...。