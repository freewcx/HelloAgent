import os
from pathlib import Path
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI

# 本文件位于 code/chapter04_classic_paradigms/ 下，向上两级是仓库根目录
load_dotenv(Path(__file__).resolve().parents[2] / ".env")


class HelloAgentsLLM:
    """为 Hello Agents 定制的 LLM 客户端（教程 4.1.3）。

    参数优先级：显式传入 > .env 环境变量。
    兼容任何 OpenAI 接口协议的服务（DeepSeek / 通义 / 本地模型等）。
    """

    def __init__(self, model: str = None, apiKey: str = None,
                 baseUrl: str = None, timeout: int = None):
        self.model = model or os.getenv("LLM_MODEL_ID")
        apiKey = apiKey or os.getenv("LLM_API_KEY")
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or int(os.getenv("LLM_TIMEOUT", 60))

        if not all([self.model, apiKey, baseUrl]):
            raise ValueError("模型ID、API密钥和服务地址必须被提供或在 .env 文件中定义。")

        self.client = OpenAI(api_key=apiKey, base_url=baseUrl, timeout=timeout)

    def think(self, messages: List[Dict[str, str]], temperature: float = 0) -> str:
        """调用 LLM 进行思考：流式打印响应，并返回完整文本。"""
        print(f"🧠 正在调用 {self.model} 模型...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )
            print("✅ 大语言模型响应成功:")
            collected_content = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()
            return "".join(collected_content)
        except Exception as e:
            print(f"❌ 调用 LLM API 时发生错误: {e}")
            return None
