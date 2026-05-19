**AsyncSequence** 的邏輯與標準 Sequence 相似，但處理子節點切換的方式不同。關鍵特性在於 SUCCESS 時會「讓出」執行權（Yield），回傳 RUNNING 並結束當前 Tick。

| 當前 Tick 任一 Children 值 （尚未遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 是 | 下一個 Child |
| FAILURE | 是 | Root |
| RUNNING | 是 | RUNNING Children |

| 當前值 （已遍歷所有 Children） | 結束當前 Tick | 下一個 Tick 的起始點 |
| --- | :---: | --- |
| SUCCESS | 否 | ? |
| FAILURE | 是 | Root |
| RUNNING | - | RUNNING Children |

舉例來說：

```xml
<ReactiveSequence>
    <IsEnemyVisible/>
    <AsyncSequence>
        <AimWeapon/>
        <FireWeapon/>
        <ReloadWeapon/>
    </AsyncSequence>
</ReactiveSequence>
```

在這個範例中，`IsEnemyVisible` 會在 AsyncSequence 的每個步驟之間重新檢查。如果敵人在 `AimWeapon` 成功後消失，序列會在 `FireWeapon` 開始之前中斷。

這適用於需要在執行步驟間持續檢查環境變化的情境。