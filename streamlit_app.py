import os
import sys
import streamlit as st

from data.loader import load_dataset
from recommender.profile import build_product_profiles
from recommender.matcher import recommend


@st.cache_data
def load_data():
    base = os.path.dirname(os.path.abspath(sys.argv[0] if sys.argv[0] else __file__))
    path = os.path.join(base, "Dataset for Data Analytics.xlsx")
    records = load_dataset(path)
    profiles = build_product_profiles(records)
    return records, profiles


def main():
    st.set_page_config(page_title="AI Recommendation System", layout="centered")
    records, profiles = load_data()

    st.title("AI Recommendation System")
    st.markdown("Tell us your preferences and we'll find the perfect product match.")

    with st.form("preferences"):
        cols = st.columns(2)

        products = ["No Preference"] + sorted(profiles.keys())
        budgets = ["No Preference", "Low", "Medium", "High"]
        payments = ["No Preference"] + sorted({r["payment_method"] for r in records})
        referrals = ["No Preference"] + sorted({r["referral_source"] for r in records})

        with cols[0]:
            product = st.selectbox("What product category interests you?", products)
            budget = st.selectbox("What is your budget range?", budgets)

        with cols[1]:
            payment = st.selectbox("Preferred payment method?", payments)
            referral = st.selectbox("How did you hear about us?", referrals)

        submitted = st.form_submit_button("Get Recommendations", type="primary", use_container_width=True)

    if submitted:
        user_prefs = {
            "product": product,
            "budget": budget,
            "payment": payment,
            "referral": referral,
        }

        results = recommend(profiles, user_prefs)

        st.divider()
        st.subheader("Top Recommendations for You")

        for i, (score, profile) in enumerate(results, 1):
            with st.container(border=True):
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"### #{i}")
                    st.markdown(f"**{score:.0%}** match")
                with col2:
                    st.markdown(f"### {profile['name']}")
                    st.markdown(
                        f"**Avg Price:** ${profile['avg_price']:.2f} ({profile['price_category']})  |  "
                        f"**Popular Payment:** {', '.join(profile['top_payments'])}  |  "
                        f"**Common Referrals:** {', '.join(profile['top_referrals'])}"
                    )


if __name__ == "__main__":
    main()
