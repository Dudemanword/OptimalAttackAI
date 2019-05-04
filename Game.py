from Player import Player
from Enemy import Enemy
from GameLog import GameLog
from Result import Result
import random

INITAL_ENEMY_HEALTH = 120

mainPlayer = Player(strongAttackDamageValue=30, weakAttackDamageValue=10)

logs = []
for iterator in range(0, 10):
    badGuy = Enemy(INITAL_ENEMY_HEALTH)
    log = GameLog(INITAL_ENEMY_HEALTH)
    while(log.numberOfActions < 5):
        randomAction = random.randint(0, 2)
        if randomAction == 0:
            damage = mainPlayer.PerformWeakAttack()
            log.actionsTaken.append("Weak Attack, ")
        else:
            damage = mainPlayer.PerformStrongAttack()
            log.actionsTaken.append("Strong Attack, ")

        badGuy.TakeDamage(damage)

        log.damageDone += damage
        log.numberOfActions += 1
        log.remainingEnemyHealth = badGuy.health
    if(log.remainingEnemyHealth < 0):
        log.finalResult = Result.SUCCESS
    else:
        log.finalResult = Result.FAILURE

    logs.append(log)

print ("Hello")
