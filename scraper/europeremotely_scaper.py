import requests

def fetch_europeremotely_jobs(keyword=None, location=None):
    url = "https://europeremotely.com/api/jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    jobs = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        for job in data.get("jobs", []):
            title = job.get("title")
            company = job.get("company")
            job_location = job.get("location", "Remote")
            job_url = job.get("url")
            if keyword and keyword.lower() not in title.lower():
                continue
            if location and location.lower() not in job_location.lower():
                continue
            jobs.append({"title": title, "company": company, "location": job_location, "url": job_url})
    except Exception as e:
        print("Failed to fetch jobs from EuropeRemotely:", e)
    return jobs

