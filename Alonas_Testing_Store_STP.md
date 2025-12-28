# Software Test Plan (STP)
## Alona's Testing Store

---

## 📋 Document Information

| **Field** | **Details** |
|---|---|
| **Project Name** | Alona's Testing Store |
| **Application URL** | https://alonas-testing-store.lovable.app/ |
| **Document Type** | Software Test Plan (STP) |
| **Version** | 1.0 |
| **Last Updated** | 2025-12-28 |
| **Author** | Alona |

---

## 1. 📖 Introduction

### 1.1 Purpose
This document describes the **Software Test Plan (STP)** for *Alona's Testing Store*, a demo e-commerce web application built with React and a mock API layer.

### 1.2 Objectives
The goal of this STP is to define:
- **E2E UI** testing strategies
- **Service-level (mock API)** testing approaches
- Test scope and coverage matrix
- Concrete test cases and scenarios
- Entry/exit criteria and deliverables

### 1.3 Intended Audience
This STP serves both as:
- A **real QA document** for test planning and execution
- A **portfolio/demo artifact** demonstrating professional QA practices

---

## 2. 🎯 System Under Test (SUT)

### 2.1 Application Overview
**URL:** [https://alonas-testing-store.lovable.app/](https://alonas-testing-store.lovable.app/)

**Technology Stack:**
- Frontend: React
- API Layer: Mock service (`mockApi.ts`)
- State Management: Context API

### 2.2 Application Routes
| Route | Page | Description |
|---|---|---|
| `/` | HomePage | Product catalog with search, filters, sorting |
| `/product/:id` | ProductPage | Product details, quantity selector, add-to-cart |
| `/cart` | CartPage | Cart items, coupon application, totals |
| `/checkout` | CheckoutPage | Customer info, payment method, order submission |
| `/order-confirmation/:orderId` | OrderConfirmationPage | Order summary and confirmation message |
| `*` | NotFound | 404 error page |

### 2.3 Data / API Layer
The application uses a **mock service layer (`mockApi.ts`)** instead of real HTTP endpoints:

| API Method | Purpose |
|---|---|
| `getProducts()` | Retrieve product catalog |
| `getProduct(id)` | Retrieve single product details |
| `validateCoupon(code)` | Validate coupon code and return discount |
| `checkout(items, customer, paymentMethod, couponCode?)` | Process order submission |
| `setCheckoutError(boolean)` | Toggle deterministic checkout failure for testing |

---

## 3. 📊 Test Scope

### 3.1 In Scope ✅
- **End-to-End (E2E) UI testing** using Playwright
- **Service-level testing** of mock API business logic
- **Functional validation:**
  - Cart calculations and totals accuracy
  - Coupon application and discount logic
  - Checkout success and failure scenarios
  - Navigation and routing flows
  - Error states and boundary conditions
  - Empty states (cart, product lists)
- **Cross-browser testing** (Chromium, Firefox, WebKit)

### 3.2 Out of Scope ❌
- Load and performance testing
- Security and penetration testing
- Visual regression testing
- Real payment gateway integration
- Mobile native app testing
- Internationalization (i18n) testing

---

## 4. 🧪 Test Strategy

### 4.1 E2E UI Testing Approach

**Test Automation Framework:**
- **Tool:** Playwright (Python)
- **Programming Language:** Python 3.x
- **Test Runner:** pytest

**Selector Strategy:**
- **Primary:** `data-testid` attributes (stable, test-specific)
- **Secondary:** ARIA roles and semantic HTML
- **Avoid:** Fragile CSS selectors and XPath

**Test Design Principles:**
- Tests are **deterministic** (mock data, no randomness)
- No hard waits; rely on Playwright's auto-waiting
- Use async assertions for dynamic UI states
- Independent test execution (no test dependencies)

### 4.2 Service / API Testing Approach

Since the application uses in-app mock APIs:

**Validation Methods:**
1. **Direct Service Tests** (optional, Node.js)
   - Unit tests for mock API business logic
   - Validate data transformations and calculations

2. **UI-Driven Contract Assertions** (Python Playwright)
   - Verify API responses through UI behavior
   - Validate cart math, coupon logic, and checkout flows

**Error Simulation:**
- Checkout failures use `SIMULATE_CHECKOUT_ERROR` environment variable
- Deterministic error scenarios for negative testing

---

## 5. 📈 Test Matrix

| Module | Route | E2E UI | Service Logic | Priority |
|---|---|---|---|---|
| Catalog | `/` | Load, search, filter, sort | Product list correctness | P0 |
| Product details | `/product/:id` | Render, qty, add‑to‑cart | Stock rules | P0 |
| Cart | `/cart` | Qty, totals, coupon | Discount math | P0 |
| Checkout | `/checkout` | Validation, submit | Order creation | P0 |
| Confirmation | `/order-confirmation/:orderId` | Summary display | Order schema | P1 |
| 404 | `*` | NotFound page | — | P1 |

---

## 6. 🔬 Test Suites

### 6.1 Smoke Suite (PR Gate)
**Execution:** Pre-merge, CI/CD pipeline
**Duration:** ~2-3 minutes
**Purpose:** Validate critical happy paths

| # | Test Case | Expected Result |
|---|---|---|
| 1 | Home page loads and products are displayed | Product grid visible with items |
| 2 | Open product details from catalog | Product page displays with correct info |
| 3 | Add product to cart | Cart badge increments, item in cart |
| 4 | Cart total updates on quantity change | Subtotal recalculates correctly |
| 5 | Successful checkout redirects to confirmation | Order confirmation page displayed |
| 6 | Invalid route shows 404 page | 404 error page rendered |

### 6.2 Sanity Suite (Nightly)
**Execution:** Daily, scheduled runs
**Duration:** ~5-7 minutes
**Purpose:** Validate key business logic and edge cases

| # | Test Case | Expected Result |
|---|---|---|
| 1 | Valid coupon applies 10% discount | Discount line shown, total updated |
| 2 | Invalid coupon shows error | Error message displayed, no discount |
| 3 | Checkout form validations | Required field errors shown |
| 4 | Product not found behavior | 404 or error state for invalid product ID |
| 5 | Empty cart behavior on Cart page | "Your cart is empty" message |
| 6 | Empty cart behavior on Checkout page | Redirect or disabled checkout |

### 6.3 Regression Suite
**Execution:** Pre-release, weekly
**Duration:** ~10-15 minutes
**Purpose:** Comprehensive coverage including negative scenarios

| # | Test Case | Expected Result |
|---|---|---|
| 1 | Checkout failure mode | Error alert displayed, remains on checkout |
| 2 | Case-insensitive coupon validation | "SAVE10" and "save10" both work |
| 3 | Multi-item cart math accuracy | Correct subtotals with multiple items |
| 4 | Direct navigation to confirmation without order | Handle missing order state gracefully |
| 5 | Search functionality | Results filter correctly |
| 6 | Product filtering and sorting | Products update based on selections |
| 7 | Cross-browser compatibility | Tests pass on Chromium, Firefox, WebKit |

---

## 7. 📝 Detailed Test Cases (Sample)

### TC-E2E-001: Add Product to Cart

| **Field** | **Details** |
|---|---|
| **Test ID** | TC-E2E-001 |
| **Priority** | P0 |
| **Route** | `/product/:id` |
| **Test Type** | E2E UI - Positive |

**Preconditions:**
- Application is accessible
- At least one product exists in catalog

**Test Steps:**
1. Navigate to product details page for a valid product
2. Verify product information is displayed (name, price, image)
3. Increase quantity using the quantity selector
4. Click "Add to Cart" button

**Expected Results:**
- Cart badge increments to show correct item count
- Product appears in cart page with correct quantity
- Product subtotal calculated correctly (price × quantity)

**Postconditions:**
- Cart contains the added product

---

### TC-E2E-005: Apply Valid Coupon

| **Field** | **Details** |
|---|---|
| **Test ID** | TC-E2E-005 |
| **Priority** | P0 |
| **Route** | `/cart` |
| **Test Type** | E2E UI - Positive |

**Preconditions:**
- Cart contains at least one product
- Valid coupon code is known (e.g., "SAVE10")

**Test Steps:**
1. Navigate to cart page
2. Verify current subtotal amount
3. Enter valid coupon code in coupon input field
4. Click "Apply" or submit coupon

**Expected Results:**
- Discount line is displayed showing 10% discount
- Total is recalculated: `Total = Subtotal - (Subtotal × 0.10)`
- Success message confirms coupon applied

**Postconditions:**
- Coupon remains applied for checkout

---

### TC-E2E-009: Checkout Failure Handling

| **Field** | **Details** |
|---|---|
| **Test ID** | TC-E2E-009 |
| **Priority** | P1 |
| **Route** | `/checkout` |
| **Test Type** | E2E UI - Negative |

**Preconditions:**
- Cart contains at least one product
- Checkout error simulation is enabled (`SIMULATE_CHECKOUT_ERROR=true`)

**Test Steps:**
1. Navigate to checkout page
2. Fill in all required customer information fields:
   - Full name
   - Email address
   - Shipping address
3. Select payment method
4. Click "Submit Order" or "Place Order" button

**Expected Results:**
- Error alert is displayed with appropriate error message
- User remains on checkout page (no redirect)
- Form data is preserved (not cleared)
- Cart state is unchanged

**Postconditions:**
- Order is not created
- User can retry checkout after fixing issues

---

## 8. ✅ Entry / Exit Criteria

### 8.1 Entry Criteria
Before test execution begins, the following conditions must be met:

- [ ] Application is deployed and accessible at test environment URL
- [ ] All `data-testid` attributes are present in UI components
- [ ] Mock API service is functioning correctly
- [ ] Test data is deterministic and consistent
- [ ] Test environment is isolated (no production data)
- [ ] Playwright and all dependencies are installed
- [ ] Test scripts are peer-reviewed and version-controlled

### 8.2 Exit Criteria
Testing phase can be concluded when:

- [ ] **Smoke suite:** 100% pass rate
- [ ] **Sanity suite:** ≥ 95% pass rate
- [ ] **Regression suite:** ≥ 90% pass rate
- [ ] No open **P0** defects
- [ ] No open **P1** defects in critical flows (cart, checkout)
- [ ] All test execution reports are generated and reviewed
- [ ] Known issues are documented and tracked

---

## 9. 📦 Deliverables

| **Deliverable** | **Format** | **Description** |
|---|---|---|
| **Software Test Plan** | Markdown (`.md`) | This document |
| **Test Automation Framework** | Python/Playwright | Automated test suite code |
| **Test Execution Reports** | HTML / Allure | Test results with pass/fail status |
| **CI/CD Pipeline Configuration** | YAML | GitHub Actions or similar |
| **Test Data Sets** | JSON / Python fixtures | Mock data for testing |
| **Defect Reports** | Issue tracker | Logged bugs with repro steps |

---

## 10. 🛠️ Test Environment

### 10.1 Environment Details
| **Component** | **Details** |
|---|---|
| **Application URL** | https://alonas-testing-store.lovable.app/ |
| **Test Framework** | Playwright 1.x+ |
| **Programming Language** | Python 3.8+ |
| **Test Runner** | pytest |
| **Browsers** | Chromium, Firefox, WebKit |
| **CI/CD** | GitHub Actions |
| **Reporting** | pytest-html, Allure |

### 10.2 Test Data Management
- **Product catalog:** Mock data with 10-20 products
- **Coupon codes:** "SAVE10" (10% discount)
- **Test users:** Hardcoded customer info for checkout
- **Order IDs:** Generated deterministically

---

## 11. 🚨 Risks and Mitigation

| **Risk** | **Impact** | **Mitigation** |
|---|---|---|
| Mock API behavior differs from real backend | High | Document API contracts; validate with backend team |
| Test flakiness due to timing issues | Medium | Use Playwright auto-waiting; avoid hard waits |
| Test environment unavailable | High | Local environment setup instructions; containerization |
| Test data inconsistency | Medium | Use fixtures; reset state between tests |
| Browser compatibility issues | Low | Run tests across all target browsers in CI |

---

## 12. 📚 References

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Project Repository](https://github.com/username/e-commerce-test-playwright-python)
- [Application URL](https://alonas-testing-store.lovable.app/)

---

## 13. 📝 Document Revision History

| **Version** | **Date** | **Author** | **Changes** |
|---|---|---|---|
| 1.0 | 2025-12-28 | Alona | Initial version - complete STP |

---

## 14. ✨ Conclusion

This Software Test Plan provides a comprehensive testing approach for **Alona's Testing Store**, covering:
- Detailed test strategy for E2E and service-level testing
- Well-defined test suites (Smoke, Sanity, Regression)
- Concrete test cases with clear expected results
- Entry/exit criteria and deliverables

The plan serves as both a **professional QA artifact** and a **portfolio demonstration** of modern test automation practices using Playwright and Python.

**For questions or updates to this plan, please contact the test automation team.**
