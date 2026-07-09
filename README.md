# Citekit


## What it is
 
A command-line research tool for policy debaters. Paste a URL, get a formatted debate card that includes qualifications, authors, publication, and date.
 
---
 
## The Problem
 
Policy debaters spend hours manually formatting evidence. Author qualifications get forgotten and citation format is inconsistent. Citekit automates the tedious part of cutting evidence so debaters can focus on the evidence itself.
 
---
 
## What It Does
 
- Paste a URL and automatically pull the author, title, publication, and date
- Handles multi-author cards correctly — two authors get `Smith & Jones`, three or more get `Smith et al`
- Prompts you for qualifications, tag, notes, and signature
- Saves every source to a local JSON database
- Search saved sources by any keyword
- Filter by author or tag
- Generate a formatted debate citation on demand
---
 
## Example Output
 
```
[US China competition]
Dunnmon et al 26 — Jared Dunnmon & Avanika Narayan & Jon Saad-Falcon, 2026-05-29,
Jared Dunnmon is a Rhodes Scholar and PhD in Mechanical Engineering from Stanford.
"China's AI Heist," Foreign Affairs,
https://www.foreignaffairs.com/china/chinas-ai-heist, GJM
```
 
---
 
## How to Run
 
```bash
git clone https://github.com/yourusername/citekit.git
cd citekit
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python main.py
```
 
---
 
## Menu
 
```
1. Add source manually
2. Scrape source from URL
3. View saved sources
4. Search sources
5. Export citation
6. Quit
```
 
---
 
## Current Limitations
 
URL scraping currently works best with Foreign Affairs. Support for RAND, Brookings, CSIS, and other policy sources is "in development".
 
---
 
## Potential New Features
 
- [ ] Site-specific scrapers for RAND, Brookings, CSIS, War on the Rocks
- [ ] Export citations to a text file
- [ ] Delete and edit saved sources
---
 
## Author
 
Garrett Martin -- built to learn basic Python through a topic I care about


