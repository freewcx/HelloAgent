# 第四章：智能体经典范式构建

教程对应章节：[第四章](https://datawhalechina.github.io/hello-agents/#/chapter4/)（官方配套代码 `code/chapter4/`）

| 文件 | 对应小节 | 说明 |
|---|---|---|
| `llm_client.py` | 4.1.3 | `HelloAgentsLLM`：统一 LLM 客户端封装，读取 `.env` 的 `LLM_*` 变量，`think()` 流式调用 |
| `demo_llm.py` | 4.1.3 | 冒烟测试：验证封装能正常调用 |
| `tools.py` | 4.2 | 工具定义（SerpApi 搜索 / ToolExecutor），待添加 |
| `ReAct.py` | 4.3 | ReAct 范式，待添加 |
| `Plan_and_solve.py` | 4.4 | Plan-and-Solve 范式，待添加 |
| `Reflection.py` | 4.5 | Reflection 范式，待添加 |

## 运行

在仓库根目录下：

```bash
python code/chapter04_classic_paradigms/demo_llm.py
```

## 备注

- 环境变量统一用 `LLM_API_KEY` / `LLM_MODEL_ID` / `LLM_BASE_URL` / `LLM_TIMEOUT`，与教程一致；模板见根目录 `.env.example`。
- 教程 4.2 的搜索工具默认用 SerpApi；第一章案例用的是 Tavily，实现 `tools.py` 时二选一。
