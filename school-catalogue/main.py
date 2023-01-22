class School:
    initialStudents = 1

    def __init__(self, name, level, numberOfStudents):
        self.name = name
        if level not in ["primary", "middle", "high"]:
            raise ValueError(f"\nGot {level}: expected primary," f" middle, or high")
        self.level = level
        if not (isinstance(numberOfStudents, int) and numberOfStudents > 0):
            raise ValueError(
                f"\npositive number of students expected," f" got {numberOfStudents}"
            )
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_NumOfStudents(self):
        return self.numberOfStudents

    def set_NumOfStudents(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents

    def __repr__(self):
        return "A {} school named {} with {} students.".format(
            self.level, self.name, self.numberOfStudents
        )


class Primary(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name=name, level="primary", numberOfStudents=numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + " The pickup policy is {pickupPolicy}".format(
            pickupPolicy=self.pickupPolicy
        )

    def getPickupPolicy(self):
        return self.pickupPolicy


class Middle(School):
    def __init__(self, name, numberOfStudents):
        super().__init__(name=name, level="middle", numberOfStudents=numberOfStudents)


class High(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name=name, level="high", numberOfStudents=numberOfStudents)
        self.sportsTeams = sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + " The school's sports teams are {sportsTeams}".format(
            sportsTeams=self.sportsTeams
        )

    def getSportsTeams(self):
        return self.sportsTeams


a = School("Codecademy", "high", 100)
print(a)
# print(a.get_name())
# print(a.get_level())
# a.set_NumOfStudents(200)
# print(a.get_NumOfStudents())

# b = Primary("Codecademy", 300, "Pickup Allowed")
# # print(b.getPickupPolicy())
# print(repr(b))

# c = High("Codecademy High", 500, ["Tennis", "Basketball"])
# print(c.getSportsTeams())
# print(c)
