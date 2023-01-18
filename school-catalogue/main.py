class School():
  initialStudents = 1
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
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
    return 'A {} school named {} with {} students.'.format(
      self.level, 
      self.name, 
      self.numberOfStudents
                  )

