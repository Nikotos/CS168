from count_min_sketch import CountMinSketch


"""
    In this solver we know amount of elements in stream
    It's predetermined!
    (but we consider storing only required frequency)
"""

class Heavy_Hitters_Solver:
    def __init__(self, count_min_sketch, heavy_hitter_min_count):
        self.count_min_sketch = count_min_sketch
        self.heavy_hitter_min_count = heavy_hitter_min_count
        self.heavy_hitters_set = set()
        
    """
        Performs adding element to Count Min Sketch
        And checking if element becomes 'Heavy Hitter'
        
        Input:
            x - string
    """
    def Inc(self, x):
        self.count_min_sketch.Inc(x)
        test_count = self.count_min_sketch.Count(x)
        if (test_count >= self.heavy_hitter_min_count):
            self.heavy_hitters_set.add(x)
        
        
    """
        returns list of supposed heavy hitters
    """
    def heavy_hitters(self):
        return self.heavy_hitters_set
        
        
        
        
        
    
