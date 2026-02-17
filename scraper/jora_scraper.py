import requests

def fetch_jora_jobs(keyword=None, location=None):
    """
    Fetch jobs from Jora API.
    """
    jobs = []
    url = "https://api.jora.com/JobSearch"
    params = {"keywords": keyword or "", "location": location or ""}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        for job in data.get("jobs", []):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company"),
                "location": job.get("location"),
                "url": job.get("url")
            })
    except Exception as e:
        print("Failed to fetch jobs from Jora:", e)
    return jobs

