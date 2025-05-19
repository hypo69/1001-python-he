import random

class Tank:
    """
    מחלקה בסיסית לטנקים.
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        אתחול טנק.
         
        Args:
            model: דגם הטנק.
            armor: שריון הטנק.
            min_damage: נזק מינימלי של הטנק.
            max_damage: נזק מקסימלי של הטנק.
            health: בריאות הטנק.
        """
        self.model = model
        self.armor = armor
        self.min_damage = min_damage  # שומרים את הנזק המינימלי
        self.max_damage = max_damage  # שומרים את הנזק המקסימלי
        self.health = health
        
    def calculate_damage(self) -> int:
        """
        מחשב נזק אקראי של הטנק בטווח הנתון.

        Returns:
             נזק אקראי.
        """
        return random.randint(self.min_damage, self.max_damage)

    def print_info(self) -> None:
        """
        מדפיס מידע על הטנק.
        """
        print(f"{self.model} בעל שריון קדמי {self.armor}מ\"מ עם {self.health} נקודות בריאות ונזק בטווח מ-{self.min_damage} עד {self.max_damage} יחידות")

    def health_down(self, enemy_damage: int) -> None:
        """
        מפחית את בריאות הטנק.
        
        Args:
             enemy_damage: נזק שנגרם על ידי היריב.
        """
        self.health -= enemy_damage
        print(f"\n{self.model}:")
        print(f"מפקד, צוות ה-{self.model} נפגע, נותרו לנו {self.health} נקודות בריאות")

    def shot(self, enemy: object) -> None:
        """
        הטנק יורה על היריב.
        
        Args:
            enemy: טנק יריב.
        """
        damage = self.calculate_damage() # מחשבים את הנזק
        if enemy.health <= 0 :
             print(f"צוות טנק {enemy.model} כבר הושמד")
        elif damage >= enemy.health:
            enemy.health = 0
            print(f"\n{self.model}:")
            print(f"צוות טנק {enemy.model} הושמד")
        else:
            enemy.health_down(damage)
            print(f"\n{self.model}:")
            print(f"פגיעה ישירה, ליריב {enemy.model} נותרו {enemy.health} נקודות בריאות")


class SuperTank(Tank):
    """
    מחלקה לסופר-טנק, יורשת מ-Tank.
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        אתחול סופר-טנק.
        
        Args:
            model: דגם הטנק.
            armor: שריון הטנק.
            min_damage: נזק מינימלי של הטנק.
            max_damage: נזק מקסימלי של הטנק.
            health: בריאות הטנק.
        """
        super().__init__(model, armor, min_damage, max_damage, health)
        self.forceArmor = True

    def health_down(self, enemy_damage: int) -> None:
        """
        מפחית את בריאות הסופר-טנק בהתחשב בשריון המשופר.
        
        Args:
            enemy_damage: נזק שנגרם על ידי היריב.
        """
        effective_damage = max(0, enemy_damage - self.armor // 2) # מפחיתים את הנזק בהתאם לשריון
        self.health -= effective_damage
        print(f"\n{self.model}:")
        print(f"מפקד, צוות ה-{self.model} נפגע, נותרו לנו {self.health} נקודות בריאות")

def main():
    """
    הפונקציה הראשית של המשחק.
    """
    tank1 = Tank("Т-34", 50, 20, 30, 100)
    tank2 = SuperTank("Тигр", 80, 25, 35, 150)

    print("מתחיל קרב טנקים!")
    tank1.print_info()
    tank2.print_info()

    current_tank = tank1
    enemy_tank = tank2

    while tank1.health > 0 and tank2.health > 0:
        current_tank.shot(enemy_tank)
        current_tank, enemy_tank = enemy_tank, current_tank  # החלפת תור

    if tank1.health <= 0:
        print(f"\nניצח {tank2.model}!")
    else:
        print(f"\nניצח {tank1.model}!")

if __name__ == "__main__":
    main()