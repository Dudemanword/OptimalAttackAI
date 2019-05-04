class Enemy:
    __health = 100

    def __init__(self, health:int = 100):
            self.__health = health
    
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    def TakeDamage(self, damage:int):
        self.health -= damage
    
    def Heal(self, amountToHeal: int):
        self.health += amountToHeal