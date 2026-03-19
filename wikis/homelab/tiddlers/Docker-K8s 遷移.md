自 2025-12-23 起，將服務從 [Beta 節點](<#Beta 節點>)的 Docker Swarm 遷移到 [Delta 節點](<#Delta 節點>)的過程。

程序大致如下：

1. 起草 K8s YAML
    - 除了手寫以外亦可透過 [Kompose](#Kompose) 輔助。
2. [確定待遷移的資料量](<#從檔案系統檢查 Volume 大小>)
3. 建立 [Volume 臨時容器](<#Volume 臨時容器>)
4. 使用 `kubectl cp` 或是其他工具（如：`rclone`、`rsync`）傳輸資料
5. 佈署服務使其與完成轉移的資料整合
6. 移除臨時容器