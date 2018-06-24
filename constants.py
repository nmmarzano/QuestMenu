INGREDIENT = {"Tiny Mushroom":0,"Bluk Berry":1,"Apricorn":2,"Fossil":3,"Big Root":4,"Icy Rock":5,"Honey":6,"Balm Mushroom":7,"Rainbow Matter":8}
INVERSE_INGREDIENT = {INGREDIENT[k]:k for k in INGREDIENT}
QUALITY = {"Normal":0,"Good":1,"Very Good":2,"Special":3}
INVERSE_QUALITY = {QUALITY[k]:k for k in QUALITY}
POT = {"Normal":3,"Bronze":10,"Silver":15,"Gold":20}

RECIPES = {
	"Red Stew":{
		QUALITY["Normal"]:{
			INGREDIENT["Tiny Mushroom"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["Big Root"]:5
		}
	},
	"Blue Soda":{
		QUALITY["Normal"]:{
			INGREDIENT["Bluk Berry"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["Icy Rock"]:5
		}
	},
	"Yellow Curry":{
		QUALITY["Normal"]:{
			INGREDIENT["Apricorn"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["Honey"]:5
		}
	},
	"Grey Porridge":{
		QUALITY["Normal"]:{
			INGREDIENT["Fossil"]:5
		},
		QUALITY["Special"]:{
			INGREDIENT["Balm Mushroom"]:5
		}
	},
	"Mouth-Watering Dip":{
		QUALITY["Normal"]:{
			INGREDIENT["Bluk Berry"]:3,
			INGREDIENT["Tiny Mushroom"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Bluk Berry"]:3,
			INGREDIENT["Apricorn"]:1,
			INGREDIENT["Honey"]:1
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Icy Rock"]:1,
			INGREDIENT["Bluk Berry"]:2,
			INGREDIENT["Honey"]:2
		}
	},
	"Plain Crepe":{
		QUALITY["Normal"]:{
			INGREDIENT["Bluk Berry"]:3,
			INGREDIENT["Fossil"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Bluk Berry"]:2,
			INGREDIENT["Honey"]:1,
			INGREDIENT["Fossil"]:2
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Bluk Berry"]:1,
			INGREDIENT["Honey"]:2,
			INGREDIENT["Balm Mushroom"]:2
		},
		QUALITY["Special"]:{
			INGREDIENT["Honey"]:3,
			INGREDIENT["Balm Mushroom"]:2
		}
	},
	"Sludge Soup":{
		QUALITY["Normal"]:{
			INGREDIENT["Tiny Mushroom"]:3,
			INGREDIENT["Balm Mushroom"]:2
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Tiny Mushroom"]:2,
			INGREDIENT["Balm Mushroom"]:3
		},
		QUALITY["Special"]:{
			INGREDIENT["Tiny Mushroom"]:1,
			INGREDIENT["Balm Mushroom"]:3,
			INGREDIENT["Rainbow Matter"]:1
		}
	},
	"Mud Pie":{
		QUALITY["Normal"]:{
			INGREDIENT["Tiny Mushroom"]:3,
			INGREDIENT["Fossil"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Tiny Mushroom"]:3,
			INGREDIENT["Icy Rock"]:2
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Icy Rock"]:2,
			INGREDIENT["Honey"]:2,
			INGREDIENT["Bluk Berry"]:1
		},
		QUALITY["Special"]:{
			INGREDIENT["Honey"]:3,
			INGREDIENT["Icy Rock"]:2
		}
	},
	"Veggie Smoothie":{
		QUALITY["Normal"]:{
			INGREDIENT["Big Root"]:3,
			INGREDIENT["Balm Mushroom"]:1,
			INGREDIENT["Apricorn"]:1
		},
		QUALITY["Good"]:{
			INGREDIENT["Apricorn"]:3,
			INGREDIENT["Tiny Mushroom"]:1,
			INGREDIENT["Big Root"]:1
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Big Root"]:3,
			INGREDIENT["Apricorn"]:2
		},
		QUALITY["Special"]:{
			INGREDIENT["Big Root"]:3,
			INGREDIENT["Apricorn"]:1,
			INGREDIENT["Rainbow Matter"]:1
		}
	},
	"Honey Nectar":{
		QUALITY["Normal"]:{
			INGREDIENT["Honey"]:2,
			INGREDIENT["Bluk Berry"]:2,
			INGREDIENT["Apricorn"]:1
		},
		QUALITY["Good"]:{
			INGREDIENT["Honey"]:3,
			INGREDIENT["Bluk Berry"]:2
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Honey"]:3,
			INGREDIENT["Icy Rock"]:1,
			INGREDIENT["Bluk Berry"]:1
		},
		QUALITY["Special"]:{
			INGREDIENT["Honey"]:3,
			INGREDIENT["Bluk Berry"]:1,
			INGREDIENT["Rainbow Matter"]:1
		}
	},
	"Brain Food":{
		QUALITY["Normal"]:{
			INGREDIENT["Bluk Berry"]:3,
			INGREDIENT["Apricorn"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Bluk Berry"]:2,
			INGREDIENT["Apricorn"]:2,
			INGREDIENT["Honey"]:1
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Honey"]:2,
			INGREDIENT["Icy Rock"]:1,
			INGREDIENT["Apricorn"]:1,
			INGREDIENT["Bluk Berry"]:1
		}
	},
	"Stone Soup":{
		QUALITY["Normal"]:{
			INGREDIENT["Fossil"]:3,
			INGREDIENT["Apricorn"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Apricorn"]:2,
			INGREDIENT["Fossil"]:2,
			INGREDIENT["Icy Rock"]:1
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Fossil"]:1,
			INGREDIENT["Icy Rock"]:3,
			INGREDIENT["Apricorn"]:1
		},
		QUALITY["Special"]:{
			INGREDIENT["Icy Rock"]:3,
			INGREDIENT["Fossil"]:1,
			INGREDIENT["Rainbow Matter"]:1
		}
	},
	"Light-as-Air Casserole":{
		QUALITY["Normal"]:{
			INGREDIENT["Fossil"]:2,
			INGREDIENT["Big Root"]:2,
			INGREDIENT["Icy Rock"]:1
		},
		QUALITY["Special"]:{
			INGREDIENT["Icy Rock"]:3,
			INGREDIENT["Big Root"]:2
		}
	},
	"Hot Pot":{
		QUALITY["Normal"]:{
			INGREDIENT["Tiny Mushroom"]:3,
			INGREDIENT["Bluk Berry"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Honey"]:2,
			INGREDIENT["Tiny Mushroom"]:3
		},
		QUALITY["Special"]:{
			INGREDIENT["Balm Mushroom"]:3,
			INGREDIENT["Big Root"]:2
		}
	},
	"Watt a Risotto":{
		QUALITY["Normal"]:{
			INGREDIENT["Honey"]:2,
			INGREDIENT["Tiny Mushroom"]:2,
			INGREDIENT["Apricorn"]:1
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Honey"]:2,
			INGREDIENT["Balm Mushroom"]:1,
			INGREDIENT["Big Root"]:1,
			INGREDIENT["Apricorn"]:1
		},
		QUALITY["Special"]:{
			INGREDIENT["Honey"]:3,
			INGREDIENT["Balm Mushroom"]:1,
			INGREDIENT["Big Root"]:1
		}
	},
	"Get Swole Syrup":{
		QUALITY["Normal"]:{
			INGREDIENT["Honey"]:1,
			INGREDIENT["Bluk Berry"]:2,
			INGREDIENT["Tiny Mushroom"]:2
		},
		QUALITY["Good"]:{
			INGREDIENT["Bluk Berry"]:2,
			INGREDIENT["Tiny Mushroom"]:1,
			INGREDIENT["Honey"]:1,
			INGREDIENT["Balm Mushroom"]:1
		},
		QUALITY["Very Good"]:{
			INGREDIENT["Bluk Berry"]:1,
			INGREDIENT["Tiny Mushroom"]:1,
			INGREDIENT["Honey"]:2,
			INGREDIENT["Balm Mushroom"]:1
		}
	}
}