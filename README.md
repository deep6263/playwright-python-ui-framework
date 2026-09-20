# Enterprise Playwright Python UI Automation Framework

[![Playwright Python Tests](https://github.com/deep6263/playwright-python-ui-framework/actions/workflows/pytest.yml/badge.svg)](https://github.com/deep6263/playwright-python-ui-framework/actions/workflows/pytest.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-orange)



A scalable and maintainable UI automation framework built using **Python, Playwright, Pytest, and Allure**.

This project demonstrates enterprise-style test automation practices including Page Object Model, environment-based configuration, reusable fixtures, test data management, failure screenshots, reporting, and CI/CD integration with GitHub Actions.

---

## 🚀 Project Overview

This framework automates the end-to-end shopping workflow of [SauceDemo](https://www.saucedemo.com/).

### Automated Flow

Login → Products → Cart → Checkout

The framework validates both positive and negative scenarios across the application.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | UI automation |
| Pytest | Test framework |
| Allure | Test reporting |
| python-dotenv | Environment configuration |
| JSON | Test data management |
| Git | Version control |
| GitHub Actions | CI/CD |
| Chromium | CI browser |

---

## 🏗️ Framework Architecture

```text
playwright-python-ui-framework/
│
├── config/
│   ├── config.py
│   ├── dev.json
│   └── qa.json
│
├── data/
│   └── users.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── smoke/
│   │   ├── test_framework_setup.py
│   │   └── test_login.py
│   │
│   └── regression/
│       ├── test_products.py
│       ├── test_cart.py
│       └── test_checkout.py
│
├── utils/
│   └── data_loader.py
│
├── screenshots/
├── reports/
├── logs/
├── .github/
│   └── workflows/
│       └── pytest.yml
│
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md