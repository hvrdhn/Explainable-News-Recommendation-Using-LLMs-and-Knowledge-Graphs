## Folder Structure
<pre><code>
news_recomm/
├── data/
│   └── mind/
│       └── MINDsmall_train/        # MIND dataset files
│           ├── behaviors.tsv       # User behavior logs
│           ├── news.tsv           # News article metadata
│           ├── entity_embedding.vec # Pre-computed entity embeddings
│           └── relation_embedding.vec # Pre-computed relation embeddings
└── scripts/
    ├── check_data.py              # Data validation and inspection
    └── verify_setup.py            # Environment setup verification
</code></pre>

## Current Progress
Phase 1: Data Exploration  

Environment setup and verification Completed  

MIND dataset integration Completed  

Data validation scripts Completed  

Basic data exploration framework Completed  


In Progress:  


Comprehensive data analysis  

User behavior pattern identification  

Entity relationship mapping  

Phase 2: Knowledge Graph Construction  

Static KG construction from MIND data  

Dynamic KG updates from NewsAPI  

Entity disambiguation and linking  

Temporal consistency management  

