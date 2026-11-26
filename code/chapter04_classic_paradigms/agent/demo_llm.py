"""4.1.3 冒烟测试：验证 HelloAgentsLLM 封装能正常调用。

运行（仓库根目录下）：
    python code/chapter04_classic_paradigms/demo_llm.py
"""
from llm_client import HelloAgentsLLM

# --- 客户端使用示例 ---
if __name__ == '__main__':
    try:
        llmClient = HelloAgentsLLM()

        exampleMessages = [
            {"role": "system", "content": "You are a helpful assistant that writes Python code."},
            {"role": "user", "content": "写一个快速排序算法"}
        ]

        print("--- 调用LLM ---")
        responseText = llmClient.think(exampleMessages)
        if responseText:
            print("\n\n--- 完整模型响应 ---")
            print(responseText)

    except ValueError as e:
        print(e)
