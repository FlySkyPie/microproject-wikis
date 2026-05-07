CQRS (Command Query Responsibility Segregation) 是指把對資料的操作分為兩種：

1.  Command：會改變系統狀態的行為，如新增學生。
2.  Query：不會改變系統狀態的查詢，如查詢學生成績。

在面對涉及[CAP定理](#CAP定理)的分散式或微服務架構系統中尤其有用。