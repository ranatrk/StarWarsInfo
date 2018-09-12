import requests, sys, getopt, pprint
import species as species
import person as person

# prompt user to input the character name they want their details for
def get_char_from_user_input():
  character = input("Please enter a character name\n")
  # print("user input : " ,character)
  return character

# using the URI given of a certain world , the world name is retrieved and returned from the API
def get_world(session, uri):
  if uri is None:
    return
  world = session.get(uri).json()
  if world is not None:
    result_world = world['name']
  return result_world

# using the URI given of a certain species , the species details are retrieved and returned from the API
def get_species(session, uri):
  if uri is None:
    return
  one_species = session.get(uri).json()

  if one_species is not None:
    species_obj = species.Species(one_species['name'],one_species['average_lifespan'],get_world(session, one_species['homeworld']))
    return species_obj

# using the URI given of a film, the film name is retrieved and returned from the API
def get_film(session, uri):
  if uri is None:
    return
  film = session.get(uri).json()
  if film is not None:
    result_film = film['title']
  return result_film

def get_person(character_name):
  """
  Given a character name  , the person details are retrieved and returned from the API. Multiple API calls are used accordingly
  """
  base_url = "https://swapi.co/api/people/?search="
  session = requests.Session()

  one_person = session.get(base_url+character_name).json()['results']
  # one_person =   next((person for person in all_people["results"] if person['name'] == character_name), None)
  if one_person is not None and len(one_person)>0 :
    one_person = one_person[0]
    person_obj = person.Person(one_person['name'], one_person['gender'])
    if one_person['species'] is not None:
      for single_species in one_person['species']:
        retrieved_species = get_species(session,single_species)
        person_obj.add_species(retrieved_species)
    if one_person['films'] is not None:
      for film in one_person['films']:
        retrieved_film = get_film(session,film)
        person_obj.add_film(retrieved_film)
    return person_obj
  # return result_person



#Using inline arguments as input
cmd_arguments = sys.argv
input_arguments = cmd_arguments[1:]
unixOptions = "h:n"
gnuOptions = ["help", "name="]

try:
    arguments, values = getopt.getopt(input_arguments, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

for currentArgument, currentValue in arguments:
  if currentArgument in ("-h", "--help"):
      print ("displaying help")
  elif currentArgument in ("-n", "--name"):
      print (("Fetching character details for (%s)") % (currentValue))
      character_name = currentValue

#If character name was not written in the command, the user is prompted to input it to retrieve the character details
if(len(sys.argv) == 1):
  character_name = get_char_from_user_input()
person_details = get_person(character_name)
print(person_details)


