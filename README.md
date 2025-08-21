# Explainable News Recommendation Using LLMs and Knowledge Graphs  

A two-component news recommendation system that combines Large Language Models (LLMs) and dynamic Knowledge Graphs (KGs) to deliver personalized, explainable, and real-time news recommendations.  

![image alt](https://github.com/hvrdhn/Explainable-Real-Time-News-Recommendation-Using-LLMs-and-Knowledge-Graphs/blob/fef6295a11708a5521bc1f2f3b1bb6f153c973ef/architecture.jpeg)

# Folder Structure
<pre><code>
news_recomm/
├── data/
│   └── mind/
│       └── MINDsmall_train/        # MIND dataset files
│           ├── behaviors.tsv       # User behavior logs
│           ├── news.tsv            # News article metadata
│           ├── entity_embedding.vec  # Entity embeddings
│           └── relation_embedding.vec  # Relation embeddings
└── scripts/
    ├── check_data.py              # Data Verification
    └── verify_setup.py            # Environment setup verification
</code></pre>


# Phase 1: Data Preparation & Exploration 

### Data Preparation

- This project uses the [MIND dataset](https://msnews.github.io/) for news recommendation tasks.  
 > **Note:** The dataset is large and not included in this repository. Please download it directly from the official website.

- Download the MIND dataset from Microsoft Research  
- Extract to `data/mind/MINDsmall_train/`  
- Ensure the following files are present:  
  - `news.tsv`  
  - `behaviors.tsv`  
  - `entity_embedding.vec`  

### MIND Dataset contains:
- 51,282 news articles  
- 156,965 user behavior records  
- 26,904 entity embeddings  
- Rich metadata including categories, subcategories, and entity annotations  

---

## Phase 2: Knowledge Graph Construction  

- Static KG construction from MIND data  

### Graph Structure:
- **Nodes: 129,041 total**
  - 27,759 Entity nodes  
  - 51,282 News nodes  
  - 50,000 User nodes  
- **Edges: 7,526,846 total**
  - Entity–News relationships (mentions)  
  - Entity–Entity co-occurrences  
  - User–News interactions (clicks/views)  

### Usage
from kg_construction import (
    load_mind_data, 
    build_knowledge_graph, 
    add_user_interactions, 
    add_entity_relations, 
    get_graph_stats, 
    save_knowledge_graph
)

### Load MIND dataset
- `news_df, behaviors_df, entity_embeddings = load_mind_data()`

### Build base knowledge graph (News + Entities)
- `KG = build_knowledge_graph(all_entities, entity_news_mapping, news_df)`

### Add user interactions (clicks/views from behaviors.tsv)
- `KG = add_user_interactions(KG, behaviors_df)`

### Add entity-entity co-occurrence relations (from entity embeddings or news mentions)
- `KG = add_entity_relations(KG, entity_embeddings)`

### Check graph statistics
- `stats = get_graph_stats(KG)`

### Save knowledge graph to file (json or pickle)
- `save_knowledge_graph(KG, "outputs/knowledge_graph.json")`


---

## Phase 3: LLM Integration

```python
from llm_integration import (
    load_knowledge_graph, 
    query_knowledge_graph, 
    generate_llm_response
)

### Load knowledge graph (from Phase 2)
-KG = load_knowledge_graph("outputs/knowledge_graph.graphml")

### Example query: retrieve news + entities for a given user
-context = query_knowledge_graph(KG, user_id)

### Pass KG context into LLM for reasoning
-prompt = f"""
    You are a recommendation assistant. 
    Here is the user’s interaction context from the Knowledge Graph:
    {context}
    Suggest 3 personalized news articles and explain why.
    """

-response = generate_llm_response(prompt)```
```

## Phase 4: Evaluation

```python
from evaluation import evaluate_auc, evaluate_mrr, evaluate_ndcg
```

### Run evaluation
    -auc_score   = evaluate_auc(predictions, ground_truth)
    -mrr_score   = evaluate_mrr(predictions, ground_truth)
    -ndcg_5      = evaluate_ndcg(predictions, ground_truth, k=5)
    -ndcg_10     = evaluate_ndcg(predictions, ground_truth, k=10)



