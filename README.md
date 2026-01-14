# Selenium Automation Test Suite with Allure Reports

A complete Selenium-based UI automation test suite for [practicesoftwaretesting.com](https://practicesoftwaretesting.com) with integrated Allure reporting.

## Project Structure

```
├── config/
│   └── config.py              # Configuration (BASE_URL, test credentials)
├── pages/
│   ├── base_page.py           # Base class with common Selenium methods
│   ├── login_page.py          # Login page object
│   ├── contact_page.py        # Contact form page object
│   ├── product_page.py        # Product page object
│   └── cart_page.py           # Shopping cart page object
├── tests/
│   ├── test_login.py          # Login functionality tests
│   ├── test_contact_form.py   # Contact form submission tests
│   └── test_add_to_cart.py    # Product page navigation tests
├── utils/
│   └── driver_factory.py      # WebDriver initialization
├── allure-results/            # Raw Allure test data (auto-generated)
├── allure-report/             # HTML Allure report (auto-generated)
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── open_report.py            # Script to open Allure report in browser
└── README.md                 # This file
```

## Installation

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Allure command-line tool (optional, for serving reports)

### Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Install Allure CLI for advanced report features:
```bash
# On Windows (requires Scoop, Chocolatey, or manual installation)
# https://docs.qameta.io/allure/#_installing_a_commandline

# Or use the Python wrapper:
pip install allure-pytest
```

## Running Tests

### Run All Tests
```bash
pytest
```

### Run with Verbose Output
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest tests/test_login.py -v
```

### Run Specific Test
```bash
pytest tests/test_login.py::test_login -v
```

## Generating and Viewing Reports

### Generate Allure Report
```bash
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
```

### View Report in Browser
```python
python open_report.py
```

Or manually open:
```bash
allure open allure-report
```

Or open the HTML file directly:
```
allure-report/index.html
```

## Test Features

### Features Covered
1. **Authentication** - User login functionality
2. **Contact Form** - Form submission with validation
3. **Product Catalog** - Product page navigation

### Page Object Model
- All page interactions are encapsulated in page classes
- Locators defined at class level
- Inherited methods from `BasePage` for common operations:
  - `click(locator)` - Click element with wait
  - `type(locator, text)` - Type text with clear
  - `get_text(locator)` - Get element text

### Explicit Waits
- 10-second WebDriverWait for all operations
- Element visibility checks before interactions
- No implicit waits or sleep() calls

## Configuration

Edit `config/config.py` to change:
- **BASE_URL**: Target website
- **EMAIL**: Test account email
- **PASSWORD**: Test account password

## Allure Report Features

The report includes:
- **Test Overview**: Pass/fail summary with timeline
- **Features**: Organized by feature and story
- **Steps**: Detailed steps for each test
- **Timeline**: Test execution timeline
- **Trends**: Historical test trends
- **Categories**: Test categorization and filtering

## Test Coverage

| Test | Status | Description |
|------|--------|-------------|
| test_login | ✅ PASSED | Verify login form submission |
| test_contact_form_submission | ✅ PASSED | Verify contact form with all fields |
| test_add_to_cart | ✅ PASSED | Verify product page navigation |

## Development Workflow

### Adding New Tests
1. Create test file in `tests/` directory
2. Import page objects and driver factory
3. Follow the pattern:
   ```python
   import allure
   from utils.driver_factory import get_driver
   from pages.your_page import YourPage

   @allure.feature("Feature Name")
   @allure.story("Story Name")
   def test_your_test():
       driver = get_driver()
       try:
           with allure.step("Step description"):
               # Test code here
               pass
       finally:
           driver.quit()
   ```

### Adding New Page Objects
1. Create class inheriting from `BasePage`
2. Define locators as class-level tuples
3. Implement page-specific methods
4. Use inherited `click()`, `type()`, `get_text()` methods

## Troubleshooting

### Tests Fail on Element Not Found
- Verify the website structure hasn't changed
- Check locators in page objects match current DOM
- Update selectors using browser DevTools

### Allure Report Not Generated
- Ensure `pytest.ini` is present
- Run: `pytest --alluredir=allure-results`
- Verify `allure-results/` directory is created
- Run: `allure generate allure-results -o allure-report --clean`

### Browser Driver Issues
- Ensure ChromeDriver is compatible with your Chrome version
- `webdriver-manager` automatically manages this
- Clear `.wdm/` cache if issues persist

## CI/CD Integration

To integrate with CI/CD pipelines:

```bash
# Run tests and generate report
pytest --alluredir=allure-results -v

# Generate HTML report
allure generate allure-results -o allure-report --clean

# Archive reports for artifact storage
# (add allure-report/ to CI artifacts)
```

## Dependencies

- **selenium**: WebDriver automation framework
- **pytest**: Test runner and framework
- **webdriver-manager**: Automatic WebDriver management
- **allure-pytest**: Allure reporting plugin

## License

MIT License

## Contributing

1. Follow the Page Object Model pattern
2. Use explicit waits instead of implicit
3. Add meaningful test descriptions and steps
4. Generate Allure reports for all test runs
5. Update documentation when adding features
