import os
import pandas as pd

def check_mind_data():
    """Check what MIND data we have"""
    base_path = "data\\mind\\MINDsmall_train"
    
    expected_files = {
        "behaviors.tsv": "User interaction logs",
        "news.tsv": "News articles metadata", 
        "entity_embedding.vec": "Entity embeddings (100-dim)",
        "relation_embedding.vec": "Relation embeddings (100-dim)"
    }
    
    print(" Checking MIND Dataset Files")
    print("=" * 40)
    
    all_good = True
    for filename, description in expected_files.items():
        filepath = os.path.join(base_path, filename)
        
        if os.path.exists(filepath):
            size_mb = os.path.getsize(filepath) / (1024*1024)
            print(f" {filename:<25} {size_mb:>6.1f} MB - {description}")
        else:
            print(f" {filename:<25} {'':>6} MB - Missing!")
            all_good = False
    
    return all_good

def peek_at_data():
    """Quick peek at the data structure"""
    base_path = "data\\mind\\MINDsmall_train"
    
    print(f"\n Quick Data Preview")
    print("=" * 40)
    
    try:
        # Check behaviors.tsv
        behaviors_path = os.path.join(base_path, "behaviors.tsv")
        if os.path.exists(behaviors_path):
            df = pd.read_csv(behaviors_path, sep='\t', header=None, nrows=3)
            print(f" behaviors.tsv shape: {df.shape}")
            print(f"   Columns: ImpressionID, UserID, Time, History, Impressions")
            print(f"   Sample UserID: {df.iloc[0, 1]}")
        
        # Check news.tsv  
        news_path = os.path.join(base_path, "news.tsv")
        if os.path.exists(news_path):
            df = pd.read_csv(news_path, sep='\t', header=None, nrows=3)
            print(f" news.tsv shape: {df.shape}")
            print(f"   Columns: NewsID, Category, Subcategory, Title, Abstract, URL, Entities...")
            if len(df) > 0:
                print(f"   Sample: '{str(df.iloc[0, 3])[:50]}...' ({df.iloc[0, 1]} category)")
        
        # Check embeddings
        entity_path = os.path.join(base_path, "entity_embedding.vec")
        if os.path.exists(entity_path):
            with open(entity_path, 'r') as f:
                first_line = f.readline().strip().split('\t')
            print(f" entity_embedding.vec: {first_line[0]} -> 100-dim vector")
        
    except Exception as e:
        print(f" Error reading data: {e}")
        print("This is normal if pandas isn't installed yet")
    
    return True

def count_data():
    """Count total records"""
    base_path = "data\\mind\\MINDsmall_train"
    
    try:
        # Count behaviors
        behaviors_path = os.path.join(base_path, "behaviors.tsv")
        if os.path.exists(behaviors_path):
            with open(behaviors_path, 'r') as f:
                behavior_count = sum(1 for line in f)
            print(f" Total user impressions: {behavior_count:,}")
        
        # Count news
        news_path = os.path.join(base_path, "news.tsv")
        if os.path.exists(news_path):
            with open(news_path, 'r') as f:
                news_count = sum(1 for line in f)
            print(f" Total news articles: {news_count:,}")
        
        # Count entities
        entity_path = os.path.join(base_path, "entity_embedding.vec")
        if os.path.exists(entity_path):
            with open(entity_path, 'r') as f:
                entity_count = sum(1 for line in f)
            print(f" Total entities: {entity_count:,}")
            
    except Exception as e:
        print(f" Error counting: {e}")

if __name__ == "__main__":
    print(" MIND Dataset Checker")
    print("=" * 50)
    
    if check_mind_data():
        print(f"\n All required files found!")
        peek_at_data()
        count_data()
        print(f"\n You're ready to start development!")
        print(f"\nNext steps:")
        print(f"1. Install remaining packages if needed")
        print(f"2. Create first exploration notebook") 
        print(f"3. Start building knowledge graph")
    else:
        print(f"\n Missing some files.")
        print(f"Expected location: data\\mind\\MINDsmall_train\\")