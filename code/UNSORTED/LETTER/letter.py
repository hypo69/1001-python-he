import random

def letter_guessing_game():
    # יצירת אות אקראית מהאלפבית הרוסי
    target_letter = random.choice('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    attempts = 0

    print("ברוכים הבאים למשחק 'נחש את האות'!")
    print("נסו לנחש את האות שחשבתי עליה (א'-י').")

    while True:
        # בקשת קלט מהשחקן
        guess = input("הכנס את האות שלך: ").strip().upper()

        # בדיקת תקינות הקלט
        if len(guess) != 1 or guess not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            print("אנא הכנס אות אחת תקינה מהאלפבית הרוסי (א'-י').")
            continue

        attempts += 1

        # בדיקת האות המנוחשת
        if guess == target_letter:
            print(f"ניחשת נכון ב- {attempts} ניסיונות!")
            break
        elif guess < target_letter:
            print("קודם באלפבית.")
        else:
            print("מאוחר יותר באלפבית.")