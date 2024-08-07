import statistics
def getStatistics(numbers: list[int]) -> dict:
    return { "average": statistics.mean(numbers), "sum": sum(numbers), "max": max(numbers), \
            "min": min(numbers), "length": len(numbers) }

print(getStatistics([10,20,30,40,50]))