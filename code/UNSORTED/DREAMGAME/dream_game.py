import numpy as np
import pandas as pd
from collections import Counter
from random import randint as rnd
import google.generativeai as genai
from typing import List, Dict, Tuple
import os
import random

# בדיקת קיום מפתח API של Gemini
if 'GOOGLE_API_KEY' not in os.environ:
    raise EnvironmentError("מפתח ה-API של Gemini לא נמצא. אנא הגדר את משתנה הסביבה GOOGLE_API_KEY.")
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


def generate_random_dream_numbers(num_dreams: int, max_square: int = 48) -> List[int]:
    """מייצר רשימה של מספרי "חלומות" אקראיים ייחודיים."""
    if num_dreams > max_square:
        raise ValueError("מספר החלומות אינו יכול להיות גדול ממספר התאים בלוח.")
    return random.sample(range(1, max_square + 1), num_dreams)


class DreamGame:
    """
    מחלקה המדמה משחק איסוף "חלומות" על גבי לוח המשחק.
    """

    def __init__(self, num_dreams: int, moves: int = 3, num_iterations: int = 100_000, max_square: int = 48):
        """
        מאתחל את המשחק.

        ארגומנטים:
            num_dreams: מספר ה"חלומות" שיש לייצר.
            moves: מספר הטלות הקוביות במשחק יחיד.
            num_iterations: מספר הדמיות המשחק.
            max_square: מספר התא המרבי
        """
        if num_dreams > max_square:
           raise ValueError(f"מספר החלומות ({num_dreams}) אינו יכול להיות גדול ממספר התאים בלוח ({max_square}).")
        self.dream_numbers = generate_random_dream_numbers(num_dreams, max_square) # מייצרים מספרי חלומות אקראיים
        self.moves = moves
        self.num_iterations = num_iterations
        self.dreams: Dict[int, str] = {}
        self._generate_dream_names()  # מייצרים את שמות ה"חלומות" בעת האתחול
    
    def _generate_dream_names(self) -> None:
        """
        מייצר את שמות ה"חלומות" באמצעות מודל Gemini.
        """
        prompt = f"Придумай {len(self.dream_numbers)} уникальных коротких (не более 5 слов) и интересных названий для \"мечт\", связанных с путешествиями, приключениями, развлечениями. Выдай ответ списком, где каждое название на новой строке."
        response = model.generate_content(prompt)
        
        if response.text:
            dream_names = response.text.strip().split('\n')
        else:
             raise ValueError("מודל Gemini לא החזיר טקסט כלשהו.")

        if len(dream_names) != len(self.dream_numbers):
            raise ValueError(f"מספר השמות שנוצרו ({len(dream_names)}) אינו תואם את מספר מספרי החלומות ({len(self.dream_numbers)}).")

        self.dreams = {number: f"{number}_{name}" for number, name in zip(self.dream_numbers, dream_names)}
        
    def _simulate_game(self) -> Counter[str]:
         """
         מדמה משחק יחיד ומחזירה את תדירות הביקור ב"חלומות".

         החזרה:
             Counter: מונה תדירויות הביקור ב"חלומות".
         """
         dreams_frequency = Counter()
         square = 0
         visited_dreams = set()

         for _ in range(self.moves):
            square += rnd(1, 6) + rnd(1, 6)
            square = square % 48 if square > 48 else square

            if square in self.dream_numbers and square not in visited_dreams:
                dreams_frequency[self.dreams[square]] += 1
                visited_dreams.add(square) # חלום שבוקר מתווסף לקבוצה

         return dreams_frequency

    def run_experiment(self) -> pd.DataFrame:
        """
        מריץ את הדמיית המשחק מספר פעמים ומחזיר DataFrame עם התוצאות.

        החזרה:
            pandas.DataFrame: DataFrame המכיל את תדירות והסתברות הביקור בכל "חלום".
        """
        dreams_frequency = sum( (self._simulate_game() for _ in range(self.num_iterations)), Counter()) # מסכמים את מונים (Counter()) מהגנרטורים
        df = pd.DataFrame(dreams_frequency.items(), columns=['Мечта', 'Частота']).sort_values('Частота', ascending=False)
        df['Вероятность'] = df['Частота'] / self.num_iterations
        return df

def run_simulation_with_intervals(moves: int, num_iterations: int) -> None:
    """
    מריץ את הדמיית המשחק עם טווחי מספר חלומות שונים.

    ארגומנטים:
        moves: מספר הטלות הקוביות במשחק יחיד.
        num_iterations: מספר הדמיות המשחק.
    """

    # 1. מספר אקראי של "חלומות" בטווח (10 - 20)
    num_dreams_normal = random.randint(10, 20)
    game_normal = DreamGame(num_dreams=num_dreams_normal, moves=moves, num_iterations=num_iterations)
    df_normal = game_normal.run_experiment()
    print(f"תוצאות עם {num_dreams_normal} חלומות (טווח 10-20):\n{df_normal}\n")

    # 2. מספר אקראי של "חלומות" עם צפיפות מעט נמוכה יותר (5 - 15)
    num_dreams_less = random.randint(5, 15)
    game_less = DreamGame(num_dreams=num_dreams_less, moves=moves, num_iterations=num_iterations)
    df_less = game_less.run_experiment()
    print(f"תוצאות עם {num_dreams_less} חלומות (טווח 5-15):\n{df_less}\n")

    # 3. מספר אקראי של "חלומות" עם צפיפות מעט גבוהה יותר (15 - 25)
    num_dreams_more = random.randint(15, 25)
    game_more = DreamGame(num_dreams=num_dreams_more, moves=moves, num_iterations=num_iterations)
    df_more = game_more.run_experiment()
    print(f"תוצאות עם {num_dreams_more} חלומות (טווח 15-25):\n{df_more}\n")

if __name__ == '__main__':
    moves = 3  # מספר המהלכים למשחק
    num_iterations = 10_000  # מספר ההדמיות
    run_simulation_with_intervals(moves, num_iterations)