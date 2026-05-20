# 📺 YouTube Channel Scraper with Browser-Based CSV Viewer

A two-part project that **scrapes video data from any YouTube channel** using Selenium with smart waiting logic, then displays the results in a clean **browser-based CSV viewer** with real-time search and keyword highlighting — no backend needed.

---

## ✨ Features

### 🤖 Scraper (Python)
- Scrapes **any YouTube channel's video list** — just change the URL
- Extracts **Video Title**, **View Count**, and **Upload Date** for each video
- Uses `WebDriverWait` for reliable scraping of dynamically loaded content
- Built-in **data consistency check** — warns if title/view/date counts don't match
- Exports all data to a clean **CSV file**

### 🌐 CSV Viewer (Browser UI)
- Upload the scraped CSV directly in the browser
- Displays data in a formatted **HTML table** with uppercase headers
- **Real-time search** — filters rows instantly as you type
- **Keyword highlighting** — matched text is visually highlighted
- Zero dependencies — pure HTML, CSS, Vanilla JavaScript

---

## 🔁 How It Works

```
Edit channel URL in main.py
        ↓
Run main.py
        ↓
Selenium opens YouTube channel page
        ↓
WebDriverWait loads all video elements
        ↓
Titles, Views & Dates extracted
        ↓
videos.csv saved locally
        ↓
Open index.html in browser
        ↓
Upload videos.csv
        ↓
Browse & search all videos 🎉
```

---

## 🛠️ Tech Stack

| Category       | Technology                              |
|----------------|-----------------------------------------|
| Scraping       | Python, Selenium, WebDriverWait         |
| Data Export    | Python CSV module                       |
| UI             | HTML5, CSS3, Vanilla JavaScript         |
| Browser Parser | FileReader API, DOM Manipulation, XPath |

---

## 📁 Project Structure

```
Web_Scraper_Youtube/
│
├── main.py       # Scraper — fetches YouTube video data & saves to CSV
├── index.html    # CSV Viewer UI — upload, display, search
├── script.js     # FileReader, table rendering & search/highlight logic
└── style.css     # Styling for the viewer interface
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Google Chrome + ChromeDriver (matching your Chrome version)

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Hirad1380/Web_Scraper_Youtube.git
cd Web_Scraper_Youtube

# 2. Install dependencies
pip install selenium
```

### Scrape a YouTube Channel
```python
# In main.py, change this line to any YouTube channel:
url = "https://www.youtube.com/@NetworkChuck/videos"
```

```bash
python main.py
```
A file called `videos.csv` will be created in the project folder.

### View the Results
1. Open `index.html` in your browser
2. Click **Choose a file** and upload `videos.csv`
3. Browse and search all scraped videos

---

## 📊 CSV Output Format

| id | title | view | date |
|----|-------|------|------|
| 0  | How I became a hacker... | 1.2M views | 3 months ago |
| 1  | FREE CCNA Course | 890K views | 1 year ago |
| ...| ...   | ...  | ...  |

---

## ⚠️ Notes

> - YouTube's page structure may change over time, which could require updating the XPath selectors in `main.py`
> - Only videos **visible on the page** are scraped — scroll down first to load more videos before running the script

---

## 👨‍💻 Author

**Hirad Bayat**  
M.Sc. Applied Computer Science — University of Duisburg-Essen  
📧 Bayathirad7@gmail.com  
🔗 LinkedIn: [Hirad Bayat](https://www.linkedin.com/in/hirad-bayat-911480383)  
🐙 GitHub: [Hirad1380](https://github.com/Hirad1380)
