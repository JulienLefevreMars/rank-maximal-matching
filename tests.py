from matching.games import HospitalResident
import numpy as np
import sys

def random_experience(num_residents, num_hospitals):
	np.random.seed()

	uniform_capacity = int(num_residents/num_hospitals)+1

	resident_prefs = {
		r: np.argsort(np.random.random(size=num_hospitals))
		for r in range(num_residents)
	}

	hospital_prefs = {
		h: np.argsort(np.random.random(size=num_residents))
		for h in range(num_hospitals)
	}

	capacities = {h: num_hospitals for h in hospital_prefs}
	capacities = {h: uniform_capacity for h in hospital_prefs}
	game = HospitalResident.create_from_dictionaries(resident_prefs, hospital_prefs, capacities)
	_ = game.solve() 
	return game,resident_prefs


def count_ranks(game,num_hospitals,resident_prefs):
	# Count the number of first choices, second choices etc

	count_choices = np.zeros((num_hospitals,))

	for i in range(num_hospitals):
		matched_residents = game.matching[game.hospitals[i]]
		for resident in matched_residents:
			pref = resident_prefs[resident.name]
			count_choices[np.where(pref == i)[0][0]] +=1
			
	return count_choices
	
	
if __name__ =="__main__":
	num_residents = int(sys.argv[1])
	num_hospitals = int(sys.argv[2])
	
	game,resident_prefs = random_experience(num_residents, num_hospitals)
	count_choices = count_ranks(game,num_hospitals,resident_prefs)
	print(count_choices)
