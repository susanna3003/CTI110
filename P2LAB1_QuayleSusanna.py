gasMileage = float(input('')) 

gasCost = float(input(''))

distance1 = 20
distance2 = 75
distance3 = 500

distanceCost1 = distance1 / gasMileage * gasCost
distanceCost2 = distance2 / gasMileage * gasCost
distanceCost3 = distance3 / gasMileage * gasCost

print(f'{distanceCost1:.2f} {distanceCost2:.2f} {distanceCost3:.2f}')

