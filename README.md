# Flask Hello World Application

A simple Flask web application that displays "Hello, World!" in your browser.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone this repository or download the files to your local machine.

2. Navigate to the project directory:
   ```bash
   cd HelloAll
   ```

3. (Recommended) Create and activate a virtual environment:
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   # python -m venv venv
   # .\venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: With virtualenv activated, all Python packages will be installed in the virtual environment, keeping your global Python installation clean.

5. To deactivate the virtual environment when you're done:
   ```bash
   deactivate
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and visit:
   ```
   http://localhost:6001
   ```

3. You should see "Hello, World!" displayed in your browser.

## Development

- The application runs in debug mode by default, which means it will automatically reload when you make changes to the code.
- The server runs on port 6001 by default. You can change this in `app.py` if needed.
- Always activate your virtual environment before working on the project:
  ```bash
  # From the project root directory
  source venv/bin/activate  # On macOS/Linux
  # .\venv\Scripts\activate  # On Windows
  ```
- To install new dependencies, activate the virtual environment first, then use pip:
  ```bash
  pip install package_name
  # Update requirements.txt after adding new packages
  pip freeze > requirements.txt
  ```

## Testing

### Running Tests

The project includes both unit and integration tests. To run them:

1. Install test dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run all tests:
   ```bash
   python -m pytest tests/ -v
   ```

3. Run only unit tests:
   ```bash
   python -m pytest tests/unit/ -v
   ```

4. Run only integration tests:
   ```bash
   python -m pytest tests/integration/ -v
   ```

5. Run a specific test file:
   ```bash
   python -m pytest tests/unit/test_app.py -v
   ```

6. Run tests with coverage report:
   ```bash
   python -m pytest --cov=app tests/
   ```

### Adding New Dependencies

To add new dependencies:
1. Activate your virtual environment
2. Install the package:
   ```bash
   pip install package_name
   ```
3. Update requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

## Virtual Environment Management

### Creating a new virtual environment
If you need to recreate the virtual environment (e.g., after cloning the repository to a new location):

```bash
# Remove the existing virtual environment (if any)
rm -rf venv/

# Create a new virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# .\venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Verifying the virtual environment
To ensure you're working in the virtual environment, check that the terminal prompt shows `(venv)` at the beginning. Also:

```bash
which python  # Should point to the venv directory
pip list     # Should show only the installed packages from requirements.txt
```

## License

This project is open source and available under the [MIT License](LICENSE).
testing pull request flow
