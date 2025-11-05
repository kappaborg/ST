def mean(numbers):
    """Calculate average"""
    if not numbers:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  

def median(numbers):
    """Get median value"""
    if not numbers:
        return 0
    # Sort the list (modifies in place)
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        # Even number of elements
        return (numbers[mid] + numbers[mid-1]) / 2
    else:
        # Odd number of elements
        return numbers[mid]  

def mode(numbers):
    """Find most common number"""
    if not numbers:
        return None
    # Build frequency dictionary
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1
    max_freq = max(freq.values())
    # Get all numbers with max frequency
    modes_list = [k for k, v in freq.items() if v == max_freq]
    return modes_list[0]  # Just return first one

def range_list(numbers):
    """Calculate range"""
    if not numbers:
        return 0
    return max(numbers) - min(numbers)  

def remove_outliers(numbers, threshold=2):
    """
    Remove outliers using standard deviation
    threshold determines how many std devs away is considered outlier
    Uses IQR method which is more robust to extreme outliers
    """
    if not numbers or len(numbers) < 2:
        return numbers[:]
    
    # Sort numbers
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    # Calculate quartiles
    q1_idx = n // 4
    q3_idx = (3 * n) // 4
    q1 = sorted_nums[q1_idx]
    q3 = sorted_nums[q3_idx]
    
    # Calculate IQR
    iqr = q3 - q1
    
    if iqr == 0:
        # If IQR is 0, use standard deviation method
        avg = mean(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
        std_dev = variance ** 0.5
        if std_dev == 0:
            return numbers[:]
        result = []
        for n in numbers:
            if abs(n - avg) <= threshold * std_dev:
                result.append(n)
        return result
    
    # Calculate bounds using IQR method (more robust)
    # Using threshold as multiplier for IQR
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    
    # Filter numbers within bounds
    result = []
    for n in numbers:
        if lower_bound <= n <= upper_bound:
            result.append(n)
    
    return result
