# 1 can paint cover 5 sq.meter of area
import math

h=int(input("whats height of area in m ?"))
w=int(input("whats width of area in m ?"))

def can_determiner(height,width):
    coverage=5
    total_can_required=math.ceil((height*width)/coverage)
    print(f"It requires {total_can_required} can of paint to cover the area")
    
can_determiner(width=w,height=h)