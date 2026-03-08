以 [FlyPie](FlyPie) 的幾個 Side Project 為例。

## SweetHome3DTS

SweetHome3D 是一個大眾取向的 3D 室內設計軟體，用於模擬家具擺設等基本使用。它本身是一個桌面應用程式，透過 [JSweet](JSweet) 建立另外一個能夠在網頁執行的版本，主要作為功能較為陽春的線上 Demo。

經過 [FlyPie](FlyPie) 一番努力，已經獲得了一個最低混淆可運作的版本（[SweetHome3DTS](#SweetHome3DTS)），成功脫離 Java 體系，但是當中有一個 `SweetHome3D.ts` 檔案高達 73180 行。為了使該專案能夠被維護以及修復遷移過程造成的一些瑕疵，必須進行大規模重構將該檔案拆分掉。

## Biomes

[Biomes](#Biomes) 是一個技術棧十分複雜的專案，涉及 C++, Rust, Python, Typescript，應用程式層級主要以 Typescript 為主，並且透過 Zod 定義大量的資料結構 (Schema)。

然而這些 Zod Schema 之間有嚴重的循環仰賴，當中的許多 Schema 是寫在同一個檔案之中，讓仰賴的調查更為困難，為了後續維護以及修復循環仰賴，必須進行大規模重構將 Schema 檔案拆成單一職責的程式碼檔案。