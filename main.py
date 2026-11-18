# 修复：顶部必须先 import agent 包（触发 agent/__init__.py 的 load_dotenv()）
from agent.llm import OpenAICompatibleClient
from agent.tools import available_tools
from agent.prompt import AGENT_SYSTEM_PROMPT
import os
import re

'''
下面的主循环将整合所有组件，并通过格式化后的 Prompt 驱动 LLM 进行决策。
'''
# --- 1. 配置LLM客户端 ---
# 请根据您使用的服务，将这里替换成对应的凭证和地址
API_KEY = os.getenv("DEEPSEEK_API_KEY")
BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
MODEL_ID = os.getenv("DEEPSEEK_MODEL")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


llm = OpenAICompatibleClient(
    model=MODEL_ID,
    api_key=API_KEY,
    base_url=BASE_URL
)

# --- 2. 初始化 ---
# 用户请求
user_prompt = "你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。"
# 列表接收所有交互历史（这就是Agent上下文管理（Context Management）的一个简单实现）
prompt_history = [f"用户请求: {user_prompt}"]

print(f"用户输入: {user_prompt}\n" + "=" * 40)

# --- 3. 运行主循环 ---
for i in range(5):  # 设置最大循环次数
    print(f"--- 循环 {i + 1} ---\n") #i从0开始因此打印 i+1表示循环次数

    # 3.1. 构建Prompt
    full_prompt = "\n".join(prompt_history) # 将列表中的所有字符串使用换行符连接成一个字符串：（因为generate方法需要一个字符串作为输入，而prompt_history是一个列表）

    # 3.2. 调用LLM进行思考
    llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
    # 模型可能会输出多余的Thought-Action，需要截断（正则表达式）
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
    if match:
        truncated = match.group(1).strip()
        if truncated != llm_output.strip():
            llm_output = truncated
            print("已截断多余的 Thought-Action 对")
    print(f"模型输出:\n{llm_output}\n")
    prompt_history.append(llm_output)

    # 3.3. 解析并执行行动
    action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
    if not action_match:
        observation = "错误: 未能解析到 Action 字段。请确保你的回复严格遵循 'Thought: ... Action: ...' 的格式。"
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)
        continue
    action_str = action_match.group(1).strip()

    if action_str.startswith("Finish"):
        final_answer = re.match(r"Finish\[(.*)\]", action_str).group(1)
        print(f"任务完成，最终答案: {final_answer}")
        break

    tool_name = re.search(r"(\w+)\(", action_str).group(1)
    args_str = re.search(r"\((.*)\)", action_str).group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    if tool_name in available_tools:
        observation = available_tools[tool_name](**kwargs)
    else:
        observation = f"错误:未定义的工具 '{tool_name}'"

    # 3.4. 记录观察结果
    observation_str = f"Observation: {observation}"
    print(f"{observation_str}\n" + "=" * 40)
    prompt_history.append(observation_str)
