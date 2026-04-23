import json
import time
from playwright.sync_api import sync_playwright

OUTPUT_FILE = "cookies.json"

def get_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # keep False first time
        context = browser.new_context()

        page = context.new_page()

        # Open Myntra homepage
        page.goto("https://www.myntra.com/", timeout=60000)

        # wait for JS + Akamai to settle
        time.sleep(10)

        # optional: scroll a bit (helps trigger more cookies)
        page.mouse.wheel(0, 2000)
        time.sleep(3)

        # get cookies
        cookies = context.cookies()

        # convert to dict format Scrapy expects
        cookie_dict = {c['name']: c['value'] for c in cookies}

        # save
        with open(OUTPUT_FILE, "w") as f:
            json.dump(cookie_dict, f, indent=4)

        print(f"Saved {len(cookie_dict)} cookies")

        browser.close()


if __name__ == "__main__":
    get_cookies()