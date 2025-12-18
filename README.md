# Metro-X

This is a solution to GeekTrust backend design problem : [Geekdemy](https://www.geektrust.com/coding/detailed/geekdemy)

## Setup Instructions

### 1. Create a Virtual Environment

**Windows:**
```
python -m venv venv
```

**Linux/Mac:**
```
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**Windows:**
```
venv\Scripts\activate
```

**Linux/Mac:**
```
source venv/bin/activate
```

### 3. Install Requirements

```
pip install -r requirements.txt
```

### 4. Run the Main File

```
python main.py sample_input/input1.txt
```

## TODO :
- Add test cases for current development.
- Discount calculation & pro membership related logic needs to be separated from purchase class.
- Refactor logic
- Add Persistent data-store
- Containerization
