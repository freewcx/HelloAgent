# llm_client.py

## or 为什么能用来读取默认配置？
比如说：`self.model = model or os.getenv("LLM_MODEL_ID")`
你可以将其理解为：优先使用调用者传入的参数`model`，如果参数是假值比如 `null`、空字符串、空列表等，就从环境变量`LLM_MODEL_ID`加载。

## messages 为什么需要多个消息？
因为大模型 API 通常使用消息列表来表达对话上下文。
每轮对话放在dict 字典中
多轮对话就把对个 dict 放到列表中
因此 messages: List[Dict[str, str]]，其中 str 表示字典的键值对都是 str 字符串


## if __name__ == '__main__':是什么意思？
表示只有直接运行当前Python 文件时，才执行下面的代码

## 列表推导式是什么？

看代码中的例子：
```python
[
    f"- {name}: {info['description']}"
    for name, info in self.tools.items()
]
```

正常的顺序是先执行 for 循环，在循环内部拿到每一次遍历的键值对，格式化成字符串以后再追加到列表内
比如说：

```python
descriptions = []

for name, info in self.tools.items():
    text = f"- {name}: {info['description']}"
    descriptions.append(text)

return "\n".join(descriptions)
```

外部我们是需要先定义一个 列表名为descriptions 的列表的，
然后用 for 循环去遍历字典，配合字典自带的 item()方法可以拿到字典里的每一个键值对，

比如说：
```python
self.tools = {
    "Search": {
        "description": "网页搜索工具",
        "func": search
    },
    "Calculator": {
        "description": "数学计算工具",
        "func": calculator
    }
}
```

那么第一次从字典里取出的结果就是：
```python
"Search": {
        "description": "网页搜索工具",
        "func": search
    }
```

然后把键 赋值给 name，把值赋值给 info
得到：

```python
name = 'Search'
info = {"description": "网页搜索工具","func": search}
```
通过 info[description]拿到工具函数的描述信息："网页搜索工具"

然后执行`text = f"- {name}: {info['description']}"`进行格式化字符串拼接：
拼接结果：
- Search:"网页搜索工具"
执行`descriptions.append(text)`把这个字符串追加到列表中

再进入下一轮循环，流程同上

最后用`"\n".join(descriptions)`把列表进行换行拼接，作为工具信息查找函数的返回值

再看列表表达式为什么怎么写？
```python
"\n".join([
        f"- {name}: {info['description']}"
        for name, info in self.tools.items()
    ])
```

可以理解为：
> 我要生成一个列表，列表中每个元素长什么样？从哪里获取生成这些元素的数据？

因此它要先写生成什么，再写数据从哪里来。

所以把`f"- {name}: {info['description']}"`含义是我要把拿到的 name 和 info[description]进行字符串拼接
然后 `for name, info in self.tools.items()])`则表示数据的来源，从当前的 for 循环遍历中拿
可以看出列表表达式更适合处理这种追加列表的代码，是对其的简写。

总结一下列表表达式的知识：

> 省去了列表拼接这一步，直接在[]内定义你要对数据怎么处理，然后写数据从哪里来，
最后由列表表达式帮你把处理过的数据作为列表的元素，省去了自定义列表和把数据append 到列表中这两步
区别就是代码的书写顺序需要遵守列表表达式的规则



