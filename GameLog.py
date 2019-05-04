from Result import Result
class GameLog:
    #action taken, damage done, remaining health left, number of actions
    def __init__(self, initialEnemyHealth):
        self.__remainingHealth = initialEnemyHealth
        self.__actionsTaken = []
        self.__damageDone = 0
        self.__numberOfActions = 0
        self.__finalResult = Result.FAILURE

    @property
    def actionsTaken(self):
        return self.__actionsTaken

    @property
    def damageDone(self):
        return self.__damageDone

    @property
    def remainingEnemyHealth(self):
        return self.__remainingHealth

    @property
    def numberOfActions(self):
        return self.__numberOfActions

    @property
    def finalResult(self):
        return self.__finalResult

    @damageDone.setter
    def damageDone(self, damageDone):
        self.__damageDone = damageDone
        return self.damageDone    
    
    @actionsTaken.setter
    def actionsTaken(self, actionsTaken):
        self.__actionsTaken = actionsTaken
        return self.__actionsTaken

    @remainingEnemyHealth.setter
    def remainingEnemyHealth(self, remainingEnemyHealth):
        self.__remainingHealth = remainingEnemyHealth
        return self.__remainingHealth

    @numberOfActions.setter
    def numberOfActions(self, numberOfActions):
        self.__numberOfActions = numberOfActions
        return self.__numberOfActions
    
    @finalResult.setter
    def finalResult(self, finalResult):
        self.__finalResult = finalResult
        return self.__finalResult

    