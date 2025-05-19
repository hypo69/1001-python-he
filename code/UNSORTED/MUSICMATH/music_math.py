# @title מודול MusicMath: דוגמאות לקשר בין מתמטיקה ומוזיקה.

"""
מודול MusicMath: דוגמאות לקשר בין מתמטיקה ומוזיקה.
"""
import math
from fractions import Fraction
import re

def calculate_frequency(note_number, concert_a_freq=440.0):
    """
    מחשב את תדר התו, בידיעת מספרו בסולם הכרומטי.

    Args:
        note_number (int): מספר התו ביחס ל-A4 (A4 = 0).
        concert_a_freq (float, optional): תדר התו A4. ברירת מחדל היא 440.0.

    Returns:
        float: תדר התו בהרץ.
    """
    return concert_a_freq * math.pow(2, note_number / 12)

def calculate_interval_ratio(note1_number, note2_number):
    """
    מחשב את יחס התדרים בין שני תווים, בידיעת מספריהם.

    Args:
        note1_number (int): מספר התו הראשון.
        note2_number (int): מספר התו השני.

    Returns:
         str: יחס התדרים כביטוי של שבר פשוט.
    """
    freq1 = calculate_frequency(note1_number)
    freq2 = calculate_frequency(note2_number)
    ratio = freq2/freq1 if freq2>freq1 else freq1/freq2
    fraction_ratio = Fraction(ratio).limit_denominator(100)  # Limit to reasonable denominators
    return str(fraction_ratio)

def calculate_tempo_duration(bpm, beat_length, beats):
     """
    מחשב את משך הזמן הכולל בשניות של קטע מוזיקלי.

    Args:
         bpm (int): קצב בפעימות לדקה.
         beat_length(float): משך פעימה בודדת בשניות.
         beats (int): מספר הפעימות בקטע המוזיקלי.

    Returns:
        float: משך הזמן הכולל של הקטע בשניות.
    """
     return beat_length*beats

def calculate_note_duration(tempo, note_value):
    """
    מחשב את משך התו בשניות.

    Args:
        tempo (int): קצב בפעימות לדקה.
        note_value (float): משך התו ביחס לתו שלם (1.0 = שלם, 0.5 = חצי, 0.25 = רבע וכו').

    Returns:
        float: משך התו בשניות.
    """
    beat_duration = 60 / tempo
    return beat_duration * note_value

def calculate_rhythm_pattern(bar_length, note_values):
    """
    מחשב את משך הזמן הכולל של תבנית קצב בשניות.

    Args:
         bar_length (float): משך תיבה במספר תווים שלמים.
         note_values (list): רשימת משכי תווים (ביחס לתו שלם)

    Returns:
         float: משך הזמן הכולל של תבנית הקצב בשניות.
    """
    pattern_duration = 0
    for value in note_values:
       pattern_duration += bar_length * value
    return pattern_duration

def calculate_note_number(frequency, concert_a_freq=440.0):
    """
    מחשב את מספר התו בסולם הכרומטי על בסיס תדר.

    Args:
        frequency (float): תדר התו בהרץ.
        concert_a_freq (float, optional): תדר התו A4. ברירת מחדל היא 440.0.

    Returns:
        int: מספר התו ביחס ל-A4 (A4 = 0).
    """
    return round(12 * math.log2(frequency / concert_a_freq))

def generate_scale_frequencies(root_note_number, scale_pattern, concert_a_freq=440.0):
    """
    מייצר את תדרי התווים של סולם נתון.

    Args:
        root_note_number (int): מספר תו השורש.
        scale_pattern (list): תבנית הסולם (רצף חצאי טונים).
        concert_a_freq (float, optional): תדר התו A4. ברירת מחדל היא 440.0.

    Returns:
        list: רשימה של תדרי התווים בסולם.
    """
    frequencies = []
    current_note = root_note_number
    for interval in scale_pattern:
        frequencies.append(calculate_frequency(current_note, concert_a_freq))
        current_note += interval
    return frequencies

def calculate_tuning_deviation(target_frequency, actual_frequency):
    """
    מחשב את סטיית התדר מהתדר המטרה באחוזים.

    Args:
        target_frequency (float): תדר המטרה.
        actual_frequency (float): התדר בפועל.

    Returns:
        float: אחוז הסטייה.
    """
    return ((actual_frequency - target_frequency) / target_frequency) * 100

def get_note_name(note_number):
    """
    מחזיר את שם התו לפי מספרו בסולם הכרומטי.

    Args:
        note_number (int): מספר התו ביחס ל-A4 (A4 = 0).

    Returns:
        str: שם התו (לדוגמה: "A4", "C#5", "Bb3").
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    octave = (note_number // 12) + 4  # A4 היא 0, לכן מוסיפים 4
    note_index = note_number % 12
    return f"{notes[note_index]}{octave}"

def get_note_info_from_freq(freq):
    """
    מציג מידע על תו לפי תדר.

    Args:
        freq (float): תדר התו בהרץ.
    """
    note_num = calculate_note_number(freq)
    note_name = get_note_name(note_num)
    print(f"תדר {freq:.2f} הרץ, מתאים לתו {note_name}, מספר {note_num}")


def tune_instrument(target_freq, actual_freq):
    """
    מציג מידע על מידת הסטייה של כלי נגינה מתדר מטרה.

    Args:
        target_freq (float): תדר המטרה.
        actual_freq (float): התדר בפועל.
    """
    dev = calculate_tuning_deviation(target_freq, actual_freq)
    if dev > 0:
        print(f"גבוה ב- {dev:.2f}%. צריך להנמיך.")
    elif dev < 0:
        print(f"נמוך ב- {abs(dev):.2f}%. צריך להגביה.")
    else:
        print("מכוון באופן מושלם!")

def note_name_to_number(note_name):
    """
    ממיר שם תו (לדוגמה: "A4") למספר ביחס ל-A4 (A4 = 0).

    Args:
        note_name (str): שם התו (לדוגמה: "A4", "C#5", "Bb3").

    Returns:
        int: מספר התו ביחס ל-A4 (A4 = 0), או None אם הקלט לא תקין.
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    match = re.match(r"([A-Ga-g]#?)(-?\d+)", note_name)
    if not match:
        return None
    note = match.group(1).upper()
    octave = int(match.group(2))

    try:
        note_index = notes.index(note)
    except ValueError:
        return None

    return (octave - 4) * 12 + note_index

def find_nearest_notes(frequency, concert_a_freq=440.0):
    """
    מוצא את שני התווים הקרובים ביותר (מלמעלה ומלמטה) לתדר נתון.

    Args:
        frequency (float): תדר התו בהרץ.
        concert_a_freq (float, optional): תדר התו A4. ברירת מחדל היא 440.0.

    Returns:
      tuple: זוג (שם התו התחתון, שם התו העליון).
    """
    note_number = 12 * math.log2(frequency / concert_a_freq)
    lower_note_num = math.floor(note_number)
    upper_note_num = math.ceil(note_number)

    lower_note_name = get_note_name(lower_note_num)
    upper_note_name = get_note_name(upper_note_num)
    return lower_note_name, upper_note_name
def print_musical_examples():
    """
    מציג דוגמאות לשימוש בפונקציות.
    """
    print("---------------------------------------------------------")
    print("דוגמאות לחישוב תדרי תווים:")
    print(f"תדר התו A4: {calculate_frequency(0):.2f} הרץ")
    print(f"תדר התו C5: {calculate_frequency(3):.2f} הרץ")  # C5 נמצא 3 חצאי טונים מעל A4
    print(f"תדר התו A3: {calculate_frequency(-12):.2f} הרץ") # A3 נמצא 12 חצאי טונים מתחת A4
    print("---------------------------------------------------------")
    print("דוגמאות לחישוב מרווחים:")
    print(f"יחס התדרים בין A4 ל-C5: {calculate_interval_ratio(0, 3)}")
    print(f"יחס התדרים בין A4 ל-A5: {calculate_interval_ratio(0, 12)}")
    print(f"יחס התדרים בין C4 ל-G4: {calculate_interval_ratio(-9, -2)}")
    print("---------------------------------------------------------")
    print("דוגמאות לחישוב משכי תווים:")
    print(f"משך תו רבע בטמפו 120 BPM: {calculate_note_duration(120, 0.25):.3f} שניות.")
    print(f"משך תו חצי בטמפו 60 BPM: {calculate_note_duration(60, 0.5):.3f} שניות.")
    print(f"משך תו שלם בטמפו 100 BPM: {calculate_note_duration(100, 1):.3f} שניות.")
    print("---------------------------------------------------------")
    print("דוגמה לחישוב משך זמן כולל של קטע מוזיקלי:")
    print(f"משך 4 תיבות 4/4 ב-120BPM: {calculate_tempo_duration(120, 0.5, 16):.3f} שניות")
    print("---------------------------------------------------------")
    print("דוגמה לחישוב משך תבנית קצב:")
    print(f"משך מקצב 4/4 עם תווים [0.25, 0.25, 0.5]: {calculate_rhythm_pattern(1, [0.25, 0.25, 0.5]):.2f} תווים שלמים")
    print(f"משך מקצב 2/4 עם תווים [0.125, 0.125, 0.25]: {calculate_rhythm_pattern(0.5, [0.125, 0.125, 0.25]):.2f} תווים שלמים")
    print("---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("דוגמה לזיהוי מספר תו לפי תדר:")
    freq_example = 440.0
    note_number_example = calculate_note_number(freq_example)
    print(f"מספר תו עבור תדר {freq_example:.2f} הרץ: {note_number_example} (A4=0)")
    freq_example = 261.63
    note_number_example = calculate_note_number(freq_example)
    print(f"מספר תו עבור תדר {freq_example:.2f} הרץ: {note_number_example} (C4=-9)")
    print("---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("דוגמה ליצירת תדרי סולם:")
    major_scale = [2, 2, 1, 2, 2, 2, 1]  # תבנית סולם מז'ור
    c_major_freqs = generate_scale_frequencies(-9, major_scale) # C4 = -9
    print("תדרי תווים בסולם מז'ור מ-C4 (C, D, E, F, G, A, B):")
    for freq in c_major_freqs:
        print(f"{freq:.2f} הרץ", end=", ")
    print("\n---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("דוגמה לחישוב סטייה מתדר מטרה:")
    target_freq = 440.0
    actual_freq = 442.0
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    print(f"סטייה של {actual_freq:.2f} הרץ מ- {target_freq:.2f} הרץ: {deviation:.2f}%")
    target_freq = 261.63
    actual_freq = 260
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    print(f"סטייה של {actual_freq:.2f} הרץ מ- {target_freq:.2f} הרץ: {deviation:.2f}%")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("דוגמה לזיהוי מידע על תו:")
    get_note_info_from_freq(440.0)
    get_note_info_from_freq(329.63)
    print("---------------------------------------------------------")
    print("דוגמה לשימוש בטיונר:")
    tune_instrument(440.0,438.0)
    tune_instrument(261.63, 262.0)
    tune_instrument(440.0, 440.0)
    print("---------------------------------------------------------")

if __name__ == "__main__":
    print_musical_examples()

    # דוגמאות עם קלט משתמש (מחוץ לפונקציה print_musical_examples):
    print("\n--- דוגמאות עם קלט משתמש ---")