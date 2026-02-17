# Remote Job Finder CLI

Remote Job Finder CLI aggregates remote job listings from multiple sources and displays them in a terminal-friendly table.  
It saves results to `data/jobs.json` for later reference.

---

## Features

- Fetch remote jobs from multiple sources:  
  - Remotive  
  - RemoteOK  
  - JustRemote  
  - WeWorkRemotely  
- Filter by job keyword and location  
- Display results in colored tables using [Rich](https://github.com/willmcgugan/rich)  
- Save results to JSON for reuse  
- Graceful error handling for sources that fail

---

## Installation

Clone the repository via SSH:

```bash
git clone git@github.com:ashavab/remote-job-finder-cli.git
cd remote-job-finder-cli

