## 定義與差別
* **參數 (Parameter)**：定義在方法、函數宣告中的變數。
* **引數 (Argument)**：實際傳入方法、函數的數值或物件。

## 類比理解
可以將 **參數 (parameter)** 想成「停車位 (parking space)」，而 **引數 (argument)** 則是「汽車 (automobile)」。 就像不同的汽車可以在不同時間停入同一個車位，呼叫端每次呼叫函式時，可以傳送不同的引數給同一個參數。

## 範例
```javascript
function foo(parameter) { ... } // 這裡定義的是 parameter
foo(argument)                   // 這裡傳入的是 argument