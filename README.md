## Folder Structure
<pre><code>
news_recommendation_system/
├── README.md
├── requirements.txt
├── .gitignore
├── setup.py
├── config/
│   ├── __init__.py
│   ├── config.yaml                 # Configuration files
│   ├── logging_config.yaml         
│   └── api_keys.yaml.example       
├── data/
│   ├── raw/
│   │   ├── mind/
│   │   │   └── MINDsmall_train/    # MIND dataset
│   │   │       ├── behaviors.tsv
│   │   │       ├── news.tsv
│   │   │       ├── entity_embedding.vec
│   │   │       └── relation_embedding.vec
│   │   └── newsapi/                # NewsAPI cached data
│   ├── processed/
│   │   ├── knowledge_graphs/       # Processed KG files
│   │   ├── user_profiles/          # User preference data
│   │   └── embeddings/             # Generated embeddings
│   └── outputs/
│       ├── recommendations/        # Generated recommendations
│       └── explanations/           # Recommendation explanations
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── mind_loader.py          # MIND dataset loader
│   │   ├── newsapi_client.py       # NewsAPI integration
│   │   ├── data_processor.py       # Data preprocessing
│   │   └── data_validator.py       # Data validation utilities
│   ├── knowledge_graph/
│   │   ├── __init__.py
│   │   ├── kg_constructor.py       # Knowledge Graph construction
│   │   ├── entity_extractor.py     # Named Entity Recognition
│   │   ├── entity_linker.py        # Entity linking and disambiguation
│   │   ├── temporal_updater.py     # Dynamic KG updates
│   │   └── graph_manager.py        # Graph storage and querying
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── llm_interface.py        # LLM API interface
│   │   ├── prompt_templates.py     # Prompt engineering
│   │   ├── reasoning_engine.py     # Chain-of-thought reasoning
│   │   └── explanation_generator.py # Explanation generation
│   ├── recommendation/
│   │   ├── __init__.py
│   │   ├── recommender.py          # Main recommendation engine
│   │   ├── user_profiler.py        # User preference modeling
│   │   ├── candidate_selector.py   # Candidate article selection
│   │   └── ranking_system.py       # Recommendation ranking
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── metrics.py              # Evaluation metrics
│   │   ├── baseline_models.py      # Baseline implementations
│   │   └── user_study.py           # User study framework
│   └── utils/
│       ├── __init__.py
│       ├── logging.py              # Logging utilities
│       ├── cache.py                # Caching mechanisms
│       └── helpers.py              # Helper functions
├── notebooks/
│   ├── 01_data_exploration.ipynb   # MIND dataset exploration
│   ├── 02_kg_construction.ipynb    # Knowledge Graph building
│   ├── 03_llm_integration.ipynb    # LLM integration testing
│   ├── 04_system_evaluation.ipynb # System evaluation
│   └── 05_results_analysis.ipynb  # Results and insights
├── scripts/
│   ├── setup_environment.py       # Environment setup
│   ├── download_data.py           # Data download utilities
│   ├── train_model.py             # Model training script
│   ├── run_evaluation.py          # Evaluation runner
│   └── deploy_system.py           # Deployment script
</code></pre
