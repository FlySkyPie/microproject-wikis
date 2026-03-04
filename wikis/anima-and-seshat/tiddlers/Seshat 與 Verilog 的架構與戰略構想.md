[Seshat](#Seshat) 將指關注於處理 [BNN](#BNN) 基因演算法的部份，[BNN Runtime](<#BNN Runtime>) 則交由 Verilog 處理，理由如下：

- [BNN](#BNN) 是一個新興且冷門的概念，無法使用現有的機器學習或人工智慧工具鏈，需要自行打造整個生態系，工作繁雜且龐大。
- [BNN 染色體](<#BNN 染色體>)和 [BNN Runtime](<#BNN Runtime>) 明顯屬於兩種問題領域 (Domain)。
- 作為「如何運行或模擬邏輯閘」的問題領域 (Problem Domain)，Verilog 是其對應的方案領域 (Solution Domain)。
- 「使用 Verilog 作為 [BNN Runtime](<#BNN Runtime>)」意味著將問題從「開發 [BNN Runtime](<#BNN Runtime>)」轉換成「將 [BNN 染色體](<#BNN 染色體>) 編譯成 Verilog」

在此架構下，[BNN Runtime](<#BNN Runtime>) 將分成三個階段（型態）：

1. 模擬階段
    1. 使用 Verilog 原本的生態系與工具鏈，以軟體模擬的方式運行。
2. 硬體加速階段
    1. 將 [BNN](#BNN) 編譯到 FPGA 上，實現硬體加速。
3. 佈署階段
    1. 將 [BNN](#BNN) 編譯成 Verilog，送廠製成晶片。