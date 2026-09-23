import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="राहुल जनरल स्टोर - डिजिटल खाता", page_icon="🛒", layout="wide")

# App Header
st.title("🛒 राहुल जनरल स्टोर - डिजिटल खाता")
st.write("यहाँ ग्राहकों का हिसाब चुटकियों में रखें, सुरक्षित और आसान तरीके से।")

# Initialize Session State for Data Persistence
if 'khata_data' not in st.session_state:
    st.session_state.khata_data = pd.DataFrame(columns=[
        "तारीख (Date)", "ग्राहक का नाम (Customer)", 
        "लेन-देन (Type)", "रकम (Amount)", "विवरण (Note)"
    ])

# Sidebar / Main Form for Adding Entries
st.subheader("📝 नया हिसाब दर्ज करें")

with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        customer_name = st.text_input("ग्राहक का नाम (Customer Name)")
        entry_type = st.selectbox("लेन-देन का प्रकार (Type)", ["उधार दिया (Debit - Given)", "पैसा मिला (Credit - Received)"])
    with col2:
        amount = st.number_input("रकम (Amount in ₹)", min_value=0.0, step=1.0)
        entry_date = st.date_input("तारीख (Date)", datetime.today())
    
    note = st.text_area("विवरण / सामान का नाम (Note / Items)")
    submit_button = st.form_submit_button(label="हिसाब सेव करें")

    if submit_button:
        if customer_name.strip() == "":
            st.warning("कृपया ग्राहक का नाम दर्ज करें!")
        elif amount <= 0:
            st.warning("कृपया सही रकम दर्ज करें!")
        else:
            new_row = {
                "तारीख (Date)": str(entry_date),
                "ग्राहक का नाम (Customer)": customer_name,
                "लेन-देन (Type)": entry_type,
                "रकम (Amount)": amount,
                "विवरण (Note)": note
            }
            st.session_state.khata_data = pd.concat([st.session_state.khata_data, pd.DataFrame([new_row])], ignore_index=True)
            st.success(f"सफलतापूर्वक सेव हो गया: {customer_name} का हिसाब!")

# Display Khata Records
st.markdown("---")
st.subheader("📊 सभी लेन-देन का रिकॉर्ड")

if not st.session_state.khata_data.empty:
    # Search Filter
    search_query = st.text_input("🔍 ग्राहक के नाम से खोजें (Search Customer)")
    
    filtered_data = st.session_state.khata_data
    if search_query:
        filtered_data = filtered_data[filtered_data["ग्राहक का नाम (Customer)"].str.contains(search_query, case=False, na=False)]
    
    st.dataframe(filtered_data, use_container_width=True)
    
    # Summary Metrics
    total_given = st.session_state.khata_data[st.session_state.khata_data["लेन-देन (Type)"] == "उधार दिया (Debit - Given)"]["रकम (Amount)"].sum()
    total_received = st.session_state.khata_data[st.session_state.khata_data["लेन-देन (Type)"] == "पैसा मिला (Credit - Received)"]["रकम (Amount)"].sum()
    
    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("कुल उधार दिया (Total Given)", f"₹ {total_given}")
    mcol2.metric("कुल पैसा मिला (Total Received)", f"₹ {total_received}")
    mcol3.metric("बाकी लेना है (Net Balance)", f"₹ {total_given - total_received}")
    
    # Download Button
    csv = st.session_state.khata_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 सारा डेटा डाउनलोड करें (CSV)",
        data=csv,
        file_name='rahul_general_store_khata.csv',
        mime='text/csv',
    )
else:
    st.info("अभी तक कोई हिसाब दर्ज नहीं किया गया है। ऊपर दिए गए फॉर्म से एंट्री शुरू करें!")
    
