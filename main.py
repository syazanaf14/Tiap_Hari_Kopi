import streamlit as st

st.set_page_config(page_title="Digital Branding Dashboard", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("TIAP HARI KOPI")
page = st.sidebar.radio(
    "Navigation",
    ["Business Profile", "Menu & Promotion", "Customer View",
     "Login (Staff)", "Analytics Dashboard"]
)

# --- Pages ---

if page == "Business Profile":
    st.title("Tiap Hari Kopi")
    st.subheader("About Us")
    st.write("""
    Tiap Hari Kopi is a local café located in Kubang Kerian,
    offering a mix of Eastern and Western food with specialty coffee.
    """)

    st.subheader("Location")
    st.write("Kubang Kerian, Kelantan")

elif page == "Menu & Promotion":
    st.title("Menu & Promotions")
    st.info("This section displays menu items and current promotions.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Signature Coffee", "RM 12")
    col2.metric("Pasta Series", "RM 15")
    col3.metric("Student Combo", "RM 10")

elif page == "Customer View":
    st.title("Customer Engagement")
    st.write("⭐ Ratings: 4.5 / 5")
    st.write("💬 Latest Reviews")
    st.success("“Nice environment and affordable coffee!”")
    st.warning("“Waiting time slightly long during peak hours.”")

elif page == "Login (Staff)":
    st.title("Staff Login")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")

elif page == "Analytics Dashboard":
    st.title("Business Analytics Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", "1,259")
    col2.metric("Average Rating", "4.5")
    col3.metric("Brand Sentiment", "Positive")

    st.subheader("Engagement Overview")
    st.line_chart([10, 20, 15, 30, 25])
