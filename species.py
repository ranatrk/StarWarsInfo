#class stores details of species that have been recieved from the API
class Species:

  def __init__(self,name=None,avg_lifespan=None,homeworld=None):
    self.name = name
    self.avg_lifespan = avg_lifespan
    self.homeworld = homeworld

  def __str__(self):
    return str(vars(self))

  def __repr__(self):
    return self.__str__()
