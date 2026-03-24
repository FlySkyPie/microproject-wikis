
1. 遷移必須是靜態的且可回滾的。如果你的遷移依賴於動態生成的資料，那麼確保只有資料本身是動態的，而不是其結構。
2. 生成具有描述性名稱和slug的遷移。slug是必需的，應該解釋所做的更改。
3. 為新遷移設定人類可讀的檔案範本。我們使用`date*_*slug*.py`模式，例如`2022-08-24_post_content_idx.py`

```
# alembic.ini
file_template = %%(year)d-%%(month).2d-%%(day).2d_%%(slug)s
```