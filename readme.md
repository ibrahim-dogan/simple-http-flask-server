# Installation

### You can use this command in Python3 to create venv
    python3 -m venv venv

### Active your virtual environment:    
    source venv/bin/activate
    
### To deactivate:
    deactivate

### To install requirements:
    pip install -r requirements.txt

### To run local server on port 5000:
    python app.py

### Test via cURL:
    curl -X GET "http://localhost:5000/myservice?word=hello"
