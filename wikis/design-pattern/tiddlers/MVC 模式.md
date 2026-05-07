MVC 模式是指將軟體依據職責拆分成 Model、View 和 Controller 的[設計模式](#設計模式)，它的職責拆分大致如下：

- [Model](#Model)
  - 儲存或處理資料模型，亦可理解成狀態。
- [View](#View)
  - 處理視圖，亦可理解為使用者界面。
- [Controller](#Controller)
  - 通常作為程式行為的進入點，調用與組織包含 [Model](#Model) 和 [View](#View) 在內的其他組件，盡可能減少事務邏輯，職責專注於[編排](#Orchestration)上。

在現代軟體工程中，涉及使用者界面 (View) 的應用程式通常遵守該模式，或該模式的變體。