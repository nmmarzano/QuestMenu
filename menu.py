import constants

def printRecipes(recipes):
	for recipe in recipes:
		print("\t"+recipe+" à la Cube:")
		for quality in recipes[recipe]:
			print("\t\t"+quality+":")
			for ingredient in recipes[recipe][quality]:
				print("\t\t\t"+ingredient+":",recipes[recipe][quality][ingredient])
		print()

def getPossibleRecipes(userIngredients, quantity):
	possibleRecipes = {}
	canMake = 1
	for recipe in constants.RECIPES:
		for quality in constants.RECIPES[recipe]:
			canMake = 1
			for ingredient in constants.RECIPES[recipe][quality]:
				if userIngredients[ingredient] < constants.RECIPES[recipe][quality][ingredient]*quantity:
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
	userIngredients[constants.ingredient.tinyMushroom] = int(input("Tiny Mushrooms: "))
	userIngredients[constants.ingredient.blukBerry] = int(input("Bluk Berries: "))
	userIngredients[constants.ingredient.apricorn] = int(input("Apricorns: "))
	userIngredients[constants.ingredient.fossil] = int(input("Fossils: "))
	userIngredients[constants.ingredient.bigRoot] = int(input("Big Roots: "))
	userIngredients[constants.ingredient.icyRock] = int(input("Icy Rocks: "))
	userIngredients[constants.ingredient.honey] = int(input("Honey: "))
	userIngredients[constants.ingredient.balmMushroom] = int(input("Balm Mushrooms: "))
	userIngredients[constants.ingredient.rainbowMatter] = int(input("Rainbow Matter: "))
	return userIngredients

def main():
	userIngredients = getIngredientQuantities()
	print("\nNormal Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.potQuantity.normal))
	print("\nBronze Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.potQuantity.bronze))
	print("\nSilver Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.potQuantity.silver))
	print("\nGold Pot:")
	printRecipes(getPossibleRecipes(userIngredients, constants.potQuantity.gold))

if __name__ == "__main__":
	main()
