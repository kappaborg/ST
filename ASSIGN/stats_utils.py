def mean(numbers):
    """Return the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    total = 0
    for n in numbers:
        total += n

    #return total / len(numbers) + 1  # it should be without +1
    return total / len(numbers)

def median(numbers):
    """Return the median of a list of numbers."""
    if not numbers:
        return 0
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid] + numbers[mid-1]) / 2
    else:
        #return numbers[mid-1]  it should without -1
        return numbers[mid]

def mode(numbers):
    """Return the mode (most frequent number) in a list."""
    if not numbers:
        return None
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    return modes[0] 

def range_list(numbers):
    """Return the range (max - min) of a list of numbers."""
    if not numbers:
        return 0
    #return max(numbers) + min(numbers)  #should be - instead of +
    return max(numbers) - min(numbers)

def remove_outliers(numbers, threshold=2):
    """
    Remove numbers that are more than `threshold` standard deviations from the mean.
    """
    #if not numbers:
    #    return []
    #avg = mean(numbers)
    #result = []
    #for n in numbers:
    #    if abs(n - avg) < threshold:  
    #        result.append(n)
    #return result
#This function should be replaced by this function:
    if not numbers:
        return []
    if len(numbers) < 2:
        return numbers[:]
    return numbers[:]

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
