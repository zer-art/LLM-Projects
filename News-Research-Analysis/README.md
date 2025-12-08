# 📰 News Research Chatbot: RAG-Powered News Analysis

An intelligent news research assistant using Retrieval-Augmented Generation (RAG) to extract insights from multiple news sources. Powered by Gemini 2.0 Flash with HuggingFace embeddings for semantic search and contextual understanding.

---



---

## 🚀 Key Features

- **Advanced RAG Pipeline**: Retrieval-Augmented Generation for factually grounded answers
- **Response Time**: Tuned for speed with streaming support
- **Multi-Source Integration**: Process and synthesize multiple news URLs simultaneously
- **Semantic Search**: HuggingFace embeddings for accurate document ranking
- **Low Hallucination**: Grounding in source material to minimize errors

---

## 🛠️ Technical Stack

**Backend:**
- Streamlit (Python 3.8+)
- LangChain with Gemini 2.0 Flash
- HuggingFace Embeddings for semantic search
- LangChain community loaders for web scraping
- Chroma vector database for similarity search

**Architecture:**
- Retrieval-Augmented Generation (RAG) pipeline
- Semantic similarity with top-k retrieval (k=2)
- Chain of Thought reasoning for synthesis
- Temperature tuning (0.2) for consistency
- Max output tokens: 1024 for balanced responses
- Top-p sampling (0.95) for diversity

**Performance Optimizations:**
- Parallel document loading for multi-URL support
- Batch embedding generation
- Efficient vector similarity search
- Response streaming for real-time feedback

---

## 📈 Business Impact & Results

- **Processed multiple news articles** for synthesis
- **Reduced research time** vs manual reading
- **Multi-source synthesis** form multiple URLs
- **Factually grounded answers** via RAG
- **Context grounding**: Uses BERT-based embeddings for semantic alignment
- **Production-ready**: Handles concurrent queries

---



---

## 🔑 Key Technical Decisions

- **Gemini 2.0 Flash**: Selected for speed and accuracy balance
- **Top-k=2**: Optimal balance between context richness and cost
- **Temperature 0.2**: Ensures factually consistent answers
- **Max tokens 1024**: Comprehensive answers without excessive length
- **Top-p 0.95**: Diverse yet coherent synthesis from multiple sources

---

## ⚖️ Evaluation Methodology & Limitations

> [!NOTE]
> The performance metrics referenced in earlier versions of this project (NDCG@5, Accuracy %) were simulated for demonstration purposes.

To address transparency regarding the evaluation framework:

1.  **NDCG@5 Measurement**: This metric was **not measured on real data** in the current repository state. A true NDCG calculation requires a dataset of (query, document) pairs with manually annotated relevance scores (e.g., 0-4 scale), which is outside the scope of this initial implementation.
2.  **Ground Truth**: There is **no manually annotated ground truth** for news articles included here. The project aims to demonstrate the RAG architecture rather than claim SOTA performance on a specific benchmark.
3.  **Framework**: A proper evaluation would involve:
    - Collecting a "Golden Dataset" of questions and ideal answers/relevant chunks.
    - Using tools like `RAGAS` or `TruLens` for automated evaluation, or human annotators for ground truth.

The metrics script (`evaluate_metrics.py`) serves as a placeholder to show *how* one might structure an evaluation pipeline, but it uses hardcoded/simulated values.

---

1. **Clone the repository:**
    ```bash
    git clone https://github.com/zer-art/News-Research-Analysis
    
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**
    - Create a `.env` file in the project root:
      ```
      GEMINI_API_KEY=your_google_gemini_api_key
      ```
    - You can get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

4. **Run the app:**
    ```bash
    streamlit run app.py
    ```


### ✅ Real-World Performance (Verified)

We include a `benchmark_performance.py` script to test the system's actual latency on your machine.
Running the benchmark on 3 dense Wikipedia articles (AI, ML, Deep Learning) yielded:

- **Document Loading & Indexing**: ~25.8s (for 3 long articles)
- **Retrieval Latency**: ~288ms (Average vector search time)
- **Generation Speed**: *Dependent on Gemini API latency (typically 2-3s)*

> **To Reproduce:** Run `python benchmark_performance.py` in your environment.

## Usage

**Example Research Queries:**
- "Compare the key differences between the two articles"
- "What are the main takeaways from these news stories?"
- "Summarize the impact on the tech industry"
- "Find all mentions of [company name] across the sources"

**Supported News Sources:**
- BBC News
- CNN
- Reuters
- TechCrunch
- And any article with accessible text content

---

## 🎯 Use Cases

1. **Market Research**: Analyze competitor news across multiple sources
2. **Trend Analysis**: Identify emerging patterns from recent articles
3. **Due Diligence**: Research companies through multiple news outlets
4. **Content Curation**: Synthesize information for newsletters/reports
5. **Crisis Monitoring**: Track real-time news on key topics

---

## 🚨 Best Practices

- Use direct article links (not homepage URLs)
- Provide 2-5 sources for best synthesis accuracy
- Specific questions yield better results than broad queries
- News content with clear HTML structure works best
- For paywalled sites, use article summaries or public previews

---

## 📝 License & Contact

Built by **[Pawan Kumar]** | [GitHub](https://github.com/zer-art)

Contributions welcome! Pull requests and issues appreciated.

---