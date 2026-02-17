import requests
from bs4 import BeautifulSoup

def fetch_wework_jobs(keyword=None, location=None):
    url = "https://weworkremotely.com/remote-jobs/search?term=" + (keyword or "")
    jobs = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for li in soup.select("section.jobs li.feature"):
            a = li.find("a", href=True)
            if not a:
                continue
            title = a.find("span", class_="title").text.strip()
            company = a.find("span", class_="company").text.strip()
            job_location = a.find("span", class_="region").text.strip() if a.find("span", class_="region") else "Remote"
            job_url = "https://weworkremotely.com" + a["href"]
            if keyword and keyword.lower() not in title.lower():
                continue
            if location and location.lower() not in job_location.lower():
                continue
            jobs.append({"title": title, "company": company, "location": job_location, "url": job_url})
    except Exception as e:
        print("Failed to fetch jobs from WeWorkRemotely:", e)
    return jobs

