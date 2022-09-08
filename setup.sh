mkdir -p ~/.streamlit/
echo "[theme]
# primaryColor = '#E694FF'
# backgroundColor = ‘#00172b’
# secondaryBackgroundColor = ‘#0083bb’
# textColor= ‘#ffffff’
# font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
