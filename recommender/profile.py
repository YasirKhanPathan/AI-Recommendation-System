from collections import Counter, defaultdict


def categorize_price(price):
    if price < 250:
        return "Low"
    elif price <= 450:
        return "Medium"
    else:
        return "High"


def build_product_profiles(records):
    product_data = defaultdict(
        lambda: {
            "prices": [],
            "payments": Counter(),
            "referrals": Counter(),
            "statuses": Counter(),
            "coupons": Counter(),
        }
    )

    for r in records:
        p = r["product"]
        d = product_data[p]
        d["prices"].append(r["unit_price"])
        d["payments"][r["payment_method"]] += 1
        d["referrals"][r["referral_source"]] += 1
        d["statuses"][r["order_status"]] += 1
        if r["coupon_code"]:
            d["coupons"][r["coupon_code"]] += 1

    profiles = {}
    for product, data in product_data.items():
        avg_price = sum(data["prices"]) / len(data["prices"])
        profiles[product] = {
            "name": product,
            "price_category": categorize_price(avg_price),
            "avg_price": round(avg_price, 2),
            "top_payments": [m for m, _ in data["payments"].most_common(2)],
            "top_referrals": [m for m, _ in data["referrals"].most_common(2)],
            "top_statuses": [m for m, _ in data["statuses"].most_common(2)],
            "top_coupons": [m for m, _ in data["coupons"].most_common(2)],
        }
    return profiles
