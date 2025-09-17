# PyPI Deployment Guide for cob-ai

## Prerequisites

1. Make sure you have a PyPI account at https://pypi.org/
2. Install required dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Build and Upload Process

### 1. Clean Previous Builds (Optional)
```bash
rmdir /s /q dist build cob_ai.egg-info 2>nul
```

### 2. Build the Package
```bash
python -m build
```

### 3. Check the Package
```bash
python -m twine check dist/*
```

### 4. Upload to PyPI

For testing first (recommended):
```bash
python -m twine upload --repository testpypi dist/*
```

For production PyPI:
```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

## After Upload

Once uploaded, users can install your package with:
```bash
pip install cob-ai
```

And import it as requested:
```python
from cob_ai import COB
```

## Version Updates

To release a new version:
1. Update the version in `pyproject.toml`
2. Update the version in `cob_ai/__init__.py`
3. Rebuild and upload following the steps above

## Package Structure

The package is structured as:
```
cob-ai/
├── cob_ai/           # Main package directory
│   ├── __init__.py   # Package initialization with exports
│   ├── client.py     # COB client class
│   └── models.py     # Data models
├── pyproject.toml    # Package configuration
├── README.md         # Package documentation
└── LICENSE           # MIT license
```

This structure allows users to:
- `from cob_ai import COB` (main client)
- `from cob_ai import SearchResponse, SearchResult` (models)
- Access all exported classes and functions