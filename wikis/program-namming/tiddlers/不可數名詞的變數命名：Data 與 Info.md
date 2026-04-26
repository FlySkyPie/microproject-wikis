針對 `data` 或 `info` 等不可數名詞，可根據其呈現方式選擇命名策略：

## 視為特定物件的修飾
若 `data` 指向具體的單位，則以該單位為核心命名：
- `dataFileCount` (資料檔案數)
- `dataPointCount` (資料點數)
- `dataStreamCount` (資料流數)
- `dataEntry` (資料條目)

## 視為整體屬性
- [不可數名詞的數量變數](<#不可數名詞的數量變數>)：`dataSize` (儲存空間大小)、`dataLength` (長度，暗示 array/list 結構)。
- 帶單位的命名：`dataInMegabytes` (以 MB 計的資料量)。