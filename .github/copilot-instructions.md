# Copilot Instructions for Selenium Automation Test Suite

## Project Overview
This is a Selenium-based UI automation test suite for [practicesoftwaretesting.com](https://practicesoftwaretesting.com). The project tests core user workflows: login, product browsing/cart management, and contact form submission.

## Architecture Patterns

### Page Object Model (POM)
**Location:** `pages/` directory
- All page interactions are encapsulated in page classes inheriting from `BasePage`
- Locators are defined as class-level tuples using `(By.<strategy>, "<selector>")`
- Each page class represents a distinct UI page or component
- Example: `LoginPage` encapsulates login form interactions, `ProductPage` handles product actions

**Key Files:**
- `pages/base_page.py` - Base class with reusable Selenium methods (`click()`, `type()`, `get_text()`)
- `pages/login_page.py` - Credentials from `config.py`, provides `login()` method
- `pages/product_page.py`, `pages/cart_page.py`, `pages/contact_page.py` - Domain-specific page classes

### Test Execution
**Location:** `tests/` directory
- Tests follow pattern: initialize driver → instantiate page objects → perform actions → assert results
- Each test calls `driver.quit()` in `finally` block to ensure cleanup
- Tests use page methods, never direct Selenium commands
- Example: `test_add_to_cart()` chains LoginPage → ProductPage → CartPage actions

### Configuration & Setup
- **Config:** `config.py` stores BASE_URL, TEST_EMAIL, TEST_PASSWORD (credentials for test account)
- **Driver Factory:** `utils/driver_factory.py` provides `get_driver()` - returns Chrome WebDriver with `--start-maximized` option using webdriver-manager

### Implicit Waits & Conditions
- `BasePage` initializes `WebDriverWait(driver, 10)` - all page methods use explicit waits
- Wait strategies: `EC.element_to_be_clickable()` for clicks, `EC.visibility_of_element_located()` for text ops
- Never use implicit waits or Thread.sleep() in page methods

## Testing Conventions

1. **Locator Naming:** UPPERCASE_WITH_UNDERSCORES (e.g., `ADD_TO_CART = (By.ID, "btn-add-to-cart")`)
2. **Method Naming:** action verbs (e.g., `login()`, `add_to_cart()`, `update_quantity()`)
3. **Assertions:** Clear, specific messages: `assert condition, "Human-readable message"`
4. **Multi-step Workflows:** Chain page instantiations in sequence, reuse page methods

## Development Workflow

**Run all tests:**
```bash
pytest
```

**Run specific test:**
```bash
pytest tests/test_login.py
```

**Run with verbose output:**
```bash
pytest -v
```

**Dependencies:** selenium, pytest, webdriver-manager (see `requirements.txt`)

## Common Patterns to Follow

- **New Page Classes:** Inherit from `BasePage`, define all locators at class level, use `self.wait` and inherited click/type/get_text methods
- **New Tests:** Import page classes and driver factory, follow test_add_to_cart.py structure (driver init → page setup → actions → assertions → cleanup)
- **Locator Updates:** Modify only in page class, never in test files - tests reference page methods only
- **Cross-Page Navigation:** Use `driver.get(BASE_URL + "/path")` only in page classes (`open()` methods), test files stay high-level

## Integration Points

- **External Site:** Tests run against live site at BASE_URL (practicesoftwaretesting.com) - locators are tied to current DOM structure
- **WebDriver Management:** Chrome only (via webdriver-manager), no Firefox/Safari support currently
- **Test Account:** Single shared test account (EMAIL/PASSWORD in config.py) - all tests assume this account exists and is accessible
