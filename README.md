# agent-journey 
1.这个仓库是干什么的？
我在 2026 秋招季系统学习 Agent 开发的实践仓库，记录从 Python 基础到 LLM 应用落地的全过程。
这是我的第一个 Git 仓库，所有代码由我手写完成。
2.学习目标：
- **LLM API 调用**：messages / role / temperature / 流式输出 / 异步并发 / 失败重试
- **Function Calling**：不依赖框架手写 ReAct Agent，理解工具调用的底层机制
- **RAG**：embedding、向量检索、重排序
- **多 Agent 编排**：LangGraph 工作流
3.目录结构：
| 目录 | 内容 |
| --- | --- |
| `week1/` | LLM API 基础调用、流式输出、异步并发、命令行对话机器人 |
4.运行环境：
python- Python 3.13
- DeepSeek API（OpenAI 兼容接口）
5.进度清单：
- [x] Day 1 初始化仓库，完成首次提交与推送
- [ ] Day 2 手写 API 调用脚本 `chat.py`
- [ ] Day 3 流式输出与异步并发
- [ ] Day 4 类封装与重试装饰器
- [ ] Day 5 环境变量与日志管理
- [ ] Day 6 命令行多轮对话机器人