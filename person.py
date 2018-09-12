import species as species

class Person():
  """
  Class stores details of the character that have been recieved from the API
  """

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender
    self.species = list()
    self.films = list()

  def __str__(self):
    species_str = "\nSpecies:\n"
    films_str = "\nFilms:\n"
    for s in self.species:
      species_str += str(s) +"\n"
    for f in self.films:
      films_str += f + "\n"

    value_str = "Name:" + self.name + "\nGender: " + self.gender + "\n" + species_str + films_str
    # return  str(vars(self))
    return value_str

  def __repr__(self):
    return self.__str__()

  def add_species(self,new_species):
    """
    Adding a species object to the species list of the person
    """
    self.species.append(new_species)

  def add_film(self,film):
    """
    Add a film/movie the person appeared in to the list of films they have appeared in
    """
    self.films.append(film)




