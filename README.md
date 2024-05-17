# Capsolver Extension Python

Capsolver Extension Python helps you easily use Capsolver Extension in Botasaurus, Selenium, and Playwright.

You can easily configure Capsolver with an API key without needing to download the Capsolver Extension, update config files, etc.


## Installation

```bash 
python -m pip install capsolver_extension_python
```

## Usage with [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)

```python
from botasaurus.browser import browser, Driver
from capsolver_extension_python import Capsolver

@browser(
    extensions=[Capsolver(api_key="CAP-MY_KEY")], # TODO: Replace with your own CapSolver Key
)  
def solve_captcha(driver: Driver, data):
    driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    driver.prompt()

solve_captcha()
```

## Usage with Selenium 

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_autoinstaller import install
from capsolver_extension_python import Capsolver

# Set Chrome options
options = Options()
options.add_argument(Capsolver(api_key="CAP-MY_KEY").load()) # TODO: Replace with your own CapSolver Key
# Install and set up the driver
driver_path = install()
driver = webdriver.Chrome(driver_path, options=options)

# Navigate to the desired URL
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")

# Prompt for user input
input("Press Enter to exit...")

# Clean up
driver.quit()
```

## Usage with Playwright

```python
from playwright.sync_api import sync_playwright
from capsolver_extension_python import Capsolver
import random

def generate_random_profile():
    return str(random.randint(1, 1000))

with sync_playwright() as p:
    extension_path = Capsolver(api_key="CAP-MY_KEY").load(with_command_line_option=False) # TODO: Replace with your own CapSolver Key
    browser = p.chromium.launch_persistent_context(
        user_data_dir=generate_random_profile(),
        headless=False,
        args=[
            '--disable-extensions-except='+ extension_path,
            '--load-extension=' + extension_path,
        ],
    )
    page = browser.new_page()
    page.goto("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    input("Press Enter to exit...")
    browser.close()
```
## Use App ID

```python
from botasaurus.browser import browser, Driver
from capsolver_extension_python import Capsolver

@browser(
    extensions=[Capsolver(api_key="CAP-MY_KEY", app_id="DC601421-43D5-45E4-9FDB-B3BAF7A2C3FD")], # TODO: Replace with your own CapSolver Key and App ID
)  
def solve_captcha(driver: Driver, data):
    driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    driver.prompt()

solve_captcha()
```

## Note

When you use the Capsolver Extension, we integrate our own app ID into the extension if you haven't provided one. This allows us to earn a small commission from each captcha you solve, at no extra cost to you. 

These funds supports us in our efforts to develop awesome open-source projects to make your life easy.

## Love It? [Star It ⭐!](https://github.com/omkarcloud/capsolver-extension-python)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/capsolver-extension-python](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=capsolver-extension-python)](https://github.com/omkarcloud/capsolver-extension-python/stargazers)
