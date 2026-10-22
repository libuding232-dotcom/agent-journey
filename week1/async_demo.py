# TODO 1: 导入 asyncio、time、os、sys，以及 from openai import AsyncOpenAI
import asyncio
import time
import os
import sys
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


# TODO 2: 读 key、创建 AsyncOpenAI client（同一个 base_url）
api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    print("Please set the DEEPSEEK_API_KEY environment variable.")
    sys.exit(1)
client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com")
PROMPTS = [
    "用一句话解释什么是递归",
    "用一句话解释什么是哈希表",
    "用一句话解释什么是装饰器",
]


# TODO 3: 写 async def ask(prompt): 内部 await client.chat.completions.create(...)
#         返回 response.choices[0].message.content
#         注意：这里必须 await，不 await 拿到的是协程对象
async def ask(prompt):
    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=1.5,
    )
    return response.choices[0].message.content



# TODO 4: 写 async def run_serial(): for 循环逐个 await ask(p)，记录总耗时
async def run_serial():
    start_time = time.time()
    for p in PROMPTS:
        await ask(p)
    end_time = time.time()
    print(f"Serial: {end_time - start_time} seconds")


# TODO 5: 写 async def run_concurrent(): await asyncio.gather(*(ask(p) for p in PROMPTS))，记录总耗时
async def run_concurrent():
    start_time = time.time()
    await asyncio.gather(*[ask(p) for p in PROMPTS])
    end_time = time.time()
    print(f"Concurrent: {end_time - start_time} seconds")

# TODO 6: 写 async def main(): 先跑串行、再跑并发，打印两个耗时和加速比
async def main():
    await run_serial()
    await run_concurrent()

# TODO 7: 入口 if __name__ == "__main__": asyncio.run(main())
if __name__ == "__main__":
    asyncio.run(main())
