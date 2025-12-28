# Selenium Pytest E-Commerce Automation Framework

![Selenium Tests](https://github.com/phanikumar240/Selenium-Pytest-HandsOn/actions/workflows/main.yml/badge.svg)

## 🚀 Project Overview
This is a professional-grade Selenium automation framework built using **Python** and **Pytest**. It verifies the end-to-end purchase flow of a Zara Coat on a practice e-commerce site, covering both positive and negative scenarios.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Testing Framework:** Pytest
* **Automation Tool:** Selenium WebDriver (Chrome)
* **Reporting:** Pytest-HTML (with embedded Base64 screenshots)
* **CI/CD:** GitHub Actions



## 📋 Features
- **Data-Driven Testing:** 3 positive and 2 negative test cases implemented using `@pytest.mark.parametrize`.
- **Synchronization:** Uses Explicit Waits and JavaScript executors to handle dynamic AJAX elements and loaders.
- **Reporting:** Generates a self-contained HTML report with high-fidelity screenshots for every test case (Success and Failure).
- **Stability:** Integrated `pytest-rerunfailures` to manage UI flakiness on dynamic elements.

## 📁 Project Structure
- `test_ecommerce.py`: Main test suite containing the test cases.
- `conftest.py`: Fixtures for WebDriver setup and the HTML reporting hook for screenshots.
- `product_logic.py`: Core interaction logic for the e-commerce site.
- `orderid.py`: Logic for verifying orders and extracting unique Order IDs.
- `.github/workflows/main.yml`: CI/CD configuration for GitHub Actions.

## ⚙️ How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/phanikumar240/Selenium-Pytest-HandsOn.git](https://github.com/phanikumar240/Selenium-Pytest-HandsOn.git)