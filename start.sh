#!/bin/bash

# Start FastAPI in the background
gunicorn -w 4 -k uvicorn.workers.UvicornWorker api:app --bind 0.0.0.0:8000 &

# Start Streamlit UI
streamlit run streamlit_ui.py --server.port 8501 --server.address 0.0.0.0
