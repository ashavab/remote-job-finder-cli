import requests

def fetch_remoteok_jobs(keyword=None, location=None):
    url = "https://remoteok.io/api"
    headers = {"User-Agent": "Mozilla/5.0"}
    jobs = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        for job in data[1:]:  # first element is metadata
            title = job.get("position")
            company = job.get("company")
            job_location = job.get("location", "Remote")
            job_url = job.get("url")
            if keyword and keyword.lower() not in title.lower():
                continue
            if location and location.lower() not in job_location.lower():
                continue
            jobs.append({"title": title, "company": company, "location": job_location, "url": "https://remoteok.io"+job_url})
    except Exception as e:
        print("Failed to fetch jobs from RemoteOK:", e)
    return jobs

