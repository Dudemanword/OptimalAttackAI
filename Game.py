from Player import Player
from Enemy import Enemy
from GameLog import GameLog
from Result import Result
from Attacks import Attacks
from typing import List,Tuple
import random

class Game:
    __INITAL_ENEMY_HEALTH = 120

    def __init__(self, enemy = None, player = None, enemyHealth = None):
        health = self.__INITAL_ENEMY_HEALTH if enemyHealth == None else enemyHealth
        self.__enemy = Enemy(health) if enemy == None else enemy
        self.__player = Player(strongAttackDamageValue=30, weakAttackDamageValue=10) if player == None else player
              

    def performAttacks(self, attacks:List[Attacks]) -> Result:
        for attack in attacks:
            if attack == Attacks.StrongAttack:
                damage = self.__player.PerformStrongAttack()
            elif attack == Attacks.WeakAttack:
                damage = self.__player.PerformWeakAttack()
            self.__enemy.TakeDamage(damage)
        if self.__enemy.health > 0:
            return Result.FAILURE
        else:
            return Result.SUCCESS

                