import requests
import xml.etree.ElementTree as ET

def fetch_stackoverflow_jobs(keyword=None, location=None):
    url = "https://stackoverflow.com/jobs/feed"
    headers = {"User-Agent": "Mozilla/5.0"}
    jobs = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        for item in root.findall(".//item"):
            title = item.find("title").text
            link = item.find("link").text
            job_location = item.find("location").text if item.find("location") is not None else "Remote"
            company = item.find("company").text if item.find("company") is not None else "N/A"
            if keyword and keyword.lower() not in title.lower():
                continue
            if location and location.lower() not in job_location.lower():
                continue
            jobs.append({"title": title, "company": company, "location": job_location, "url": link})
    except Exception as e:
        print("Failed to fetch jobs from Stack Overflow:", e)
    return jobs

