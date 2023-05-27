class Usertest:
  # allows us to skip over indents
  pass
usertest_1 = Usertest()
usertest_1.id = '001'


class User:
  def __init__(self, attribute) -> None:
    self.attribute = attribute
    print(f"new user being created...{self.attribute}")

# self has to be passed into class method
  def follow(self, user):
    self.attribute = user

