def roman_to_arabic(roman):
  total = 0
  for i in range(len(roman) - 1):
    left_char = roman[i]
    print(left_char)

    right_char = roman[i + 1]
    print(right_char)

    left_value = convert_character(left_char)
    print(f"Left Value: {left_value}")

    right_value = convert_character(right_char)
    print(f"Right Value: {right_value}")
    if left_value < right_value:
      left_value += left_value
    total += left_value
    if roman:
      total += convert_character(roman[-1])
    print(f"Total: {total}")
    return total


def convert_character(roman_char):
  conversion_map = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
  }

  return conversion_map.get(roman_char)


# Let’s try CXLII, which should equal 142 if the algorithm is correct

if __name__ == "__main__":
  roman_to_arabic('XXXXX')

