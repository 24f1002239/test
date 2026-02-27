from playwright.sync_api import sync_playwright

def main():
    total_sum = 0
    base_url = "https://sanand0.github.io/tdsdata/js_table/?seed="
    
    with sync_playwright() as p:
        # Launch headless browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for seed in range(50, 60):
            url = f"{base_url}{seed}"
            print(f"Navigating to {url}...")
            page.goto(url)
            
            # Best practice for dynamic content: wait for the specific element to appear
            page.wait_for_selector("table td", timeout=10000)
            
            # Extract all table data cells
            cells = page.query_selector_all("table td")
            
            page_sum = 0
            for cell in cells:
                text = cell.inner_text().strip()
                try:
                    # Convert text to float and add to sum
                    page_sum += float(text)
                except ValueError:
                    # Skip any non-numeric headers or empty cells
                    pass 
            
            print(f"Sum for seed {seed}: {page_sum}")
            total_sum += page_sum
            
        print(f"\n--- FINAL TOTAL SUM: {total_sum} ---")
        browser.close()

if __name__ == "__main__":
    main()
