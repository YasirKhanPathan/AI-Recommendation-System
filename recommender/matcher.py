def jaccard_similarity(set_a, set_b):
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0


def get_user_features(user_prefs):
    features = set()
    if user_prefs.get("product") and user_prefs["product"] != "No Preference":
        features.add("product:" + user_prefs["product"])
    if user_prefs.get("budget") and user_prefs["budget"] != "No Preference":
        features.add("budget:" + user_prefs["budget"])
    if user_prefs.get("payment") and user_prefs["payment"] != "No Preference":
        features.add("payment:" + user_prefs["payment"])
    if user_prefs.get("referral") and user_prefs["referral"] != "No Preference":
        features.add("referral:" + user_prefs["referral"])
    return features


def get_product_features(profile):
    features = set()
    features.add("product:" + profile["name"])
    features.add("budget:" + profile["price_category"])
    for p in profile["top_payments"]:
        features.add("payment:" + p)
    for r in profile["top_referrals"]:
        features.add("referral:" + r)
    return features


def recommend(profiles, user_prefs, top_n=3):
    user_features = get_user_features(user_prefs)

    if not user_features:
        scored = [(0.5, p) for p in profiles.values()]
    else:
        scored = []
        for product, profile in profiles.items():
            product_features = get_product_features(profile)
            score = jaccard_similarity(user_features, product_features)
            scored.append((score, profile))

    scored.sort(key=lambda x: (-x[0], x[1]["name"]))
    return scored[:top_n]
