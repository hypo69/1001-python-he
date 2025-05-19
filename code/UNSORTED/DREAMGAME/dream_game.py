import numpy as np
import pandas as pd
from collections import Counter
from random import randint as rnd
import google.generativeai as genai
from typing import List, Dict, Tuple
import os
import random

# בדיקת נוכחות מפתח API של ג'מיני
if 'GOOGLE_API_KEY' not in os.environ:
    raise EnvironmentError("מפתח API של ג'מיני לא נמצא. אנא הגדר את משתנה הסביבה GOOGLE_API_KEY.")
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


def generate_random_dream_numbers(num_dreams: int, max_square: int = 48) -> List[int]:
    """מייצר רשימה של מספרי "משאלות" אקראיים וייחודיים."""
    if num_dreams > max_square:
        raise ValueError("מספר המשאלות אינו יכול להיות גדול ממספר התאים על הלוח.")
    return random.sample(range(1, max_square + 1), num_dreams)


class DreamGame:
    """
    מחלקה המדמה משחק של איסוף "משאלות" על גבי לוח משחק.
    """

    def __init__(self, num_dreams: int, moves: int = 3, num_iterations: int = 100_000, max_square: int = 48):
        """
        מאתחל את המשחק.

        Args:
            num_dreams: מספר ה"משאלות" שיש לייצר.
            moves: מספר הטלות קוביה למשחק בודד.
            num_iterations: מספר סימולציות המשחק.
            max_square: המספר המרבי של התא.
        """
        if num_dreams > max_square:
           raise ValueError(f"מספר המשאלות ({num_dreams}) אינו יכול להיות גדול ממספר התאים על הלוח ({max_square}).")
        self.dream_numbers = generate_random_dream_numbers(num_dreams, max_square) # מייצרים מספרי משאלות אקראיים
        self.moves = moves
        self.num_iterations = num_iterations
        self.dreams: Dict[int, str] = {}
        self._generate_dream_names()  # מייצרים שמות "משאלות" בעת האתחול

    def _generate_dream_names(self) -> None:
        """
        מייצר שמות "משאלות" באמצעות מודל ג'מיני.
        """
        prompt = f"המצא {len(self.dream_numbers)} שמות ייחודיים, קצרים (לא יותר מ-5 מילים) ומעניינים ל\"משאלות\", הקשורים למסעות, הרפתקאות, בילויים. הצג את התשובה כרשימה, כאשר כל שם בשורה חדשה."
        response = model.generate_content(prompt)

        if response.text:
            dream_names = response.text.strip().split('\n')
        else:
             raise ValueError("מודל ג'מיני לא החזיר טקסט כלשהו.")

        if len(dream_names) != len(self.dream_numbers):
            raise ValueError(f"מספר השמות שנוצרו ({len(dream_names)}) אינו תואם את מספר מספרי המשאלות ({len(self.dream_numbers)}).")

        self.dreams = {number: f"{number}_{name}" for number, name in zip(self.dream_numbers, dream_names)}

    def _simulate_game(self) -> Counter[str]:
         """
         מדמה משחק בודד ומחזיר את תדירות הביקור ב"משאלות".

         Returns:
             Counter: מונה התדירויות של ביקור ב"משאלות".
         """
         dreams_frequency = Counter()
         square = 0
         visited_dreams = set()

         for _ in range(self.moves):
            square += rnd(1, 6) + rnd(1, 6)
            square = square % 48 if square > 48 else square

            if square in self.dream_numbers and square not in visited_dreams:
                dreams_frequency[self.dreams[square]] += 1
                visited_dreams.add(square) # משאלה בה בוצע ביקור מוספת לקבוצה

         return dreams_frequency

    def run_experiment(self) -> pd.DataFrame:
        """
        מריץ את סימולציית המשחק מספר פעמים ומחזיר DataFrame עם התוצאות.

        Returns:
            pandas.DataFrame: DataFrame עם התדירות וההסתברות לביקור בכל "משאלה".
        """
        dreams_frequency = sum( (self._simulate_game() for _ in range(self.num_iterations)), Counter()) # מסכמים את מונים מהגנרטורים
        df = pd.DataFrame(dreams_frequency.items(), columns=['משאלה', 'תדירות']).sort_values('תדירות', ascending=False)
        df['הסתברות'] = df['תדירות'] / self.num_iterations
        return df

def run_simulation_with_intervals(moves: int, num_iterations: int) -> None:
    """
    מריץ סימולציה של המשחק עם מרווחים שונים של כמות משאלות.

    Args:
        moves: מספר הטלות קוביה למשחק בודד.
        num_iterations: מספר סימולציות המשחק.
    """

    # 1. מספר אקראי של "משאלות" בטווח (10 - 20)
    num_dreams_normal = random.randint(10, 20)
    game_normal = DreamGame(num_dreams=num_dreams_normal, moves=moves, num_iterations=num_iterations)
    df_normal = game_normal.run_experiment()
    print(f"תוצאות עם {num_dreams_normal} משאלות (טווח 10-20):\n{df_normal}\n")

    # 2. מספר אקראי של "משאלות" בצפיפות נמוכה יותר (5 - 15)
    num_dreams_less = random.randint(5, 15)
    game_less = DreamGame(num_dreams=num_dreams_less, moves=moves, num_iterations=num_iterations)
    df_less = game_less.run_experiment()
    print(f"תוצאות עם {num_dreams_less} משאלות (טווח 5-15):\n{df_less}\n")

    # 3. מספר אקראי של "משאלות" בצפיפות גבוהה יותר (15 - 25)
    num_dreams_more = random.randint(15, 25)
    game_more = DreamGame(num_dreams=num_dreams_more, moves=moves, num_iterations=num_iterations)
    df_more = game_more.run_experiment()
    print(f"תוצאות עם {num_dreams_more} משאלות (טווח 15-25):\n{df_more}\n")

if __name__ == '__main__':
    moves = 3  # מספר מהלכים למשחק
    num_iterations = 10_000  # מספר סימולציות
    run_simulation_with_intervals(moves, num_iterations)