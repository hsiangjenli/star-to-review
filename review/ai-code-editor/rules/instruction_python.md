<!-- 
Reference:
https://github.com/slime21023/windsurf-rules-toolbox/blob/cf111dde1f66431d12a642eabb7967bf5695fbb6/python.windsurfrules
 -->
<python_coding_standards>

<code_style>
- 遵循 PEP 8 風格指南，使用 Ruff 自動檢查和修正
- 使用 4 個空格進行縮進，不使用 Tab
- 每行代碼最大長度為 88 個字符（與 Black 格式化工具默認值一致）
- 使用空行分隔函數和類，以及較大的代碼塊
- 使用空格（如運算符兩側、逗號後面、冒號後面）
- 使用 snake_case 命名變量和函數
- 使用 PascalCase 命名類
- 使用 UPPERCASE 命名常量
- 將相關的導入語句分組，並按標準庫、第三方庫、本地應用程序導入順序排列
</code_style>

<documentation>
- 為所有公共模塊、函數、類和方法編寫文檔字符串
- 使用 Google 或 NumPy 風格的文檔字符串格式
- 包含參數類型、返回類型和可能的異常信息
- 提供使用示例，特別是對於複雜的函數
- 保持文檔字符串與代碼同步更新
- 對於複雜的代碼塊添加內聯註釋
- 使用 TODO 註釋標記需要改進的地方，包括問題描述和負責人
- 使用 Ruff 的 D 規則集檢查文檔字符串質量和一致性
</documentation>

<code_organization>
- 遵循模塊化原則，每個模塊應該有單一的責任
- 使用類和函數組織代碼，避免過長的函數
- 函數應該專注於單一任務，通常不超過 50 行
- 將相關的功能分組到類中
- 使用包結構組織大型項目
- 將實用工具函數放在專用模塊中
- 將常量定義在模塊頂部
- 使用 `if __name__ == "__main__":` 模式進行可執行腳本
</code_organization>

<best_practices>
- 使用列表、字典、集合推導式提高代碼可讀性和性能
- 優先使用內置函數和庫
- 使用異常處理而不是返回錯誤代碼
- 使用上下文管理器（with 語句）處理資源
- 避免使用全局變量
- 使用生成器處理大數據集以節省內存
- 使用 f-strings 進行字符串格式化（Python 3.6+）
- 使用類型提示提高代碼可讀性和工具支持（Python 3.5+）
- 使用 `collections` 模塊中的數據結構（如 defaultdict, Counter）
</best_practices>

<performance>
- 使用性能分析工具（如 cProfile）識別瓶頸
- 優先使用內置數據結構和算法
- 使用適當的數據結構（列表用於序列，字典用於查找，集合用於唯一性檢查）
- 對於數值計算，使用 NumPy 和 Pandas
- 避免在循環中進行昂貴的操作
- 使用生成器表達式進行迭代
- 考慮使用 PyPy 或 Cython 加速關鍵代碼
- 使用多進程（multiprocessing）處理 CPU 密集型任務
- 使用異步 IO（asyncio）處理 IO 密集型任務
</performance>

<testing>
- 為所有代碼編寫單元測試
- 使用 pytest 作為測試框架
- 測試覆蓋率目標至少為 80%
- 包括正面測試和邊緣情況測試
- 使用模擬（mock）對象隔離外部依賴
- 為回歸測試創建測試用例
- 使用參數化測試減少重複代碼
- 使用 fixtures 設置測試環境
- 在 CI 管道中自動運行測試
</testing>

<security>
- 避免使用 eval() 和 exec() 函數
- 驗證所有用戶輸入
- 使用參數化查詢防止 SQL 注入
- 安全地處理密碼（使用 bcrypt 或 Argon2）
- 不要在代碼中硬編碼敏感信息
- 使用環境變量或配置文件存儲敏感信息
- 定期更新依賴項以修復安全漏洞
- 使用 HTTPS 進行網絡通信
- 實施適當的訪問控制和權限檢查
</security>

<dependency_management>
- 使用 uv 進行快速、可靠的依賴管理
- 使用 uv pip install 安裝依賴包
- 使用 uv pip compile 生成鎖定文件確保依賴一致性
- 使用虛擬環境（uv venv）隔離項目依賴
- 使用 requirements.txt 或 pyproject.toml 記錄依賴
- 指定依賴的版本號或版本範圍
- 定期使用 uv pip sync 更新依賴以獲取錯誤修復和安全更新
- 最小化外部依賴數量
- 在 CI/CD 管道中驗證依賴的兼容性
</dependency_management>

<linting_and_formatting>
- 使用 Ruff 作為主要的 linter 和 formatter
- 在 pyproject.toml 中配置 Ruff 規則集
- 啟用 Ruff 的自動修復功能（ruff --fix）
- 使用 Ruff 的 isort 功能自動排序導入語句
- 使用 Ruff 的 pyupgrade 功能自動更新到現代 Python 語法
- 啟用 Ruff 的類型檢查規則（TCH）
- 在 CI 管道中運行 Ruff 檢查
- 使用 pre-commit 鉤子自動運行 Ruff
</linting_and_formatting>

<type_checking>
- 使用類型註解增強代碼可讀性和可維護性
- 使用 mypy 或 Pyright 進行靜態類型檢查
- 為公共 API 提供完整的類型註解
- 使用 typing 模塊中的泛型類型（List, Dict, Optional 等）
- 使用 TypeVar 實現泛型函數和類
- 使用 Protocol 定義結構化類型
- 使用 @overload 裝飾器明確函數的多種類型簽名
- 在 CI 管道中運行類型檢查
</type_checking>

<project_structure>
- 使用 src 佈局組織包源代碼
- 使用 pyproject.toml 作為主要配置文件
- 使用 setup.py 或 setup.cfg 配置包元數據
- 將測試代碼放在單獨的 tests 目錄中
- 使用 docs 目錄存放文檔
- 使用 .github 或 .gitlab 目錄存放 CI 配置
- 包含 README.md, LICENSE, CHANGELOG.md 等標準文件
- 使用 .gitignore 排除不應提交的文件
</project_structure>

<development_workflow>
- 使用 uv 創建和管理虛擬環境
- 使用 uv pip install -e . 以可編輯模式安裝開發中的包
- 使用 git 進行版本控制
- 實施分支策略（如 GitHub Flow 或 GitLab Flow）
- 使用拉取請求或合併請求進行代碼審查
- 在提交前使用 Ruff 檢查代碼質量
- 使用語義化版本控制
- 自動化測試和部署流程
</development_workflow>

<documentation_tools>
- 使用 Sphinx 生成項目文檔
- 使用 Read the Docs 或 GitHub Pages 發布文檔
- 使用 sphinx-autodoc 自動從代碼生成 API 文檔
- 包含使用教程和示例
- 使用 Markdown 或 reStructuredText 編寫文檔
- 保持文檔與代碼同步
- 包含安裝和貢獻指南
- 記錄重大更改和版本歷史
</documentation_tools>

<continuous_integration>
- 使用 GitHub Actions, GitLab CI 或類似工具實施 CI/CD
- 自動運行測試套件
- 使用 Ruff 進行代碼質量檢查
- 運行類型檢查器
- 測量代碼覆蓋率
- 自動構建和發布包
- 使用矩陣測試多個 Python 版本
- 實施依賴安全掃描
</continuous_integration>

</python_coding_standards>