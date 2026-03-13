# 快速入门

欢迎使用 EXO！本指南将帮助你快速开始使用 EXO 进行 AI Agent 技能开发。

## 前置要求

- Python 3.8 或更高版本
- OpenRouter API 密钥（访问 [openrouter.ai](https://openrouter.ai) 获取）

## 安装

### 使用 pip 安装

```bash
pip install exo
```

### 从源码安装

```bash
git clone https://github.com/Yuan-ManX/EXO.git
cd EXO
pip install -e .
```

## 配置 API 密钥

在使用 EXO 之前，你需要设置 OpenRouter API 密钥：

### 方式 1：环境变量

```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

### 方式 2：.env 文件

在项目根目录创建 `.env` 文件：

```
OPENROUTER_API_KEY=your-api-key-here
```

## 快速开始

### 方法 1：Python API

```python
from exo import EXO

# 初始化 EXO
exo = EXO()

# 将 URL 转换为 Markdown
content = exo.convert_url("https://example.com")
print(content[:500])  # 打印前 500 个字符

# 创建一个新技能
skill = exo.create_skill(
    "一个读取 CSV 文件并生成统计摘要的技能",
    name="csv-analyzer"
)

# 从文件创建技能，使用文件作为资源
skill_with_resources = exo.create_skill(
    "根据提供的数据文件创建数据分析技能",
    resources=["data/sample.csv", "docs/reference.pdf"]
)
```

### 方法 2：命令行

```bash
# 转换 URL
exo convert https://example.com -o output.md

# 创建技能
exo create "一个处理 JSON 数据的技能" -n json-processor

# 进化技能
exo evolve skills/old-skill.py "添加更好的错误处理"
```

### 方法 3：便捷函数

```python
from exo import convert, create, parse

# 转换 URL
content = convert("https://example.com")

# 解析文件
resource = parse("data/document.pdf")
print(resource.to_skill_resource())

# 创建技能
skill = create("一个天气数据获取技能")
```

## 解析文件资源

EXO 支持解析多种文件格式作为技能创建的资源：

```python
from exo import EXO

exo = EXO()

# 解析单个文件
parsed = exo.parse_file("document.pdf")
print(parsed.text_content)

# 解析多个文件
resources = exo.parse_multiple_files([
    "data.csv",
    "reference.docx",
    "image.png"
])

# 直接转换为技能资源格式
skill_resource = exo.parse_to_skill_resource("manual.pdf")
```

## 下一步

- 查看 [示例](./examples.md) 了解更多实际使用案例
- 阅读 [API 参考](./api-reference.md) 了解完整的 API 文档
- 探索 [高级主题](./advanced-topics.md) 深入了解 EXO 的工作原理
