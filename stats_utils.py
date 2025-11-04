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
    """
    if not numbers or len(numbers) < 2:
        return numbers[:]  # Need at least 2 numbers for std dev
    
    # Calculate mean
    avg = mean(numbers)
    
    # Calculate standard deviation
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    
    # Keep numbers within threshold
    result = []
    for n in numbers:
        if std_dev == 0 or abs(n - avg) <= threshold * std_dev:
            result.append(n)
    return result
