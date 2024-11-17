import streamlit as st
from newspaper import Article
from analyze_article import analyze_article
from extract_tickers import extract_tickers, get_stock_info

st.title("Alpha Detector from Text")
url = st.text_input("Enter the URL of a finance article:")

if url:
    try:
        article = Article(url)
        article.download()
        article.parse()
        article_text = article.text
        with st.spinner("Analyzing the article..."):
            analysis = analyze_article(article_text)
            st.subheader("Analysis and Recommendations")
            st.write(analysis)
        
        tickers = extract_tickers(analysis)
        if tickers:
            st.subheader("Mentioned Stocks")
            for ticker in set(tickers):
                try:
                    info = get_stock_info(ticker)
                    st.write(f"**{ticker}**: {info.get('longName', 'N/A')}")
                    st.write(f"Current Price: {info.get('currentPrice', 'N/A')}")
                except Exception as e:
                    st.write(f"Could not retrieve data for {ticker}: {e}")

    except Exception as e:
        st.error(f"Error fetching the article: {e}")
        
st.markdown("---")
st.caption("Powered by OpenAI and Streamlit")

