# SQL Chatbot: Natural Language Database Query Engine

An intelligent SQL query generator that converts natural language questions into optimized SQL queries. Powered by Gemini 2.0 Flash with few-shot semantic prompting for enterprise e-commerce databases.

---


## 🧪 Internal Test Scenarios

> [!NOTE]
> Performance benchmarks are based on an internal simulation of **10 test queries** covering various SQL complexities. They do not represent production data or large-scale evaluation.

| Metric | Value |
|--------|-------|
| **Test Set Size** | 10 queries |
| **Simple Queries (Select/Where)** | 100% Pass Rate (Simulated) |
| **Complex Queries (Join/Group)** | ~87% Pass Rate (Simulated) |
| **Average Gen Time** | 0.8s |

### Test Coverage
- **SELECT / WHERE**: Basic data retrieval
- **JOIN operations**: Multi-table data merging
- **Aggregations**: SUM, COUNT, AVG
- **GROUP BY**: Categorical analysis

---

## 🚀 Key Features

- **Natural Language to SQL**: Converts questions to executable SQL.
- **Sub-1s Response Time**: 0.8s average query execution
- **Semantic Few-Shot Prompting**: 8 carefully selected examples for optimal accuracy
- **Dual Query Modes**: Agent-based and Few-Shot QA chains
- **HuggingFace Embeddings**: MiniLM-L6-v2 for fast semantic similarity
- **Production Database Support**: MySQL with connection pooling

## 🛠️ Technical Stack

**Backend:**
- Streamlit (Python 3.8+)
- LangChain with Gemini 2.0 Flash
- SQLAlchemy for database operations
- HuggingFace Embeddings (MiniLM-L6-v2)
- Chroma vector store for semantic similarity

**Architecture:**
- Few-Shot Prompt Engineering with SemanticSimilarityExampleSelector
- ReAct Agent pattern for complex queries
- Chain of Thought reasoning for SQL generation
- Temperature tuning (0.2) for consistency

**Database:**
- MySQL with PyMySQL driver
- Connection pooling for scalability
- Sample rows in table info (3 rows) for context

---

## 📈 Business Impact & Results

- **Automated Query Generation**: Reduces need for manual SQL writing.
- **Verification**: Executes generated SQL to ensure syntax correctness.
- **Support for common patterns**: Handles SELECT, JOIN, and Aggregations.
- **Semantic Selection**: Uses embedding-based example selection.

---



---

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Ecom-chatbot.git
   cd Ecom-chatbot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory with:

   ```
   GOOGLE_API_KEY=your_google_api_key
   MYSQL_PASSWORD=your_mysql_password
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

## Usage

Ask questions about your e-commerce database in natural language:

**Example Queries:**
- "How many T-shirts were sold last month?" → `SELECT COUNT(*) FROM sales WHERE ...`
- "Which products have the highest revenue?" → `SELECT product, SUM(revenue) FROM sales GROUP BY product ORDER BY revenue DESC`
- "What's the average order value by customer segment?" → `SELECT segment, AVG(order_value) FROM customers JOIN orders ON ... GROUP BY segment`

**Two Query Modes:**
1. **Agent Mode**: Uses ReAct framework for complex multi-step reasoning
2. **Few-Shot QA Mode**: Uses semantic similarity to select best examples

---

## 🔑 Key Technical Decisions

- **Gemini 2.0 Flash**: Selected for speed (0.8s) and reasoning capability
- **Semantic Few-Shot Selection**: Dynamically selects relevant examples from vector store
- **Temperature 0.2**: Ensures consistent, deterministic SQL generation
- **MiniLM Embeddings**: Fast semantic ranking for few-shot selection
- **Connection Pooling**: Efficient database connection management

---

## ⚖️ Evaluation Methodology & Limitations

To address referencing of performance metrics:

1.  **Measurement Method**: The metrics cited in early versions (91.2% accuracy) were derived from `evaluate_metrics.py`, which uses a **simulated/heuristic evaluation** on **10 specific queries**. It does not represent a result on a standard benchmark like Spider or WikiSQL.
2.  **Complexity Handling**: The test set includes specific examples of JOINs and Aggregations, but successes are judged based on heuristic string matching or binary execution success in a controlled environment.
3.  **Ambiguity Handling**: The system currently handles ambiguous questions by relying on the semantic similarity selector to find the closest few-shot example. There is no explicit "clarification question" loop implemented yet.

This project is a Proof of Concept (PoC) for RAG-based Text-to-SQL systems.

---

## 📚 Project Structure

- `app.py` — Streamlit chat interface
- `src/utils.py` — LLM and database chain logic
- `src/few_shorts_queries.py` — Few-shot examples for prompting
- `src/mysql_prompt.py` — Custom prompt templates

---

## 🎯 Use Cases

1. **Business Analytics**: "What are top 5 selling products by region?"
2. **Sales Reporting**: "Generate monthly revenue by product category"
3. **Customer Insights**: "Find customers who haven't purchased in 90 days"
4. **Inventory Management**: "Which items are below stock threshold?"
5. **Performance Tracking**: "Compare Q3 vs Q4 sales metrics"

---

## 📝 License & Contact

Built by **[Pawan Parida]** | [GitHub](https://github.com/zer-art)

Contributions welcome! Pull requests and issues appreciated.

---