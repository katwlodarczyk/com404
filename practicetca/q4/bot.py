def cast_spell_with(ingredient):
    print("Double, double toil and trouble. Fire burn and caldron bubble.")
    if (ingredient == "newt"):
        print("In goes the eye of a newt that is not so cute.")
    elif(ingredient == "toad"):
        print("In goes a toad to add to our horrible load.")
    else:
        print("In goes an ingredient unknown for a spell that will be overblown.")
        print("\n")


cast_spell_with("newt")
cast_spell_with("toad")
cast_spell_with("bat")