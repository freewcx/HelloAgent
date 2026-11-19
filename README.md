# HelloAgent

从零手写 Agent，不依赖 LangChain 的 `create_agent`，把「思考 → 行动 → 观察 → 再思考」这个循环掰开揉碎实现一遍。

跟随 Datawhale [Hello-Agents](https://github.com/datawhalechina/hello-agents) 教程推进，代码按章节组织在 `code/` 下，每章自包含、可直接运行。

## 目录结构

```
HelloAgent/
├── code/
│   ├── chapter01_travel_assistant/     # 教程第一章案例：智能旅行助手（ReAct 最小实现）
│   │   ├── main.py                     # 入口：驱动 ReAct 循环
│   │   └── agent/
│   │       ├── __init__.py             # load_dotenv()，import 时加载 .env
│   │       ├── llm.py                  # 模型客户端（DeepSeek，走 OpenAI 兼容协议）
│   │       ├── prompt.py               # ReAct 提示词模板
│   │       └── tools.py                # 工具集（wttr.in 天气 + Tavily 景点搜索）
│   └── chapter04_classic_paradigms/    # 教程第四章：智能体经典范式（进行中）
│       ├── llm_client.py               # 4.1.3 HelloAgentsLLM 统一客户端封装
│       ├── demo_llm.py                 # 4.1.3 冒烟测试
│       └── (ReAct.py / Plan_and_solve.py / Reflection.py)   # 4.2~4.4 待添加
├── docs/notes/                         # 学习笔记（按章节）
├── .env.example                        # 环境变量模板（复制为 .env 后填真实密钥）
└── requirements.txt
```

## 快速开始

**1. 环境**：Python 3.13（conda 环境 `langchain1.2`）

**2. 安装依赖**

```bash
pip install -r requirements.txt
```

**3. 配置密钥**

```bash
cp .env.example .env    # 然后填入真实 key
```

| 变量 | 用途 |
|---|---|
| `LLM_API_KEY` / `LLM_MODEL_ID` / `LLM_BASE_URL` | LLM 客户端（第四章起统一用这组） |
| `DEEPSEEK_API_KEY` / `DEEPSEEK_BASE_URL` / `DEEPSEEK_MODEL` | 第一章案例的模型客户端 |
| `TAVILY_API_KEY` / `SERPAPI_API_KEY` | 搜索工具（二选一） |

> `.env` 已在 `.gitignore` 里，不会被提交。

**4. 运行各章节案例**

```bash
# 第一章：智能旅行助手
python code/chapter01_travel_assistant/main.py

# 第四章 4.1.3：HelloAgentsLLM 封装冒烟测试
python code/chapter04_classic_paradigms/demo_llm.py
```

## 学习进度

| 教程章节 | 目录 | 内容 | 状态 |
|---|---|---|---|
| 第一章 初识智能体 | `code/chapter01_travel_assistant/` | 智能旅行助手：ReAct 循环手写实现 | ✅ 完成 |
| 第四章 经典范式构建 | `code/chapter04_classic_paradigms/` | 4.1.3 HelloAgentsLLM 客户端封装 | 🚧 进行中 |
| 第四章 经典范式构建 | 同上 | 4.2~4.4 ReAct / Plan-and-Solve / Reflection | ⬜ 待开始 |

## 第一章实现清单

- [x] 工具层：天气查询（wttr.in）、景点推荐（Tavily，含异常兜底）
- [x] 模型客户端：DeepSeek 接入 + `.env` 加载（`agent/llm.py`，`agent/__init__.py` 里 `load_dotenv()`）
- [x] ReAct 提示词模板：约定 Thought / Action / Observation 的输出格式（`agent/prompt.py`）
- [x] 主循环：解析模型输出、调度工具、拼接观察结果（`main.py`）
- [x] 终止条件：识别 `Finish` 并提取最终答案
- [ ] 多轮记忆与工具调用日志

学习笔记见 [docs/notes/chapter01.md](docs/notes/chapter01.md)。

## 参考

- [Hello-Agents](https://github.com/datawhalechina/hello-agents) — Datawhale 的 Agent 教程，本项目跟随其思路手写实现
