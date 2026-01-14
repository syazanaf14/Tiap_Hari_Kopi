import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Tiap Hari Kopi",
    page_icon="☕",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS (Blue & White Theme)
# --------------------------------------------------
st.markdown("""
<style>
body { background-color: #f4f7fb; }
.card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    text-align: center;
}
.price {
    color: #1e88e5;
    font-weight: bold;
}
.footer {
    background-color: #0d3b66;
    color: white;
    padding: 10px;
    text-align: center;
}
.rating-badge {
    position: fixed;
    right: 20px;
    bottom: 20px;
    background-color: #1e88e5;
    color: white;
    padding: 15px 20px;
    border-radius: 50px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("☕ TIAP HARI KOPI")

page = st.sidebar.radio(
    "Navigation",
    ["Business Profile", "Customer Engagement", "Login", "Analytics Dashboard"]
)

# --------------------------------------------------
# MENU DATA
# --------------------------------------------------
menu_items = [
    {"name": "Signature Latte", "category": "Beverage", "price": 12, "image": "assets/latte.jpg"},
    {"name": "Iced Americano", "category": "Beverage", "price": 10, "image": "assets/americano.jpg"},
    {"name": "Chocolate Cake", "category": "Dessert", "price": 8, "image": "assets/cake.jpg"},
    {"name": "Nasi Goreng", "category": "Local Food", "price": 9, "image": "assets/nasi.jpg"},
    {"name": "Chicken Chop", "category": "Western Food", "price": 15, "image": "assets/chicken.jpg"},
    {"name": "Carbonara Pasta", "category": "Western Food", "price": 14, "image": "assets/pasta.jpg"},
]

# --------------------------------------------------
# BUSINESS PROFILE
# --------------------------------------------------
if page == "Business Profile":

    st.title("Welcome to Tiap Hari Kopi ☕")

    tab1, tab2, tab3, tab4 = st.tabs(["🍽 Menu", "📅 Reservation", "🎁 Rewards", "ℹ️ About Us"])

    # ---------- MENU ----------
    with tab1:
        st.subheader("Our Menu")

        category = st.selectbox(
            "Select Category",
            ["All", "Beverage", "Dessert", "Local Food", "Western Food"]
        )

        filtered = [
            item for item in menu_items
            if category == "All" or item["category"] == category
        ]

        cols = st.columns(3)
        for i, item in enumerate(filtered):
            with cols[i % 3]:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                try:
                    st.image(item["image"], use_container_width=True)
                except:
                    st.image("https://via.placeholder.com/300x200")
                st.subheader(item["name"])
                st.write(item["category"])
                st.markdown(f"<p class='price'>RM {item['price']}</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

    # ---------- RESERVATION ----------
    with tab2:
        st.subheader("Make a Reservation")
        st.info("Click below to reserve via WhatsApp")
        st.markdown("[📲 WhatsApp Reservation](https://wa.me/60123456789)")

    # ---------- REWARDS ----------
    with tab3:
        st.subheader("Customer Rewards")
        st.metric("Points Balance", "150 pts")
        st.progress(0.75)
        st.success("🎉 Redeem free drink at 200 points")

    # ---------- ABOUT US ----------
    with tab4:
        st.subheader("About Us")
        st.write("""
        📍 Kubang Kerian, Kelantan  
        ☕ Established in 2021  
        📞 012-3456789  
        """)
        st.map(pd.DataFrame({"lat": [6.095], "lon": [102.275]}))

    st.markdown('<div class="footer">© 2026 Tiap Hari Kopi</div>', unsafe_allow_html=True)

# --------------------------------------------------
# CUSTOMER ENGAGEMENT
# --------------------------------------------------
elif page == "Customer Engagement":

    st.title("Customer Engagement & Feedback")

    st.metric("⭐ Average Rating", "4.5 / 5")
    st.markdown('<div class="rating-badge">⭐ 4.5</div>', unsafe_allow_html=True)

    st.subheader("Customer Reviews")
    reviews = [
        ("⭐⭐⭐⭐⭐", "Great ambience and coffee!"),
        ("⭐⭐⭐⭐", "Affordable price and friendly staff."),
        ("⭐⭐⭐", "Waiting time a bit long during peak hours."),
        ("⭐⭐⭐⭐⭐", "Perfect place for students!")
    ]

    for r in reviews:
        st.success(f"{r[0]} — {r[1]}")

    st.subheader("Leave Your Feedback")
    st.text_input("Your Name")
    st.selectbox("Rating", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    st.text_area("Your Feedback")
    st.button("Submit Feedback")

# --------------------------------------------------
# LOGIN PAGE
# --------------------------------------------------
elif page == "Login":

    st.title("Staff / Business Login")

    option = st.radio("Select Option", ["Login", "Create Account", "Forgot Password"])

    if option == "Login":
        st.text_input("Username")
        st.text_input("Password", type="password")
        st.button("Login")

    elif option == "Create Account":
        st.text_input("Full Name")
        st.text_input("Email")
        st.text_input("Password", type="password")
        st.text_input("Confirm Password", type="password")
        st.button("Create Account")

    elif option == "Forgot Password":
        st.text_input("Registered Email")
        st.button("Reset Password")

# --------------------------------------------------
# ANALYTICS DASHBOARD
# --------------------------------------------------
elif page == "Analytics Dashboard":

    st.title("Business Analytics Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", "1,259")
    col2.metric("Positive Sentiment", "72%")
    col3.metric("Returning Customers", "48%")

    sentiment_df = pd.DataFrame({
        "Sentiment": ["Positive", "Neutral", "Negative"],
        "Count": [720, 350, 189]
    })

    fig1 = px.pie(
        sentiment_df,
        values="Count",
        names="Sentiment",
        title="Customer Sentiment"
    )

    st.plotly_chart(fig1, use_container_width=True)

    engagement_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Engagement": [200, 320, 280, 400, 450]
    })

    fig2 = px.bar(
        engagement_df,
        x="Month",
        y="Engagement",
        title="Monthly Engagement"
    )

    st.plotly_chart(fig2, use_container_width=True)
