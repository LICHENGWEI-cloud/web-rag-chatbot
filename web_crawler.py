import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

def load_webpage(url: str) -> Document:
    """
    自定义静态网页爬虫：请求网页、清洗html，返回LangChain Document
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding

    soup = BeautifulSoup(resp.text, "html.parser")
    # 删除无用标签 script / style
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # 提取正文
    raw_text = soup.get_text(separator="\n")
    # 简单清理多余空行
    clean_lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    clean_text = "\n".join(clean_lines)

    # 封装Document，metadata存url来源
    doc = Document(
        page_content=clean_text,
        metadata={"source_url": url}
    )
    return doc


if __name__ == "__main__":
    doc = load_webpage("https://example.com")
    print(doc.page_content[:800])
