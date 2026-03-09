# AutoVideoMiner

一个两阶段 Agentic 视频挖掘系统骨架实现：

- 阶段一：泛搜学习 + RAG 沉淀 + 切分归档
- 阶段二：定向检索 + 采样评估反馈闭环 + 工业化切分

## 模型配置

当前默认模型在 `app/agent/base.py` 中配置为：`chatgpt`。

## 运行

```bash
python AutoVideoMiner/main.py
```
