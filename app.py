import streamlit as st
from textblob import TextBlob

# Page setup
st.set_page_config(page_title="Smart Text & Sentiment Analyzer", page_icon="🤖", layout="centered")

st.title("📊 Smart Text & Sentiment Analyzer")
st.write("Apna text niche enter karein aur dekhein ki AI uske bare mein kya kehta hai!")

# Text input box
user_text = st.text_area("Yahan apna text ya review likhein:", placeholder="Jaise: This product is amazing, I loved it!")

if st.button("Analyze Karo"):
    if user_text.strip() == "":
        st.warning("Pehle kuch text toh likhiye!")
    else:
        # Sentiment analysis
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity
        
        words = len(user_text.split())
        chars = len(user_text)
        
        st.subheader("📈 Analysis Results:")
        
        col1, col2 = st.columns(2)
        col1.metric("Total Words", words)
        col2.metric("Total Characters", chars)
        
        st.markdown("### 🧠 Sentiment Result:")
        if polarity > 0:
            st.success(f"😊 Positive Review! (Score: {polarity:.2f})")
        elif polarity < 0:
            st.error(f"😞 Negative Review! (Score: {polarity:.2f})")
        else:
            st.info(f"😐 Neutral Review! (Score: {polarity:.2f})")