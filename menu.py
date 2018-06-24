import constants

def printRecipes(recipes):
	for recipe in recipes:
		print("\t"+recipe+" à la Cube:")
		for quality in recipes[recipe]:
			print("\t\t"+constants.INVERSE_QUALITY[quality]+":")
			for ingredient in recipes[recipe][quality]:
				print("\t\t\t"+constants.INVERSE_INGREDIENT[ingredient]+":",recipes[recipe][quality][ingredient])
		print()

def getPossibleRecipes(userIngredients, quantity):
	possibleRecipes = {}
	canMake = 1
	for recipe in constants.RECIPES:
		for quality in constants.RECIPES[recipe]:
			canMake = 1
			for ingredient in constants.RECIPES[recipe][quality]:
				if userIngredients[constants.INVERSE_INGREDIENT[ingredient]] < constants.RECIPES[recipe][quality][ingredient]*quantity:
					canMake = 0
			if canMake == 1:
				try:
					possibleRecipes[recipe][quality] = constants.RECIPES[recipe][quality]
				except KeyError:
					possibleRecipes[recipe] = {}
					possibleRecipes[recipe][quality] = constants.RECIPES[recipe][quality]
	return possibleRecipes

def getIngredientQuantities():
	userIngredients = {}
	print("Enter ingredient quantities:")
	userIngredients["Tiny Mushroom"] = int(input("Tiny Mushrooms: "))
	userIngredients["Bluk Berry"] = int(input("Bluk Berries: "))
	userIngredients["Apricorn"] = int(input("Apricorns: "))
	userIngredients["Fossil"] = int(input("Fossils: "))
	userIngredients["Big Root"] = int(input("Big Roots: "))
	userIngredients["Icy Rock"] = int(input("Icy Rocks: "))
	userIngredients["Honey"] = int(input("Honey: "))
	userIngredients["Balm Mushroom"] = int(input("Balm Mushrooms: "))
	userIngredients["Rainbow Matter"] = int(input("Rainbow Matter: "))
	return userIngredients

def main():
	userIngredients = getIngredientQuantities()
	print("\nNormal Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.POT["Normal"]))
	print("\nBronze Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.POT["Bronze"]))
	print("\nSilver Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.POT["Silver"]))
	print("\nGold Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.POT["Gold"]))

if __name__ == "__main__":
	main()
