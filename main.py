import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Tiap Hari Kopi | Digital Branding Platform",
    page_icon="☕",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS (Blue & White Theme)
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #f5f8fc;
}
.sidebar .sidebar-content {
    background-color: #0d3b66;
}
.sidebar h1, .sidebar h2, .sidebar label {
    color: white;
}
.navbar {
    background-color: #0d3b66;
    padding: 10px;
    color: white;
    text-align: center;
}
.footer {
    background-color: #0d3b66;
    color: white;
    padding: 10px;
    text-align: center;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
.rating-badge {
    position: fixed;
    right: 20px;
    bottom: 20px;
    background-color: #1e88e5;
    color: white;
    padding: 15px;
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
    [
        "Business Profile",
        "Customer Engagement",
        "Login",
        "Analytics Dashboard"
    ]
)

# --------------------------------------------------
# MENU DATA
# --------------------------------------------------
menu_data = pd.DataFrame({
    "Category": [
        "Beverage", "Beverage", "Dessert",
        "Local Food", "Western Food", "Western Food"
    ],
    "Menu": [
        "Signature Latte", "Iced Americano", "Chocolate Cake",
        "Nasi Goreng", "Chicken Chop", "Carbonara Pasta"
    ],
    "Price (RM)": [12, 10, 8, 9, 15, 14]
})

# --------------------------------------------------
# BUSINESS PROFILE PAGE
# --------------------------------------------------
if page == "Business Profile":

    st.markdown('<div class="navbar"><h2>Welcome to Tiap Hari Kopi</h2></div>', unsafe_allow_html=True)

    tabs = st.tabs([
        "🍽 Menu",
        "📅 Reservation",
        "🎁 Rewards",
        "ℹ️ About Us",
        "📞 Contact Us",
        "🤖 Bot"
    ])

    # ---------------- MENU TAB ----------------
    with tabs[0]:
        st.subheader("Our Menu")

        category = st.selectbox(
            "Filter by Category",
            ["All"] + menu_data["Category"].unique().tolist()
        )

        if category != "All":
            filtered_menu = menu_data[menu_data["Category"] == category]
        else:
            filtered_menu = menu_data

        st.dataframe(filtered_menu, use_container_width=True)

    # ---------------- RESERVATION TAB ----------------
    with tabs[1]:
        st.subheader("Reservation")
        st.info("Click below to make reservation via WhatsApp")
        st.markdown(
            "[📲 Reserve via WhatsApp](https://wa.me/60123456789)",
            unsafe_allow_html=True
        )

    # ---------------- REWARDS TAB ----------------
    with tabs[2]:
        st.subheader("Loyalty Rewards")
        st.metric("Your Points", "120 pts")
        st.progress(0.6)
        st.success("Redeem free drink at 200 points")

    # ---------------- ABOUT US TAB ----------------
    with tabs[3]:
        st.subheader("About Tiap Hari Kopi")
        st.write("""
        📍 Kubang Kerian, Kelantan  
        ☕ Established in 2021  
        📶 Free WiFi & Comfortable Space  
        """)
        st.map(pd.DataFrame({"lat": [6.095], "lon": [102.275]}))

    # ---------------- CONTACT TAB ----------------
    with tabs[4]:
        st.subheader("Contact Us")
        st.text_input("Your Name")
        st.text_area("Your Message")
        st.button("Submit")

    # ---------------- BOT TAB ----------------
    with tabs[5]:
        st.subheader("Chat Bot (Prototype)")
        st.write("🤖 Hi! How can I help you today?")
        st.text_input("Type your message")

    # Footer
    st.markdown("""
    <div class="footer">
        © 2026 Tiap Hari Kopi | Digital Branding Platform
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# CUSTOMER ENGAGEMENT PAGE
# --------------------------------------------------
elif page == "Customer Engagement":

    st.title("Customer Engagement")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("⭐ Average Rating", "4.5 / 5")
        st.success("“Nice ambience and affordable coffee!”")

    with col2:
        st.metric("💬 Total Reviews", "1,259")
        st.warning("“Service can be improved during peak hours.”")

    st.markdown('<div class="rating-badge">⭐ 4.5</div>', unsafe_allow_html=True)

# --------------------------------------------------
# LOGIN PAGE
# --------------------------------------------------
elif page == "Login":

    st.title("Business Owner / Staff Login")

    with st.container():
        st.text_input("Username")
        st.text_input("Password", type="password")
        st.button("Login")

# --------------------------------------------------
# ANALYTICS DASHBOARD
# --------------------------------------------------
elif page == "Analytics Dashboard":

    st.title("Analytics Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", "1,259")
    col2.metric("Positive Sentiment", "72%")
    col3.metric("Negative Sentiment", "8%")

    # Example Charts
    sentiment_df = pd.DataFrame({
        "Sentiment": ["Positive", "Neutral", "Negative"],
        "Count": [720, 350, 189]
    })

    fig1 = px.pie(
        sentiment_df,
        values="Count",
        names="Sentiment",
        title="Customer Sentiment Distribution",
        color_discrete_sequence=["#1e88e5", "#90caf9", "#e53935"]
    )

    st.plotly_chart(fig1, use_container_width=True)

    engagement_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Engagement": [200, 320, 280, 400, 450]
    })

    fig2 = px.line(
        engagement_df,
        x="Month",
        y="Engagement",
        title="Monthly Customer Engagement Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)
