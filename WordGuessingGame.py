#Word guessing game
import random

words = [
    "bus", "house", "tree", "book", "lamp", "desk", "chair", "phone", "door",
    "window", "clock", "pencil", "shoes", "shirt", "plate", "spoon", "glass",
    "table", "paint", "brush", "bread", "milk", "water", "juice", "paper",
    "cloud", "music", "beach", "ocean", "river", "stone", "grass", "flower",
    "mouse", "snake", "horse", "tiger", "eagle", "queen", "king", "dream",
    "sleep", "smile", "dance", "laugh", "money", "sugar", "heart", "earth",
    "star", "apple", "orange", "grape", "peach", "plum", "melon", "lemon",
    "cherry", "berry", "fish", "bird", "duck", "goose", "sheep", "goat",
    "rabbit", "bear", "wolf", "deer", "lion", "zebra", "camel", "train",
    "plane", "ship", "boat", "bike", "road", "path", "hill", "lake", "pond",
    "storm", "rain", "snow", "wind", "fire", "smoke", "dust", "sand", "shell",
    "cave", "nest", "wing", "tail", "foot", "hand", "head", "face", "nose",
    "hair", "coat", "sock", "boot", "ring", "belt", "hat", "cape", "rope",
    "wire", "nail", "tool", "soap", "bowl", "fork", "knife", "box", "bag",
    "tape", "card", "gift", "game", "toy", "ball", "doll", "kite", "swing",
    "slide", "park", "farm", "town", "city", "shop", "mall", "bank", "post",
    "flag", "map", "book", "page", "note", "pen", "ink", "tape", "glue",
    "clay", "wood", "gold", "iron", "salt", "soup", "rice", "corn", "bean",
    "pear", "date", "seed", "leaf", "root", "stem", "rose", "lily", "pine",
    "oak", "palm", "weed", "moss", "fern", "vine", "mint", "sage", "soil",
    "rock", "coal", "oil", "gas", "air", "sky", "moon", "sun", "star", "beam",
    "ray", "heat", "cold", "ice", "fog", "mist", "dew", "wave", "foam", "sand",
    "mud", "clay", "dirt", "dust", "ash", "rust", "stain", "spot", "mark",
    "line", "dot", "hole", "gap", "crack", "bump", "dent", "bend", "fold",
    "edge", "side", "top", "base", "back", "front", "end", "start", "stop",
    "move", "run", "walk", "jump", "skip", "hop", "spin", "turn", "roll",
    "fall", "rise", "lift", "drop", "push", "pull", "hold", "grab", "throw",
    "catch", "hit", "kick", "bite", "eat", "drink", "cook", "bake", "fry",
    "boil", "wash", "dry", "fold", "cut", "tie", "mix", "stir", "pour", "fill",
    "empty", "pack", "wrap", "open", "close", "lock", "hide", "seek", "find",
    "lose", "win", "play", "work", "rest", "wake", "dress", "clean", "dirty",
    "dark", "light", "hot", "warm", "cool", "wet", "dry", "soft", "hard",
    "rough", "smooth", "sharp", "dull", "thick", "thin", "wide", "narrow",
    "big", "small", "tall", "short", "long", "round", "square", "flat", "deep",
    "high", "low", "far", "near", "fast", "slow", "loud", "quiet", "sweet",
    "sour", "salt", "fresh", "old", "new", "young", "late", "early", "first",
    "last", "next", "good", "bad", "nice", "mean", "kind", "rude", "brave",
    "scared", "happy", "sad", "angry", "calm", "busy", "free", "rich", "poor",
    "right", "wrong", "true", "false", "safe", "wild", "tame", "pure", "plain",
    "fancy", "prime", "raw", "ripe", "done", "neat", "messy", "clean", "dirty",
    "empty", "full", "heavy", "light", "loose", "tight", "open", "shut",
    "quick", "slow", "ready", "late", "fair", "fine", "real", "fake", "solid",
    "soft", "still", "loud", "mild", "wild", "bare", "busy", "calm", "dear",
    "deep", "dual", "dull", "dusk", "each", "east", "easy", "edge", "else",
    "even", "ever", "evil", "exit", "face", "fact", "fade", "fail", "fair",
    "fall", "fame", "farm", "fast", "fate", "fear", "feed", "feel", "feet",
    "fell", "felt", "file", "fill", "film", "find", "fine", "fire", "firm",
    "fish", "five", "flag", "flat", "flee", "flew", "flex", "flip", "flow",
    "foam", "fold", "folk", "food", "fool", "foot", "ford", "fork", "form",
    "fort", "four", "free", "frog", "from", "fuel", "full", "fund", "gain",
    "game", "gate", "gave", "gear", "gift", "girl", "give", "glad", "goal",
    "goat", "gold", "golf", "gone", "good", "gray", "grew", "grey", "grid",
    "grin", "grip", "grow", "gulf", "guru"
]
print("Welcome to word guessing game👏")
print("Please enter full word! ")
Playin = True
while Playin:
  Random_word = random.choice(words)
  index = len(Random_word)
  Random_index = random.randint(1, index) - 1
  Guess_word = Random_word[:Random_index] + "_" + Random_word[Random_index +
                                                              1:]
  user_guess = input(f"Guess this word '{Guess_word}': ")
  if user_guess.lower() == Random_word:
    print("You guess it right! ")
    Playing = input("Do you wanna play again? (Y/N): ")
    if Playing.lower() == "y":
      Playin = True
    elif Playing.lower() == "n":
      Playin = False
    else:
      print("Invalid! ")
      Playing = input("Do you wanna play again? (Y/N): ")
  else:
    print(f"You lost, the word was {Random_word} ")
    Playing = input("Do you wanna play again? (Y/N): ")
    if Playing.lower() == "y":
      Playin = True
    elif Playing.lower() == "n":
      Playin = False
      print("Thanks for playin':) ")
    while Playing.lower() != "y" and Playing.lower() != "n":
      print("Invaild! ")
      Playing = input("Do you wanna play again? (Y/N): ")
      if Playing.lower() == "y":
        Playin = True
      elif Playing.lower() == "n":
        Playin = False
        print("Thanks for playin':) ")
        continue