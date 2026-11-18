# HelloAgent

从零手写一个 **ReAct Agent**，不依赖 LangChain 的 `create_agent`，把「思考 → 行动 → 观察 → 再思考」这个循环掰开揉碎实现一遍。

## 为什么做这个

框架里一行 `create_agent()` 就能跑起来，但中间发生了什么全是黑盒：模型怎么决定调哪个工具？工具返回的结果怎么塞回上下文？循环什么时候该停？

这个项目把每一层都手写一遍，用最少的抽象看清 Agent 的最小内核。

## 核心思路

ReAct = **Rea**soning + **Act**ing。每一轮迭代做三件事：

```
用户提问
   ↓
LLM 输出 Thought（我要做什么）+ Action（调哪个工具、传什么参数）
   ↓
执行工具 → 得到 Observation（工具返回的原始结果）
   ↓
把 Observation 追加回对话历史 → 再次请求 LLM
   ↓
LLM 说 Finish → 输出 Final Answer，循环结束
```

关键点在于**状态就是一段不断变长的消息历史**，没有别的魔法。

## 目录结构

```
HelloAgent/
├── main.py              # 入口：驱动 ReAct 循环
├── agent/
│   ├── llm.py           # 模型客户端（DeepSeek，走 OpenAI 兼容协议）
│   ├── prompt.py        # ReAct 提示词模板
│   └── tools.py         # 工具集
├── .env                 # API 密钥（已 gitignore，不提交）
└── requirements.txt
```


## 快速开始

**1. 环境**

Python 3.13（conda 环境 `langchain1.2`）

**2. 安装依赖**

```bash
pip install requests python-dotenv tavily-python openai
```

**3. 配置密钥**

在项目根目录建 `.env`：

```bash
DEEPSEEK_API_KEY=你的key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-flash
TAVILY_API_KEY=你的key
```

> `.env` 已在 `.gitignore` 里，不会被提交。

**4. 运行**

```bash
python main.py
```

## 开发进度

- [x] 工具层：天气查询（wttr.in）、景点推荐（Tavily，含异常兜底）
- [x] 模型客户端：DeepSeek 接入 + `.env` 加载（`agent/llm.py`，`agent/__init__.py` 里 `load_dotenv()`）
- [x] ReAct 提示词模板：约定 Thought / Action / Observation 的输出格式（`agent/prompt.py`）
- [x] 主循环：解析模型输出、调度工具、拼接观察结果（`main.py`）
- [x] 终止条件：识别 `Finish` 并提取最终答案
- [ ] 多轮记忆与工具调用日志

## 参考

- [Hello-Agents](https://github.com/datawhalechina/hello-agents) — Datawhale 的 Agent 教程，本项目跟随其思路手写实现

