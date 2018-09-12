import species as species

class Person():

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
    self.species.append(new_species)

  def add_film(self,film):
    self.films.append(film)




