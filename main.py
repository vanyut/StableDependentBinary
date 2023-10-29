# class a:
#     total_a = 0

#     def __init__(self, name, swim=False, fly=False, walk=True):
#         self.name = name
#         self.can_swim = swim
#         self.can_fly = fly
#         self.can_walk = walk


# def swim(self):
#     if self.can_swim:
#         return f"{self.name} can swim"
#     else:
#         return f"{self.name} can't swim"

# def fly(self):
#     if self.can_fly:
#         return f"{self.name} can fly"
#     else:
#         return f"{self.name} can't fly"

# def walk(self):
#     if self.can_walk:
#         return f"{self.name} can walk"
#     else:
#         return f"{self.name} can't walk"


# tiger = a("tiger" , swim=True, fly=False, walk=True)
# butterfly = a("butterfly" , swim=False, fly=True, walk=False)
# monkey = a("monkey" , swim=False, fly=False, walk=True)


# print(tiger.can_swim)
# print(butterfly.can_fly)
# print(monkey.can_walk)


# print(f"animal in the zoo: {a.total_a}")



import random


def rand_bool():
    Value = random.randint(0, 1)
    if Value == 0:
        return False
    elif Value == 1:
        return True
    else:
        print("error")


class car:

    def __init__(self, model, color, engine_type, servo_type):
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.servo_type = servo_type


    def Break(self):
        Value = random.randint(1, 2)
        if Value == 1:
            print(f"{self.model} has broken its {self.EngineType} Engine"})

            elif Value == 2:

                print(f"{self.model} has broken its {self.ServoType} Servo")


    def Drive(self):
        print(f"")