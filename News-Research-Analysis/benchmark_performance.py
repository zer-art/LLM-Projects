
import time
import os
from src.rag import load_rag_chain
from langchain_core.messages import BaseMessage

# Use Wikipedia articles as stable targets for benchmarking
URLS = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Deep_learning"
]

QUERIES = [
    "What is the difference between AI and ML?",
    "Explain the history of deep learning briefly.",
    "What are neural networks?"
]

def run_benchmark():
    print("="*50)
    print("🚀 Starting Performance Benchmark")
    print("="*50)
    print(f"Target URLs ({len(URLS)}):")
    for u in URLS:
        print(f" - {u}")
    print("-" * 50)

    # 1. Measure Knowledge Base Loading Time
    print("\n[1/2] Benchmarking Knowledge Base Creation...")
    start_time = time.time()
    try:
        rag_chain = load_rag_chain(",".join(URLS))
    except Exception as e:
        print(f"❌ Failed to load chain: {e}")
        return
    end_time = time.time()
    
    load_time = end_time - start_time
    print(f"✅ Knowledge Base Loaded in {load_time:.2f} seconds")
    
    # 2. Measure Query Performance (Retrieval Only due to Quota)
    print("\n[2/2] Benchmarking Retrieval (skipping LLM gen due to quota)...")
    
    total_latency = 0
    
    # Access retriever from chain logic if possible, or recreate
    # Since chain is LCEL, we can't easily extract retriever unless we expose it.
    # But we can use the vectorstore from the previous step if load_rag_chain returned it?
    # load_rag_chain returns the chain.
    
    # Let's just create a new retriever for benchmarking since we know the URLS
    from src.utils import Knowledgebase
    kb = Knowledgebase(URL=URLS)
    # We already loaded, so vectorstore.pkl exists. 
    # But for clean benchmark, let's just assume we reload
    
    # Actually, let's use the 'rag_chain' but inspect it? No, LCEL is opaque.
    # We'll just run the chain and catch the error, OR we can hack it.
    
    # Better: Measure the KB construction (already done).
    # Then measure retrieval speed by calling the retriever directly.
    # We need to expose retriever from load_rag_chain or recreate it.
    
    # Re-instantiate retriever to test speed
    print("   -> Creating test retriever...")
    import pickle
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS
    
    embd = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # vectorstore should be saved by load_rag_chain in vectorstore.pkl
    if os.path.exists("vectorstore.pkl"):
        print("   -> Loading pickled vectorstore...")
        with open("vectorstore.pkl", "rb") as f:
            vectorstore = pickle.load(f)
        retriever = vectorstore.as_retriever(search_kwargs={"k":2})
        
        for i, query in enumerate(QUERIES, 1):
            print(f"\nRunning Retrieval {i}: '{query}'")
            q_start = time.time()
            docs = retriever.invoke(query)
            q_end = time.time()
            latency = q_end - q_start
            print(f"   -> Retrieval Latency: {latency:.4f}s")
            print(f"   -> Retrieved {len(docs)} docs")
            total_latency += latency
            
        avg_latency = total_latency / len(QUERIES)

        print("\n" + "="*50)
        print("📊 BENCHMARK RESULTS (REAL - RETRIEVAL ONLY)")
        print("="*50)
        print(f"KB Construction Time (3 Wiki Pages): {load_time:.2f}s")
        print(f"Average Retrieval Time:              {avg_latency:.4f}s")
        print("="*50)
        
        # Generate Markdown snippet for README
        print("\nPlaintext for README:")
        print("```text")
        print(f"- **Document Loading**: {load_time:.2f}s (3 Wiki pages)")
        print(f"- **Retrieval Latency**: {avg_latency*1000:.0f}ms (local vector search)")
        print("```")
    else:
        print("Vectorstore not found, cannot benchmark retrieval.")


if __name__ == "__main__":
    run_benchmark()
