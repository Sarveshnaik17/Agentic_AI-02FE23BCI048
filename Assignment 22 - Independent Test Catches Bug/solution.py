def coding_agent(values, minimum):
    # Deliberate regression: drops the final record.
    return [value for value in values[:-1] if value >= minimum]

def testing_agent():
    values = [3, 7, 9]
    expected = [7, 9]
    actual = coding_agent(values, 7)
    passed = actual == expected
    return {"status": "PASS" if passed else "FAIL",
            "expected": expected, "actual": actual,
            "message": "Independent requirement check: return every value at or above the threshold."}

if __name__ == "__main__":
    result = testing_agent()
    print(result)
    assert result["status"] == "FAIL"

