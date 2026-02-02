WORDLE_MODIFIED_WORD_LENGTH_MAP = {
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}


WORDLE_MODIFIED_ENV_DATA = {
    "env": "{env}",
    "agent": "You are playing a modified version of the game of wordle. Your goal is to guess the secret {agent}-letter word within six attempts (in the original version, you only guess a five-letter word). After each guess, you will receive feedback in the form of a series of statements describing how the letters in your guess compare to the secret word. Each statement corresponds to a letter in your guess: \n- 'First letter is correct and in the correct position in the target word' means the letter is correct and in the right position. \n- 'Second letter exists in the target word, but in a different position' means the letter is correct but in the wrong position. \n- 'Third letter does not exist in the target word' means the letter is not in the word at all. \nUse this feedback to refine your guesses and try to guess the secret word within six attempts.\n\nYou have to refine your guess based on this provided feedback. Keep guessing until you either guess the word correctly or use up all your attempts.\n\nPlease try to be concise. Format your response in the following way: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> your guess of what the word should be </Answer> \n\nThe game begins now, please make your first guess about the secret {agent}-letter word! Try to make your first guess as random as possible, and then proceed from there based on the feedback you receive.",
    "environment_default_response": "Sorry, your response does not follow the required format of this game, please try again. Format your response in the following way: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> your guess of what the word should be </Answer>",
    "judge_prompt_agent": None,
    "judge_prompt_env": None,
    "env_optional_message": "",
    "judge_prompt_suffix": "",
    "agent_optional_message": "\n\nMake your next guess about the hidden word. Please try to be concise. Format your response in the following way: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> your guess of what the word should be </Answer>",
    "max_turns": 6,
    "train": [
        {
            "env": "sample",
            "agent": "six"
        },
        {
            "env": "forest",
            "agent": "six"
        },
        {
            "env": "persuaded",
            "agent": "nine"
        },
        {
            "env": "canvas",
            "agent": "six"
        },
        {
            "env": "tool",
            "agent": "four"
        },
        {
            "env": "cattle",
            "agent": "six"
        },
        {
            "env": "community",
            "agent": "nine"
        },
        {
            "env": "discovery",
            "agent": "nine"
        },
        {
            "env": "rattle",
            "agent": "six"
        },
        {
            "env": "darkness",
            "agent": "eight"
        },
        {
            "env": "creation",
            "agent": "eight"
        },
        {
            "env": "static",
            "agent": "six"
        },
        {
            "env": "barrier",
            "agent": "seven"
        },
        {
            "env": "blueprint",
            "agent": "nine"
        },
        {
            "env": "bucket",
            "agent": "six"
        },
        {
            "env": "counter",
            "agent": "seven"
        },
        {
            "env": "alignment",
            "agent": "nine"
        },
        {
            "env": "entrance",
            "agent": "eight"
        },
        {
            "env": "escalator",
            "agent": "nine"
        },
        {
            "env": "harmony",
            "agent": "seven"
        },
        {
            "env": "streaming",
            "agent": "nine"
        },
        {
            "env": "portraits",
            "agent": "nine"
        },
        {
            "env": "circle",
            "agent": "six"
        },
        {
            "env": "processor",
            "agent": "nine"
        },
        {
            "env": "pull",
            "agent": "four"
        },
        {
            "env": "research",
            "agent": "eight"
        },
        {
            "env": "colleague",
            "agent": "nine"
        },
        {
            "env": "removal",
            "agent": "seven"
        },
        {
            "env": "starting",
            "agent": "eight"
        },
        {
            "env": "leaf",
            "agent": "four"
        },
        {
            "env": "composer",
            "agent": "eight"
        },
        {
            "env": "belt",
            "agent": "four"
        },
        {
            "env": "mystery",
            "agent": "seven"
        },
        {
            "env": "developer",
            "agent": "nine"
        },
        {
            "env": "hunger",
            "agent": "six"
        },
        {
            "env": "cave",
            "agent": "four"
        },
        {
            "env": "desert",
            "agent": "six"
        },
        {
            "env": "mountain",
            "agent": "eight"
        },
        {
            "env": "wind",
            "agent": "four"
        },
        {
            "env": "line",
            "agent": "four"
        },
        {
            "env": "service",
            "agent": "seven"
        },
        {
            "env": "gate",
            "agent": "four"
        },
        {
            "env": "shield",
            "agent": "six"
        },
        {
            "env": "contract",
            "agent": "eight"
        },
        {
            "env": "sanctuary",
            "agent": "nine"
        },
        {
            "env": "palm",
            "agent": "four"
        },
        {
            "env": "operation",
            "agent": "nine"
        },
        {
            "env": "toggle",
            "agent": "six"
        },
        {
            "env": "expedition",
            "agent": "ten"
        },
        {
            "env": "textbook",
            "agent": "eight"
        },
        {
            "env": "journey",
            "agent": "seven"
        },
        {
            "env": "hunter",
            "agent": "six"
        },
        {
            "env": "animal",
            "agent": "six"
        },
        {
            "env": "filter",
            "agent": "six"
        },
        {
            "env": "rain",
            "agent": "four"
        },
        {
            "env": "peel",
            "agent": "four"
        },
        {
            "env": "passion",
            "agent": "seven"
        },
        {
            "env": "span",
            "agent": "four"
        },
        {
            "env": "sunshine",
            "agent": "eight"
        },
        {
            "env": "kite",
            "agent": "four"
        },
        {
            "env": "marshal",
            "agent": "seven"
        },
        {
            "env": "magnitude",
            "agent": "nine"
        },
        {
            "env": "storyline",
            "agent": "nine"
        },
        {
            "env": "camp",
            "agent": "four"
        },
        {
            "env": "handler",
            "agent": "seven"
        },
        {
            "env": "plasma",
            "agent": "six"
        },
        {
            "env": "waterfall",
            "agent": "nine"
        },
        {
            "env": "pattern",
            "agent": "seven"
        },
        {
            "env": "assembly",
            "agent": "eight"
        },
        {
            "env": "workflow",
            "agent": "eight"
        },
        {
            "env": "mantle",
            "agent": "six"
        },
        {
            "env": "wolf",
            "agent": "four"
        },
        {
            "env": "battery",
            "agent": "seven"
        },
        {
            "env": "engineers",
            "agent": "nine"
        },
        {
            "env": "pebble",
            "agent": "six"
        },
        {
            "env": "pioneer",
            "agent": "seven"
        },
        {
            "env": "pencil",
            "agent": "six"
        },
        {
            "env": "flax",
            "agent": "four"
        },
        {
            "env": "aviation",
            "agent": "eight"
        },
        {
            "env": "colonial",
            "agent": "eight"
        },
        {
            "env": "lash",
            "agent": "four"
        },
        {
            "env": "stream",
            "agent": "six"
        },
        {
            "env": "caravan",
            "agent": "seven"
        },
        {
            "env": "detective",
            "agent": "nine"
        },
        {
            "env": "salt",
            "agent": "four"
        },
        {
            "env": "hollow",
            "agent": "six"
        },
        {
            "env": "reputation",
            "agent": "ten"
        },
        {
            "env": "trim",
            "agent": "four"
        },
        {
            "env": "cherry",
            "agent": "six"
        },
        {
            "env": "branch",
            "agent": "six"
        },
        {
            "env": "king",
            "agent": "four"
        },
        {
            "env": "admirably",
            "agent": "nine"
        },
        {
            "env": "serenity",
            "agent": "nine"
        },
        {
            "env": "thread",
            "agent": "six"
        },
        {
            "env": "stealthy",
            "agent": "eight"
        },
        {
            "env": "bishop",
            "agent": "six"
        },
        {
            "env": "captain",
            "agent": "seven"
        },
        {
            "env": "observer",
            "agent": "nine"
        },
        {
            "env": "plug",
            "agent": "four"
        },
        {
            "env": "scarcity",
            "agent": "eight"
        },
        {
            "env": "door",
            "agent": "four"
        },
        {
            "env": "ring",
            "agent": "four"
        },
        {
            "env": "sunrise",
            "agent": "seven"
        },
        {
            "env": "keyboard",
            "agent": "nine"
        },
        {
            "env": "vessel",
            "agent": "six"
        },
        {
            "env": "wonderful",
            "agent": "nine"
        },
        {
            "env": "saffron",
            "agent": "seven"
        },
        {
            "env": "disaster",
            "agent": "eight"
        },
        {
            "env": "bark",
            "agent": "four"
        },
        {
            "env": "clue",
            "agent": "four"
        },
        {
            "env": "signal",
            "agent": "six"
        },
        {
            "env": "tension",
            "agent": "seven"
        },
        {
            "env": "platform",
            "agent": "eight"
        },
        {
            "env": "coin",
            "agent": "four"
        },
        {
            "env": "fragmented",
            "agent": "nine"
        },
        {
            "env": "explore",
            "agent": "seven"
        },
        {
            "env": "surgeon",
            "agent": "seven"
        },
        {
            "env": "sculpture",
            "agent": "nine"
        },
        {
            "env": "subject",
            "agent": "seven"
        },
        {
            "env": "sergeant",
            "agent": "nine"
        },
        {
            "env": "sand",
            "agent": "four"
        },
        {
            "env": "president",
            "agent": "nine"
        },
        {
            "env": "hurricane",
            "agent": "nine"
        },
        {
            "env": "horizon",
            "agent": "seven"
        },
        {
            "env": "formation",
            "agent": "nine"
        },
        {
            "env": "song",
            "agent": "four"
        },
        {
            "env": "slab",
            "agent": "four"
        },
        {
            "env": "overcome",
            "agent": "eight"
        },
        {
            "env": "resolve",
            "agent": "seven"
        },
        {
            "env": "structure",
            "agent": "nine"
        },
        {
            "env": "landscape",
            "agent": "eight"
        },
        {
            "env": "portal",
            "agent": "six"
        },
        {
            "env": "summer",
            "agent": "six"
        },
        {
            "env": "recovered",
            "agent": "nine"
        },
        {
            "env": "shrine",
            "agent": "six"
        },
        {
            "env": "gallery",
            "agent": "seven"
        },
        {
            "env": "grip",
            "agent": "four"
        },
        {
            "env": "frozen",
            "agent": "six"
        },
        {
            "env": "reaction",
            "agent": "eight"
        },
        {
            "env": "freedom",
            "agent": "seven"
        },
        {
            "env": "pond",
            "agent": "four"
        },
        {
            "env": "moon",
            "agent": "four"
        },
        {
            "env": "mineral",
            "agent": "seven"
        },
        {
            "env": "echo",
            "agent": "four"
        },
        {
            "env": "commerce",
            "agent": "eight"
        },
        {
            "env": "treasure",
            "agent": "eight"
        },
        {
            "env": "brigade",
            "agent": "seven"
        },
        {
            "env": "picture",
            "agent": "seven"
        },
        {
            "env": "chemistry",
            "agent": "nine"
        },
        {
            "env": "funnel",
            "agent": "six"
        },
        {
            "env": "legend",
            "agent": "six"
        },
        {
            "env": "terrain",
            "agent": "seven"
        },
        {
            "env": "card",
            "agent": "four"
        },
        {
            "env": "garden",
            "agent": "six"
        },
        {
            "env": "pathway",
            "agent": "seven"
        },
        {
            "env": "painting",
            "agent": "eight"
        },
        {
            "env": "saddle",
            "agent": "six"
        },
        {
            "env": "elephant",
            "agent": "eight"
        },
        {
            "env": "face",
            "agent": "four"
        },
        {
            "env": "drum",
            "agent": "four"
        },
        {
            "env": "network",
            "agent": "seven"
        },
        {
            "env": "wander",
            "agent": "six"
        },
        {
            "env": "sunlight",
            "agent": "eight"
        },
        {
            "env": "grid",
            "agent": "four"
        },
        {
            "env": "column",
            "agent": "six"
        },
        {
            "env": "barren",
            "agent": "six"
        },
        {
            "env": "producing",
            "agent": "nine"
        },
        {
            "env": "request",
            "agent": "seven"
        },
        {
            "env": "kingdom",
            "agent": "seven"
        },
        {
            "env": "justice",
            "agent": "seven"
        },
        {
            "env": "eternal",
            "agent": "seven"
        },
        {
            "env": "drip",
            "agent": "four"
        },
        {
            "env": "path",
            "agent": "four"
        },
        {
            "env": "baseplate",
            "agent": "nine"
        },
        {
            "env": "tray",
            "agent": "four"
        },
        {
            "env": "feedback",
            "agent": "eight"
        },
        {
            "env": "project",
            "agent": "seven"
        },
        {
            "env": "lamp",
            "agent": "four"
        },
        {
            "env": "philosophy",
            "agent": "ten"
        },
        {
            "env": "adventure",
            "agent": "nine"
        },
        {
            "env": "mortar",
            "agent": "six"
        },
        {
            "env": "mile",
            "agent": "four"
        },
        {
            "env": "hike",
            "agent": "four"
        },
        {
            "env": "praise",
            "agent": "six"
        },
        {
            "env": "recreated",
            "agent": "nine"
        },
        {
            "env": "habitat",
            "agent": "seven"
        },
        {
            "env": "brilliant",
            "agent": "nine"
        },
        {
            "env": "gateway",
            "agent": "seven"
        },
        {
            "env": "reindeer",
            "agent": "eight"
        },
        {
            "env": "sibling",
            "agent": "seven"
        },
        {
            "env": "bridge",
            "agent": "six"
        },
        {
            "env": "mentally",
            "agent": "eight"
        },
        {
            "env": "engine",
            "agent": "six"
        },
        {
            "env": "land",
            "agent": "four"
        },
        {
            "env": "helm",
            "agent": "four"
        },
        {
            "env": "couple",
            "agent": "six"
        },
        {
            "env": "beacon",
            "agent": "six"
        },
        {
            "env": "alliance",
            "agent": "eight"
        },
        {
            "env": "dust",
            "agent": "four"
        },
        {
            "env": "polished",
            "agent": "eight"
        },
        {
            "env": "fragment",
            "agent": "eight"
        },
        {
            "env": "wish",
            "agent": "four"
        },
        {
            "env": "parallel",
            "agent": "eight"
        },
        {
            "env": "chip",
            "agent": "four"
        },
        {
            "env": "sandbox",
            "agent": "seven"
        },
        {
            "env": "personal",
            "agent": "eight"
        },
        {
            "env": "glow",
            "agent": "four"
        },
        {
            "env": "candidates",
            "agent": "nine"
        },
        {
            "env": "unlimited",
            "agent": "nine"
        },
        {
            "env": "seed",
            "agent": "four"
        },
        {
            "env": "explorer",
            "agent": "eight"
        },
        {
            "env": "damage",
            "agent": "six"
        },
        {
            "env": "rocket",
            "agent": "six"
        },
        {
            "env": "storage",
            "agent": "seven"
        },
        {
            "env": "creature",
            "agent": "eight"
        },
        {
            "env": "bronze",
            "agent": "six"
        },
        {
            "env": "gravity",
            "agent": "seven"
        },
        {
            "env": "town",
            "agent": "four"
        },
        {
            "env": "childhood",
            "agent": "nine"
        },
        {
            "env": "flight",
            "agent": "six"
        },
        {
            "env": "bolt",
            "agent": "four"
        },
        {
            "env": "movement",
            "agent": "nine"
        },
        {
            "env": "village",
            "agent": "seven"
        },
        {
            "env": "summit",
            "agent": "six"
        },
        {
            "env": "romantic",
            "agent": "eight"
        },
        {
            "env": "tunnel",
            "agent": "six"
        },
        {
            "env": "banner",
            "agent": "six"
        },
        {
            "env": "tank",
            "agent": "four"
        },
        {
            "env": "opposition",
            "agent": "ten"
        },
        {
            "env": "silver",
            "agent": "six"
        },
        {
            "env": "tree",
            "agent": "four"
        },
        {
            "env": "fantastic",
            "agent": "nine"
        },
        {
            "env": "burrow",
            "agent": "six"
        },
        {
            "env": "remains",
            "agent": "seven"
        },
        {
            "env": "armchair",
            "agent": "eight"
        },
        {
            "env": "window",
            "agent": "six"
        },
        {
            "env": "prisoner",
            "agent": "eight"
        },
        {
            "env": "horn",
            "agent": "four"
        },
        {
            "env": "beauty",
            "agent": "six"
        },
        {
            "env": "producer",
            "agent": "eight"
        },
        {
            "env": "fish",
            "agent": "four"
        },
        {
            "env": "delivery",
            "agent": "eight"
        },
        {
            "env": "warehouse",
            "agent": "nine"
        },
        {
            "env": "edge",
            "agent": "four"
        },
        {
            "env": "anchor",
            "agent": "six"
        },
        {
            "env": "firefly",
            "agent": "seven"
        },
        {
            "env": "pressure",
            "agent": "eight"
        },
        {
            "env": "dock",
            "agent": "four"
        },
        {
            "env": "ripple",
            "agent": "six"
        },
        {
            "env": "station",
            "agent": "seven"
        },
        {
            "env": "notebook",
            "agent": "eight"
        },
        {
            "env": "despair",
            "agent": "seven"
        },
        {
            "env": "happiness",
            "agent": "nine"
        },
        {
            "env": "spirit",
            "agent": "six"
        },
        {
            "env": "pillar",
            "agent": "six"
        },
        {
            "env": "affection",
            "agent": "nine"
        },
        {
            "env": "mannequin",
            "agent": "nine"
        },
        {
            "env": "carousel",
            "agent": "eight"
        },
        {
            "env": "gardener",
            "agent": "eight"
        },
        {
            "env": "pleasures",
            "agent": "nine"
        },
        {
            "env": "admirers",
            "agent": "eight"
        },
        {
            "env": "fountain",
            "agent": "eight"
        },
        {
            "env": "bulb",
            "agent": "four"
        },
        {
            "env": "foam",
            "agent": "four"
        },
        {
            "env": "context",
            "agent": "seven"
        },
        {
            "env": "wave",
            "agent": "four"
        },
        {
            "env": "gold",
            "agent": "four"
        },
        {
            "env": "factory",
            "agent": "seven"
        },
        {
            "env": "barn",
            "agent": "four"
        },
        {
            "env": "bird",
            "agent": "four"
        },
        {
            "env": "fortune",
            "agent": "seven"
        },
        {
            "env": "painter",
            "agent": "seven"
        },
        {
            "env": "audience",
            "agent": "eight"
        },
        {
            "env": "armored",
            "agent": "seven"
        },
        {
            "env": "horrified",
            "agent": "nine"
        },
        {
            "env": "twin",
            "agent": "four"
        },
        {
            "env": "star",
            "agent": "four"
        },
        {
            "env": "crop",
            "agent": "four"
        },
        {
            "env": "fire",
            "agent": "four"
        },
        {
            "env": "universe",
            "agent": "eight"
        },
        {
            "env": "herald",
            "agent": "six"
        },
        {
            "env": "lake",
            "agent": "four"
        },
        {
            "env": "compress",
            "agent": "eight"
        },
        {
            "env": "venture",
            "agent": "seven"
        },
        {
            "env": "mission",
            "agent": "seven"
        },
        {
            "env": "museum",
            "agent": "six"
        },
        {
            "env": "claw",
            "agent": "four"
        },
        {
            "env": "sphinx",
            "agent": "six"
        },
        {
            "env": "vertical",
            "agent": "eight"
        },
        {
            "env": "sunbeam",
            "agent": "seven"
        },
        {
            "env": "hospital",
            "agent": "eight"
        },
        {
            "env": "equation",
            "agent": "eight"
        },
        {
            "env": "narrow",
            "agent": "six"
        },
        {
            "env": "freight",
            "agent": "seven"
        },
        {
            "env": "enquiry",
            "agent": "seven"
        },
        {
            "env": "dancer",
            "agent": "six"
        },
        {
            "env": "frog",
            "agent": "four"
        },
        {
            "env": "release",
            "agent": "seven"
        },
        {
            "env": "temple",
            "agent": "six"
        },
        {
            "env": "silence",
            "agent": "seven"
        },
        {
            "env": "witness",
            "agent": "seven"
        },
        {
            "env": "axis",
            "agent": "four"
        },
        {
            "env": "density",
            "agent": "seven"
        },
        {
            "env": "standard",
            "agent": "eight"
        },
        {
            "env": "appetizer",
            "agent": "nine"
        },
        {
            "env": "crossbow",
            "agent": "eight"
        },
        {
            "env": "definition",
            "agent": "ten"
        },
        {
            "env": "palace",
            "agent": "six"
        },
        {
            "env": "rectangle",
            "agent": "nine"
        },
        {
            "env": "program",
            "agent": "seven"
        },
        {
            "env": "schedule",
            "agent": "eight"
        },
        {
            "env": "navigation",
            "agent": "ten"
        },
        {
            "env": "road",
            "agent": "four"
        },
        {
            "env": "shadow",
            "agent": "six"
        },
        {
            "env": "trap",
            "agent": "four"
        },
        {
            "env": "harvest",
            "agent": "seven"
        },
        {
            "env": "faculty",
            "agent": "seven"
        },
        {
            "env": "candles",
            "agent": "seven"
        },
        {
            "env": "charity",
            "agent": "seven"
        },
        {
            "env": "attention",
            "agent": "nine"
        },
        {
            "env": "whistler",
            "agent": "eight"
        },
        {
            "env": "clay",
            "agent": "four"
        },
        {
            "env": "talent",
            "agent": "six"
        },
        {
            "env": "starter",
            "agent": "seven"
        },
        {
            "env": "bottle",
            "agent": "six"
        },
        {
            "env": "function",
            "agent": "eight"
        },
        {
            "env": "bright",
            "agent": "six"
        },
        {
            "env": "carpentry",
            "agent": "nine"
        },
        {
            "env": "ranger",
            "agent": "six"
        },
        {
            "env": "statue",
            "agent": "six"
        },
        {
            "env": "snap",
            "agent": "four"
        },
        {
            "env": "ship",
            "agent": "four"
        },
        {
            "env": "simple",
            "agent": "six"
        },
        {
            "env": "theory",
            "agent": "six"
        },
        {
            "env": "scrape",
            "agent": "six"
        },
        {
            "env": "merchant",
            "agent": "eight"
        },
        {
            "env": "telescope",
            "agent": "nine"
        },
        {
            "env": "paradise",
            "agent": "eight"
        },
        {
            "env": "bend",
            "agent": "four"
        },
        {
            "env": "passage",
            "agent": "seven"
        },
        {
            "env": "roof",
            "agent": "four"
        },
        {
            "env": "experience",
            "agent": "ten"
        },
        {
            "env": "aircraft",
            "agent": "eight"
        },
        {
            "env": "desire",
            "agent": "six"
        },
        {
            "env": "concept",
            "agent": "seven"
        },
        {
            "env": "bedrock",
            "agent": "seven"
        },
        {
            "env": "evolution",
            "agent": "nine"
        },
        {
            "env": "glance",
            "agent": "six"
        },
        {
            "env": "success",
            "agent": "seven"
        },
        {
            "env": "forester",
            "agent": "eight"
        },
        {
            "env": "word",
            "agent": "four"
        },
        {
            "env": "marketing",
            "agent": "nine"
        },
        {
            "env": "book",
            "agent": "four"
        },
        {
            "env": "shipping",
            "agent": "eight"
        },
        {
            "env": "wonder",
            "agent": "six"
        },
        {
            "env": "jungle",
            "agent": "six"
        },
        {
            "env": "envelope",
            "agent": "eight"
        },
        {
            "env": "laundry",
            "agent": "seven"
        },
        {
            "env": "curl",
            "agent": "four"
        },
        {
            "env": "landlord",
            "agent": "eight"
        },
        {
            "env": "outpost",
            "agent": "seven"
        },
        {
            "env": "culture",
            "agent": "seven"
        },
        {
            "env": "futurists",
            "agent": "nine"
        },
        {
            "env": "renovated",
            "agent": "nine"
        },
        {
            "env": "importance",
            "agent": "ten"
        },
        {
            "env": "questions",
            "agent": "nine"
        },
        {
            "env": "landing",
            "agent": "seven"
        },
        {
            "env": "muffler",
            "agent": "seven"
        },
        {
            "env": "buildings",
            "agent": "nine"
        },
        {
            "env": "meadow",
            "agent": "six"
        },
        {
            "env": "framework",
            "agent": "nine"
        },
        {
            "env": "castle",
            "agent": "six"
        },
        {
            "env": "yarn",
            "agent": "four"
        },
        {
            "env": "voyage",
            "agent": "six"
        },
        {
            "env": "explosion",
            "agent": "nine"
        },
        {
            "env": "ball",
            "agent": "four"
        },
        {
            "env": "veil",
            "agent": "four"
        },
        {
            "env": "mechanism",
            "agent": "nine"
        },
        {
            "env": "beam",
            "agent": "four"
        },
        {
            "env": "monument",
            "agent": "eight"
        },
        {
            "env": "flap",
            "agent": "four"
        },
        {
            "env": "education",
            "agent": "nine"
        },
        {
            "env": "together",
            "agent": "nine"
        },
        {
            "env": "literature",
            "agent": "ten"
        },
        {
            "env": "root",
            "agent": "four"
        },
        {
            "env": "galaxy",
            "agent": "six"
        },
        {
            "env": "plague",
            "agent": "six"
        },
        {
            "env": "valley",
            "agent": "six"
        },
        {
            "env": "spring",
            "agent": "six"
        },
        {
            "env": "lock",
            "agent": "four"
        },
        {
            "env": "freelance",
            "agent": "nine"
        },
        {
            "env": "victory",
            "agent": "seven"
        },
        {
            "env": "festival",
            "agent": "eight"
        },
        {
            "env": "balance",
            "agent": "seven"
        },
        {
            "env": "monster",
            "agent": "seven"
        },
        {
            "env": "hint",
            "agent": "four"
        },
        {
            "env": "wrap",
            "agent": "four"
        },
        {
            "env": "curtain",
            "agent": "seven"
        }
    ],
}