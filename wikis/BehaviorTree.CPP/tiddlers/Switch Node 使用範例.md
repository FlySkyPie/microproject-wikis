以下是 `Switch3` 的 XML 配置範例，包含三個條件分支與一個預設分支：

```zml
<Switch3 variable="{robot_state}" case_1="IDLE" case_2="WORKING" case_3="ERROR">
    <HandleIdle/>          
    <HandleWorking/>      
    <HandleError/>        
    <HandleUnknownState/>  
</Switch3>
```

雖然同樣的行為可以使用 Sequence, Fallback 與 Condition 組合達成，但使用 Switch Node 更為簡潔且易讀。