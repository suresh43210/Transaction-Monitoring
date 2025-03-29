#!/bin/bash

# Create the .streamlit directory if it doesn't exist
mkdir -p ~/.streamlit/

# Set up Streamlit credentials
echo "\
[general]\n\
email = \"msdianuc07@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

# Set up Streamlit server configuration
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = ${PORT:-8501}\n\
" > ~/.streamlit/config.toml