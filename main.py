
INGREDIENT = {"TinyMushroom":0,"BlukBerry":1,"Apricorn":2,"Fossil":3,"BigRoot":4,"IcyRock":5,"Honey":6,"BalmMushroom":7,"RainbowMatter":8,"MysticalShell":9}
QUALITY = {"Normal":0,"Good":1,"VeryGood":2,"Special":3}
RECIPES = {
	"MulliganStew":{
		QUALITY["Special"]:{
			INGREDIENT["RainbowMatter"]:5
		}
	},
	"RedStew":{
		QUALITY["Normal"]:{
			INGREDIENT["TinyMushroom"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["BigRoot"]:5
		}
	},
	"BlueSoda":{
		QUALITY["Normal"]:{
			INGREDIENT["BlukBerry"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["IcyRock"]:5
		}
	},
	"YellowCurry":{
		QUALITY["Normal"]:{
			INGREDIENT["Apricorn"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["Honey"]:5
		}
	},
	"GreyPorridge":{
		QUALITY["Normal"]:{
			INGREDIENT["Fossil"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["BalmMushroom"]:5
		}
	},
}

def printRecipes():
	for recipe in RECIPES:
		print(recipe+":")
		for quality in RECIPES[recipe]:
			for reverseQuality in QUALITY:
				if(quality==QUALITY[reverseQuality]):
					print("\t"+reverseQuality+":")
			for ingredient in RECIPES[recipe][quality]:
				for reverseIngredient in INGREDIENT:
					if(ingredient==INGREDIENT[reverseIngredient]):
						print("\t\t"+reverseIngredient+":",RECIPES[recipe][quality][ingredient])
		print()

def main():
	printRecipes()

if __name__ == "__main__":
	main()