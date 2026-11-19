# 第一章案例：智能旅行助手

跟随 Hello-Agents 教程第一章手写的 ReAct 最小实现：LLM 输出 `Thought / Action`，主循环解析 Action 调用工具，把 `Observation` 拼回上下文，直到 `Finish[最终答案]`。

| 文件 | 职责 |
|---|---|
| `main.py` | 入口：ReAct 主循环（构建 Prompt → 调 LLM → 解析 Action → 执行工具 → 拼接 Observation） |
| `agent/llm.py` | `OpenAICompatibleClient`：DeepSeek（OpenAI 兼容协议）客户端 |
| `agent/prompt.py` | 系统提示词：约束 Thought/Action 输出格式 |
| `agent/tools.py` | `get_weather`（wttr.in）、`get_attraction`（Tavily） |

学习笔记：[docs/notes/chapter01.md](../../docs/notes/chapter01.md)

## 运行

在仓库根目录下：

```bash
python code/chapter01_travel_assistant/main.py
```
