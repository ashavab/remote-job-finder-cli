import sys
import os
import json
from datetime import datetime
import argparse
from tabulate import tabulate
from filters.filter_jobs import filter_jobs

from rich.console import Console
from rich.table import Table

console = Console()

# Display jobs in a nice table
table = Table(title=f"Remote Jobs for '{keyword}' in '{location}'")

table.add_column("#", style="cyan", width=4)
table.add_column("Job Title", style="magenta")
table.add_column("Company", style="green")
table.add_column("Location", style="yellow")
table.add_column("Link", style="blue", overflow="fold")

for i, j in enumerate(all_jobs, 1):
    table.add_row(str(i), j["title"], j["company"], j["location"], j["url"])

console.print(table)

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all scrapers
from scraper.remotive_scraper import fetch_remotive_jobs
from scraper.remoteok_scraper import fetch_remoteok_jobs
from scraper.justremote_scraper import fetch_justremote_jobs
from scraper.wework_scraper import fetch_wework_jobs

# Placeholder scrapers (add code later)
from scraper.jobbatical_scraper import fetch_jobbatical_jobs
from scraper.europeremotely_scraper import fetch_europeremotely_jobs
from scraper.stackoverflow_scraper import fetch_stackoverflow_jobs
from scraper.landing_scraper import fetch_landing_jobs
from scraper.pangian_scraper import fetch_pangian_jobs

def save_jobs_to_json(jobs, filename="data/jobs.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data_to_save = {
        "timestamp": datetime.now().isoformat(),
        "jobs": jobs
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    print(f"\n✅ Jobs saved to {filename}")

def safe_fetch(fetch_func, keyword, location, source_name):
    try:
        return fetch_func(keyword, location)
    except Exception as e:
        print(f"Failed to fetch jobs from {source_name}: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Remote Job Finder CLI")
    parser.add_argument("-k", "--keyword", type=str, help="Job keyword (e.g., Python, Data Engineer)")
    parser.add_argument("-l", "--location", type=str, help="Location (e.g., UK, Canada, Remote)")
    args = parser.parse_args()

    keyword = args.keyword or input("Enter job keyword: ").strip()
    location = args.location or input("Enter location: ").strip()

    # Fetch jobs safely
    remotive_jobs = safe_fetch(fetch_remotive_jobs, keyword, location, "Remotive")
    remoteok_jobs = safe_fetch(fetch_remoteok_jobs, keyword, location, "RemoteOK")
    justremote_jobs = safe_fetch(fetch_justremote_jobs, keyword, location, "JustRemote")
    wework_jobs = safe_fetch(fetch_wework_jobs, keyword, location, "WeWorkRemotely")
    
    # Placeholder scrapers (may fail if API keys not set)
    jobbatical_jobs = safe_fetch(fetch_jobbatical_jobs, keyword, location, "Jobbatical")
    euro_jobs = safe_fetch(fetch_europeremotely_jobs, keyword, location, "EuropeRemotely")
    so_jobs = safe_fetch(fetch_stackoverflow_jobs, keyword, location, "Stack Overflow Jobs")
    landing_jobs = safe_fetch(fetch_landing_jobs, keyword, location, "Landing.jobs")
    pangian_jobs = safe_fetch(fetch_pangian_jobs, keyword, location, "Pangian")

    # Combine all jobs
    all_jobs = (
        remotive_jobs + remoteok_jobs + justremote_jobs + wework_jobs +
        jobbatical_jobs + euro_jobs + so_jobs + landing_jobs + pangian_jobs
    )

    if not all_jobs:
        print("No jobs found.")
        return

    # Filter by keyword and location
    all_jobs = filter_jobs(all_jobs, keyword=keyword, location=location)

    # Display jobs
    table = [
        [i+1, j["title"], j["company"], j["location"], j["url"]]
        for i, j in enumerate(all_jobs)
    ]
    print(tabulate(table, headers=["#", "Job Title", "Company", "Location", "Link"], tablefmt="grid"))

    # Save jobs
    save_jobs_to_json(all_jobs)

if __name__ == "__main__":
    main()

