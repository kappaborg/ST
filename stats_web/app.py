from flask import Flask, render_template, request, jsonify
import sys
import os

# Add parent directory to path to import stats_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from stats_utils import mean, median, mode, range_list, remove_outliers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    numbers_str = data.get('numbers', '')
    threshold = data.get('threshold', 2)
    function = data.get('function', 'mean')
    
    try:
        # Parse numbers from string (comma or space separated)
        numbers = []
        for part in numbers_str.replace(',', ' ').split():
            try:
                numbers.append(float(part))
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': f'Invalid number: {part}'
                })
        
        if not numbers:
            return jsonify({
                'success': False,
                'error': 'Please enter at least one number'
            })
        
        result = {}
        
        if function == 'mean':
            result['value'] = mean(numbers)
            result['description'] = f'Mean of {len(numbers)} numbers'
        elif function == 'median':
            result['value'] = median(numbers)
            result['description'] = f'Median of {len(numbers)} numbers'
        elif function == 'mode':
            mode_value = mode(numbers)
            result['value'] = mode_value if mode_value is not None else 'No mode (all values unique)'
            result['description'] = f'Mode of {len(numbers)} numbers'
        elif function == 'range':
            result['value'] = range_list(numbers)
            result['description'] = f'Range (max - min) of {len(numbers)} numbers'
        elif function == 'outliers':
            result['value'] = remove_outliers(numbers, threshold)
            result['description'] = f'Numbers after removing outliers (threshold: {threshold} std dev)'
            result['original_count'] = len(numbers)
            result['filtered_count'] = len(result['value'])
            result['removed_count'] = result['original_count'] - result['filtered_count']
        
        return jsonify({
            'success': True,
            'result': result,
            'input': numbers
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/test_case', methods=['POST'])
def test_case():
    """Run predefined test cases"""
    data = request.json
    test_case_id = data.get('test_case', '')
    
    test_cases = {
        'mean_normal': {
            'function': 'mean',
            'numbers': [1, 2, 3, 4, 5],
            'expected': 3.0,
            'description': 'Mean of [1, 2, 3, 4, 5]'
        },
        'mean_empty': {
            'function': 'mean',
            'numbers': [],
            'expected': 0,
            'description': 'Mean of empty list'
        },
        'median_even': {
            'function': 'median',
            'numbers': [1, 2, 3, 4],
            'expected': 2.5,
            'description': 'Median of [1, 2, 3, 4] (even length)'
        },
        'median_odd': {
            'function': 'median',
            'numbers': [1, 2, 3, 4, 5],
            'expected': 3,
            'description': 'Median of [1, 2, 3, 4, 5] (odd length)'
        },
        'mode_single': {
            'function': 'mode',
            'numbers': [1, 2, 2, 3],
            'expected': 2,
            'description': 'Mode of [1, 2, 2, 3]'
        },
        'range_normal': {
            'function': 'range',
            'numbers': [10, 2, 7, 5],
            'expected': 8,
            'description': 'Range of [10, 2, 7, 5] (max - min = 10 - 2 = 8)'
        },
        'outliers_normal': {
            'function': 'outliers',
            'numbers': [1, 2, 3, 100],
            'threshold': 2,
            'description': 'Remove outliers from [1, 2, 3, 100]'
        }
    }
    
    if test_case_id not in test_cases:
        return jsonify({
            'success': False,
            'error': 'Test case not found'
        })
    
    tc = test_cases[test_case_id]
    numbers = tc['numbers']
    
    # Calculate actual result
    if tc['function'] == 'mean':
        actual = mean(numbers)
    elif tc['function'] == 'median':
        actual = median(numbers)
    elif tc['function'] == 'mode':
        actual = mode(numbers)
    elif tc['function'] == 'range':
        actual = range_list(numbers)
    elif tc['function'] == 'outliers':
        actual = remove_outliers(numbers, tc.get('threshold', 2))
    
    return jsonify({
        'success': True,
        'test_case': tc,
        'actual': actual,
        'expected': tc.get('expected', 'N/A'),
        'passed': actual == tc.get('expected', None) if 'expected' in tc else None
    })

if __name__ == '__main__':
    app.run(debug=True, port=5003)

