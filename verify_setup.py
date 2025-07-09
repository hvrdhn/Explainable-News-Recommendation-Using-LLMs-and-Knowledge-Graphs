import sys
import os
import importlib

def check_python():
    """Check Python version"""
    version = sys.version_info
    print(f"Python: {version.major}.{version.minor}.{version.micro}")
    
    if version < (3, 8):
        print("WARNING: Python 3.8+ recommended")
        return False
    return True

def check_packages():
    """Check if required packages are installed"""
    required_packages = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computing', 
        'requests': 'HTTP requests',
        'transformers': 'Hugging Face transformers',
        'torch': 'PyTorch',
        'spacy': 'NLP library',
        'networkx': 'Graph processing',
        'sklearn': 'Machine learning'
    }
    
    print(f"\nChecking packages...")
    missing = []
    
    for package, description in required_packages.items():
        try:
            importlib.import_module(package)
            print(f"OK  {package:<15} - {description}")
        except ImportError:
            print(f"MISSING {package:<15} - {description}")
            missing.append(package)
    
    return len(missing) == 0, missing

def check_spacy_model():
    """Check spaCy English model"""
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        print(f"\nOK spaCy English model loaded")
        return True
    except ImportError:
        print(f"\nMISSING spaCy not installed")
        return False
    except OSError:
        print(f"\nMISSING spaCy English model not found")
        print("Run: python -m spacy download en_core_web_sm")
        return False

def check_mind_data():
    """Check MIND dataset"""
    mind_path = "data\\mind\\MINDsmall_train"
    required_files = [
        "behaviors.tsv",
        "news.tsv", 
        "entity_embedding.vec"
    ]
    
    print(f"\nChecking MIND dataset...")
    
    if not os.path.exists(mind_path):
        print(f"MISSING MIND directory not found: {mind_path}")
        return False
    
    missing_files = []
    for file in required_files:
        full_path = os.path.join(mind_path, file)
        if os.path.exists(full_path):
            size_mb = os.path.getsize(full_path) / (1024*1024)
            print(f"OK  {file:<25} ({size_mb:.1f} MB)")
        else:
            print(f"MISSING {file:<25}")
            missing_files.append(file)
    
    return len(missing_files) == 0

def suggest_next_steps(python_ok, packages_ok, missing_packages, spacy_ok, data_ok):
    """Suggest what to do next"""
    print(f"\nNext Steps:")
    
    if not python_ok:
        print("1. Update Python to 3.8+")
        
    if not packages_ok:
        print("2. Install missing packages:")
        for pkg in missing_packages:
            if pkg in ['torch', 'transformers']:
                print(f" pip install {pkg}")
            else:
                print(f" conda install {pkg}  # or pip install {pkg}")
    
    if not spacy_ok:
        print("3. Install spaCy model:")
        print("   python -m spacy download en_core_web_sm")
    
    if not data_ok:
        print("4. Download MIND dataset:")
        #print("   Download from: https://mind201910small.blob.core.windows.net/release/MINDsmall_train.zip")
        print("   Extract to: data\\mind\\")
    
    if python_ok and packages_ok and spacy_ok and data_ok:
        print("Everything looks good!")
        print("1. Create exploration notebook")
        print("2. Start building knowledge graph")
        print("3. Begin LLM integration")

def main():
    print("News Recommendation System - Setup Verification")
    print("=" * 55)
    
    # Run all checks
    python_ok = check_python()
    packages_ok, missing_packages = check_packages() 
    spacy_ok = check_spacy_model()
    data_ok = check_mind_data()
    
    # Summary
    print(f"\nSetup Status:")
    print(f"Python: {'OK' if python_ok else 'MISSING'}")
    print(f"Packages:    {'OK' if packages_ok else 'MISSING'} ({len(missing_packages)} missing)")
    print(f"spaCy Model: {'OK' if spacy_ok else 'MISSING'}")
    print(f"MIND Data:   {'OK' if data_ok else 'MISSING'}")
    
    all_good = python_ok and packages_ok and spacy_ok and data_ok
    
    if all_good:
        print(f"\nSetup complete! Ready for development.")
    else:
        suggest_next_steps(python_ok, packages_ok, missing_packages, spacy_ok, data_ok)
    
    return all_good

if __name__ == "__main__":
    main()