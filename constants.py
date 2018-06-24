class ingredient:
	tinyMushroom="Tiny Mushroom"
	blukBerry="Bluk Berry"
	apricorn="Apricorn"
	fossil="Fossil"
	bigRoot="Big Root"
	icyRock="Icy Rock"
	honey="Honey"
	balmMushroom="Balm Mushroom"
	rainbowMatter="Rainbow Matter"

class quality:
	normal="Normal"
	good="Good"
	veryGood="Very Good"
	special="Special"

class potQuantity:
	normal=3
	bronze=10
	silver=15
	gold=20

RECIPES = {
	"Red Stew":{
		quality.normal:{
			ingredient.tinyMushroom:5
		},
		quality.special:{
			ingredient.bigRoot:5
		}
	},
	"Blue Soda":{
		quality.normal:{
			ingredient.blukBerry:5
		},
		quality.special:{
			ingredient.icyRock:5
		}
	},
	"Yellow Curry":{
		quality.normal:{
			ingredient.apricorn:5
		},
		quality.special:{
			ingredient.honey:5
		}
	},
	"Grey Porridge":{
		quality.normal:{
			ingredient.fossil:5
		},
		quality.special:{
			ingredient.balmMushroom:5
		}
	},
	"Mouth-Watering Dip":{
		quality.normal:{
			ingredient.blukBerry:3,
			ingredient.tinyMushroom:2
		},
		quality.good:{
			ingredient.blukBerry:3,
			ingredient.apricorn:1,
			ingredient.honey:1
		},
		quality.veryGood:{
			ingredient.icyRock:1,
			ingredient.blukBerry:2,
			ingredient.honey:2
		}
	},
	"Plain Crepe":{
		quality.normal:{
			ingredient.blukBerry:3,
			ingredient.fossil:2
		},
		quality.good:{
			ingredient.blukBerry:2,
			ingredient.honey:1,
			ingredient.fossil:2
		},
		quality.veryGood:{
			ingredient.blukBerry:1,
			ingredient.honey:2,
			ingredient.balmMushroom:2
		},
		quality.special:{
			ingredient.honey:3,
			ingredient.balmMushroom:2
		}
	},
	"Sludge Soup":{
		quality.normal:{
			ingredient.tinyMushroom:3,
			ingredient.balmMushroom:2
		},
		quality.veryGood:{
			ingredient.tinyMushroom:2,
			ingredient.balmMushroom:3
		},
		quality.special:{
			ingredient.tinyMushroom:1,
			ingredient.balmMushroom:3,
			ingredient.rainbowMatter:1
		}
	},
	"Mud Pie":{
		quality.normal:{
			ingredient.tinyMushroom:3,
			ingredient.fossil:2
		},
		quality.good:{
			ingredient.tinyMushroom:3,
			ingredient.icyRock:2
		},
		quality.veryGood:{
			ingredient.icyRock:2,
			ingredient.honey:2,
			ingredient.blukBerry:1
		},
		quality.special:{
			ingredient.honey:3,
			ingredient.icyRock:2
		}
	},
	"Veggie Smoothie":{
		quality.normal:{
			ingredient.bigRoot:3,
			ingredient.balmMushroom:1,
			ingredient.apricorn:1
		},
		quality.good:{
			ingredient.apricorn:3,
			ingredient.tinyMushroom:1,
			ingredient.bigRoot:1
		},
		quality.veryGood:{
			ingredient.bigRoot:3,
			ingredient.apricorn:2
		},
		quality.special:{
			ingredient.bigRoot:3,
			ingredient.apricorn:1,
			ingredient.rainbowMatter:1
		}
	},
	"Honey Nectar":{
		quality.normal:{
			ingredient.honey:2,
			ingredient.blukBerry:2,
			ingredient.apricorn:1
		},
		quality.good:{
			ingredient.honey:3,
			ingredient.blukBerry:2
		},
		quality.veryGood:{
			ingredient.honey:3,
			ingredient.icyRock:1,
			ingredient.blukBerry:1
		},
		quality.special:{
			ingredient.honey:3,
			ingredient.blukBerry:1,
			ingredient.rainbowMatter:1
		}
	},
	"Brain Food":{
		quality.normal:{
			ingredient.blukBerry:3,
			ingredient.apricorn:2
		},
		quality.good:{
			ingredient.blukBerry:2,
			ingredient.apricorn:2,
			ingredient.honey:1
		},
		quality.veryGood:{
			ingredient.honey:2,
			ingredient.icyRock:1,
			ingredient.apricorn:1,
			ingredient.blukBerry:1
		}
	},
	"Stone Soup":{
		quality.normal:{
			ingredient.fossil:3,
			ingredient.apricorn:2
		},
		quality.good:{
			ingredient.apricorn:2,
			ingredient.fossil:2,
			ingredient.icyRock:1
		},
		quality.veryGood:{
			ingredient.fossil:1,
			ingredient.icyRock:3,
			ingredient.apricorn:1
		},
		quality.special:{
			ingredient.icyRock:3,
			ingredient.fossil:1,
			ingredient.rainbowMatter:1
		}
	},
	"Light-as-Air Casserole":{
		quality.normal:{
			ingredient.fossil:2,
			ingredient.bigRoot:2,
			ingredient.icyRock:1
		},
		quality.special:{
			ingredient.icyRock:3,
			ingredient.bigRoot:2
		}
	},
	"Hot Pot":{
		quality.normal:{
			ingredient.tinyMushroom:3,
			ingredient.blukBerry:2
		},
		quality.good:{
			ingredient.honey:2,
			ingredient.tinyMushroom:3
		},
		quality.special:{
			ingredient.balmMushroom:3,
			ingredient.bigRoot:2
		}
	},
	"Watt a Risotto":{
		quality.normal:{
			ingredient.honey:2,
			ingredient.tinyMushroom:2,
			ingredient.apricorn:1
		},
		quality.veryGood:{
			ingredient.honey:2,
			ingredient.balmMushroom:1,
			ingredient.bigRoot:1,
			ingredient.apricorn:1
		},
		quality.special:{
			ingredient.honey:3,
			ingredient.balmMushroom:1,
			ingredient.bigRoot:1
		}
	},
	"Get Swole Syrup":{
		quality.normal:{
			ingredient.honey:1,
			ingredient.blukBerry:2,
			ingredient.tinyMushroom:2
		},
		quality.good:{
			ingredient.blukBerry:2,
			ingredient.tinyMushroom:1,
			ingredient.honey:1,
			ingredient.balmMushroom:1
		},
		quality.veryGood:{
			ingredient.blukBerry:1,
			ingredient.tinyMushroom:1,
			ingredient.honey:2,
			ingredient.balmMushroom:1
		}
	}
}