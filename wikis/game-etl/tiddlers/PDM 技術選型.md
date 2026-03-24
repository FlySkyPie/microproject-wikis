[uv](https://github.com/astral-sh/uv) 是一個比起 [PDM](#PDM) 更為熱門的 Python 套件管理工具，以下是 [Python 綠地專案 SOP](<#Python 綠地專案 SOP>) 仍以 [PDM](#PDM) 為主的原因：

- [PDM](#PDM) 的核心價值是遵守 [PEP](#PEP)，這對於工具的長期穩定性十分重要。
- [PDM](#PDM) 本身基於 Python，不像 uv 以 Rust 實做，這對仰賴鏈的穩定與簡化十分重要。
- [PDM 的腳本機制](https://pdm-project.org/latest/usage/scripts/)比起 [uv 的腳本機制](https://docs.astral.sh/uv/guides/scripts/)，允許直接將特定的指令寫入 `pyproject.toml`，體驗對於習慣使用 npm 的開發者較為熟悉。
  - 在此之上，[PDM](#PDM) 的 `pyproject.toml` 允許比起 npm 更複雜的指令組合與環境變數設定。