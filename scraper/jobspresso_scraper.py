import requests

def fetch_jobspresso_jobs(keyword=None, location=None):
    jobs = []
    url = "https://jobspresso.co/api/jobs/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for job in data.get("jobs", []):
            title = job.get("title")
            job_location = job.get("location")
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
        print("Failed to fetch jobs from Jobspresso:", e)
    return jobs

