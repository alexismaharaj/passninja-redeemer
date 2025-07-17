
# Pass Expiration API

This simple Flask server provides a `/redeem` endpoint that marks a PassNinja pass as expired when accessed.

## Setup Instructions

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Run the app
```
python app.py
```

### 3. Example usage
Access in your browser:
```
http://localhost:5000/redeem?serial=YOUR_PASS_SERIAL
```

Or deploy it and replace the URL with your server:
```
https://yourdomain.com/redeem?serial=YOUR_PASS_SERIAL
```

Once redeemed, the pass will be marked as expired and display "This pass has expired" in the barcode.
