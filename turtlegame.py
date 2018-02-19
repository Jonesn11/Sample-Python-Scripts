from turtle import *
orient = 18
turnDegree = 144
steps = 60

def changeOrient(orient):
    orient += 35
    return orient

def changeTurnDegree(turnDegree):
    turnDegree += 72
    return turnDegree

def moveForward(steps):
    return forward(steps)

def changeDirection(degree):
    return right(degree)

def refactorDegree(degree):
    if degree >= 360:
        degree -= 360
        return degree
    else:
        return degree

for x in range(5):
    if x == 0:
        pass
    elif x > 0:
        orient = refactorDegree(changeOrient(orient))
        turnDegree = refactorDegree(changeTurnDegree(turnDegree))
        changeDirection(orient)
    changeDirection(orient)
    for x in range(5):
        moveForward(steps)
        changeDirection(turnDegree)
