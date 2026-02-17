def filter_jobs(jobs, keyword=None, location=None):
    filtered = []
    for job in jobs:
        if keyword and keyword.lower() not in job["title"].lower():
            continue
        if location and location.lower() not in job["location"].lower():
            continue
        filtered.append(job)
    return filtered

