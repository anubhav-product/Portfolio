from playwright.sync_api import sync_playwright
import os

def generate_og_image():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1200, 'height': 630})
        
        # Navigate to the HTML file
        html_path = os.path.join(os.path.dirname(__file__), 'static', 'og-image.html')
        page.goto(f'file://{html_path}')
        
        # Take screenshot
        output_path = os.path.join(os.path.dirname(__file__), 'static', 'og-image.png')
        page.screenshot(path=output_path)
        
        browser.close()
        print(f"✅ OG image generated: {output_path}")

if __name__ == '__main__':
    generate_og_image()
