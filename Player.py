class Player:
    strongAttackDamage:int = 22
    weakAttackDamage:int = 15

    def __init__(self, strongAttackDamageValue:int = 22, weakAttackDamageValue:int = 15):
        self.strongAttackDamage = strongAttackDamageValue
        self.weakAttackDamage = weakAttackDamageValue

    def PerformStrongAttack(self) -> int:
        return self.strongAttackDamage

    def PerformWeakAttack(self) -> int:
        return self.weakAttackDamage