from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def validate_shoe_entry(line):
    if not line or not line.strip():
        return {"valid": False, "error": "Empty line", "covered_classes": ["EC28"]}
    # Blank space ignoring
    line_clean = line.strip()
    # Comma seperator
    parts = [part.strip() for part in line_clean.split(',')]
    if len(parts) < 2:
        return {"valid": False, "error": "No sizes provided", "covered_classes": ["EC23"]}
    item_name = parts[0]
    sizes = parts[1:]

    # Validate item name & 2 < x < 15 char
    if not item_name:
        return {"valid": False, "error": "Empty item name", "covered_classes": ["EC17"]}
    if len(item_name) < 2:
        return {"valid": False, "error": "Item name too short (minimum 2 characters)", "covered_classes": ["EC13"]}
    if len(item_name) > 15:
        return {"valid": False, "error": "Item name too long (maximum 15 characters)", "covered_classes": ["EC14"]}
    
    if not item_name.isalpha():
        if any(char.isdigit() for char in item_name):
            return {"valid": False, "error": "Item name contains numeric characters", "covered_classes": ["EC15"]}
        else:
            return {"valid": False, "error": "Item name contains special characters", "covered_classes": ["EC16"]}
    
    # Validate sizes x =< 5 acceptable
    if len(sizes) > 5:
        return {"valid": False, "error": "Too many sizes (maximum 5 allowed)", "covered_classes": ["EC22"]}
    
    valid_sizes = []
    covered_classes = []
    
    #Name length equivalence class
    if len(item_name) == 2:
        covered_classes.append("EC1")
    elif len(item_name) == 15:
        covered_classes.append("EC3")
    else:
        covered_classes.append("EC2")
    
    #Size count equivalence class
    if len(sizes) == 1:
        covered_classes.append("EC7")
    elif len(sizes) == 5:
        covered_classes.append("EC9")
    else:
        covered_classes.append("EC8")
    for i, size_str in enumerate(sizes):

        #Decimal Check
        if '.' in size_str:
            return {"valid": False, "error": f"Size '{size_str}' contains decimal point", "covered_classes": ["EC20"]}
        
        # Check if size contains alphabetic characters
        if not size_str.isdigit():
            return {"valid": False, "error": f"Size '{size_str}' contains alphabetic characters", "covered_classes": ["EC21"]}
        
        try:
            size = int(size_str)
        except ValueError:
            return {"valid": False, "error": f"Invalid size format: '{size_str}'", "covered_classes": ["EC21"]}
        if size < 26:
            return {"valid": False, "error": f"Size {size} is below minimum (26)", "covered_classes": ["EC18"]}
        if size > 55:
            return {"valid": False, "error": f"Size {size} is above maximum (55)", "covered_classes": ["EC19"]}
        
        # Check size range equivalence class
        if size == 26:
            covered_classes.append("EC4")
        elif size == 55:
            covered_classes.append("EC6")
        else:
            covered_classes.append("EC5")
        
        valid_sizes.append(size)
    
    # Check if sizes are in ascending order
    if valid_sizes != sorted(valid_sizes):
        return {"valid": False, "error": "Sizes must be in ascending order", "covered_classes": ["EC24"]}
    
    covered_classes.append("EC10")  # Ascending order
    covered_classes.append("EC11")  #Comma separation
    
    # Check for spaces around commas (should be ignored/valid)
    if ' , ' in line or ', ' in line or ' ,' in line:
        covered_classes.append("EC12")
    
    return {
        "valid": True,
        "item_name": item_name,
        "sizes": valid_sizes,
        "covered_classes": sorted(set(covered_classes))
    }
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    input_line = data.get('input', '')
    
    result = validate_shoe_entry(input_line)
    return jsonify(result)

@app.route('/test_cases')
def test_cases():
    test_cases = [
        {"id": 1, "input": "reebok,40,43", "expected": "VALID", "classes": ["EC1", "EC4", "EC7", "EC9", "EC10", "EC13", "EC16", "EC18", "EC20"]},
        {"id": 2, "input": "ab,26,30,35,40,55", "expected": "VALID", "classes": ["EC1", "EC4", "EC6", "EC9", "EC10", "EC13", "EC16", "EC18", "EC20"]},
        {"id": 3, "input": "nike,41,42,43,44,45,46", "expected": "INVALID", "classes": ["EC22"]},
        {"id": 4, "input": "abcdefghijklmno,40,45", "expected": "VALID", "classes": ["EC3", "EC5", "EC8", "EC10", "EC13", "EC16", "EC18", "EC20"]},
        {"id": 5, "input": "a,40", "expected": "INVALID", "classes": ["EC13"]},
        {"id": 6, "input": "abcdefghijklmnop,40", "expected": "INVALID", "classes": ["EC14"]},
        {"id": 7, "input": "nike123,40", "expected": "INVALID", "classes": ["EC15"]},
        {"id": 8, "input": "nike@pro,40", "expected": "INVALID", "classes": ["EC16"]},
        {"id": 9, "input": ",40,45", "expected": "INVALID", "classes": ["EC17"]},
        {"id": 10, "input": "nike,25", "expected": "INVALID", "classes": ["EC18"]},
        {"id": 11, "input": "nike,56", "expected": "INVALID", "classes": ["EC19"]},
        {"id": 12, "input": "nike,40.5", "expected": "INVALID", "classes": ["EC20"]},
        {"id": 13, "input": "nike,40a", "expected": "INVALID", "classes": ["EC21"]},
        {"id": 14, "input": "nike", "expected": "INVALID", "classes": ["EC23"]},
        {"id": 15, "input": "nike,45,40", "expected": "INVALID", "classes": ["EC24"]},
    ]
    return render_template('test_cases.html', test_cases=test_cases)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

