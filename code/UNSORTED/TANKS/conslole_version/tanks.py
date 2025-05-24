import random

class Tank:
    """
    מחלקת בסיס לטנקים.
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        אתחול הטנק.
         
        Args:
            model: דגם הטנק.
            armor: שריון הטנק.
            min_damage: נזק מינימלי של הטנק.
            max_damage: נזק מקסימלי של הטנק.
            health: בריאות הטנק.
        """
        self.model = model
        self.armor = armor
        self.min_damage = min_damage  # שמירת הנזק המינימלי
        self.max_damage = max_damage  # שמירת הנזק המקסימלי
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
        print(f"{self.model} בעל שריון קדמי של {self.armor}מ\"מ עם {self.health} נקודות בריאות ונזק בטווח שבין {self.min_damage} ל-{self.max_damage} יחידות")

    def health_down(self, enemy_damage: int) -> None:
        """
        מפחית את בריאות הטנק.
        
        Args:
             enemy_damage: נזק שנגרם על ידי היריב.
        """
        self.health -= enemy_damage
        print(f"\n{self.model}:")
        print(f"מפקד, צוות {self.model} נפגע, נותרו לנו {self.health} נקודות בריאות")

    def shot(self, enemy: object) -> None:
        """
        הטנק יורה ביריב.
        
        Args:
            enemy: טנק-יריב.
        """
        damage = self.calculate_damage() # חישוב הנזק
        if enemy.health <= 0 :
             print(f"צוות הטנק {enemy.model} כבר הושמד")
        elif damage >= enemy.health:
            enemy.health = 0
            print(f"\n{self.model}:")
            print(f"צוות הטנק {enemy.model} הושמד")
        else:
            enemy.health_down(damage)
            print(f"\n{self.model}:")
            print(f"פגיעה מדויקת, ליריב {enemy.model} נותרו {enemy.health} יחידות בריאות")


class SuperTank(Tank):
    """
    מחלקה לסופר-טנק, יורשת מ-Tank.
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        אתחול הסופר-טנק.
        
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
        מפחית את בריאות הסופר-טנק תוך התחשבות בשריון המשופר.
        
        Args:
            enemy_damage: נזק שנגרם על ידי היריב.
        """
        effective_damage = max(0, enemy_damage - self.armor // 2) # הפחתת הנזק בהתאם לשריון
        self.health -= effective_damage
        print(f"\n{self.model}:")
        print(f"מפקד, צוות {self.model} נפגע, נותרו לנו {self.health} נקודות בריאות")

def main():
    """
    פונקציית המשחק הראשית.
    """
    tank1 = Tank("Т-34", 50, 20, 30, 100)
    tank2 = SuperTank("Тигр", 80, 25, 35, 150)

    print("קרב הטנקים מתחיל!")
    tank1.print_info()
    tank2.print_info()

    current_tank = tank1
    enemy_tank = tank2

    while tank1.health > 0 and tank2.health > 0:
        current_tank.shot(enemy_tank)
        current_tank, enemy_tank = enemy_tank, current_tank  # החלפת תור

    if tank1.health <= 0:
        print(f"\n{tank2.model} ניצח!")
    else:
        print(f"\n{tank1.model} ניצח!")

if __name__ == "__main__":
    main()