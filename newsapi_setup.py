import requests
import json
from datetime import datetime, timedelta
import os

def test_newsapi():
    """Test NewsAPI connection"""
    
    # Check for API key
    api_key = os.getenv('NEWSAPI_KEY')
    if not api_key:
        print(" NewsAPI key not found!")
        print("1. Get API key from: https://newsapi.org/")
        print("2. Create .env file with: NEWSAPI_KEY=your_key_here")
        return False
    
    print(f" Found NewsAPI key: {api_key[:10]}...")
    
    # Test API call
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'apiKey': api_key,
        'country': 'us',
        'pageSize': 5
    }
    
    try:
        print(f" Testing API connection...")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f" API working! Found {data['totalResults']} articles")
            
            # Show sample articles
            print(f"\n Sample articles:")
            for i, article in enumerate(data['articles'][:3], 1):
                title = article['title'][:60] + "..." if len(article['title']) > 60 else article['title']
                print(f"{i}. {title}")
                print(f"   Source: {article['source']['name']}")
                print(f"   Published: {article['publishedAt']}")
                print()
            
            return True
            
        elif response.status_code == 401:
            print(f" API key invalid or expired")
            return False
        elif response.status_code == 429:
            print(f" Rate limit exceeded")
            return False
        else:
            print(f" API error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f" Connection error: {e}")
        return False

if __name__ == "__main__":
    print(" NewsAPI Tester")
    print("=" * 30)
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print(" python-dotenv not installed, checking OS environment")
    
    if test_newsapi():
        print(f" NewsAPI ready for use!")
    else:
        print(f" NewsAPI setup needed")