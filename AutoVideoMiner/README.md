# AutoVideoMiner

一个两阶段 Agentic 视频挖掘系统骨架实现：

- 阶段一：泛搜学习 + RAG 沉淀 + 切分归档
- 阶段二：定向检索 + 采样评估反馈闭环 + 工业化切分

## 模型配置

当前默认模型在 `app/agent/base.py` 中配置为：`chatgpt`。

## 运行

```bash
python AutoVideoMiner/main.py
# 或
python -m AutoVideoMiner
```

## VSCode 运行

- 已提供 `.vscode/launch.json`，打开 VSCode 后选择 `Run AutoVideoMiner` 即可启动。
- 如果编辑器没有显示单文件运行按钮，也可以直接按 `F5` 使用上述 Launch 配置。
