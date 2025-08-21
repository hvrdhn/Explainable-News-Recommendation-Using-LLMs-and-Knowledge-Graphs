# Explainable News Recommendation Using LLMs and Knowledge Graphs  

A two-component news recommendation system that combines Large Language Models (LLMs) and dynamic Knowledge Graphs (KGs) to deliver personalized, explainable, and real-time news recommendations.  

![image alt](https://github.com/hvrdhn/Explainable-Real-Time-News-Recommendation-Using-LLMs-and-Knowledge-Graphs/blob/fef6295a11708a5521bc1f2f3b1bb6f153c973ef/image.png)

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

