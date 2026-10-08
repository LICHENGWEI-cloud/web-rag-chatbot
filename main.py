import gradio as gr
from web_crawler import load_webpage
from rag_pipeline import build_rag_chain, ask_question

qa_chain_global = None

def load_url_and_build_rag(url):
    global qa_chain_global
    try:
        doc = load_webpage(url)
        qa_chain_global = build_rag_chain([doc])
        return "✅ Webpage loaded & RAG knowledge base built! You can ask questions now."
    except Exception as e:
        return f"❌ Error: {str(e)}"

def chat_query(user_question):
    global qa_chain_global
    if qa_chain_global is None:
        return "⚠️ Please load a webpage URL first!", ""
    res = ask_question(qa_chain_global, user_question)
    answer_out = res["answer"]
    source_out = "\n\n======== Source Reference (page_content) ========\n"
    for i, s in enumerate(res["source_texts"]):
        source_out += f"\n[{i+1}]\n{s}\n"
    return answer_out, source_out

with gr.Blocks(title="Web RAG QA Bot") as demo:
    gr.Markdown("# Web Knowledge Base QA Chatbot")
    gr.Markdown("Input webpage URL → Build knowledge base → Ask questions with source citation")
    url_input = gr.Textbox(label="Webpage URL")
    load_btn = gr.Button("Load Webpage & Build KB")
    load_status = gr.Textbox(label="Status", interactive=False)

    question_input = gr.Textbox(label="Your Question")
    submit_btn = gr.Button("Ask")
    ans_output = gr.Textbox(label="AI Answer", lines=8)
    source_output = gr.Textbox(label="Source Page Content (Citation)", lines=10)

    load_btn.click(load_url_and_build_rag, inputs=[url_input], outputs=[load_status])
    submit_btn.click(chat_query, inputs=[question_input], outputs=[ans_output, source_output])

if __name__ == "__main__":
    demo.launch()
