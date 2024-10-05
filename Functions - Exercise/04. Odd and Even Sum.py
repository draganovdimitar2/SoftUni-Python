def odd_even_sums(number: str) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:  # int(digit) % 2 != 0 -> digit is odd
            sum_of_odd_digits += int(digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
 
 
some_number = input()
print(odd_even_sums(some_number))