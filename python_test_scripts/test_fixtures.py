import pytest
# ---->
# class Fruit:
#     def __init__(self, name):
#         self.name = name 

#     def __eq__(self, other):
#         return self.name == other.name

# @pytest.fixture
# def my_fruit():
#     return Fruit("apple")

# @pytest.fixture
# def fruit_basket(my_fruit):
#     return [Fruit("banana"), my_fruit]

# def test_my_fruit_in_basket(my_fruit, fruit_basket):
#     assert my_fruit in fruit_basket
# ---->

# ---->
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

@pytest.mark.skip
def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
# ---->
