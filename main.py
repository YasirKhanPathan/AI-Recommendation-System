import os
import sys
from data.loader import load_dataset
from recommender.profile import build_product_profiles
from recommender.matcher import recommend


def ask_choice(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        try:
            choice = input(f"Enter number (1-{len(options)}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        except ValueError:
            pass
        print(f"Invalid input. Enter a number between 1 and {len(options)}.")


def main():
    base = os.path.dirname(os.path.abspath(sys.argv[0] if sys.argv[0] else __file__))
    dataset_path = os.path.join(base, "Dataset for Data Analytics.xlsx")

    print("=" * 60)
    print("  AI Recommendation System")
    print("  Find your perfect product match!")
    print("=" * 60)

    records = load_dataset(dataset_path)
    profiles = build_product_profiles(records)

    products = ["No Preference"] + sorted(profiles.keys())
    budgets = ["No Preference", "Low", "Medium", "High"]
    payments = ["No Preference"] + sorted(
        {r["payment_method"] for r in records}
    )
    referrals = ["No Preference"] + sorted(
        {r["referral_source"] for r in records}
    )
    statuses = ["No Preference", "Delivered", "Shipped", "Pending", "Returned", "Cancelled"]

    print("\n--- Tell us about your preferences ---\n")

    product = ask_choice("What product category interests you?", products)
    budget = ask_choice("What is your budget range?", budgets)
    payment = ask_choice("Preferred payment method?", payments)
    referral = ask_choice("How did you hear about us?", referrals)
    status = ask_choice("Preferred order status?", statuses)

    user_prefs = {
        "product": product,
        "budget": budget,
        "payment": payment,
        "referral": referral,
        "status": status,
    }

    print("\n" + "=" * 60)
    print("  Analyzing your preferences...")
    print("=" * 60)

    results = recommend(profiles, user_prefs)

    print("\n  Top Recommendations for You:\n")
    for i, (score, profile) in enumerate(results, 1):
        print(f"  {i}. {profile['name']}  (Match Score: {score:.0%})")
        print(f"     Avg Price: ${profile['avg_price']} ({profile['price_category']})")
        print(f"     Popular Payment: {', '.join(profile['top_payments'])}")
        print(f"     Common Referrals: {', '.join(profile['top_referrals'])}")
        print()

    print("=" * 60)


if __name__ == "__main__":
    main()
