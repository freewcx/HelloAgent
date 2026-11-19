"""4.1.3 冒烟测试：验证 HelloAgentsLLM 封装能正常调用。

运行（仓库根目录下）：
    python code/chapter04_classic_paradigms/demo_llm.py
"""
from llm_client import HelloAgentsLLM

if __name__ == "__main__":
    llm = HelloAgentsLLM()
    answer = llm.think([{"role": "user", "content": "用一句话解释什么是智能体"}])
    print("\n--- 返回内容 ---")
    print(answer)
