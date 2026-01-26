# Circle Area Comparison with Validation
import math

def circleAreaCoverage(radiusCircle1, radiusCircle2):
    if radiusCircle1 > 0 and radiusCircle2 > 0:
        areaCircle1 = math.pi * radiusCircle1 ** 2
        areaCircle2 = math.pi * radiusCircle2 ** 2
        print("Area of first circle: ", areaCircle1)
        print("Area of second circle: ", areaCircle2)
        coveredArea = min(areaCircle1, areaCircle2) / max(areaCircle1, areaCircle2)
        print("Percentage of area covered by smaller circle: ", coveredArea*100, "%")
    else:
        print("Invalid input, please enter two positive integers")

circleAreaCoverage(8, 10)