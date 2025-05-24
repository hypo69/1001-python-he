def sum_of_divisors(n):
    """
    מחשבת את סכום המחלקים העצמיים של המספר n.

    Args:
        n: מספר שלם.

    Returns:
        סכום המחלקים העצמיים של המספר n.
    """
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # כדי לא להוסיף מחלק פעמיים (למשל, עבור 16 = 4*4)
                total += n // i
    return total


def is_perfect_number(n):
    """
    בודקת האם המספר n הוא מספר משוכלל.

    Args:
        n: מספר שלם.

    Returns:
        True, אם המספר n משוכלל, אחרת False.
    """
    return n > 1 and sum_of_divisors(n) == n


def find_perfect_numbers(limit):
    """
    מוצאת את כל המספרים המשוכללים בטווח נתון.

    Args:
        limit: הגבול העליון של הטווח (כולל).

    Returns:
        רשימה של כל המספרים המשוכללים בטווח שבין 1 ל-limit.
    """
    perfect_numbers = []
    for i in range(2, limit + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


if __name__ == '__main__':
    limit = 10000
    perfect_nums = find_perfect_numbers(limit)
    print(f"מספרים משוכללים עד {limit}: {perfect_nums}")