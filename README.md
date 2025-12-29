# Alona's Testing Store – E2E Test Automation

Test automation project for **Alona's Testing Store**, a demo e-commerce web application. This project implements comprehensive E2E UI testing using **Playwright (Python)** and validates service-level business logic.

## 📋 Documentation

For the complete testing strategy, scope, test matrix, and detailed test cases, see the [Software Test Plan (STP)](docs/Alonas_Testing_Store_STP.md).

## 🎯 Project Overview

**System Under Test:** [https://alonas-testing-store.lovable.app/](https://alonas-testing-store.lovable.app/)

This is a portfolio/demo project demonstrating modern QA automation practices for an e-commerce application with the following features:
- Product catalog with search, filters, and sorting
- Product details and cart management
- Coupon application and discount calculations
- Checkout flow with form validation
- Order confirmation

## 🧪 Test Coverage

### System Under Test
- **Application:** React-based e-commerce store with mock API layer
- **Routes:** Home, Product Details, Cart, Checkout, Order Confirmation, 404

### Test Scope
- ✅ End-to-End (E2E) UI testing
- ✅ Service-level testing of mock API business logic
- ✅ Cart calculations and coupon logic
- ✅ Checkout success/failure scenarios
- ✅ Navigation, routing, and error states

### Test Suites
- **Smoke Suite (PR Gate):** Core happy path flows
- **Sanity Suite (Nightly):** Validation logic and edge cases
- **Regression Suite:** Error scenarios and comprehensive coverage

## 🛠️ Technology Stack

- **Test Framework:** Playwright (Python)
- **Selector Strategy:** `data-testid` (primary), ARIA roles (secondary)
- **Reporting:** HTML / Allure reports
- **CI/CD:** Automated pipeline execution

## 📊 Test Priority Matrix

| Module | Priority | Coverage |
|---|---|---|
| Product Catalog | P0 | Load, search, filter, sort |
| Product Details | P0 | Render, quantity, add-to-cart |
| Cart | P0 | Quantity updates, totals, coupon |
| Checkout | P0 | Form validation, submit flow |
| Order Confirmation | P1 | Summary display |
| 404 Page | P1 | Not found handling |

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Playwright

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Running Tests
```bash
# Run all tests
pytest

# Run smoke suite
pytest -m smoke

# Run with headed browser
pytest --headed

# Generate HTML report
pytest --html=report.html
```

## 📈 Entry/Exit Criteria

### Entry Criteria
- Application deployed or running locally
- Stable test IDs present in UI
- Deterministic product data available

### Exit Criteria
- Smoke suite: 100% pass rate
- No open P0/P1 defects in cart or checkout flow

## 📝 Notes

This project serves as both:
- A **real QA automation framework** with production-ready practices
- A **portfolio/demo artifact** showcasing modern test automation skills

For detailed test cases, test matrix, and comprehensive testing strategy, refer to the [STP document](docs/Alonas_Testing_Store_STP.md).
