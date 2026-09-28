#
# TODO 1: 导入需要的模块（os 和 openai）
import os
from openai import OpenAI, api_key
import sys
from dotenv import load_dotenv

load_dotenv()
# TODO 2: 从环境变量读取 API key（os.environ.get），没有就 print 提示并退出
api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    print("Please set the DEEPSEEK_API_KEY environment variable.")
    sys.exit(1)
# TODO 3: 创建客户端实例 —— 提示：base_url 是 https://api.deepseek.com，model 用 deepseek-chat
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)
# TODO 4: 构造 messages 列表，包含一个 system 和一个 user 消息
messages = [
    {"role": "system", "content": "你是一个只会说反话的猫"},
    {"role": "user", "content": "截断发生在什么层面？"}
]
# TODO 5: 调用接口拿到回复，打印出回答内容
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=messages,
    temperature=1.5,
    stream=False,
    reasoning_effort="high",
    extra_body={"thingking":{"type":"enable"}}
)
print("AI回复：")
print(response.choices[0].message.content)
# TODO 6: 打印本次用了多少 token（在返回对象里找 usage 字段）
print("\n==== Token消耗 ====")
print(f"输入token(prompt_tokens):{response.usage.prompt_tokens}")
print(f"输出token(completed_tokens):{response.usage.completion_tokens}")
print(f"总token(total_tokens):{response.usage.total_tokens}")
