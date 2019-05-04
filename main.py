from Game import Game
from Attacks import Attacks
import random

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

NUMBER_OF_TRAINING_ITERATIONS = 10000
NUMBER_OF_TESTING_ITERATIONS = 60000

def GenerateData(numberOfIterations: int):
    trainingAttackSet = []
    trainingResultSet = []
    for iteration in range(1, numberOfIterations):
        attacks = []
        trainingGame = Game()
        for numberOfAttacks in range(0, 5):
            attackDeterminator = random.randint(0, 1)
            if attackDeterminator == 0:
                attacks.append(Attacks.StrongAttack)
            elif attackDeterminator == 1:
                attacks.append(Attacks.WeakAttack)
        result = trainingGame.performAttacks(attacks)
        attackSetValues = [attack.value for attack in attacks]
        resultSetValues = result.value
        trainingAttackSet.append(attackSetValues)
        trainingResultSet.append(resultSetValues)

    return (trainingAttackSet, trainingResultSet)


(trainingAttackSet, trainingResultSet) = GenerateData(NUMBER_OF_TRAINING_ITERATIONS)
(testAttackSet, testResults) = GenerateData(NUMBER_OF_TESTING_ITERATIONS)

model = keras.Sequential([
    keras.layers.Dense(3, activation=tf.nn.relu, input_shape = (5,)),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(np.array(trainingAttackSet), np.array(trainingResultSet), epochs=5, steps_per_epoch=1000)
test_loss, test_acc = model.evaluate(np.array(testAttackSet), np.array(testResults))
print('Test accuracy:', test_acc)


