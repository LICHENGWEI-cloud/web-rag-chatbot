from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_core.documents import Document

def build_rag_chain(docs: list[Document], chunk_size=1000, chunk_overlap=200):
    """
    输入：LangChain Document列表（来自bs4爬虫提取的网页内容）
    输出：RAG检索问答链，开启return_source_documents
    """
    # 1. 文本切片
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    split_chunks = text_splitter.split_documents(docs)

    # 2. 本地Embedding模型（ollama nomic-embed-text）
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # 3. 构建FAISS向量库
    vector_db = FAISS.from_documents(split_chunks, embeddings)

    # 4. 检索器，top_k=4，取最相关4段原文
    retriever = vector_db.as_retriever(search_kwargs={"k": 4})

    # 5. 本地大模型，推荐llama3.2，轻量适合demo
    llm = Ollama(model="llama3.2", temperature=0.2)

    # 6. 核心！return_source_documents=True 开启溯源返回page_content
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain


def ask_question(qa_chain, query: str):
    """
    执行提问，返回答案 + 溯源原文片段
    返回字典：answer, source_texts（list，每一段page_content）
    """
    result = qa_chain.invoke({"query": query})
    answer = result["result"]
    source_docs = result["source_documents"]
    # 提取page_content，供前端Gradio展示溯源
    source_texts = [doc.page_content for doc in source_docs]
    return {
        "answer": answer,
        "source_texts": source_texts
    }


if __name__ == "__main__":
    # 简单自测代码
    test_doc = [Document(page_content="This is test webpage content for RAG pipeline test.")]
    chain = build_rag_chain(test_doc)
    res = ask_question(chain, "What is this about?")
    print("Answer:\n", res["answer"])
    print("\nSource Reference:\n")
    for idx, txt in enumerate(res["source_texts"]):
        print(f"[{idx+1}] {txt}")
