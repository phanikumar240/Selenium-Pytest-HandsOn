import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    
    _driver = webdriver.Chrome(options=chrome_options)
    yield _driver
    _driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures screenshots for ALL test cases and embeds them in the HTML report.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call':
        driver = item.funcargs.get('driver')
        if driver:
            # Capture screenshot as base64 string
            screenshot = driver.get_screenshot_as_base64()
            label = "PASSED" if report.passed else "FAILED"
            
            # Embed the image into the HTML report
            html = (f'<div><b>{label} TEST SCREENSHOT:</b><br>'
                    f'<img src="data:image/png;base64,{screenshot}" alt="screenshot" '
                    'style="width:400px;height:300px;" onclick="window.open(this.src)" align="right"/></div>')
            extras.append(pytest_html.extras.html(html))
        report.extras = extras