#!/bin/bash
# ==============================================================================
# MSME Credit Risk Assistant - Automated One-Click Launcher
# ==============================================================================

PROJECT_DIR="/Users/avinashsharma/msme_credit_risk_assistant"
cd "$PROJECT_DIR" || exit 1

echo "=================================================================="
echo "    MSME Credit Risk Assistant - One-Click Launcher              "
echo "=================================================================="

# Check if an existing server is already active on port 8501
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null ; then
    echo "✓ Assistant server is already running on port 8501."
    echo "Opening portal in your browser..."
    open "http://localhost:8501"
    echo "=================================================================="
    echo "Portal opened at: http://localhost:8501"
    echo "To stop the assistant, press Ctrl + C or close this window."
    echo "=================================================================="
    # Keep the window open so user sees status
    while true; do sleep 5; done
else
    # Background trigger to guarantee browser popup after Streamlit initializes
    (sleep 2 && open "http://localhost:8501") &

    # Activate virtual environment
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    fi

    echo "Starting Streamlit application..."
    echo "Opening http://localhost:8501 in your default browser..."
    echo "=================================================================="

    exec streamlit run app.py --server.headless false --server.port 8501
fi
