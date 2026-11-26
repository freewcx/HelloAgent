# llm_client.py

## or 为什么能用来读取默认配置？
比如说：`self.model = model or os.getenv("LLM_MODEL_ID")`
你可以将其理解为：优先使用调用者传入的参数`model`，如果参数是假值比如 `null`、空字符串、空列表等，就从环境变量`LLM_MODEL_ID`加载。

## messages 为什么需要多个消息？
因为大模型 API 通常使用消息列表来表达对话上下文。
每轮对话放在dict 字典中
多轮对话就把对个 dict 放到列表中
因此 messages: List[Dict[str, str]]，其中 str 表示字典的键值对都是 str 字符串
