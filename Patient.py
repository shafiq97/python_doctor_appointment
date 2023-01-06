from Person import Person

# Inheritance concept
class Patient(Person):
  def __init__(self, age, race, height, weight, occupation, home_address, state, current_health_conditions, name, telephone_number, identity_number):
    super().init(name, telephone_number, identity_number)
    self.age = age
    self.race = race
    self.height = height
    self.weight = weight
    self.occupation = occupation
    self.home_address = home_address
    self.state = state
    self.current_health_conditions = current_health_conditions