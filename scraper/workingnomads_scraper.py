import requests

def fetch_workingnomads_jobs(keyword=None, location=None):
    jobs = []
    url = "https://www.workingnomads.co/api/v1/jobs"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for job in data:
            title = job.get("title")
            job_location = job.get("tags", {}).get("location", "Remote")
            if keyword and keyword.lower() not in title.lower():
                continue
            if location and location.lower() not in job_location.lower():
                continue
            jobs.append({
                "title": title,
                "company": job.get("company"),
                "location": job_location,
                "url": job.get("url")
            })
    except Exception as e:
        print("Failed to fetch jobs from WorkingNomads:", e)
    return jobs


