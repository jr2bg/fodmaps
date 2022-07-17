import unidecode

def wrangle_input(ingredients: str) -> list:
    """Function to convert the text into a list of ingredients"""
    ingredients = unidecode.unidecode(ingredients) \
                    .lower()                       \
                    .replace("%", ",")             \
                    .replace("(", ",")             \
                    .replace(")", ",")             \
                    .replace("\n", ",")             \
                    .split(",")                    
                    
    return [ingredient.strip() for ingredient in ingredients]

def is_ingredient_fodmap(ingredient: str) -> bool:
    """Function to determine if a given ingredient has high FODMAPS"""
    # Lista de ingredientes altos en FODMAPs para buscar dentro de un producto
    FODMAPS = ["leche","lactosa","solidos de leche","fructosa","jmaf","jarabe de maiz de alta fructosa",
          "miel","jugo de fruta","concentrado de jugo","frutos secos","jarabe de agave","sorbitol",
          "manitol","xilitol","isomalt","eritrol","ajo","cebolla","trigo","centeno","inulina",
           "fructanos","fructooligosacaridos","harina de trigo","leche entera", "granos enteros de trigo",
          "leche descremada en polvo", "chocolate con leche","leche descremada","jarabe de maiz",
          "almidon de trigo","miel de abeja","harina de trigo integral","solidos de la leche",
          "jugo de manzana reconstituido","leche descremada en polvo", "leche entera reconstituida",
          "jugo de pera", "frijol", "frijol negro"]

    for fodmap in FODMAPS:
        if fodmap in ingredient:
            return True
    
    return False

def get_fodmap_ingredients(text: str) -> list:
    """Function to get a list of all high FODMAP ingredients in a text"""

    ingredients = wrangle_input(text)

    # head = "Los ingredientes con altos foodmaps son:\n-----\n"
    # return head + " * ".join(list(filter(is_ingredient_fodmap, ingredients)))
    return list(filter(is_ingredient_fodmap, ingredients))
