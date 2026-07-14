# AI-Recommendation-System

A rule-based recommendation system that suggests products to users based on their preferences using Jaccard similarity matching.

## How it works

1. Reads an e-commerce order dataset (Excel) with 1200 orders across 7 product categories
2. Builds feature profiles for each product (price range, popular payment methods, referral sources)
3. Asks the user 4 questions via CLI or Streamlit UI:
   - Product category (or "No Preference")
   - Budget range (Low / Medium / High)
   - Preferred payment method
   - How they heard about the store
4. Compares preferences to product profiles using Jaccard similarity
5. Returns the top 3 best-matching products ranked by match score

## Requirements

- Python 3.8+
- openpyxl
- streamlit (optional, for web UI)

## Usage

### CLI

```bash
pip install openpyxl
python main.py
```

### Streamlit Web UI

```bash
pip install openpyxl streamlit
streamlit run streamlit_app.py
```

## Screenshots

Screenshots are available in the `SCREENSHOTS/` folder.
