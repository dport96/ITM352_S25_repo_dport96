def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress

def determine_progress2(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    progress = "Get going!"
    if hits_spins_ratio > 0:
        progress = "On your way!"
    if hits_spins_ratio >= 0.25:
        progress = "Almost there!"
    if hits_spins_ratio >= 0.5 and hits < spins:
        progress = "You win!"

    return progress
   

def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio == 0:
        return "Get going!"
    elif hits_spins_ratio < 0.25:
        return "On your way!"
    elif hits_spins_ratio < 0.5:
        return "Almost there!"
    elif hits < spins:
        return "You win!"
    
    return "Almost there!"  # This ensures a return value for all cases

def test_determine_progress(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed"
    assert progress_function(2, 5) == "Almost there!", "Test case 2 failed"
    assert progress_function(1, 5) == "On your way!", "Test case 3 failed"
    assert progress_function(5, 10) == "You win!", "Test case 4 failed"
    
test_determine_progress(determine_progress3)
