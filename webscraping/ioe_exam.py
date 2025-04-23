import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
from datetime import datetime, date

url = "http://exam.ioe.edu.np"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

notices = soup.select("table tbody tr")

today_notices = []

for notice in notices:
    tds = notice.find_all("td")

    # check if row data is incomplete
    if len(tds) < 4:
        continue

    # Parse the string to a date object
    date_str = tds[2].text.strip()
    try:
        notice_date = datetime.strptime(date_str, "%A, %B %d, %Y").date()
    except ValueError:
        continue 

    # Add the today's notices to the data
    if notice_date != date.today():
        data = {}

        data["date"] = notice_date.isoformat()
        title_tag = tds[1].find("a")
        data["title"] = title_tag.text.strip()

        relative_link = title_tag["href"]
        encoded_path = quote(relative_link, safe="/")
        data["link"] = urljoin(url, encoded_path)

        today_notices.append(data)


filename = f"data_{str(date.today())}.json"

with open(filename, "w") as f:
    json.dump(today_notices, f, indent=2)
