from app.agent.base import AgentState, BaseAgent
from app.tool.ask_human import ask_human
from app.tool.dedup_tool import DedupTool
from app.tool.yt_dlp_tool import YtDlpTool


class CrawlerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="crawler", system_prompt="你是鲁棒的 ReAct 爬虫")
        self.dedup = DedupTool()
        self.downloader = YtDlpTool()

    def crawl(self, urls: list[str], state: AgentState, allow_human: bool = False) -> list[str]:
        self.run(state, {"urls": urls})
        downloads: list[str] = []
        for url in urls:
            if self.dedup.exists(url):
                continue
            if "captcha" in url and allow_human:
                ask_human({"reason": "captcha", "url": url})
            downloads.append(self.downloader.download(url))
            self.dedup.mark(url)
        return downloads
