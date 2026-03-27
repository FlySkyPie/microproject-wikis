Biomes Story 是 [FlyPie](#FlyPie) 版本的 [Biomes](#Biomes) 分支。

## 命名

[Biomes](#Biomes) 原名缺乏辨別度，一般情況下難以搜尋與語意定位。Story 係參考自另外一款[類 Minecraft](<#類 Minecraft>) 遊戲：Vintage Story。

## 目的

在 [FlyPie](#FlyPie) 的其他專案中，需要一個高度客製化的[類 Minecraft](<#類 Minecraft>) 的環境。若選用 Minecraft 作為基底則須面對商業閉源軟體、修改幅度巨大的問題，亦考量 Minetest 等成熟的 [Minecraft Clone](<#類 Minecraft>) 開源專案作為基底，但是技術棧為 C++ 之類 [FlyPie](#FlyPie) 不熟悉的語言。

[Biomes](#Biomes) 專案說明為：

> Biomes is an open source sandbox MMORPG built for the web using web technologies such as Next.js, Typescript, React and WebAssembly. 

並且使用 [ECS](#ECS) 架構，也是 [FlyPie](#FlyPie) 原計畫考量的軟體架構，因此計畫使用 [Biomes](#Biomes) 的程式碼作為其計畫之基底。

## 工作範圍

[Biomes](#Biomes) 開源的程式碼使用單底架構，並且根據 Git 紀錄明顯有「匆促開源」的跡象，不只部份組件缺少版控紀錄、像是引湊組裝在一起一般，亦有關鍵資料包之網路資源已經失效；文件描述疑似過期...等問題。

因此主要工作有兩大目標：分解與運行。

將單體架構根據技術棧、模組職責...分解成能獨立編譯、測試的模組。並將分解的模組重新組裝以建立一個可運行的 Biomes 實例。

Biomes Story 不包含 [FlyPie](#FlyPie) 的衍生計畫，也不包含 [Biomes](#Biomes) 可能的後續更新（新功能），僅作為重構與維護模式執行。

## 軟體組件

請見條目：[Biomes Story 組件](<#Biomes Story 組件>)。