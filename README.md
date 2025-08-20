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

# Current Progress
## Phase 1: Data Exploration  

Environment setup and verification Completed  

MIND dataset integration Completed  

Data validation scripts Completed  

Basic data exploration framework Completed  


In Progress:  


Comprehensive data analysis  

User behavior pattern identification  

Entity relationship mapping  

## Phase 2: Knowledge Graph Construction  

Static KG construction from MIND data  

Dynamic KG updates from NewsAPI  

Entity disambiguation and linking  

Temporal consistency management  

