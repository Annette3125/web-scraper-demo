# web-scraper-demo
Demo project: Python web scraper for CNN headlines.

## Prerequisites

Before you start, make sure you have:

- **Python 3.11+** installed  
  Download from https://www.python.org/downloads/  
- **Git** installed (for cloning the repo) 

### Code Editor

- A code editor or IDE of your choice
- Recommended  PyCharm Community Edition or VS Code
- Any editor that supports Python will work.


## Installation

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

- For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

- For Windows CMD:

```comandline
.venv\Scripts\activate.bat
```

## Upgrade pip (all OS)
```commandline
python -m pip install --upgrade pip
```

## Dependencies

```commandline
pip install -r requirements.txt
```

## Clone the Repo

```commandline
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## Development
 - I use **Black** and **Isort** for code styling and formatting.

```commandline
pip install black isort
```


## Usage and Running

#### How to run script:

```commandline
python scrape.py

```
##### CSV file

Saves web_scraper_demo/data/headlines1.scv with columns: Source,url,Heading,author,date.
CSV file will be generated in directory data/healines1/.

Example of csv output:

```
Source,url,Heading,author,date
edition.cnn.com,https://edition.cnn.com/2025/07/25/investing/us-stock-market,Sweet spot for tariffs,John Towfighi,
edition.cnn.com,https://edition.cnn.com/2025/07/25/india/india-bjp-english-language-tensions-intl-hnk-dst,The language dilemma,,"PUBLISHED Jul 25, 2025, 8:30 PM ET"
edition.cnn.com,https://edition.cnn.com/science/hawaii-mosquitoes-rare-birds-drones-c2e-spc,Drones drop mosquitoes,Nell Lewis,
edition.cnn.com,https://edition.cnn.com/2025/07/25/climate/heat-speed-up-biological-aging,Extreme heat and aging,Laura Paddison,"PUBLISHED Jul 25, 2025, 8:12 AM ET"
edition.cnn.com,https://edition.cnn.com/2025/07/25/travel/european-versus-us-ice-water-debate,Ice-obsessed Americans,Francesca Street,"PUBLISHED Jul 25, 2025, 9:40 AM ET"
edition.cnn.com,https://edition.cnn.com/2025/07/25/science/neanderthal-diet-maggots-rotten-meat,The real Paleo diet,Katie Hunt,"PUBLISHED Jul 25, 2025, 2:00 PM ET"
edition.cnn.com,https://edition.cnn.com/2025/07/25/entertainment/kelly-osbourne-ozzy-death-intl-scli,Kelly Osbourne,Issy Ronald,"PUBLISHED Jul 25, 2025, 5:24 AM ET"
edition.cnn.com,https://edition.cnn.com/2025/07/25/politics/donald-trump-israel-hamas-war,Trump tells Israel to ‘finish the job’ against Hamas,Kevin Liptak,"PUBLISHED Jul 25, 2025, 3:43 PM ET"
edition.cnn.com,https://edition.cnn.com/world/live-news/israel-hamas-gaza-news-07-26-25,Six-month-old baby dies in Gaza amid starvation crisis,Laura Sharman,
```


###### JSON file
Saves web_scraper_demo/data/headlines1.json with columns: Source,url,Heading,author,date.
CSV file will be generated in directory data/healines1/.

Example of json output:

```
[
    {
        "source": "edition.cnn.com",
        "url": "https://edition.cnn.com/2025/07/25/investing/us-stock-market",
        "heading": "Sweet spot for tariffs",
        "date": null,
        "author": "John Towfighi"
    },
    {
        "source": "edition.cnn.com",
        "url": "https://edition.cnn.com/2025/07/25/india/india-bjp-english-language-tensions-intl-hnk-dst",
        "heading": "The language dilemma",
        "date": "PUBLISHED Jul 25, 2025, 8:30 PM ET",
        "author": null
    },
    ]

```


```commandline
deactivate
```
And activate as you start again.

Future Improvements

 - - Add SQLite integration for persistent storage.

Created by Annette demonstrating web scrapping demo for CNN healines.







