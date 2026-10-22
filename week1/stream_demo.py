# TODO 1: 导入 os、sys、time、OpenAI、load_dotenv，调用 load_dotenv()
import os
import sys
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# TODO 2: 读 DEEPSEEK_API_KEY，没有就打印提示并 sys.exit(1)
api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    print("Please set the DEEPSEEK_API_KEY environment variable.")
    sys.exit(1)

# TODO 3: 创建 client（base_url="https://api.deepseek.com"）
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# TODO 4: 记下开始时间 start = time.perf_counter()
start = time.perf_counter()

first_token_time = None
full_text = ""
usage_info = None

# TODO 5: 调用 create()，参数：model="deepseek-chat", messages=[...], stream=True,
#          stream_options={"include_usage": True}
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用50字介绍重庆"}],
    stream=True,
    stream_options={"include_usage": True}
)

# TODO 6: for chunk in response: 逐个处理
print("AI: ", end="", flush=True)
for chunk in response:
    # chunk.choices 可能是空列表（最后那个只带 usage 的 chunk）→ 先 if not chunk.choices: continue
    if not chunk.choices:
        # 这个chunk不带choices，只存usage，保存下来
        usage_info = chunk.usage
        continue

    delta = chunk.choices[0].delta.content
    # delta 可能是 None（第一个 chunk 只有 role）→ if delta: 才拼接和打印
    if delta:
        # 第一次拿到 delta 时记 first_token_time
        if first_token_time is None:
            first_token_time = time.perf_counter()
        full_text += delta
        print(delta, end="", flush=True)

print()
# TODO 7: 打印三个数
#   - 首字延迟 = first_token_time - start
#   - 总耗时 = time.perf_counter() - start
#   - usage（从最后一个 chunk 取，可能为 None，要判空）
total_cost = time.perf_counter() - start
first_latency = first_token_time - start if first_token_time else None

print("\n====统计信息====")
print(f"首token延迟：{first_latency:.4f} s")
print(f"总耗时：{total_cost:.4f} s")
if usage_info:
    print(f"输入token：{usage_info.prompt_tokens}")
    print(f"输出token：{usage_info.completion_tokens}")
    print(f"总token：{usage_info.total_tokens}")
else:
    print("未获取到usage信息")
