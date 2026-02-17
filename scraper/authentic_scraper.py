import requests

API_KEY = "YOUR_AUTHENTIC_API_KEY"  # You need a free key

def fetch_authentic_jobs(keyword=None, location=None):
    jobs = []
    url = "https://authenticjobs.com/api/"
    params = {
        "api_key": API_KEY,
        "format": "json",
        "keywords": keyword or "",
        "location": location or ""
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        for job in data.get("listings", {}).get("listing", []):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("name"),
                "location": job.get("location"),
                "url": job.get("url")
            })
    except Exception as e:
        print("Failed to fetch jobs from AuthenticJobs:", e)
    return jobs

