> 本文翻譯自 [Johnny.Decimal specification](<#Johnny.Decimal specification>)

本文件定義了 Johnny.Decimal 系統的結構與需求。

本文件中使用的關鍵字「MUST」（必須）、「MUST NOT」（絕不允許）、「REQUIRED」（必須）、「SHALL」（必須）、「SHALL NOT」（絕不允許）、「SHOULD」（應該）、「SHOULD NOT」（不應該）、「RECOMMENDED」（建議）、「MAY」（可以）以及「OPTIONAL」（選用）應按照 [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt) 中的描述進行解釋。

---

# 類型 (Types)

Johnny.Decimal 系統中的每條記錄都有一個類型。公開類型資訊的實作方式「必須」使用以下規範值：

| 類型 (Type) | 數值 (Value) |
| ----------- | ------------ |
| System      | `system`     |
| Area        | `area`       |
| Category    | `category`   |
| ID          | `id`         |

類型數值「必須」為小寫。

---

# 標題 (Titles)

System、Area、Category 與 ID 都「必須」擁有標題。

## 格式

一個標題：

- 「必須」包含至少 1 個字元。
- 「絕不允許」超過 255 個字元。

## 限制

- 標題「可以」包含任何可列印的 Unicode 字元。

---

# 系統 (Systems)

## 定義

**System**（系統）是一個包含 Area、Category 與 ID 的容器集合。

## 系統識別碼 (System identifier)

系統識別碼是「選用」的。

若存在系統識別碼，該識別碼：

- 「必須」符合型樣 `[A-Z][0-9][0-9]`。
  - 有效範圍：`A00` 到 `Z99`。
- 在所有範圍內的系統中「必須」是唯一的。

## 限制

- 沒有識別碼的系統是有效的。
- 一個系統「可以」包含零個或多個 Area。

---

# 領域 (Areas)

## 定義

**Area**（領域）是 Category 的高階分組。Area 代表系統內廣泛的範疇。

## 格式

一個 Area 識別碼：

- 「必須」符合型樣 `[0-9]0-[0-9]9`，且兩個數字必須相同。
  - 有效數值：`00-09`, `10-19`, `20-29`, `30-39`, `40-49`, `50-59`, `60-69`, `70-79`, `80-89`, `90-99`。

## 限制

- Area 在其所屬系統內「必須」是唯一的。
- 一個 Area 「可以」包含零個或多個 Category。
- 一個 Area 「必須」僅包含首位數字與該 Area 首位數字相符的 Category。
  - Area `10-19` 「可以」包含 Category `10` 到 `19`。
  - Area `10-19` 「絕不允許」包含 Category `20`。

---

# 類別 (Categories)

## 定義

**Category**（類別）是 ID 的分組。Category 代表特定的工作領域或相關項目的集合。

## 格式

一個 Category 識別碼：

- 「必須」符合型樣 `[0-9][0-9]`。
  - 有效範圍：`00` 到 `99`。

## 限制

- Category 在其所屬系統內「必須」是唯一的。
- 一個 Category 「必須」隸屬於恰好一個 Area。
- 一個 Category 「必須」包含在範圍涵蓋該 Category 編號的 Area 內。
  - Category `11` 「必須」隸屬於 Area `10-19`。
  - Category `11` 「絕不允許」隸屬於 Area `20-29`。
- 一個 Category 「可以」包含零個或多個 ID。
- Category 「絕不允許」在沒有父級 Area 的情況下存在。

---

# ID

## 定義

**ID** 是 Johnny.Decimal 系統中組織的基本單位。一個 ID 代表單一專案、主題或相關項目的集合。

## 格式

一個 ID：

- 「必須」符合型樣 `[0-9][0-9].[0-9][0-9]`。
  - 有效範圍：`00.00` 到 `99.99`。

小數點前的部分是 **Category 元件**。小數點後的部分是 **ID 元件**。

## 限制

- ID 在其所屬系統內「必須」是唯一的。
- 一個 ID 「必須」隸屬於恰好一個 Category。
- 一個 ID 「必須」包含在與其 Category 元件相符的 Category 內。
  - ID `15.52` 「必須」隸屬於 Category `15`。
  - ID `15.52` 「絕不允許」隸屬於 Category `16`。
- ID 「絕不允許」在沒有父級 Category 的情況下存在。

---

# 元數據 (Metadata)

## 定義

**Metadata**（元數據）是附加到 ID 的鍵值對（key/value pairs）集合。

## 適用性

- Metadata 「可以」附加到 ID 上。
- Metadata 「絕不允許」附加到 System、Area 或 Category 上。

### 原理

ID 是 Johnny.Decimal 系統的葉節點，也是數據存在的唯一位置。關於高階結構的元數據使用「**標準零**」(standard zeros) 進行存儲：

| 結構           | 標準零 (Standard zero) |
| -------------- | ---------------------- |
| System         | `00.00`                |
| Area `20-29`   | `20.00`                |
| Category `21`  | `21.00`                |

若要存儲關於 Category `21` 的元數據，請將其附加到 ID `21.00`。若要存儲關於 Area `20-29` 的元數據，請將其附加到 ID `20.00`。若要存儲關於系統本身的元數據，請將其附加到 ID `00.00`。

## 鍵 (Keys)

一個元數據鍵：

- 「必須」包含至少 1 個字元。
- 「必須」符合型樣 `[a-zA-Z][a-zA-Z0-9_]*`。
- 在單一 ID 的元數據中「必須」是唯一的。

### 保留鍵

以下鍵為保留鍵，並具有定義的語義：

| 鍵 (Key)      | 類型 (Type)            | 描述 (Description)            |
| ------------- | ---------------------- | ----------------------------- |
| `description` | string                 | ID 的人類可讀描述              |
| `relatesTo`   | array of ID references | 對同系統中其他 ID 的引用        |
| `url`         | array of URIs          | 與此 ID 相關聯的外部資源        |

實作端「必須」根據其類型定義對保留鍵進行驗證。

若使用者嘗試將保留鍵用於無效數值，實作端「應該」發出警告。

### 使用者定義鍵

未列為保留鍵的鍵「可以」由使用者自由使用。

使用者定義鍵「應該」使用 camelCase（小駝峰式命名法）以與保留鍵保持一致。

## 數值 (Values)

一個元數據數值：

- 「必須」是有效的 JSON 數值（字串、數字、布林值、陣列或物件）。
- 「絕不允許」為 null。

### description

`description` 的數值：

- 「必須」為字串。
- 「可以」為任意長度。
- 被解釋為 GitHub-Flavored Markdown (GFM)。不含格式的純文本也是有效的。
- 不支持 Markdown 渲染的實作端「應該」顯示原始文本。

### relatesTo

`relatesTo` 的數值：

- 「必須」為陣列。
- 每個元素「必須」是符合 ID 格式 (`[0-9][0-9].[0-9][0-9]`) 的字串。
- 每個被引用的 ID 「應該」存在於同一個系統中。
- 關係是單向的；實作端「可以」衍生出反向連結。

### url

`url` 的數值：

- 「必須」為陣列。
- 每個元素「必須」是有效的 URI（根據 RFC 3986）。