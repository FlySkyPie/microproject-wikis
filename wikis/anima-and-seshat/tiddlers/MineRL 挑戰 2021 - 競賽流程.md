## 第一階段：一般規則

在這個階段中，團隊最多可以有六名成員，以下為參賽流程：

1. 在 AICrowd 競賽網站上註冊並使用下列資料。 或者，可以使用競賽的頁面上找到 "Create Team" 的按鈕組建隊伍（必須登入才能創建隊伍）。
    1. 用於運行競賽任務環境的[入門代碼](https://github.com/minerllabs/competition_submission_starter_template)。 另請參閱 AICrowd 上的 "Notebooks" 部分。
    2. 主辦方提供的[基本實作](https://github.com/minerllabs/baselines)。
    3. [人類玩家的資料集](https://minerl.io/dataset/)
    4. 主辦方用來評分參賽隊伍提交模型時使用的 Docker image 和[入門模板](https://github.com/minerllabs/competition_submission_template)。
    5. 支援主流的付費雲端運算服務，用於測試參賽者提交的樣本效率。 
2. 使用主辦方提供的人類玩家資料集來開發與測試模型的訓練效果，以製作出能達成比賽課題的程式。
3. 編寫以及訓練參賽隊伍的 agents。
    1.  Intro 組，撰寫/訓練他們的模型以達成 `MineRLObtainDiamond-v0` 環境課題。 當他們對模型感到滿意時，提交他們經過訓練的模型進行評分。
    2.  Research 組，在四天內只能使用 8,000,000 個環境樣本訓練他們的模型以達成 `MineRLObtainDiamondVectorObf-v0` 環境課題。 提交的模板將包含用於訓練和評分 agent 的腳本（在評分的伺服器上也是使用相同的腳本）。 
4. 當參賽隊伍對模型感到滿意時，提交他們經過訓練的模型進行評分。 自動化評分系統會將提交的程式放置在測試用的環境中進行評分，並計算與回報競賽排行榜上的積分。 
5. 重複步驟 2 到步驟 4 直到第一屆階段截止！

當第一階段完成後，主辦方將會：

- 檢查排行榜上分數最高的提交的程式碼，以確保其符合比賽規則。 
- Research 組
  - 符合比賽規則的最高分提交將自動由比賽編排平台重新訓練。 
  - 執行生成的模型數百回合並對其評分，以決定最終排名。 
  - Fork 團隊提交的程式碼，並清除任何大於 30MB 的文件，以確保參與者在後續輪次中不使用任何預先訓練的模型。

## 第二階段：決賽 （僅適用 Research 組）

在這個階段中中，來自 Research 組的前 15 名團隊將繼續開發他們的算法。 他們的作品將會在某種對所有參賽者保密的環境與額外的資料集中進行測試與評分。 

參賽者將能夠在第 2 階段期間每兩週提交最多一次程式碼。對於每次提交，自動評分器將在額外的測試數據集和模擬器上訓練他們的程序，評分訓練後的模型，並報告分數和指標返回給參賽者。最終排名將基於每個團隊在第二階段中表現最好的提交 。

原文：https://www.aicrowd.com/challenges/neurips-2021-minerl-diamond-competition#competition-structure