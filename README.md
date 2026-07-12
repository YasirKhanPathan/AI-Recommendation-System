# AI-Recommendation-System

A rule-based recommendation system that suggests products to users based on their preferences using Jaccard similarity matching.

## How it works

1. Reads an e-commerce order dataset (Excel)
2. Builds feature profiles for each product category
3. Asks the user about their preferences via CLI
4. Compares preferences to product profiles using Jaccard similarity
5. Returns the top 3 best-matching products

## Requirements

- Python 3.8+
- openpyxl

## Usage

```bash
pip install openpyxl
python main.py
```
