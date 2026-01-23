import httpx
import time

BASE_URL = "http://127.0.0.1:8000"
RAPID_API_KEY = "test-verification-key"

def test_api():
    print("--- Starting API Verification ---")
    
    # 1. Test Health Check
    try:
        resp = httpx.get(f"{BASE_URL}/")
        print(f"Health Check: {resp.status_code} - {resp.json()}")
    except Exception as e:
        print(f"Health Check Failed: {e}")
        return

    # 2. Test Auth Failure (Missing Key)
    resp = httpx.post(f"{BASE_URL}/twitter/tweet/analytics", params={"tweet_url": "https://x.com/test"})
    print(f"Auth Failure (Missing Header): {resp.status_code} - {resp.json()}")

    # 3. Test Tweet Analytics
    headers = {"X-RapidAPI-Key": RAPID_API_KEY}
    resp = httpx.post(
        f"{BASE_URL}/twitter/tweet/analytics", 
        params={"tweet_url": "https://x.com/elonmusk/status/123456"},
        headers=headers
    )
    print(f"Tweet Analytics: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Data: {resp.json().get('metrics')}")

    # 4. Test Video Analytics
    resp = httpx.post(
        f"{BASE_URL}/twitter/video/analytics", 
        params={"tweet_url": "https://x.com/elonmusk/status/987654"},
        headers=headers
    )
    print(f"Video Analytics: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Data: {resp.json().get('metrics')}")

    # 5. Test Hashtag Insights
    resp = httpx.post(
        f"{BASE_URL}/twitter/hashtag/insights", 
        params={"hashtag": "Python"},
        headers=headers
    )
    print(f"Hashtag Insights: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Data: {resp.json().get('popularity')}")

    print("--- Verification Complete ---")

if __name__ == "__main__":
    # Wait a bit for server to spin up
    print("Waiting for server...")
    time.sleep(2)
    test_api()
