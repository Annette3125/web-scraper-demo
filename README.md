# web-scraper-demo
Python web scraper for CNN headlines. Respects `robots.txt`, avoids duplicates, and saves output to CSV/JSON.

## Prerequisites

Before you start, make sure you have:

- **Python 3.11+** installed  
  Download from https://www.python.org/downloads/  
- **Git** installed (for cloning the repo) 

## Clone the Repo

```commandline
git clone https://github.com/Annette3125/web-scraper-demo.git
cd web-scraper-demo
```
---
### Create virtual environment in project's root directory:
- For Linux/Mac
```
python3 -m venv venv
```
- For Windows 

```
python -m venv venv
```

### Activate the virtual environment

- For Linux/Mac:

```commandline 
source venv/bin/activate
```

- For Windows 

```commandline
venv\Scripts\activate
```

## Dependencies

```commandline
pip install -r requirements.txt
```

## Development
 - I use **Black** and **Isort** for code styling and formatting.

```commandline
pip install black isort
isort .
black .
```

### Run

```commandline
python scrape.py
```

### Output files
The script generates:
- `data/headlines.csv`
- `data/headlines.json`

### CSV format
Columns: `source,url,heading,author,date`
Example of csv output:

```
source,url,heading,author,date
edition.cnn.com,https://edition.cnn.com/2026/03/04/politics/us-troop-deaths-iran-trump-hegseth,Trump’s and Hegseth’s awkward comments about US troop deaths in Iran war,Aaron Blake,"PUBLISHED Mar 4, 2026, 4:45 PM ET"
edition.cnn.com,https://edition.cnn.com/travel/social-bathhouses-north-america,The new going-out spot isn’t a bar. It’s so much hotter than that,,"PUBLISHED Mar 4, 2026, 8:24 AM ET"

```

###### JSON output
A list of objects with keys: `source,url,heading,author,date`

Example of json output:

```

[
    {
        "source": "edition.cnn.com",
        "url": "https://edition.cnn.com/2026/03/12/economy/costs-iran-war-price-groceries",
        "heading": "What Iran war could soon cost you",
        "date": "PUBLISHED Mar 12, 2026, 7:00 AM ET",
        "author": "Elisabeth Buchwald"
    },
   ]

```

## Notes
- The scraper respects `robots.txt` and uses small delays to avoid overloading the website.
- Output files are generated in the `data/` directory.


## License

This project is MIT-licensed. See LICENSE.

###### Future Improvements

 - Add SQLite integration for persistent storage.

A complete Python web scraping pipeline (requests → BeautifulSoup → JSON/CSV).

