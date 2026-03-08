def read_log_file(uploaded_file):
    try:
        return uploaded_file.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return f"ERROR: Failed to read uploaded file: {str(e)}"