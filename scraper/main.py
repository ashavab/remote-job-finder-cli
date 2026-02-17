import sys
import os
import json
from datetime import datetime
import argparse
from tabulate import tabulate

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all scrapers
from scraper.remotive_scraper import fetch_remotive_jobs
from scraper.wework_scraper import fetch_wework_jobs
from scraper.remoteok_scraper import fetch_remoteok_jobs
from scraper.workingnomads_scraper import fetch_workingnomads_jobs
from scraper.jobbatical_scraper import fetch_jobbatical_jobs
from scraper.europeremotely_scraper import fetch_europeremotely_jobs
from scraper.stackoverflow_scraper import fetch_stackoverflow_jobs
from scraper.landing_scraper import fetch_landing_jobs
from scraper.justremote_scraper import fetch_justremote_jobs
from scraper.pangian_scraper import fetch_pangian_jobs

# Import filter utility
from filters.filter_jobs import filter_jobs

def save_jobs_to_json(jobs, filename="data/jobs.json"):
    """Save jobs to JSON with timestamp"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data_to_save = {
        "timestamp": datetime.now().isoformat(),
        "jobs": jobs
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    print(f"\n✅ Jobs saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Remote Job Finder CLI")
    parser.add_argument("-k", "--keyword", type=str, help="Job keyword (e.g., Python, Data Engineer)")
    parser.add_argument("-l", "--location", type=str, help="Location (e.g., UK, Canada, Remote)")
    args = parser.parse_args()

    keyword = args.keyword or input("Enter job keyword: ").strip()
    location = args.location or input("Enter location: ").strip()

    # Fetch jobs from all 10 sources
    print("\nFetching jobs from Remotive...")
    remotive_jobs = fetch_remotive_jobs(keyword, location)

    print("Fetching jobs from WeWorkRemotely...")
    wework_jobs = fetch_wework_jobs(keyword, location)

    print("Fetching jobs from RemoteOK...")
    remoteok_jobs = fetch_remoteok_jobs(keyword, location)

    print("Fetching jobs from Working Nomads...")
    workingnomads_jobs = fetch_workingnomads_jobs(keyword, location)

    print("Fetching jobs from Jobbatical...")
    jobbatical_jobs = fetch_jobbatical_jobs(keyword, location)

    print("Fetching jobs from EuropeRemotely...")
    euro_jobs = fetch_europeremotely_jobs(keyword, location)

    print("Fetching jobs from Stack Overflow Jobs...")
    so_jobs = fetch_stackoverflow_jobs(keyword, location)

    print("Fetching jobs from Landing.jobs...")
    landing_jobs = fetch_landing_jobs(keyword, location)

    print("Fetching jobs from JustRemote...")
    justremote_jobs = fetch_justremote_jobs(keyword, location)

    print("Fetching jobs from Pangian...")
    pangian_jobs = fetch_pangian_jobs(keyword, location)

    # Combine all jobs
    all_jobs = (
        remotive_jobs + wework_jobs + remoteok_jobs +
        workingnomads_jobs + jobbatical_jobs + euro_jobs +
        so_jobs + landing_jobs + justremote_jobs + pangian_jobs
    )

    if not all_jobs:
        print("No jobs found.")
        return

    # Filter jobs by keyword and location
    all_jobs = filter_jobs(all_jobs, keyword=keyword, location=location)

    # Display jobs in table
    table = [
        [i+1, j["title"], j["company"], j["location"], j["url"]]
        for i, j in enumerate(all_jobs)
    ]
    print(tabulate(table, headers=["#", "Job Title", "Company", "Location", "Link"], tablefmt="grid"))

    # Save jobs to JSON
    save_jobs_to_json(all_jobs)

if __name__ == "__main__":
    main()

