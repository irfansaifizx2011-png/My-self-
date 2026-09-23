import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="राहुल जनरल स्टोर - डिजिटल खाता", page_icon="🛒", layout="centered")

# App Header
st.title("🛒 राहुल जनरल स्टोर - डिजिटल खाता बुक")
st.write("यहाँ ग्राहकों का हिसाब चुटकियों में रखें, जो कभी डिलीट नहीं होगा!")

# Initialize Session State for Data Persistence
if 'khata_data' not in st.session_state:
    st.session_state.khata_data = pd.DataFrame(columns=[
        "तारीख (Date)", "ग्राहक का नाम (Customer)", "लेन/দেন (Type)", 
        "रकम (Amount)", "विवरण (Note)"
    ])

# Sidebar / Main Form for Adding Entry
st.subheader("📝 नया हिसाब दर्ज करें")

with st.form("khata_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        customer_name = st.text_input("ग्राहक का नाम (जैसे: शर्मा जी)")
    with col2:
        entry_type = st.selectbox("हिसाब का प्रकार", ["बाकी (Udhar/Given)", "पैसा मिला (Payment Received)"])
        
    amount = st.number_input("रकम (₹ में)", min_value=0.0, step=1.0)
    note = st.text_input("सामान या विवरण (जैसे: 2 किलो चीनी, 1 लीटर तेल)")
    
    submit_button = st.form_submit_button(label="खाते में सेव करें 💾")
    
    if submit_button:
        if customer_name.strip() == "":
            st.warning("कृपया ग्राहक का नाम लिखें!")
        elif amount <= 0:
            st.warning("कृपया सही रकम दर्ज करें!")
        else:
            current_date = datetime.now().strftime("%d-%m-%Y %H:%M")
            new_row = pd.DataFrame({
                "तारीख (Date)": [current_date],
                "ग्राहक का नाम (Customer)": [customer_name.strip().title()],
                "लेन/দেন (Type)": [entry_type],
                "रकम (Amount)": [amount],
                "विवरण (Note)": [note]
            })
            st.session_state.khata_data = pd.concat([st.session_state.khata_data, new_row], ignore_index=True)
            st.success(f"✅ {customer_name.strip().title()} का हिसाब सफलतापर्वक सेव हो गया!")

st.markdown("---")

# Summary Section
st.subheader("📊 कुल हिसाब और बकाया")

if not st.session_state.khata_data.empty:
    df = st.session_state.khata_data
    
    # Calculate Total Udhar and Paid
    total_udhargiven = df[df["लेन/দেন (Type)"] == "बाकी (Udhar/Given)"]["रकम (Amount)"].sum()
    total_received = df[df["लेन/দেন (Type)"] == "पैसा मिला (Payment Received)"]["रकम (Amount)"].sum()
    net_due = total_udhargiven - total_received
    
     mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("कुल बाकी (Total Udhar)", f"₹ {total_udhargiven}")
    mcol2.metric("कुल मिला पैसा (Paid)", f"₹ {total_received}")
    mcol3.metric("बाकी लेना है (Net Due)", f"₹ {net_due}")
    
    st.markdown("---")
    
    # Customer Wise Filter
    st.subheader("🔍 ग्राहक के हिसाब की डायरी")
    selected_customer = st.selectbox("ग्राहक चुनें:", ["सभी ग्राहक (All Customers)"] + list(df["ग्राहक का नाम (Customer)"].unique()))
    
    if selected_customer != "सभी ग्राहक (All Customers)":
        filtered_df = df[df["ग्राहक का नाम (Customer)"] == selected_customer]
        st.dataframe(filtered_df, use_container_width=True)
        
        # Individual Customer Balance
        c_given = filtered_df[filtered_df["लेन/দেন (Type)"] == "बाकी (Udhar/Given)"]["रकम (Amount)"].sum()
        c_paid = filtered_df[filtered_df["लेन/দেন (Type)"] == "पैसा मिला (Payment Received)"]["रकम (Amount)"].sum()
        c_net = c_given - c_paid
        st.info(f"👉 **{selected_customer}** से कुल लेना बाकी है: **₹ {c_net}**")
    else:
        st.dataframe(df, use_container_width=True)
        
else:
    st.info("अभी तक कोई खाता दर्ज नहीं किया गया है। ऊपर दिए गए फॉर्म से शुरुआत करें!")
