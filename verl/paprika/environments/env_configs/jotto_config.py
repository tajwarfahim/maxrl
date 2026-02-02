JOTTO_ENV_DATA = {
    "env": "{env}",
    "agent": "You are playing a game of Jotto. Follow these rules carefully and respond EXACTLY in the required format.\n\nGAME OVERVIEW\n- Objective: You have to guess a secret word with {num_letters} letters. You have to start with a preliminary guess, and will receive numerical feedback regarding how many common letters exist between your guess and the true secret word. You have to refine your guess based on this feedback and will receive the same feedback for your refined guess at every turn. You have a total of 15 turns, and have to guess the secret word before you run out of turns to win the game. \n- The secret word is a valid English word, and all letters in this word are unique (only appears once within the word). \n\nTURN STRUCTURE\n1. You make a guess — any valid {num_letters} letter English word.\n2. The environment responds with a number (0–{num_letters}) indicating how many letters your guess shares with the secret word, regardless of position.\n • Example: Secret word = 'TRAIN', Guess = 'PLANT' → Feedback = 3 (letters A, N, T are common)\n3. You do NOT get to know which letters are correct — only the total count.\n\nGOAL\n- Use logical reasoning and information about guesses and corresponding feedback from all previous turns to deduce the secret word using as few guesses as possible.\n\nGUESSING RULES\n- Each guess must be exactly {num_letters} alphabetic letters (A–Z).\n- Each guess must be a valid English word.\n- Guesses are case-insensitive. \n\nFEEDBACK INTERPRETATION\n- The feedback number after each guess represents how many letters from your guess appear in the secret word, regardless of order or position. For example: \n- 0 means no letters overlap.\n- 3 means your guess has 3 letters common with the secret word you are trying to guess. \n\n LIMITS\n- Maximum total guesses: 15.\n- You win if you identify the secret word before using all attempts.\n\nRESPONSE FORMAT (STRICT)\n Keep your thinking concise. Please format your response as follows: <Think> Any step-by-step, short, and concise thinking to determine your next guess about the target word </Think> <Answer> Your guess of the target word </Answer> \n\nThe game begins now. Make your first guess of the {num_letters} letter English word, then refine subsequent guesses using feedback from previous turns. Keep your thinking concise!",
    "environment_default_response": "Sorry, your response does not follow the required format of the game of Jotto, please try again. The secret word you need to guess has {num_letters} letters. Please keep any thinking concise. Format your response in the following way: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> your guess of what the word should be </Answer>",
    "judge_prompt_agent": None,
    "judge_prompt_env": None,
    "env_optional_message": "",
    "judge_prompt_suffix": "",
    "agent_optional_message": "\n\nMake your next guess about the {num_letters} letter hidden word (Note: all letters within this word need to be unique). Please keep any thinking concise. Format your response in the following way: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> your guess of what the word should be </Answer>",
    "max_turns": 15,
    "train": [
        {
            "env": "regal",
            "agent": "word"
        },
        {
            "env": "agent",
            "agent": "word"
        },
        {
            "env": "unify",
            "agent": "word"
        },
        {
            "env": "solar",
            "agent": "word"
        },
        {
            "env": "hunky",
            "agent": "word"
        },
        {
            "env": "removal",
            "agent": "seven"
        },
        {
            "env": "town",
            "agent": "four"
        },
        {
            "env": "block",
            "agent": "word"
        },
        {
            "env": "wrack",
            "agent": "word"
        },
        {
            "env": "salt",
            "agent": "four"
        },
        {
            "env": "curvy",
            "agent": "word"
        },
        {
            "env": "slain",
            "agent": "word"
        },
        {
            "env": "wreak",
            "agent": "word"
        },
        {
            "env": "syrup",
            "agent": "word"
        },
        {
            "env": "cheat",
            "agent": "word"
        },
        {
            "env": "squib",
            "agent": "word"
        },
        {
            "env": "leant",
            "agent": "word"
        },
        {
            "env": "network",
            "agent": "seven"
        },
        {
            "env": "young",
            "agent": "word"
        },
        {
            "env": "waive",
            "agent": "word"
        },
        {
            "env": "renal",
            "agent": "word"
        },
        {
            "env": "flour",
            "agent": "word"
        },
        {
            "env": "harpy",
            "agent": "word"
        },
        {
            "env": "thyme",
            "agent": "word"
        },
        {
            "env": "godly",
            "agent": "word"
        },
        {
            "env": "cobra",
            "agent": "word"
        },
        {
            "env": "tweak",
            "agent": "word"
        },
        {
            "env": "crone",
            "agent": "word"
        },
        {
            "env": "taken",
            "agent": "word"
        },
        {
            "env": "froze",
            "agent": "word"
        },
        {
            "env": "beam",
            "agent": "four"
        },
        {
            "env": "stank",
            "agent": "word"
        },
        {
            "env": "prove",
            "agent": "word"
        },
        {
            "env": "scent",
            "agent": "word"
        },
        {
            "env": "frame",
            "agent": "word"
        },
        {
            "env": "yarn",
            "agent": "four"
        },
        {
            "env": "board",
            "agent": "word"
        },
        {
            "env": "hotly",
            "agent": "word"
        },
        {
            "env": "scold",
            "agent": "word"
        },
        {
            "env": "grown",
            "agent": "word"
        },
        {
            "env": "minty",
            "agent": "word"
        },
        {
            "env": "penal",
            "agent": "word"
        },
        {
            "env": "olden",
            "agent": "word"
        },
        {
            "env": "decry",
            "agent": "word"
        },
        {
            "env": "south",
            "agent": "word"
        },
        {
            "env": "branch",
            "agent": "six"
        },
        {
            "env": "purge",
            "agent": "word"
        },
        {
            "env": "lyric",
            "agent": "word"
        },
        {
            "env": "ounce",
            "agent": "word"
        },
        {
            "env": "ideal",
            "agent": "word"
        },
        {
            "env": "adobe",
            "agent": "word"
        },
        {
            "env": "alien",
            "agent": "word"
        },
        {
            "env": "grate",
            "agent": "word"
        },
        {
            "env": "truly",
            "agent": "word"
        },
        {
            "env": "trawl",
            "agent": "word"
        },
        {
            "env": "began",
            "agent": "word"
        },
        {
            "env": "epoxy",
            "agent": "word"
        },
        {
            "env": "badge",
            "agent": "word"
        },
        {
            "env": "quest",
            "agent": "word"
        },
        {
            "env": "scorn",
            "agent": "word"
        },
        {
            "env": "vixen",
            "agent": "word"
        },
        {
            "env": "mauve",
            "agent": "word"
        },
        {
            "env": "wacky",
            "agent": "word"
        },
        {
            "env": "range",
            "agent": "word"
        },
        {
            "env": "slunk",
            "agent": "word"
        },
        {
            "env": "cedar",
            "agent": "word"
        },
        {
            "env": "crept",
            "agent": "word"
        },
        {
            "env": "amble",
            "agent": "word"
        },
        {
            "env": "stain",
            "agent": "word"
        },
        {
            "env": "snaky",
            "agent": "word"
        },
        {
            "env": "gnash",
            "agent": "word"
        },
        {
            "env": "detox",
            "agent": "word"
        },
        {
            "env": "march",
            "agent": "word"
        },
        {
            "env": "abide",
            "agent": "word"
        },
        {
            "env": "budge",
            "agent": "word"
        },
        {
            "env": "agony",
            "agent": "word"
        },
        {
            "env": "zesty",
            "agent": "word"
        },
        {
            "env": "risky",
            "agent": "word"
        },
        {
            "env": "vowel",
            "agent": "word"
        },
        {
            "env": "haunt",
            "agent": "word"
        },
        {
            "env": "plunk",
            "agent": "word"
        },
        {
            "env": "screw",
            "agent": "word"
        },
        {
            "env": "twirl",
            "agent": "word"
        },
        {
            "env": "meadow",
            "agent": "six"
        },
        {
            "env": "suing",
            "agent": "word"
        },
        {
            "env": "inert",
            "agent": "word"
        },
        {
            "env": "azure",
            "agent": "word"
        },
        {
            "env": "spend",
            "agent": "word"
        },
        {
            "env": "imply",
            "agent": "word"
        },
        {
            "env": "rocket",
            "agent": "six"
        },
        {
            "env": "group",
            "agent": "word"
        },
        {
            "env": "voyage",
            "agent": "six"
        },
        {
            "env": "posit",
            "agent": "word"
        },
        {
            "env": "vista",
            "agent": "word"
        },
        {
            "env": "anime",
            "agent": "word"
        },
        {
            "env": "ovate",
            "agent": "word"
        },
        {
            "env": "surgeon",
            "agent": "seven"
        },
        {
            "env": "plate",
            "agent": "word"
        },
        {
            "env": "shoal",
            "agent": "word"
        },
        {
            "env": "gamut",
            "agent": "word"
        },
        {
            "env": "spray",
            "agent": "word"
        },
        {
            "env": "diner",
            "agent": "word"
        },
        {
            "env": "angst",
            "agent": "word"
        },
        {
            "env": "marketing",
            "agent": "nine"
        },
        {
            "env": "tiger",
            "agent": "word"
        },
        {
            "env": "borax",
            "agent": "word"
        },
        {
            "env": "mourn",
            "agent": "word"
        },
        {
            "env": "scary",
            "agent": "word"
        },
        {
            "env": "education",
            "agent": "nine"
        },
        {
            "env": "skimp",
            "agent": "word"
        },
        {
            "env": "teary",
            "agent": "word"
        },
        {
            "env": "while",
            "agent": "word"
        },
        {
            "env": "adorn",
            "agent": "word"
        },
        {
            "env": "snore",
            "agent": "word"
        },
        {
            "env": "magic",
            "agent": "word"
        },
        {
            "env": "scone",
            "agent": "word"
        },
        {
            "env": "bugle",
            "agent": "word"
        },
        {
            "env": "gourd",
            "agent": "word"
        },
        {
            "env": "watch",
            "agent": "word"
        },
        {
            "env": "rabid",
            "agent": "word"
        },
        {
            "env": "comfy",
            "agent": "word"
        },
        {
            "env": "birth",
            "agent": "word"
        },
        {
            "env": "flyer",
            "agent": "word"
        },
        {
            "env": "daisy",
            "agent": "word"
        },
        {
            "env": "gaily",
            "agent": "word"
        },
        {
            "env": "murky",
            "agent": "word"
        },
        {
            "env": "badly",
            "agent": "word"
        },
        {
            "env": "pond",
            "agent": "four"
        },
        {
            "env": "hover",
            "agent": "word"
        },
        {
            "env": "joint",
            "agent": "word"
        },
        {
            "env": "drink",
            "agent": "word"
        },
        {
            "env": "snipe",
            "agent": "word"
        },
        {
            "env": "other",
            "agent": "word"
        },
        {
            "env": "avert",
            "agent": "word"
        },
        {
            "env": "camp",
            "agent": "four"
        },
        {
            "env": "antic",
            "agent": "word"
        },
        {
            "env": "virus",
            "agent": "word"
        },
        {
            "env": "hasty",
            "agent": "word"
        },
        {
            "env": "urine",
            "agent": "word"
        },
        {
            "env": "rain",
            "agent": "four"
        },
        {
            "env": "hazel",
            "agent": "word"
        },
        {
            "env": "salvo",
            "agent": "word"
        },
        {
            "env": "lurch",
            "agent": "word"
        },
        {
            "env": "stunk",
            "agent": "word"
        },
        {
            "env": "child",
            "agent": "word"
        },
        {
            "env": "would",
            "agent": "word"
        },
        {
            "env": "claw",
            "agent": "four"
        },
        {
            "env": "chair",
            "agent": "word"
        },
        {
            "env": "gloat",
            "agent": "word"
        },
        {
            "env": "crony",
            "agent": "word"
        },
        {
            "env": "scarf",
            "agent": "word"
        },
        {
            "env": "counter",
            "agent": "seven"
        },
        {
            "env": "imbue",
            "agent": "word"
        },
        {
            "env": "epoch",
            "agent": "word"
        },
        {
            "env": "mantle",
            "agent": "six"
        },
        {
            "env": "lofty",
            "agent": "word"
        },
        {
            "env": "devil",
            "agent": "word"
        },
        {
            "env": "pushy",
            "agent": "word"
        },
        {
            "env": "shape",
            "agent": "word"
        },
        {
            "env": "dust",
            "agent": "four"
        },
        {
            "env": "lash",
            "agent": "four"
        },
        {
            "env": "jerky",
            "agent": "word"
        },
        {
            "env": "funky",
            "agent": "word"
        },
        {
            "env": "cough",
            "agent": "word"
        },
        {
            "env": "fluid",
            "agent": "word"
        },
        {
            "env": "baker",
            "agent": "word"
        },
        {
            "env": "curl",
            "agent": "four"
        },
        {
            "env": "aglow",
            "agent": "word"
        },
        {
            "env": "rifle",
            "agent": "word"
        },
        {
            "env": "unzip",
            "agent": "word"
        },
        {
            "env": "rival",
            "agent": "word"
        },
        {
            "env": "cave",
            "agent": "four"
        },
        {
            "env": "exist",
            "agent": "word"
        },
        {
            "env": "swore",
            "agent": "word"
        },
        {
            "env": "bark",
            "agent": "four"
        },
        {
            "env": "mover",
            "agent": "word"
        },
        {
            "env": "stove",
            "agent": "word"
        },
        {
            "env": "wonderful",
            "agent": "nine"
        },
        {
            "env": "climb",
            "agent": "word"
        },
        {
            "env": "route",
            "agent": "word"
        },
        {
            "env": "chirp",
            "agent": "word"
        },
        {
            "env": "crave",
            "agent": "word"
        },
        {
            "env": "berth",
            "agent": "word"
        },
        {
            "env": "shawl",
            "agent": "word"
        },
        {
            "env": "harmony",
            "agent": "seven"
        },
        {
            "env": "joist",
            "agent": "word"
        },
        {
            "env": "feral",
            "agent": "word"
        },
        {
            "env": "inlet",
            "agent": "word"
        },
        {
            "env": "cloud",
            "agent": "word"
        },
        {
            "env": "romantic",
            "agent": "eight"
        },
        {
            "env": "angle",
            "agent": "word"
        },
        {
            "env": "blimp",
            "agent": "word"
        },
        {
            "env": "tower",
            "agent": "word"
        },
        {
            "env": "smote",
            "agent": "word"
        },
        {
            "env": "miser",
            "agent": "word"
        },
        {
            "env": "plied",
            "agent": "word"
        },
        {
            "env": "gusty",
            "agent": "word"
        },
        {
            "env": "speak",
            "agent": "word"
        },
        {
            "env": "kite",
            "agent": "four"
        },
        {
            "env": "bronze",
            "agent": "six"
        },
        {
            "env": "lock",
            "agent": "four"
        },
        {
            "env": "punch",
            "agent": "word"
        },
        {
            "env": "refit",
            "agent": "word"
        },
        {
            "env": "hyena",
            "agent": "word"
        },
        {
            "env": "unlit",
            "agent": "word"
        },
        {
            "env": "bench",
            "agent": "word"
        },
        {
            "env": "dealt",
            "agent": "word"
        },
        {
            "env": "quirk",
            "agent": "word"
        },
        {
            "env": "snowy",
            "agent": "word"
        },
        {
            "env": "helm",
            "agent": "four"
        },
        {
            "env": "sport",
            "agent": "word"
        },
        {
            "env": "plumb",
            "agent": "word"
        },
        {
            "env": "chose",
            "agent": "word"
        },
        {
            "env": "couple",
            "agent": "six"
        },
        {
            "env": "brown",
            "agent": "word"
        },
        {
            "env": "women",
            "agent": "word"
        },
        {
            "env": "beast",
            "agent": "word"
        },
        {
            "env": "might",
            "agent": "word"
        },
        {
            "env": "cater",
            "agent": "word"
        },
        {
            "env": "amber",
            "agent": "word"
        },
        {
            "env": "trick",
            "agent": "word"
        },
        {
            "env": "delay",
            "agent": "word"
        },
        {
            "env": "retch",
            "agent": "word"
        },
        {
            "env": "roast",
            "agent": "word"
        },
        {
            "env": "quilt",
            "agent": "word"
        },
        {
            "env": "tawny",
            "agent": "word"
        },
        {
            "env": "swarm",
            "agent": "word"
        },
        {
            "env": "unwed",
            "agent": "word"
        },
        {
            "env": "voice",
            "agent": "word"
        },
        {
            "env": "moist",
            "agent": "word"
        },
        {
            "env": "laugh",
            "agent": "word"
        },
        {
            "env": "dunce",
            "agent": "word"
        },
        {
            "env": "squad",
            "agent": "word"
        },
        {
            "env": "noisy",
            "agent": "word"
        },
        {
            "env": "rugby",
            "agent": "word"
        },
        {
            "env": "lanky",
            "agent": "word"
        },
        {
            "env": "brink",
            "agent": "word"
        },
        {
            "env": "whistler",
            "agent": "eight"
        },
        {
            "env": "stave",
            "agent": "word"
        },
        {
            "env": "adept",
            "agent": "word"
        },
        {
            "env": "demur",
            "agent": "word"
        },
        {
            "env": "bolt",
            "agent": "four"
        },
        {
            "env": "randy",
            "agent": "word"
        },
        {
            "env": "shalt",
            "agent": "word"
        },
        {
            "env": "shuck",
            "agent": "word"
        },
        {
            "env": "leaky",
            "agent": "word"
        },
        {
            "env": "hater",
            "agent": "word"
        },
        {
            "env": "clerk",
            "agent": "word"
        },
        {
            "env": "vague",
            "agent": "word"
        },
        {
            "env": "tonic",
            "agent": "word"
        },
        {
            "env": "coupe",
            "agent": "word"
        },
        {
            "env": "frown",
            "agent": "word"
        },
        {
            "env": "drake",
            "agent": "word"
        },
        {
            "env": "crump",
            "agent": "word"
        },
        {
            "env": "birch",
            "agent": "word"
        },
        {
            "env": "husky",
            "agent": "word"
        },
        {
            "env": "jumpy",
            "agent": "word"
        },
        {
            "env": "nicer",
            "agent": "word"
        },
        {
            "env": "graph",
            "agent": "word"
        },
        {
            "env": "stock",
            "agent": "word"
        },
        {
            "env": "corny",
            "agent": "word"
        },
        {
            "env": "octal",
            "agent": "word"
        },
        {
            "env": "ghoul",
            "agent": "word"
        },
        {
            "env": "shake",
            "agent": "word"
        },
        {
            "env": "raise",
            "agent": "word"
        },
        {
            "env": "dusty",
            "agent": "word"
        },
        {
            "env": "pilot",
            "agent": "word"
        },
        {
            "env": "howdy",
            "agent": "word"
        },
        {
            "env": "evict",
            "agent": "word"
        },
        {
            "env": "loath",
            "agent": "word"
        },
        {
            "env": "rapid",
            "agent": "word"
        },
        {
            "env": "sheik",
            "agent": "word"
        },
        {
            "env": "slick",
            "agent": "word"
        },
        {
            "env": "actor",
            "agent": "word"
        },
        {
            "env": "crate",
            "agent": "word"
        },
        {
            "env": "shirk",
            "agent": "word"
        },
        {
            "env": "matey",
            "agent": "word"
        },
        {
            "env": "prowl",
            "agent": "word"
        },
        {
            "env": "kingdom",
            "agent": "seven"
        },
        {
            "env": "twice",
            "agent": "word"
        },
        {
            "env": "until",
            "agent": "word"
        },
        {
            "env": "decoy",
            "agent": "word"
        },
        {
            "env": "poser",
            "agent": "word"
        },
        {
            "env": "pride",
            "agent": "word"
        },
        {
            "env": "gavel",
            "agent": "word"
        },
        {
            "env": "hydro",
            "agent": "word"
        },
        {
            "env": "smith",
            "agent": "word"
        },
        {
            "env": "borne",
            "agent": "word"
        },
        {
            "env": "scout",
            "agent": "word"
        },
        {
            "env": "freight",
            "agent": "seven"
        },
        {
            "env": "slang",
            "agent": "word"
        },
        {
            "env": "mower",
            "agent": "word"
        },
        {
            "env": "nasty",
            "agent": "word"
        },
        {
            "env": "cleft",
            "agent": "word"
        },
        {
            "env": "shale",
            "agent": "word"
        },
        {
            "env": "flax",
            "agent": "four"
        },
        {
            "env": "biome",
            "agent": "word"
        },
        {
            "env": "shock",
            "agent": "word"
        },
        {
            "env": "spelt",
            "agent": "word"
        },
        {
            "env": "clone",
            "agent": "word"
        },
        {
            "env": "gusto",
            "agent": "word"
        },
        {
            "env": "scare",
            "agent": "word"
        },
        {
            "env": "quark",
            "agent": "word"
        },
        {
            "env": "dusky",
            "agent": "word"
        },
        {
            "env": "gumbo",
            "agent": "word"
        },
        {
            "env": "carousel",
            "agent": "eight"
        },
        {
            "env": "savoy",
            "agent": "word"
        },
        {
            "env": "angel",
            "agent": "word"
        },
        {
            "env": "wonder",
            "agent": "six"
        },
        {
            "env": "swath",
            "agent": "word"
        },
        {
            "env": "wrung",
            "agent": "word"
        },
        {
            "env": "stole",
            "agent": "word"
        },
        {
            "env": "throb",
            "agent": "word"
        },
        {
            "env": "glove",
            "agent": "word"
        },
        {
            "env": "fable",
            "agent": "word"
        },
        {
            "env": "craft",
            "agent": "word"
        },
        {
            "env": "bulky",
            "agent": "word"
        },
        {
            "env": "spoil",
            "agent": "word"
        },
        {
            "env": "spawn",
            "agent": "word"
        },
        {
            "env": "picture",
            "agent": "seven"
        },
        {
            "env": "splat",
            "agent": "word"
        },
        {
            "env": "bluer",
            "agent": "word"
        },
        {
            "env": "downy",
            "agent": "word"
        },
        {
            "env": "tunic",
            "agent": "word"
        },
        {
            "env": "scion",
            "agent": "word"
        },
        {
            "env": "sperm",
            "agent": "word"
        },
        {
            "env": "purse",
            "agent": "word"
        },
        {
            "env": "fancy",
            "agent": "word"
        },
        {
            "env": "alone",
            "agent": "word"
        },
        {
            "env": "quasi",
            "agent": "word"
        },
        {
            "env": "silver",
            "agent": "six"
        },
        {
            "env": "spire",
            "agent": "word"
        },
        {
            "env": "ghost",
            "agent": "word"
        },
        {
            "env": "neigh",
            "agent": "word"
        },
        {
            "env": "slink",
            "agent": "word"
        },
        {
            "env": "cable",
            "agent": "word"
        },
        {
            "env": "sight",
            "agent": "word"
        },
        {
            "env": "chant",
            "agent": "word"
        },
        {
            "env": "slump",
            "agent": "word"
        },
        {
            "env": "suave",
            "agent": "word"
        },
        {
            "env": "count",
            "agent": "word"
        },
        {
            "env": "foamy",
            "agent": "word"
        },
        {
            "env": "boney",
            "agent": "word"
        },
        {
            "env": "fight",
            "agent": "word"
        },
        {
            "env": "stray",
            "agent": "word"
        },
        {
            "env": "girly",
            "agent": "word"
        },
        {
            "env": "share",
            "agent": "word"
        },
        {
            "env": "feast",
            "agent": "word"
        },
        {
            "env": "grain",
            "agent": "word"
        },
        {
            "env": "rebus",
            "agent": "word"
        },
        {
            "env": "keyboard",
            "agent": "nine"
        },
        {
            "env": "resin",
            "agent": "word"
        },
        {
            "env": "ample",
            "agent": "word"
        },
        {
            "env": "using",
            "agent": "word"
        },
        {
            "env": "drive",
            "agent": "word"
        },
        {
            "env": "perky",
            "agent": "word"
        },
        {
            "env": "movie",
            "agent": "word"
        },
        {
            "env": "match",
            "agent": "word"
        },
        {
            "env": "throw",
            "agent": "word"
        },
        {
            "env": "scrap",
            "agent": "word"
        },
        {
            "env": "stung",
            "agent": "word"
        },
        {
            "env": "smoky",
            "agent": "word"
        },
        {
            "env": "ship",
            "agent": "four"
        },
        {
            "env": "spite",
            "agent": "word"
        },
        {
            "env": "relay",
            "agent": "word"
        },
        {
            "env": "shrew",
            "agent": "word"
        },
        {
            "env": "grasp",
            "agent": "word"
        },
        {
            "env": "brain",
            "agent": "word"
        },
        {
            "env": "heist",
            "agent": "word"
        },
        {
            "env": "rehab",
            "agent": "word"
        },
        {
            "env": "crop",
            "agent": "four"
        },
        {
            "env": "wish",
            "agent": "four"
        },
        {
            "env": "aunty",
            "agent": "word"
        },
        {
            "env": "fetal",
            "agent": "word"
        },
        {
            "env": "lucid",
            "agent": "word"
        },
        {
            "env": "havoc",
            "agent": "word"
        },
        {
            "env": "coast",
            "agent": "word"
        },
        {
            "env": "baler",
            "agent": "word"
        },
        {
            "env": "enact",
            "agent": "word"
        },
        {
            "env": "drawl",
            "agent": "word"
        },
        {
            "env": "blunt",
            "agent": "word"
        },
        {
            "env": "piano",
            "agent": "word"
        },
        {
            "env": "aider",
            "agent": "word"
        },
        {
            "env": "sepia",
            "agent": "word"
        },
        {
            "env": "flair",
            "agent": "word"
        },
        {
            "env": "wench",
            "agent": "word"
        },
        {
            "env": "boast",
            "agent": "word"
        },
        {
            "env": "tulip",
            "agent": "word"
        },
        {
            "env": "yearn",
            "agent": "word"
        },
        {
            "env": "snail",
            "agent": "word"
        },
        {
            "env": "milky",
            "agent": "word"
        },
        {
            "env": "mineral",
            "agent": "seven"
        },
        {
            "env": "surge",
            "agent": "word"
        },
        {
            "env": "trace",
            "agent": "word"
        },
        {
            "env": "donut",
            "agent": "word"
        },
        {
            "env": "torus",
            "agent": "word"
        },
        {
            "env": "midge",
            "agent": "word"
        },
        {
            "env": "scamp",
            "agent": "word"
        },
        {
            "env": "sting",
            "agent": "word"
        },
        {
            "env": "habit",
            "agent": "word"
        },
        {
            "env": "stork",
            "agent": "word"
        },
        {
            "env": "cigar",
            "agent": "word"
        },
        {
            "env": "image",
            "agent": "word"
        },
        {
            "env": "span",
            "agent": "four"
        },
        {
            "env": "beauty",
            "agent": "six"
        },
        {
            "env": "owner",
            "agent": "word"
        },
        {
            "env": "foray",
            "agent": "word"
        },
        {
            "env": "cutie",
            "agent": "word"
        },
        {
            "env": "bleak",
            "agent": "word"
        },
        {
            "env": "labor",
            "agent": "word"
        },
        {
            "env": "begat",
            "agent": "word"
        },
        {
            "env": "aping",
            "agent": "word"
        },
        {
            "env": "clout",
            "agent": "word"
        },
        {
            "env": "trap",
            "agent": "four"
        },
        {
            "env": "flown",
            "agent": "word"
        },
        {
            "env": "mealy",
            "agent": "word"
        },
        {
            "env": "trash",
            "agent": "word"
        },
        {
            "env": "depot",
            "agent": "word"
        },
        {
            "env": "vapid",
            "agent": "word"
        },
        {
            "env": "shiny",
            "agent": "word"
        },
        {
            "env": "surly",
            "agent": "word"
        },
        {
            "env": "serif",
            "agent": "word"
        },
        {
            "env": "sworn",
            "agent": "word"
        },
        {
            "env": "proud",
            "agent": "word"
        },
        {
            "env": "stark",
            "agent": "word"
        },
        {
            "env": "clump",
            "agent": "word"
        },
        {
            "env": "favor",
            "agent": "word"
        },
        {
            "env": "peril",
            "agent": "word"
        },
        {
            "env": "quash",
            "agent": "word"
        },
        {
            "env": "flesh",
            "agent": "word"
        },
        {
            "env": "dwarf",
            "agent": "word"
        },
        {
            "env": "flask",
            "agent": "word"
        },
        {
            "env": "flume",
            "agent": "word"
        },
        {
            "env": "score",
            "agent": "word"
        },
        {
            "env": "hospital",
            "agent": "eight"
        },
        {
            "env": "graft",
            "agent": "word"
        },
        {
            "env": "cloth",
            "agent": "word"
        },
        {
            "env": "drum",
            "agent": "four"
        },
        {
            "env": "mural",
            "agent": "word"
        },
        {
            "env": "ratio",
            "agent": "word"
        },
        {
            "env": "belch",
            "agent": "word"
        },
        {
            "env": "gulch",
            "agent": "word"
        },
        {
            "env": "oaken",
            "agent": "word"
        },
        {
            "env": "buyer",
            "agent": "word"
        },
        {
            "env": "bride",
            "agent": "word"
        },
        {
            "env": "great",
            "agent": "word"
        },
        {
            "env": "bucket",
            "agent": "six"
        },
        {
            "env": "junto",
            "agent": "word"
        },
        {
            "env": "flash",
            "agent": "word"
        },
        {
            "env": "graze",
            "agent": "word"
        },
        {
            "env": "strap",
            "agent": "word"
        },
        {
            "env": "royal",
            "agent": "word"
        },
        {
            "env": "prism",
            "agent": "word"
        },
        {
            "env": "frog",
            "agent": "four"
        },
        {
            "env": "wrath",
            "agent": "word"
        },
        {
            "env": "gaunt",
            "agent": "word"
        },
        {
            "env": "wound",
            "agent": "word"
        },
        {
            "env": "trial",
            "agent": "word"
        },
        {
            "env": "scant",
            "agent": "word"
        },
        {
            "env": "tardy",
            "agent": "word"
        },
        {
            "env": "radio",
            "agent": "word"
        },
        {
            "env": "moult",
            "agent": "word"
        },
        {
            "env": "stand",
            "agent": "word"
        },
        {
            "env": "tramp",
            "agent": "word"
        },
        {
            "env": "earth",
            "agent": "word"
        },
        {
            "env": "lefty",
            "agent": "word"
        },
        {
            "env": "vaunt",
            "agent": "word"
        },
        {
            "env": "apron",
            "agent": "word"
        },
        {
            "env": "adult",
            "agent": "word"
        },
        {
            "env": "china",
            "agent": "word"
        },
        {
            "env": "deign",
            "agent": "word"
        },
        {
            "env": "lynch",
            "agent": "word"
        },
        {
            "env": "olive",
            "agent": "word"
        },
        {
            "env": "train",
            "agent": "word"
        },
        {
            "env": "lemur",
            "agent": "word"
        },
        {
            "env": "strip",
            "agent": "word"
        },
        {
            "env": "roach",
            "agent": "word"
        },
        {
            "env": "drone",
            "agent": "word"
        },
        {
            "env": "trunk",
            "agent": "word"
        },
        {
            "env": "monster",
            "agent": "seven"
        },
        {
            "env": "niche",
            "agent": "word"
        },
        {
            "env": "story",
            "agent": "word"
        },
        {
            "env": "viper",
            "agent": "word"
        },
        {
            "env": "barge",
            "agent": "word"
        },
        {
            "env": "bacon",
            "agent": "word"
        },
        {
            "env": "crime",
            "agent": "word"
        },
        {
            "env": "guilt",
            "agent": "word"
        },
        {
            "env": "pleat",
            "agent": "word"
        },
        {
            "env": "layer",
            "agent": "word"
        },
        {
            "env": "lemon",
            "agent": "word"
        },
        {
            "env": "shrub",
            "agent": "word"
        },
        {
            "env": "viral",
            "agent": "word"
        },
        {
            "env": "modal",
            "agent": "word"
        },
        {
            "env": "swirl",
            "agent": "word"
        },
        {
            "env": "filmy",
            "agent": "word"
        },
        {
            "env": "foam",
            "agent": "four"
        },
        {
            "env": "fairy",
            "agent": "word"
        },
        {
            "env": "bunch",
            "agent": "word"
        },
        {
            "env": "clued",
            "agent": "word"
        },
        {
            "env": "thorn",
            "agent": "word"
        },
        {
            "env": "dying",
            "agent": "word"
        },
        {
            "env": "salty",
            "agent": "word"
        },
        {
            "env": "plait",
            "agent": "word"
        },
        {
            "env": "angry",
            "agent": "word"
        },
        {
            "env": "cream",
            "agent": "word"
        },
        {
            "env": "haven",
            "agent": "word"
        },
        {
            "env": "shade",
            "agent": "word"
        },
        {
            "env": "braid",
            "agent": "word"
        },
        {
            "env": "grace",
            "agent": "word"
        },
        {
            "env": "botch",
            "agent": "word"
        },
        {
            "env": "blond",
            "agent": "word"
        },
        {
            "env": "hymen",
            "agent": "word"
        },
        {
            "env": "phase",
            "agent": "word"
        },
        {
            "env": "choke",
            "agent": "word"
        },
        {
            "env": "dozen",
            "agent": "word"
        },
        {
            "env": "crane",
            "agent": "word"
        },
        {
            "env": "slide",
            "agent": "word"
        },
        {
            "env": "slung",
            "agent": "word"
        },
        {
            "env": "oxide",
            "agent": "word"
        },
        {
            "env": "aside",
            "agent": "word"
        },
        {
            "env": "crash",
            "agent": "word"
        },
        {
            "env": "tripe",
            "agent": "word"
        },
        {
            "env": "quack",
            "agent": "word"
        },
        {
            "env": "draft",
            "agent": "word"
        },
        {
            "env": "valor",
            "agent": "word"
        },
        {
            "env": "hotel",
            "agent": "word"
        },
        {
            "env": "whisk",
            "agent": "word"
        },
        {
            "env": "delta",
            "agent": "word"
        },
        {
            "env": "rowdy",
            "agent": "word"
        },
        {
            "env": "mouth",
            "agent": "word"
        },
        {
            "env": "after",
            "agent": "word"
        },
        {
            "env": "proxy",
            "agent": "word"
        },
        {
            "env": "shard",
            "agent": "word"
        },
        {
            "env": "binge",
            "agent": "word"
        },
        {
            "env": "poesy",
            "agent": "word"
        },
        {
            "env": "copse",
            "agent": "word"
        },
        {
            "env": "grime",
            "agent": "word"
        },
        {
            "env": "windy",
            "agent": "word"
        },
        {
            "env": "afoul",
            "agent": "word"
        },
        {
            "env": "value",
            "agent": "word"
        },
        {
            "env": "waste",
            "agent": "word"
        },
        {
            "env": "thank",
            "agent": "word"
        },
        {
            "env": "wider",
            "agent": "word"
        },
        {
            "env": "abort",
            "agent": "word"
        },
        {
            "env": "whack",
            "agent": "word"
        },
        {
            "env": "lager",
            "agent": "word"
        },
        {
            "env": "sunlight",
            "agent": "eight"
        },
        {
            "env": "curse",
            "agent": "word"
        },
        {
            "env": "liken",
            "agent": "word"
        },
        {
            "env": "frond",
            "agent": "word"
        },
        {
            "env": "money",
            "agent": "word"
        },
        {
            "env": "sigma",
            "agent": "word"
        },
        {
            "env": "admin",
            "agent": "word"
        },
        {
            "env": "caulk",
            "agent": "word"
        },
        {
            "env": "jaunt",
            "agent": "word"
        },
        {
            "env": "raspy",
            "agent": "word"
        },
        {
            "env": "bridge",
            "agent": "six"
        },
        {
            "env": "hunter",
            "agent": "six"
        },
        {
            "env": "stake",
            "agent": "word"
        },
        {
            "env": "clung",
            "agent": "word"
        },
        {
            "env": "skate",
            "agent": "word"
        },
        {
            "env": "ultra",
            "agent": "word"
        },
        {
            "env": "alert",
            "agent": "word"
        },
        {
            "env": "rainy",
            "agent": "word"
        },
        {
            "env": "cameo",
            "agent": "word"
        },
        {
            "env": "melon",
            "agent": "word"
        },
        {
            "env": "pedal",
            "agent": "word"
        },
        {
            "env": "vertical",
            "agent": "eight"
        },
        {
            "env": "fudge",
            "agent": "word"
        },
        {
            "env": "enquiry",
            "agent": "seven"
        },
        {
            "env": "flaky",
            "agent": "word"
        },
        {
            "env": "abled",
            "agent": "word"
        },
        {
            "env": "guest",
            "agent": "word"
        },
        {
            "env": "bilge",
            "agent": "word"
        },
        {
            "env": "coral",
            "agent": "word"
        },
        {
            "env": "craze",
            "agent": "word"
        },
        {
            "env": "zonal",
            "agent": "word"
        },
        {
            "env": "anode",
            "agent": "word"
        },
        {
            "env": "crazy",
            "agent": "word"
        },
        {
            "env": "knelt",
            "agent": "word"
        },
        {
            "env": "nadir",
            "agent": "word"
        },
        {
            "env": "nurse",
            "agent": "word"
        },
        {
            "env": "churn",
            "agent": "word"
        },
        {
            "env": "rogue",
            "agent": "word"
        },
        {
            "env": "abuse",
            "agent": "word"
        },
        {
            "env": "stony",
            "agent": "word"
        },
        {
            "env": "bylaw",
            "agent": "word"
        },
        {
            "env": "marsh",
            "agent": "word"
        },
        {
            "env": "frost",
            "agent": "word"
        },
        {
            "env": "metro",
            "agent": "word"
        },
        {
            "env": "tough",
            "agent": "word"
        },
        {
            "env": "trim",
            "agent": "four"
        },
        {
            "env": "major",
            "agent": "word"
        },
        {
            "env": "stream",
            "agent": "six"
        },
        {
            "env": "anvil",
            "agent": "word"
        },
        {
            "env": "frock",
            "agent": "word"
        },
        {
            "env": "fiber",
            "agent": "word"
        },
        {
            "env": "blown",
            "agent": "word"
        },
        {
            "env": "slurp",
            "agent": "word"
        },
        {
            "env": "porch",
            "agent": "word"
        },
        {
            "env": "bound",
            "agent": "word"
        },
        {
            "env": "lunge",
            "agent": "word"
        },
        {
            "env": "madly",
            "agent": "word"
        },
        {
            "env": "sandbox",
            "agent": "seven"
        },
        {
            "env": "broke",
            "agent": "word"
        },
        {
            "env": "humid",
            "agent": "word"
        },
        {
            "env": "mince",
            "agent": "word"
        },
        {
            "env": "orbit",
            "agent": "word"
        },
        {
            "env": "crest",
            "agent": "word"
        },
        {
            "env": "dimly",
            "agent": "word"
        },
        {
            "env": "blade",
            "agent": "word"
        },
        {
            "env": "those",
            "agent": "word"
        },
        {
            "env": "safer",
            "agent": "word"
        },
        {
            "env": "flora",
            "agent": "word"
        },
        {
            "env": "grade",
            "agent": "word"
        },
        {
            "env": "found",
            "agent": "word"
        },
        {
            "env": "paint",
            "agent": "word"
        },
        {
            "env": "empty",
            "agent": "word"
        },
        {
            "env": "bend",
            "agent": "four"
        },
        {
            "env": "spurt",
            "agent": "word"
        },
        {
            "env": "swamp",
            "agent": "word"
        },
        {
            "env": "chunk",
            "agent": "word"
        },
        {
            "env": "irony",
            "agent": "word"
        },
        {
            "env": "plank",
            "agent": "word"
        },
        {
            "env": "talon",
            "agent": "word"
        },
        {
            "env": "shelf",
            "agent": "word"
        },
        {
            "env": "stump",
            "agent": "word"
        },
        {
            "env": "drift",
            "agent": "word"
        },
        {
            "env": "snake",
            "agent": "word"
        },
        {
            "env": "intro",
            "agent": "word"
        },
        {
            "env": "dream",
            "agent": "word"
        },
        {
            "env": "relic",
            "agent": "word"
        },
        {
            "env": "youth",
            "agent": "word"
        },
        {
            "env": "drain",
            "agent": "word"
        },
        {
            "env": "stack",
            "agent": "word"
        },
        {
            "env": "slope",
            "agent": "word"
        },
        {
            "env": "inbox",
            "agent": "word"
        },
        {
            "env": "guard",
            "agent": "word"
        },
        {
            "env": "trope",
            "agent": "word"
        },
        {
            "env": "towel",
            "agent": "word"
        },
        {
            "env": "along",
            "agent": "word"
        },
        {
            "env": "louse",
            "agent": "word"
        },
        {
            "env": "sower",
            "agent": "word"
        },
        {
            "env": "learn",
            "agent": "word"
        },
        {
            "env": "snuck",
            "agent": "word"
        },
        {
            "env": "wafer",
            "agent": "word"
        },
        {
            "env": "curtain",
            "agent": "seven"
        },
        {
            "env": "acrid",
            "agent": "word"
        },
        {
            "env": "pecan",
            "agent": "word"
        },
        {
            "env": "input",
            "agent": "word"
        },
        {
            "env": "leafy",
            "agent": "word"
        },
        {
            "env": "today",
            "agent": "word"
        },
        {
            "env": "rusty",
            "agent": "word"
        },
        {
            "env": "elbow",
            "agent": "word"
        },
        {
            "env": "rebut",
            "agent": "word"
        },
        {
            "env": "debar",
            "agent": "word"
        },
        {
            "env": "coven",
            "agent": "word"
        },
        {
            "env": "tamer",
            "agent": "word"
        },
        {
            "env": "clue",
            "agent": "four"
        },
        {
            "env": "pesky",
            "agent": "word"
        },
        {
            "env": "sneak",
            "agent": "word"
        },
        {
            "env": "hoist",
            "agent": "word"
        },
        {
            "env": "awoke",
            "agent": "word"
        },
        {
            "env": "dwelt",
            "agent": "word"
        },
        {
            "env": "flint",
            "agent": "word"
        },
        {
            "env": "chide",
            "agent": "word"
        },
        {
            "env": "crawl",
            "agent": "word"
        },
        {
            "env": "round",
            "agent": "word"
        },
        {
            "env": "smoke",
            "agent": "word"
        },
        {
            "env": "pivot",
            "agent": "word"
        },
        {
            "env": "ascot",
            "agent": "word"
        },
        {
            "env": "brigade",
            "agent": "seven"
        },
        {
            "env": "chest",
            "agent": "word"
        },
        {
            "env": "flush",
            "agent": "word"
        },
        {
            "env": "their",
            "agent": "word"
        },
        {
            "env": "upset",
            "agent": "word"
        },
        {
            "env": "older",
            "agent": "word"
        },
        {
            "env": "stair",
            "agent": "word"
        },
        {
            "env": "shield",
            "agent": "six"
        },
        {
            "env": "gawky",
            "agent": "word"
        },
        {
            "env": "filet",
            "agent": "word"
        },
        {
            "env": "adopt",
            "agent": "word"
        },
        {
            "env": "fetid",
            "agent": "word"
        },
        {
            "env": "sinew",
            "agent": "word"
        },
        {
            "env": "bland",
            "agent": "word"
        },
        {
            "env": "axion",
            "agent": "word"
        },
        {
            "env": "clove",
            "agent": "word"
        },
        {
            "env": "bough",
            "agent": "word"
        },
        {
            "env": "crank",
            "agent": "word"
        },
        {
            "env": "handy",
            "agent": "word"
        },
        {
            "env": "thick",
            "agent": "word"
        },
        {
            "env": "leapt",
            "agent": "word"
        },
        {
            "env": "envoy",
            "agent": "word"
        },
        {
            "env": "phone",
            "agent": "word"
        },
        {
            "env": "zebra",
            "agent": "word"
        },
        {
            "env": "wharf",
            "agent": "word"
        },
        {
            "env": "aisle",
            "agent": "word"
        },
        {
            "env": "onset",
            "agent": "word"
        },
        {
            "env": "think",
            "agent": "word"
        },
        {
            "env": "shine",
            "agent": "word"
        },
        {
            "env": "maybe",
            "agent": "word"
        },
        {
            "env": "realm",
            "agent": "word"
        },
        {
            "env": "grand",
            "agent": "word"
        },
        {
            "env": "mocha",
            "agent": "word"
        },
        {
            "env": "cheap",
            "agent": "word"
        },
        {
            "env": "flick",
            "agent": "word"
        },
        {
            "env": "curly",
            "agent": "word"
        },
        {
            "env": "bloat",
            "agent": "word"
        },
        {
            "env": "briny",
            "agent": "word"
        },
        {
            "env": "quiet",
            "agent": "word"
        },
        {
            "env": "micro",
            "agent": "word"
        },
        {
            "env": "mount",
            "agent": "word"
        },
        {
            "env": "cruel",
            "agent": "word"
        },
        {
            "env": "focal",
            "agent": "word"
        },
        {
            "env": "inter",
            "agent": "word"
        },
        {
            "env": "worst",
            "agent": "word"
        },
        {
            "env": "dingo",
            "agent": "word"
        },
        {
            "env": "tepid",
            "agent": "word"
        },
        {
            "env": "recap",
            "agent": "word"
        },
        {
            "env": "glide",
            "agent": "word"
        },
        {
            "env": "bawdy",
            "agent": "word"
        },
        {
            "env": "brunt",
            "agent": "word"
        },
        {
            "env": "praise",
            "agent": "six"
        },
        {
            "env": "smack",
            "agent": "word"
        },
        {
            "env": "spank",
            "agent": "word"
        },
        {
            "env": "fraud",
            "agent": "word"
        },
        {
            "env": "chaos",
            "agent": "word"
        },
        {
            "env": "beard",
            "agent": "word"
        },
        {
            "env": "aphid",
            "agent": "word"
        },
        {
            "env": "chute",
            "agent": "word"
        },
        {
            "env": "sonic",
            "agent": "word"
        },
        {
            "env": "blame",
            "agent": "word"
        },
        {
            "env": "irate",
            "agent": "word"
        },
        {
            "env": "trice",
            "agent": "word"
        },
        {
            "env": "maize",
            "agent": "word"
        },
        {
            "env": "recut",
            "agent": "word"
        },
        {
            "env": "viola",
            "agent": "word"
        },
        {
            "env": "saint",
            "agent": "word"
        },
        {
            "env": "shank",
            "agent": "word"
        },
        {
            "env": "claim",
            "agent": "word"
        },
        {
            "env": "voter",
            "agent": "word"
        },
        {
            "env": "scaly",
            "agent": "word"
        },
        {
            "env": "toxic",
            "agent": "word"
        },
        {
            "env": "stein",
            "agent": "word"
        },
        {
            "env": "producing",
            "agent": "nine"
        },
        {
            "env": "rayon",
            "agent": "word"
        },
        {
            "env": "thread",
            "agent": "six"
        },
        {
            "env": "clay",
            "agent": "four"
        },
        {
            "env": "fixer",
            "agent": "word"
        },
        {
            "env": "swine",
            "agent": "word"
        },
        {
            "env": "knife",
            "agent": "word"
        },
        {
            "env": "burnt",
            "agent": "word"
        },
        {
            "env": "toxin",
            "agent": "word"
        },
        {
            "env": "filer",
            "agent": "word"
        },
        {
            "env": "arose",
            "agent": "word"
        },
        {
            "env": "threw",
            "agent": "word"
        },
        {
            "env": "unfed",
            "agent": "word"
        },
        {
            "env": "gayer",
            "agent": "word"
        },
        {
            "env": "weird",
            "agent": "word"
        },
        {
            "env": "grip",
            "agent": "four"
        },
        {
            "env": "cling",
            "agent": "word"
        },
        {
            "env": "felon",
            "agent": "word"
        },
        {
            "env": "place",
            "agent": "word"
        },
        {
            "env": "saucy",
            "agent": "word"
        },
        {
            "env": "react",
            "agent": "word"
        },
        {
            "env": "discovery",
            "agent": "nine"
        },
        {
            "env": "beach",
            "agent": "word"
        },
        {
            "env": "shunt",
            "agent": "word"
        },
        {
            "env": "forest",
            "agent": "six"
        },
        {
            "env": "ulcer",
            "agent": "word"
        },
        {
            "env": "grape",
            "agent": "word"
        },
        {
            "env": "bused",
            "agent": "word"
        },
        {
            "env": "fish",
            "agent": "four"
        },
        {
            "env": "wring",
            "agent": "word"
        },
        {
            "env": "swift",
            "agent": "word"
        },
        {
            "env": "scrub",
            "agent": "word"
        },
        {
            "env": "equation",
            "agent": "eight"
        },
        {
            "env": "sunbeam",
            "agent": "seven"
        },
        {
            "env": "spurn",
            "agent": "word"
        },
        {
            "env": "rhyme",
            "agent": "word"
        },
        {
            "env": "quail",
            "agent": "word"
        },
        {
            "env": "heavy",
            "agent": "word"
        },
        {
            "env": "lousy",
            "agent": "word"
        },
        {
            "env": "lunch",
            "agent": "word"
        },
        {
            "env": "filth",
            "agent": "word"
        },
        {
            "env": "joker",
            "agent": "word"
        },
        {
            "env": "scour",
            "agent": "word"
        },
        {
            "env": "worse",
            "agent": "word"
        },
        {
            "env": "wheat",
            "agent": "word"
        },
        {
            "env": "doubt",
            "agent": "word"
        },
        {
            "env": "carol",
            "agent": "word"
        },
        {
            "env": "gravy",
            "agent": "word"
        },
        {
            "env": "drank",
            "agent": "word"
        },
        {
            "env": "thief",
            "agent": "word"
        },
        {
            "env": "large",
            "agent": "word"
        },
        {
            "env": "least",
            "agent": "word"
        },
        {
            "env": "tidal",
            "agent": "word"
        },
        {
            "env": "scrape",
            "agent": "six"
        },
        {
            "env": "panic",
            "agent": "word"
        },
        {
            "env": "break",
            "agent": "word"
        },
        {
            "env": "flack",
            "agent": "word"
        },
        {
            "env": "swami",
            "agent": "word"
        },
        {
            "env": "whale",
            "agent": "word"
        },
        {
            "env": "cider",
            "agent": "word"
        },
        {
            "env": "sword",
            "agent": "word"
        },
        {
            "env": "dopey",
            "agent": "word"
        },
        {
            "env": "cavil",
            "agent": "word"
        },
        {
            "env": "world",
            "agent": "word"
        },
        {
            "env": "pause",
            "agent": "word"
        },
        {
            "env": "mouse",
            "agent": "word"
        },
        {
            "env": "final",
            "agent": "word"
        },
        {
            "env": "usher",
            "agent": "word"
        },
        {
            "env": "owing",
            "agent": "word"
        },
        {
            "env": "woman",
            "agent": "word"
        },
        {
            "env": "reign",
            "agent": "word"
        },
        {
            "env": "opera",
            "agent": "word"
        },
        {
            "env": "groan",
            "agent": "word"
        },
        {
            "env": "drape",
            "agent": "word"
        },
        {
            "env": "heart",
            "agent": "word"
        },
        {
            "env": "medal",
            "agent": "word"
        },
        {
            "env": "lumen",
            "agent": "word"
        },
        {
            "env": "thump",
            "agent": "word"
        },
        {
            "env": "star",
            "agent": "four"
        },
        {
            "env": "alive",
            "agent": "word"
        },
        {
            "env": "given",
            "agent": "word"
        },
        {
            "env": "garden",
            "agent": "six"
        },
        {
            "env": "teach",
            "agent": "word"
        },
        {
            "env": "remit",
            "agent": "word"
        },
        {
            "env": "guile",
            "agent": "word"
        },
        {
            "env": "patch",
            "agent": "word"
        },
        {
            "env": "logic",
            "agent": "word"
        },
        {
            "env": "bird",
            "agent": "four"
        },
        {
            "env": "fetch",
            "agent": "word"
        },
        {
            "env": "ramen",
            "agent": "word"
        },
        {
            "env": "print",
            "agent": "word"
        },
        {
            "env": "vomit",
            "agent": "word"
        },
        {
            "env": "vault",
            "agent": "word"
        },
        {
            "env": "personal",
            "agent": "eight"
        },
        {
            "env": "bloke",
            "agent": "word"
        },
        {
            "env": "metal",
            "agent": "word"
        },
        {
            "env": "brawl",
            "agent": "word"
        },
        {
            "env": "dairy",
            "agent": "word"
        },
        {
            "env": "smile",
            "agent": "word"
        },
        {
            "env": "alter",
            "agent": "word"
        },
        {
            "env": "drown",
            "agent": "word"
        },
        {
            "env": "wrap",
            "agent": "four"
        },
        {
            "env": "victory",
            "agent": "seven"
        },
        {
            "env": "freak",
            "agent": "word"
        },
        {
            "env": "guise",
            "agent": "word"
        },
        {
            "env": "line",
            "agent": "four"
        },
        {
            "env": "false",
            "agent": "word"
        },
        {
            "env": "card",
            "agent": "four"
        },
        {
            "env": "loamy",
            "agent": "word"
        },
        {
            "env": "yacht",
            "agent": "word"
        },
        {
            "env": "ombre",
            "agent": "word"
        },
        {
            "env": "snide",
            "agent": "word"
        },
        {
            "env": "wield",
            "agent": "word"
        },
        {
            "env": "meant",
            "agent": "word"
        },
        {
            "env": "sandy",
            "agent": "word"
        },
        {
            "env": "clown",
            "agent": "word"
        },
        {
            "env": "shirt",
            "agent": "word"
        },
        {
            "env": "token",
            "agent": "word"
        },
        {
            "env": "blend",
            "agent": "word"
        },
        {
            "env": "solid",
            "agent": "word"
        },
        {
            "env": "lusty",
            "agent": "word"
        },
        {
            "env": "spear",
            "agent": "word"
        },
        {
            "env": "shorn",
            "agent": "word"
        },
        {
            "env": "mangy",
            "agent": "word"
        },
        {
            "env": "cairn",
            "agent": "word"
        },
        {
            "env": "tumor",
            "agent": "word"
        },
        {
            "env": "fortune",
            "agent": "seven"
        },
        {
            "env": "storage",
            "agent": "seven"
        },
        {
            "env": "mile",
            "agent": "four"
        },
        {
            "env": "exact",
            "agent": "word"
        },
        {
            "env": "halve",
            "agent": "word"
        },
        {
            "env": "palm",
            "agent": "four"
        },
        {
            "env": "girth",
            "agent": "word"
        },
        {
            "env": "split",
            "agent": "word"
        },
        {
            "env": "bring",
            "agent": "word"
        },
        {
            "env": "peach",
            "agent": "word"
        },
        {
            "env": "lower",
            "agent": "word"
        },
        {
            "env": "blaze",
            "agent": "word"
        },
        {
            "env": "gamer",
            "agent": "word"
        },
        {
            "env": "ripen",
            "agent": "word"
        },
        {
            "env": "vegan",
            "agent": "word"
        },
        {
            "env": "minor",
            "agent": "word"
        },
        {
            "env": "field",
            "agent": "word"
        },
        {
            "env": "belt",
            "agent": "four"
        },
        {
            "env": "acute",
            "agent": "word"
        },
        {
            "env": "buxom",
            "agent": "word"
        },
        {
            "env": "wolf",
            "agent": "four"
        },
        {
            "env": "shaft",
            "agent": "word"
        },
        {
            "env": "amity",
            "agent": "word"
        },
        {
            "env": "primo",
            "agent": "word"
        },
        {
            "env": "plume",
            "agent": "word"
        },
        {
            "env": "charm",
            "agent": "word"
        },
        {
            "env": "navel",
            "agent": "word"
        },
        {
            "env": "cried",
            "agent": "word"
        },
        {
            "env": "blind",
            "agent": "word"
        },
        {
            "env": "dough",
            "agent": "word"
        },
        {
            "env": "barn",
            "agent": "four"
        },
        {
            "env": "ficus",
            "agent": "word"
        },
        {
            "env": "spilt",
            "agent": "word"
        },
        {
            "env": "sphinx",
            "agent": "six"
        },
        {
            "env": "slime",
            "agent": "word"
        },
        {
            "env": "steam",
            "agent": "word"
        },
        {
            "env": "chain",
            "agent": "word"
        },
        {
            "env": "bicep",
            "agent": "word"
        },
        {
            "env": "tubal",
            "agent": "word"
        },
        {
            "env": "diver",
            "agent": "word"
        },
        {
            "env": "bathe",
            "agent": "word"
        },
        {
            "env": "super",
            "agent": "word"
        },
        {
            "env": "mucky",
            "agent": "word"
        },
        {
            "env": "glow",
            "agent": "four"
        },
        {
            "env": "lucky",
            "agent": "word"
        },
        {
            "env": "moldy",
            "agent": "word"
        },
        {
            "env": "clamp",
            "agent": "word"
        },
        {
            "env": "setup",
            "agent": "word"
        },
        {
            "env": "risen",
            "agent": "word"
        },
        {
            "env": "showy",
            "agent": "word"
        },
        {
            "env": "helix",
            "agent": "word"
        },
        {
            "env": "spore",
            "agent": "word"
        },
        {
            "env": "waltz",
            "agent": "word"
        },
        {
            "env": "stamp",
            "agent": "word"
        },
        {
            "env": "veil",
            "agent": "four"
        },
        {
            "env": "mound",
            "agent": "word"
        },
        {
            "env": "vodka",
            "agent": "word"
        },
        {
            "env": "shark",
            "agent": "word"
        },
        {
            "env": "chemistry",
            "agent": "nine"
        },
        {
            "env": "grout",
            "agent": "word"
        },
        {
            "env": "rhino",
            "agent": "word"
        },
        {
            "env": "wimpy",
            "agent": "word"
        },
        {
            "env": "shone",
            "agent": "word"
        },
        {
            "env": "clear",
            "agent": "word"
        },
        {
            "env": "disco",
            "agent": "word"
        },
        {
            "env": "baste",
            "agent": "word"
        },
        {
            "env": "munch",
            "agent": "word"
        },
        {
            "env": "entry",
            "agent": "word"
        },
        {
            "env": "unmet",
            "agent": "word"
        },
        {
            "env": "media",
            "agent": "word"
        },
        {
            "env": "fragment",
            "agent": "eight"
        },
        {
            "env": "space",
            "agent": "word"
        },
        {
            "env": "crude",
            "agent": "word"
        },
        {
            "env": "sloth",
            "agent": "word"
        },
        {
            "env": "topic",
            "agent": "word"
        },
        {
            "env": "uncle",
            "agent": "word"
        },
        {
            "env": "goner",
            "agent": "word"
        },
        {
            "env": "clean",
            "agent": "word"
        },
        {
            "env": "spiel",
            "agent": "word"
        },
        {
            "env": "stink",
            "agent": "word"
        },
        {
            "env": "nosey",
            "agent": "word"
        },
        {
            "env": "curio",
            "agent": "word"
        },
        {
            "env": "shadow",
            "agent": "six"
        },
        {
            "env": "prong",
            "agent": "word"
        },
        {
            "env": "laundry",
            "agent": "seven"
        },
        {
            "env": "tilde",
            "agent": "word"
        },
        {
            "env": "scowl",
            "agent": "word"
        },
        {
            "env": "befit",
            "agent": "word"
        },
        {
            "env": "flier",
            "agent": "word"
        },
        {
            "env": "smelt",
            "agent": "word"
        },
        {
            "env": "homer",
            "agent": "word"
        },
        {
            "env": "brash",
            "agent": "word"
        },
        {
            "env": "banjo",
            "agent": "word"
        },
        {
            "env": "torch",
            "agent": "word"
        },
        {
            "env": "unfit",
            "agent": "word"
        },
        {
            "env": "rumba",
            "agent": "word"
        },
        {
            "env": "idler",
            "agent": "word"
        },
        {
            "env": "could",
            "agent": "word"
        },
        {
            "env": "leach",
            "agent": "word"
        },
        {
            "env": "prude",
            "agent": "word"
        },
        {
            "env": "leash",
            "agent": "word"
        },
        {
            "env": "flight",
            "agent": "six"
        },
        {
            "env": "notch",
            "agent": "word"
        },
        {
            "env": "stone",
            "agent": "word"
        },
        {
            "env": "finch",
            "agent": "word"
        },
        {
            "env": "style",
            "agent": "word"
        },
        {
            "env": "lover",
            "agent": "word"
        },
        {
            "env": "bayou",
            "agent": "word"
        },
        {
            "env": "merit",
            "agent": "word"
        },
        {
            "env": "overt",
            "agent": "word"
        },
        {
            "env": "noble",
            "agent": "word"
        },
        {
            "env": "slab",
            "agent": "four"
        },
        {
            "env": "petal",
            "agent": "word"
        },
        {
            "env": "crisp",
            "agent": "word"
        },
        {
            "env": "ashen",
            "agent": "word"
        },
        {
            "env": "sixth",
            "agent": "word"
        },
        {
            "env": "quoth",
            "agent": "word"
        },
        {
            "env": "steal",
            "agent": "word"
        },
        {
            "env": "slant",
            "agent": "word"
        },
        {
            "env": "align",
            "agent": "word"
        },
        {
            "env": "beady",
            "agent": "word"
        },
        {
            "env": "shear",
            "agent": "word"
        },
        {
            "env": "datum",
            "agent": "word"
        },
        {
            "env": "echo",
            "agent": "four"
        },
        {
            "env": "court",
            "agent": "word"
        },
        {
            "env": "steak",
            "agent": "word"
        },
        {
            "env": "third",
            "agent": "word"
        },
        {
            "env": "glint",
            "agent": "word"
        },
        {
            "env": "basil",
            "agent": "word"
        },
        {
            "env": "decor",
            "agent": "word"
        },
        {
            "env": "creak",
            "agent": "word"
        },
        {
            "env": "fire",
            "agent": "four"
        },
        {
            "env": "picky",
            "agent": "word"
        },
        {
            "env": "tipsy",
            "agent": "word"
        },
        {
            "env": "spunk",
            "agent": "word"
        },
        {
            "env": "warty",
            "agent": "word"
        },
        {
            "env": "decay",
            "agent": "word"
        },
        {
            "env": "lingo",
            "agent": "word"
        },
        {
            "env": "audio",
            "agent": "word"
        },
        {
            "env": "death",
            "agent": "word"
        },
        {
            "env": "email",
            "agent": "word"
        },
        {
            "env": "basic",
            "agent": "word"
        },
        {
            "env": "avoid",
            "agent": "word"
        },
        {
            "env": "salon",
            "agent": "word"
        },
        {
            "env": "dumpy",
            "agent": "word"
        },
        {
            "env": "ranch",
            "agent": "word"
        },
        {
            "env": "point",
            "agent": "word"
        },
        {
            "env": "snarl",
            "agent": "word"
        },
        {
            "env": "doing",
            "agent": "word"
        },
        {
            "env": "pinky",
            "agent": "word"
        },
        {
            "env": "smear",
            "agent": "word"
        },
        {
            "env": "music",
            "agent": "word"
        },
        {
            "env": "grope",
            "agent": "word"
        },
        {
            "env": "project",
            "agent": "seven"
        },
        {
            "env": "elfin",
            "agent": "word"
        },
        {
            "env": "pasty",
            "agent": "word"
        },
        {
            "env": "shrug",
            "agent": "word"
        },
        {
            "env": "ebony",
            "agent": "word"
        },
        {
            "env": "prime",
            "agent": "word"
        },
        {
            "env": "tread",
            "agent": "word"
        },
        {
            "env": "plant",
            "agent": "word"
        },
        {
            "env": "quick",
            "agent": "word"
        },
        {
            "env": "chord",
            "agent": "word"
        },
        {
            "env": "bulge",
            "agent": "word"
        },
        {
            "env": "finer",
            "agent": "word"
        },
        {
            "env": "quote",
            "agent": "word"
        },
        {
            "env": "flock",
            "agent": "word"
        },
        {
            "env": "stuck",
            "agent": "word"
        },
        {
            "env": "untie",
            "agent": "word"
        },
        {
            "env": "musky",
            "agent": "word"
        },
        {
            "env": "wispy",
            "agent": "word"
        },
        {
            "env": "spent",
            "agent": "word"
        },
        {
            "env": "sound",
            "agent": "word"
        },
        {
            "env": "haute",
            "agent": "word"
        },
        {
            "env": "daily",
            "agent": "word"
        },
        {
            "env": "qualm",
            "agent": "word"
        },
        {
            "env": "mango",
            "agent": "word"
        },
        {
            "env": "acorn",
            "agent": "word"
        },
        {
            "env": "macho",
            "agent": "word"
        },
        {
            "env": "whirl",
            "agent": "word"
        },
        {
            "env": "bishop",
            "agent": "six"
        },
        {
            "env": "boule",
            "agent": "word"
        },
        {
            "env": "spied",
            "agent": "word"
        },
        {
            "env": "magnitude",
            "agent": "nine"
        },
        {
            "env": "pansy",
            "agent": "word"
        },
        {
            "env": "endow",
            "agent": "word"
        },
        {
            "env": "mange",
            "agent": "word"
        },
        {
            "env": "ocean",
            "agent": "word"
        },
        {
            "env": "forth",
            "agent": "word"
        },
        {
            "env": "blitz",
            "agent": "word"
        },
        {
            "env": "front",
            "agent": "word"
        },
        {
            "env": "usage",
            "agent": "word"
        },
        {
            "env": "gate",
            "agent": "four"
        },
        {
            "env": "power",
            "agent": "word"
        },
        {
            "env": "soapy",
            "agent": "word"
        },
        {
            "env": "equal",
            "agent": "word"
        },
        {
            "env": "guide",
            "agent": "word"
        },
        {
            "env": "unset",
            "agent": "word"
        },
        {
            "env": "agile",
            "agent": "word"
        },
        {
            "env": "black",
            "agent": "word"
        },
        {
            "env": "prose",
            "agent": "word"
        },
        {
            "env": "dicey",
            "agent": "word"
        },
        {
            "env": "pudgy",
            "agent": "word"
        },
        {
            "env": "journey",
            "agent": "seven"
        },
        {
            "env": "cadet",
            "agent": "word"
        },
        {
            "env": "right",
            "agent": "word"
        },
        {
            "env": "foist",
            "agent": "word"
        },
        {
            "env": "snack",
            "agent": "word"
        },
        {
            "env": "cover",
            "agent": "word"
        },
        {
            "env": "demon",
            "agent": "word"
        },
        {
            "env": "horn",
            "agent": "four"
        },
        {
            "env": "tapir",
            "agent": "word"
        },
        {
            "env": "valet",
            "agent": "word"
        },
        {
            "env": "stoke",
            "agent": "word"
        },
        {
            "env": "wrong",
            "agent": "word"
        },
        {
            "env": "eying",
            "agent": "word"
        },
        {
            "env": "tonga",
            "agent": "word"
        },
        {
            "env": "waver",
            "agent": "word"
        },
        {
            "env": "whine",
            "agent": "word"
        },
        {
            "env": "vocal",
            "agent": "word"
        },
        {
            "env": "human",
            "agent": "word"
        },
        {
            "env": "prize",
            "agent": "word"
        },
        {
            "env": "morph",
            "agent": "word"
        },
        {
            "env": "broad",
            "agent": "word"
        },
        {
            "env": "trail",
            "agent": "word"
        },
        {
            "env": "tray",
            "agent": "four"
        },
        {
            "env": "vogue",
            "agent": "word"
        },
        {
            "env": "word",
            "agent": "four"
        },
        {
            "env": "flung",
            "agent": "word"
        },
        {
            "env": "pinto",
            "agent": "word"
        },
        {
            "env": "hyper",
            "agent": "word"
        },
        {
            "env": "inept",
            "agent": "word"
        },
        {
            "env": "smite",
            "agent": "word"
        },
        {
            "env": "fling",
            "agent": "word"
        },
        {
            "env": "lithe",
            "agent": "word"
        },
        {
            "env": "dancer",
            "agent": "six"
        },
        {
            "env": "dance",
            "agent": "word"
        },
        {
            "env": "fishy",
            "agent": "word"
        },
        {
            "env": "polka",
            "agent": "word"
        },
        {
            "env": "snout",
            "agent": "word"
        },
        {
            "env": "knead",
            "agent": "word"
        },
        {
            "env": "audit",
            "agent": "word"
        },
        {
            "env": "vital",
            "agent": "word"
        },
        {
            "env": "mushy",
            "agent": "word"
        },
        {
            "env": "chief",
            "agent": "word"
        },
        {
            "env": "trump",
            "agent": "word"
        },
        {
            "env": "spoke",
            "agent": "word"
        },
        {
            "env": "debit",
            "agent": "word"
        },
        {
            "env": "heady",
            "agent": "word"
        },
        {
            "env": "truck",
            "agent": "word"
        },
        {
            "env": "tango",
            "agent": "word"
        },
        {
            "env": "sumac",
            "agent": "word"
        },
        {
            "env": "bushy",
            "agent": "word"
        },
        {
            "env": "wave",
            "agent": "four"
        },
        {
            "env": "widen",
            "agent": "word"
        },
        {
            "env": "sonar",
            "agent": "word"
        },
        {
            "env": "awful",
            "agent": "word"
        },
        {
            "env": "shore",
            "agent": "word"
        },
        {
            "env": "newly",
            "agent": "word"
        },
        {
            "env": "shady",
            "agent": "word"
        },
        {
            "env": "portal",
            "agent": "six"
        },
        {
            "env": "pique",
            "agent": "word"
        },
        {
            "env": "flout",
            "agent": "word"
        },
        {
            "env": "glade",
            "agent": "word"
        },
        {
            "env": "hoard",
            "agent": "word"
        },
        {
            "env": "stare",
            "agent": "word"
        },
        {
            "env": "nerdy",
            "agent": "word"
        },
        {
            "env": "plead",
            "agent": "word"
        },
        {
            "env": "lunar",
            "agent": "word"
        },
        {
            "env": "ring",
            "agent": "four"
        },
        {
            "env": "yield",
            "agent": "word"
        },
        {
            "env": "crust",
            "agent": "word"
        },
        {
            "env": "rouse",
            "agent": "word"
        },
        {
            "env": "pulse",
            "agent": "word"
        },
        {
            "env": "macro",
            "agent": "word"
        },
        {
            "env": "sauce",
            "agent": "word"
        },
        {
            "env": "storyline",
            "agent": "nine"
        },
        {
            "env": "shave",
            "agent": "word"
        },
        {
            "env": "brute",
            "agent": "word"
        },
        {
            "env": "hunger",
            "agent": "six"
        },
        {
            "env": "build",
            "agent": "word"
        },
        {
            "env": "bison",
            "agent": "word"
        },
        {
            "env": "baton",
            "agent": "word"
        },
        {
            "env": "jumbo",
            "agent": "word"
        },
        {
            "env": "urban",
            "agent": "word"
        },
        {
            "env": "siren",
            "agent": "word"
        },
        {
            "env": "clash",
            "agent": "word"
        },
        {
            "env": "burly",
            "agent": "word"
        },
        {
            "env": "gland",
            "agent": "word"
        },
        {
            "env": "lurid",
            "agent": "word"
        },
        {
            "env": "grail",
            "agent": "word"
        },
        {
            "env": "simple",
            "agent": "six"
        },
        {
            "env": "taper",
            "agent": "word"
        },
        {
            "env": "juice",
            "agent": "word"
        },
        {
            "env": "eking",
            "agent": "word"
        },
        {
            "env": "flute",
            "agent": "word"
        },
        {
            "env": "derby",
            "agent": "word"
        },
        {
            "env": "verso",
            "agent": "word"
        },
        {
            "env": "musty",
            "agent": "word"
        },
        {
            "env": "tonal",
            "agent": "word"
        },
        {
            "env": "glaze",
            "agent": "word"
        },
        {
            "env": "crown",
            "agent": "word"
        },
        {
            "env": "trove",
            "agent": "word"
        },
        {
            "env": "spike",
            "agent": "word"
        },
        {
            "env": "straw",
            "agent": "word"
        },
        {
            "env": "column",
            "agent": "six"
        },
        {
            "env": "golem",
            "agent": "word"
        },
        {
            "env": "truce",
            "agent": "word"
        },
        {
            "env": "width",
            "agent": "word"
        },
        {
            "env": "rinse",
            "agent": "word"
        },
        {
            "env": "manor",
            "agent": "word"
        },
        {
            "env": "first",
            "agent": "word"
        },
        {
            "env": "artsy",
            "agent": "word"
        },
        {
            "env": "cause",
            "agent": "word"
        },
        {
            "env": "frisk",
            "agent": "word"
        },
        {
            "env": "dowel",
            "agent": "word"
        },
        {
            "env": "venom",
            "agent": "word"
        },
        {
            "env": "canoe",
            "agent": "word"
        },
        {
            "env": "axiom",
            "agent": "word"
        },
        {
            "env": "novel",
            "agent": "word"
        },
        {
            "env": "woven",
            "agent": "word"
        },
        {
            "env": "enjoy",
            "agent": "word"
        },
        {
            "env": "importance",
            "agent": "ten"
        },
        {
            "env": "light",
            "agent": "word"
        },
        {
            "env": "admit",
            "agent": "word"
        },
        {
            "env": "eclat",
            "agent": "word"
        },
        {
            "env": "patio",
            "agent": "word"
        },
        {
            "env": "shame",
            "agent": "word"
        },
        {
            "env": "trade",
            "agent": "word"
        },
        {
            "env": "basin",
            "agent": "word"
        },
        {
            "env": "reach",
            "agent": "word"
        },
        {
            "env": "femur",
            "agent": "word"
        },
        {
            "env": "road",
            "agent": "four"
        },
        {
            "env": "grind",
            "agent": "word"
        },
        {
            "env": "liver",
            "agent": "word"
        },
        {
            "env": "giant",
            "agent": "word"
        },
        {
            "env": "fiery",
            "agent": "word"
        },
        {
            "env": "duvet",
            "agent": "word"
        },
        {
            "env": "balmy",
            "agent": "word"
        },
        {
            "env": "patsy",
            "agent": "word"
        },
        {
            "env": "piney",
            "agent": "word"
        },
        {
            "env": "weigh",
            "agent": "word"
        },
        {
            "env": "shove",
            "agent": "word"
        },
        {
            "env": "edify",
            "agent": "word"
        },
        {
            "env": "index",
            "agent": "word"
        },
        {
            "env": "credo",
            "agent": "word"
        },
        {
            "env": "gaudy",
            "agent": "word"
        },
        {
            "env": "party",
            "agent": "word"
        },
        {
            "env": "wind",
            "agent": "four"
        },
        {
            "env": "dock",
            "agent": "four"
        },
        {
            "env": "brief",
            "agent": "word"
        },
        {
            "env": "price",
            "agent": "word"
        },
        {
            "env": "since",
            "agent": "word"
        },
        {
            "env": "gleam",
            "agent": "word"
        },
        {
            "env": "glance",
            "agent": "six"
        },
        {
            "env": "chore",
            "agent": "word"
        },
        {
            "env": "bedrock",
            "agent": "seven"
        },
        {
            "env": "taker",
            "agent": "word"
        },
        {
            "env": "vicar",
            "agent": "word"
        },
        {
            "env": "handler",
            "agent": "seven"
        },
        {
            "env": "utile",
            "agent": "word"
        },
        {
            "env": "quota",
            "agent": "word"
        },
        {
            "env": "despair",
            "agent": "seven"
        },
        {
            "env": "flame",
            "agent": "word"
        },
        {
            "env": "fetus",
            "agent": "word"
        },
        {
            "env": "tuber",
            "agent": "word"
        },
        {
            "env": "blueprint",
            "agent": "nine"
        },
        {
            "env": "denim",
            "agent": "word"
        },
        {
            "env": "brawn",
            "agent": "word"
        },
        {
            "env": "pencil",
            "agent": "six"
        },
        {
            "env": "glory",
            "agent": "word"
        },
        {
            "env": "shack",
            "agent": "word"
        },
        {
            "env": "caper",
            "agent": "word"
        },
        {
            "env": "model",
            "agent": "word"
        },
        {
            "env": "giver",
            "agent": "word"
        },
        {
            "env": "afire",
            "agent": "word"
        },
        {
            "env": "brave",
            "agent": "word"
        },
        {
            "env": "fleck",
            "agent": "word"
        },
        {
            "env": "thong",
            "agent": "word"
        },
        {
            "env": "hint",
            "agent": "four"
        },
        {
            "env": "miner",
            "agent": "word"
        },
        {
            "env": "chip",
            "agent": "four"
        }
    ],
    "test": [
        {
            "env": "baron",
            "agent": "word"
        },
        {
            "env": "glare",
            "agent": "word"
        },
        {
            "env": "locus",
            "agent": "word"
        },
        {
            "env": "welch",
            "agent": "word"
        },
        {
            "env": "crush",
            "agent": "word"
        },
        {
            "env": "laden",
            "agent": "word"
        },
        {
            "env": "forge",
            "agent": "word"
        },
        {
            "env": "ditch",
            "agent": "word"
        },
        {
            "env": "hairy",
            "agent": "word"
        },
        {
            "env": "nomad",
            "agent": "word"
        },
        {
            "env": "synod",
            "agent": "word"
        },
        {
            "env": "slate",
            "agent": "word"
        },
        {
            "env": "lymph",
            "agent": "word"
        },
        {
            "env": "chalk",
            "agent": "word"
        },
        {
            "env": "heard",
            "agent": "word"
        },
        {
            "env": "built",
            "agent": "word"
        },
        {
            "env": "optic",
            "agent": "word"
        },
        {
            "env": "froth",
            "agent": "word"
        },
        {
            "env": "satin",
            "agent": "word"
        },
        {
            "env": "whiny",
            "agent": "word"
        },
        {
            "env": "slice",
            "agent": "word"
        },
        {
            "env": "chafe",
            "agent": "word"
        },
        {
            "env": "mason",
            "agent": "word"
        },
        {
            "env": "tacky",
            "agent": "word"
        },
        {
            "env": "maker",
            "agent": "word"
        },
        {
            "env": "incur",
            "agent": "word"
        },
        {
            "env": "ovary",
            "agent": "word"
        },
        {
            "env": "quart",
            "agent": "word"
        },
        {
            "env": "thumb",
            "agent": "word"
        },
        {
            "env": "loser",
            "agent": "word"
        },
        {
            "env": "dogma",
            "agent": "word"
        },
        {
            "env": "lance",
            "agent": "word"
        },
        {
            "env": "fecal",
            "agent": "word"
        },
        {
            "env": "chasm",
            "agent": "word"
        },
        {
            "env": "sling",
            "agent": "word"
        },
        {
            "env": "manly",
            "agent": "word"
        },
        {
            "env": "shaky",
            "agent": "word"
        },
        {
            "env": "naive",
            "agent": "word"
        },
        {
            "env": "cabin",
            "agent": "word"
        },
        {
            "env": "bowel",
            "agent": "word"
        },
        {
            "env": "unity",
            "agent": "word"
        },
        {
            "env": "vapor",
            "agent": "word"
        },
        {
            "env": "cargo",
            "agent": "word"
        },
        {
            "env": "blank",
            "agent": "word"
        },
        {
            "env": "forty",
            "agent": "word"
        },
        {
            "env": "flare",
            "agent": "word"
        },
        {
            "env": "plier",
            "agent": "word"
        },
        {
            "env": "robin",
            "agent": "word"
        },
        {
            "env": "whole",
            "agent": "word"
        },
        {
            "env": "swung",
            "agent": "word"
        },
        {
            "env": "broth",
            "agent": "word"
        },
        {
            "env": "amuse",
            "agent": "word"
        },
        {
            "env": "stoic",
            "agent": "word"
        },
        {
            "env": "mayor",
            "agent": "word"
        },
        {
            "env": "perch",
            "agent": "word"
        },
        {
            "env": "spice",
            "agent": "word"
        },
        {
            "env": "gazer",
            "agent": "word"
        },
        {
            "env": "covey",
            "agent": "word"
        },
        {
            "env": "horde",
            "agent": "word"
        },
        {
            "env": "noise",
            "agent": "word"
        },
        {
            "env": "shift",
            "agent": "word"
        },
        {
            "env": "timer",
            "agent": "word"
        },
        {
            "env": "waxen",
            "agent": "word"
        },
        {
            "env": "probe",
            "agent": "word"
        },
        {
            "env": "fibre",
            "agent": "word"
        },
        {
            "env": "tribe",
            "agent": "word"
        },
        {
            "env": "short",
            "agent": "word"
        },
        {
            "env": "crowd",
            "agent": "word"
        },
        {
            "env": "voila",
            "agent": "word"
        },
        {
            "env": "dingy",
            "agent": "word"
        },
        {
            "env": "bingo",
            "agent": "word"
        },
        {
            "env": "track",
            "agent": "word"
        },
        {
            "env": "burst",
            "agent": "word"
        },
        {
            "env": "payer",
            "agent": "word"
        },
        {
            "env": "edict",
            "agent": "word"
        },
        {
            "env": "abhor",
            "agent": "word"
        },
        {
            "env": "frank",
            "agent": "word"
        },
        {
            "env": "farce",
            "agent": "word"
        },
        {
            "env": "argue",
            "agent": "word"
        },
        {
            "env": "prune",
            "agent": "word"
        },
        {
            "env": "piety",
            "agent": "word"
        },
        {
            "env": "faint",
            "agent": "word"
        },
        {
            "env": "slept",
            "agent": "word"
        },
        {
            "env": "pinch",
            "agent": "word"
        },
        {
            "env": "extra",
            "agent": "word"
        },
        {
            "env": "poise",
            "agent": "word"
        },
        {
            "env": "under",
            "agent": "word"
        },
        {
            "env": "relax",
            "agent": "word"
        },
        {
            "env": "islet",
            "agent": "word"
        },
        {
            "env": "quite",
            "agent": "word"
        },
        {
            "env": "visor",
            "agent": "word"
        },
        {
            "env": "foyer",
            "agent": "word"
        },
        {
            "env": "fritz",
            "agent": "word"
        },
        {
            "env": "wight",
            "agent": "word"
        },
        {
            "env": "debut",
            "agent": "word"
        },
        {
            "env": "tempo",
            "agent": "word"
        },
        {
            "env": "spare",
            "agent": "word"
        },
        {
            "env": "saute",
            "agent": "word"
        },
        {
            "env": "thrum",
            "agent": "word"
        },
        {
            "env": "north",
            "agent": "word"
        },
        {
            "env": "askew",
            "agent": "word"
        },
        {
            "env": "extol",
            "agent": "word"
        },
        {
            "env": "harem",
            "agent": "word"
        },
        {
            "env": "croak",
            "agent": "word"
        },
        {
            "env": "horny",
            "agent": "word"
        },
        {
            "env": "flirt",
            "agent": "word"
        },
        {
            "env": "ovine",
            "agent": "word"
        },
        {
            "env": "prank",
            "agent": "word"
        },
        {
            "env": "debug",
            "agent": "word"
        },
        {
            "env": "lying",
            "agent": "word"
        },
        {
            "env": "ankle",
            "agent": "word"
        },
        {
            "env": "crypt",
            "agent": "word"
        },
        {
            "env": "waist",
            "agent": "word"
        },
        {
            "env": "minus",
            "agent": "word"
        },
        {
            "env": "haste",
            "agent": "word"
        },
        {
            "env": "twang",
            "agent": "word"
        },
        {
            "env": "gauze",
            "agent": "word"
        },
        {
            "env": "pesto",
            "agent": "word"
        },
        {
            "env": "wager",
            "agent": "word"
        },
        {
            "env": "mercy",
            "agent": "word"
        },
        {
            "env": "duchy",
            "agent": "word"
        },
        {
            "env": "sweat",
            "agent": "word"
        },
        {
            "env": "droit",
            "agent": "word"
        },
        {
            "env": "cumin",
            "agent": "word"
        },
        {
            "env": "wreck",
            "agent": "word"
        },
        {
            "env": "storm",
            "agent": "word"
        },
        {
            "env": "whelp",
            "agent": "word"
        },
        {
            "env": "fresh",
            "agent": "word"
        },
        {
            "env": "poker",
            "agent": "word"
        },
        {
            "env": "prawn",
            "agent": "word"
        },
        {
            "env": "bonus",
            "agent": "word"
        },
        {
            "env": "night",
            "agent": "word"
        },
        {
            "env": "arise",
            "agent": "word"
        },
        {
            "env": "blush",
            "agent": "word"
        },
        {
            "env": "spiky",
            "agent": "word"
        },
        {
            "env": "gonad",
            "agent": "word"
        },
        {
            "env": "cramp",
            "agent": "word"
        },
        {
            "env": "grunt",
            "agent": "word"
        },
        {
            "env": "knave",
            "agent": "word"
        },
        {
            "env": "prone",
            "agent": "word"
        },
        {
            "env": "query",
            "agent": "word"
        },
        {
            "env": "brace",
            "agent": "word"
        },
        {
            "env": "erupt",
            "agent": "word"
        },
        {
            "env": "adore",
            "agent": "word"
        },
        {
            "env": "close",
            "agent": "word"
        },
        {
            "env": "umbra",
            "agent": "word"
        },
        {
            "env": "medic",
            "agent": "word"
        },
        {
            "env": "manic",
            "agent": "word"
        },
        {
            "env": "aptly",
            "agent": "word"
        },
        {
            "env": "rivet",
            "agent": "word"
        },
        {
            "env": "brick",
            "agent": "word"
        },
        {
            "env": "staid",
            "agent": "word"
        },
        {
            "env": "vigor",
            "agent": "word"
        },
        {
            "env": "table",
            "agent": "word"
        },
        {
            "env": "slack",
            "agent": "word"
        },
        {
            "env": "triad",
            "agent": "word"
        },
        {
            "env": "molar",
            "agent": "word"
        },
        {
            "env": "scale",
            "agent": "word"
        },
        {
            "env": "ridge",
            "agent": "word"
        },
        {
            "env": "midst",
            "agent": "word"
        },
        {
            "env": "album",
            "agent": "word"
        },
        {
            "env": "cloak",
            "agent": "word"
        },
        {
            "env": "blink",
            "agent": "word"
        },
        {
            "env": "chart",
            "agent": "word"
        },
        {
            "env": "ethos",
            "agent": "word"
        },
        {
            "env": "study",
            "agent": "word"
        },
        {
            "env": "brush",
            "agent": "word"
        },
        {
            "env": "motif",
            "agent": "word"
        },
        {
            "env": "smirk",
            "agent": "word"
        },
        {
            "env": "horse",
            "agent": "word"
        },
        {
            "env": "aloud",
            "agent": "word"
        },
        {
            "env": "spark",
            "agent": "word"
        },
        {
            "env": "tenor",
            "agent": "word"
        },
        {
            "env": "silky",
            "agent": "word"
        },
        {
            "env": "rocky",
            "agent": "word"
        },
        {
            "env": "hovel",
            "agent": "word"
        },
        {
            "env": "shown",
            "agent": "word"
        },
        {
            "env": "nudge",
            "agent": "word"
        },
        {
            "env": "limbo",
            "agent": "word"
        },
        {
            "env": "touch",
            "agent": "word"
        },
        {
            "env": "pluck",
            "agent": "word"
        },
        {
            "env": "video",
            "agent": "word"
        },
        {
            "env": "fungi",
            "agent": "word"
        },
        {
            "env": "stale",
            "agent": "word"
        },
        {
            "env": "shout",
            "agent": "word"
        },
        {
            "env": "flank",
            "agent": "word"
        },
        {
            "env": "spade",
            "agent": "word"
        },
        {
            "env": "witch",
            "agent": "word"
        },
        {
            "env": "water",
            "agent": "word"
        },
        {
            "env": "blast",
            "agent": "word"
        },
        {
            "env": "float",
            "agent": "word"
        },
        {
            "env": "broil",
            "agent": "word"
        },
        {
            "env": "plush",
            "agent": "word"
        },
        {
            "env": "grave",
            "agent": "word"
        },
        {
            "env": "privy",
            "agent": "word"
        },
        {
            "env": "lathe",
            "agent": "word"
        },
        {
            "env": "savor",
            "agent": "word"
        },
        {
            "env": "singe",
            "agent": "word"
        },
        {
            "env": "daunt",
            "agent": "word"
        },
        {
            "env": "trend",
            "agent": "word"
        },
        {
            "env": "ought",
            "agent": "word"
        },
        {
            "env": "bigot",
            "agent": "word"
        },
        {
            "env": "plane",
            "agent": "word"
        },
        {
            "env": "motel",
            "agent": "word"
        },
        {
            "env": "scuba",
            "agent": "word"
        },
        {
            "env": "plain",
            "agent": "word"
        },
        {
            "env": "juicy",
            "agent": "word"
        },
        {
            "env": "grimy",
            "agent": "word"
        },
        {
            "env": "sprig",
            "agent": "word"
        },
        {
            "env": "forum",
            "agent": "word"
        },
        {
            "env": "flunk",
            "agent": "word"
        },
        {
            "env": "judge",
            "agent": "word"
        },
        {
            "env": "white",
            "agent": "word"
        },
        {
            "env": "exult",
            "agent": "word"
        },
        {
            "env": "mulch",
            "agent": "word"
        },
        {
            "env": "deity",
            "agent": "word"
        },
        {
            "env": "speck",
            "agent": "word"
        },
        {
            "env": "sedan",
            "agent": "word"
        },
        {
            "env": "vying",
            "agent": "word"
        },
        {
            "env": "atone",
            "agent": "word"
        },
        {
            "env": "inlay",
            "agent": "word"
        },
        {
            "env": "sober",
            "agent": "word"
        },
        {
            "env": "ingot",
            "agent": "word"
        },
        {
            "env": "slave",
            "agent": "word"
        },
        {
            "env": "below",
            "agent": "word"
        },
        {
            "env": "comet",
            "agent": "word"
        },
        {
            "env": "rough",
            "agent": "word"
        },
        {
            "env": "palsy",
            "agent": "word"
        },
        {
            "env": "flake",
            "agent": "word"
        },
        {
            "env": "clink",
            "agent": "word"
        },
        {
            "env": "pearl",
            "agent": "word"
        },
        {
            "env": "alike",
            "agent": "word"
        },
        {
            "env": "stick",
            "agent": "word"
        },
        {
            "env": "whose",
            "agent": "word"
        },
        {
            "env": "raven",
            "agent": "word"
        },
        {
            "env": "hinge",
            "agent": "word"
        },
        {
            "env": "maple",
            "agent": "word"
        },
        {
            "env": "camel",
            "agent": "word"
        },
        {
            "env": "exalt",
            "agent": "word"
        },
        {
            "env": "cleat",
            "agent": "word"
        },
        {
            "env": "spiny",
            "agent": "word"
        },
        {
            "env": "reply",
            "agent": "word"
        },
        {
            "env": "shire",
            "agent": "word"
        },
        {
            "env": "batch",
            "agent": "word"
        },
        {
            "env": "grant",
            "agent": "word"
        },
        {
            "env": "caput",
            "agent": "word"
        },
        {
            "env": "feign",
            "agent": "word"
        },
        {
            "env": "champ",
            "agent": "word"
        },
        {
            "env": "brine",
            "agent": "word"
        },
        {
            "env": "pithy",
            "agent": "word"
        },
        {
            "env": "sadly",
            "agent": "word"
        },
        {
            "env": "skirt",
            "agent": "word"
        },
        {
            "env": "bleat",
            "agent": "word"
        },
        {
            "env": "thing",
            "agent": "word"
        },
        {
            "env": "being",
            "agent": "word"
        },
        {
            "env": "wordy",
            "agent": "word"
        },
        {
            "env": "diary",
            "agent": "word"
        },
        {
            "env": "pried",
            "agent": "word"
        },
        {
            "env": "bravo",
            "agent": "word"
        },
        {
            "env": "carve",
            "agent": "word"
        },
        {
            "env": "fluke",
            "agent": "word"
        },
        {
            "env": "chump",
            "agent": "word"
        },
        {
            "env": "prick",
            "agent": "word"
        },
        {
            "env": "skier",
            "agent": "word"
        },
        {
            "env": "hefty",
            "agent": "word"
        },
        {
            "env": "omega",
            "agent": "word"
        },
        {
            "env": "fruit",
            "agent": "word"
        },
        {
            "env": "candy",
            "agent": "word"
        },
        {
            "env": "faith",
            "agent": "word"
        },
        {
            "env": "sugar",
            "agent": "word"
        },
        {
            "env": "aloft",
            "agent": "word"
        },
        {
            "env": "fault",
            "agent": "word"
        },
        {
            "env": "butch",
            "agent": "word"
        },
        {
            "env": "tangy",
            "agent": "word"
        },
        {
            "env": "month",
            "agent": "word"
        },
        {
            "env": "salve",
            "agent": "word"
        },
        {
            "env": "bagel",
            "agent": "word"
        },
        {
            "env": "abode",
            "agent": "word"
        },
        {
            "env": "ready",
            "agent": "word"
        },
        {
            "env": "snare",
            "agent": "word"
        },
        {
            "env": "weary",
            "agent": "word"
        },
        {
            "env": "about",
            "agent": "word"
        },
        {
            "env": "above",
            "agent": "word"
        },
        {
            "env": "sample",
            "agent": "six"
        },
        {
            "env": "creation",
            "agent": "eight"
        },
        {
            "env": "streaming",
            "agent": "nine"
        },
        {
            "env": "leaf",
            "agent": "four"
        },
        {
            "env": "filter",
            "agent": "six"
        },
        {
            "env": "king",
            "agent": "four"
        },
        {
            "env": "plug",
            "agent": "four"
        },
        {
            "env": "signal",
            "agent": "six"
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
            "env": "subject",
            "agent": "seven"
        },
        {
            "env": "sand",
            "agent": "four"
        },
        {
            "env": "song",
            "agent": "four"
        },
        {
            "env": "shrine",
            "agent": "six"
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
            "env": "face",
            "agent": "four"
        },
        {
            "env": "wander",
            "agent": "six"
        },
        {
            "env": "grid",
            "agent": "four"
        },
        {
            "env": "justice",
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
            "env": "lamp",
            "agent": "four"
        },
        {
            "env": "hike",
            "agent": "four"
        },
        {
            "env": "land",
            "agent": "four"
        },
        {
            "env": "beacon",
            "agent": "six"
        },
        {
            "env": "polished",
            "agent": "eight"
        },
        {
            "env": "gravity",
            "agent": "seven"
        },
        {
            "env": "tank",
            "agent": "four"
        },
        {
            "env": "remains",
            "agent": "seven"
        },
        {
            "env": "anchor",
            "agent": "six"
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
            "env": "painter",
            "agent": "seven"
        },
        {
            "env": "twin",
            "agent": "four"
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
            "env": "axis",
            "agent": "four"
        },
        {
            "env": "density",
            "agent": "seven"
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
            "env": "bright",
            "agent": "six"
        },
        {
            "env": "snap",
            "agent": "four"
        },
        {
            "env": "theory",
            "agent": "six"
        },
        {
            "env": "merchant",
            "agent": "eight"
        },
        {
            "env": "jungle",
            "agent": "six"
        },
        {
            "env": "castle",
            "agent": "six"
        },
        {
            "env": "flap",
            "agent": "four"
        },
        {
            "env": "plague",
            "agent": "six"
        },
        {
            "env": "spring",
            "agent": "six"
        },
        {
            "env": "festival",
            "agent": "eight"
        },
        {
            "env": "topaz",
            "agent": "word"
        },
        {
            "env": "tried",
            "agent": "word"
        },
        {
            "env": "amend",
            "agent": "word"
        },
        {
            "env": "among",
            "agent": "word"
        },
        {
            "env": "amply",
            "agent": "word"
        },
        {
            "env": "anger",
            "agent": "word"
        },
        {
            "env": "turbo",
            "agent": "word"
        },
        {
            "env": "twine",
            "agent": "word"
        },
        {
            "env": "tying",
            "agent": "word"
        },
        {
            "env": "arson",
            "agent": "word"
        },
        {
            "env": "unite",
            "agent": "word"
        },
        {
            "env": "valid",
            "agent": "word"
        },
        {
            "env": "vinyl",
            "agent": "word"
        },
        {
            "env": "vouch",
            "agent": "word"
        },
        {
            "env": "begin",
            "agent": "word"
        },
        {
            "env": "begun",
            "agent": "word"
        },
        {
            "env": "wagon",
            "agent": "word"
        },
        {
            "env": "welsh",
            "agent": "word"
        },
        {
            "env": "blare",
            "agent": "word"
        },
        {
            "env": "wince",
            "agent": "word"
        },
        {
            "env": "winch",
            "agent": "word"
        },
        {
            "env": "wiser",
            "agent": "word"
        },
        {
            "env": "woken",
            "agent": "word"
        },
        {
            "env": "blurt",
            "agent": "word"
        },
        {
            "env": "worth",
            "agent": "word"
        },
        {
            "env": "wrest",
            "agent": "word"
        },
        {
            "env": "wrist",
            "agent": "word"
        },
        {
            "env": "write",
            "agent": "word"
        },
        {
            "env": "wrote",
            "agent": "word"
        },
        {
            "env": "boxer",
            "agent": "word"
        },
        {
            "env": "brake",
            "agent": "word"
        },
        {
            "env": "brand",
            "agent": "word"
        },
        {
            "env": "yeast",
            "agent": "word"
        },
        {
            "env": "bread",
            "agent": "word"
        },
        {
            "env": "brisk",
            "agent": "word"
        },
        {
            "env": "cagey",
            "agent": "word"
        },
        {
            "env": "caste",
            "agent": "word"
        },
        {
            "env": "chard",
            "agent": "word"
        },
        {
            "env": "chase",
            "agent": "word"
        },
        {
            "env": "chime",
            "agent": "word"
        },
        {
            "env": "choir",
            "agent": "word"
        },
        {
            "env": "clang",
            "agent": "word"
        },
        {
            "env": "clank",
            "agent": "word"
        },
        {
            "env": "clasp",
            "agent": "word"
        },
        {
            "env": "covet",
            "agent": "word"
        },
        {
            "env": "cower",
            "agent": "word"
        },
        {
            "env": "crimp",
            "agent": "word"
        },
        {
            "env": "croup",
            "agent": "word"
        },
        {
            "env": "crumb",
            "agent": "word"
        },
        {
            "env": "curve",
            "agent": "word"
        },
        {
            "env": "cyber",
            "agent": "word"
        },
        {
            "env": "decal",
            "agent": "word"
        },
        {
            "env": "depth",
            "agent": "word"
        },
        {
            "env": "dirge",
            "agent": "word"
        },
        {
            "env": "dirty",
            "agent": "word"
        },
        {
            "env": "dowry",
            "agent": "word"
        },
        {
            "env": "drawn",
            "agent": "word"
        },
        {
            "env": "drove",
            "agent": "word"
        },
        {
            "env": "drunk",
            "agent": "word"
        },
        {
            "env": "dutch",
            "agent": "word"
        },
        {
            "env": "early",
            "agent": "word"
        },
        {
            "env": "eight",
            "agent": "word"
        },
        {
            "env": "equip",
            "agent": "word"
        },
        {
            "env": "ethic",
            "agent": "word"
        },
        {
            "env": "facet",
            "agent": "word"
        },
        {
            "env": "fiend",
            "agent": "word"
        },
        {
            "env": "fjord",
            "agent": "word"
        },
        {
            "env": "focus",
            "agent": "word"
        },
        {
            "env": "force",
            "agent": "word"
        },
        {
            "env": "forte",
            "agent": "word"
        },
        {
            "env": "frail",
            "agent": "word"
        },
        {
            "env": "fried",
            "agent": "word"
        },
        {
            "env": "gecko",
            "agent": "word"
        },
        {
            "env": "gipsy",
            "agent": "word"
        },
        {
            "env": "glean",
            "agent": "word"
        },
        {
            "env": "globe",
            "agent": "word"
        },
        {
            "env": "glyph",
            "agent": "word"
        },
        {
            "env": "gnome",
            "agent": "word"
        },
        {
            "env": "grief",
            "agent": "word"
        },
        {
            "env": "gripe",
            "agent": "word"
        },
        {
            "env": "groin",
            "agent": "word"
        },
        {
            "env": "grove",
            "agent": "word"
        },
        {
            "env": "growl",
            "agent": "word"
        },
        {
            "env": "gruel",
            "agent": "word"
        },
        {
            "env": "guild",
            "agent": "word"
        },
        {
            "env": "hardy",
            "agent": "word"
        },
        {
            "env": "heron",
            "agent": "word"
        },
        {
            "env": "honey",
            "agent": "word"
        },
        {
            "env": "hound",
            "agent": "word"
        },
        {
            "env": "house",
            "agent": "word"
        },
        {
            "env": "humor",
            "agent": "word"
        },
        {
            "env": "impel",
            "agent": "word"
        },
        {
            "env": "infer",
            "agent": "word"
        },
        {
            "env": "itchy",
            "agent": "word"
        },
        {
            "env": "ivory",
            "agent": "word"
        },
        {
            "env": "joust",
            "agent": "word"
        },
        {
            "env": "junta",
            "agent": "word"
        },
        {
            "env": "lapse",
            "agent": "word"
        },
        {
            "env": "latch",
            "agent": "word"
        },
        {
            "env": "later",
            "agent": "word"
        },
        {
            "env": "liner",
            "agent": "word"
        },
        {
            "env": "lodge",
            "agent": "word"
        },
        {
            "env": "login",
            "agent": "word"
        },
        {
            "env": "lumpy",
            "agent": "word"
        },
        {
            "env": "meaty",
            "agent": "word"
        },
        {
            "env": "mirth",
            "agent": "word"
        },
        {
            "env": "mogul",
            "agent": "word"
        },
        {
            "env": "moral",
            "agent": "word"
        },
        {
            "env": "nobly",
            "agent": "word"
        },
        {
            "env": "nymph",
            "agent": "word"
        },
        {
            "env": "often",
            "agent": "word"
        },
        {
            "env": "opine",
            "agent": "word"
        },
        {
            "env": "opium",
            "agent": "word"
        },
        {
            "env": "organ",
            "agent": "word"
        },
        {
            "env": "outer",
            "agent": "word"
        },
        {
            "env": "paler",
            "agent": "word"
        },
        {
            "env": "panel",
            "agent": "word"
        },
        {
            "env": "parse",
            "agent": "word"
        },
        {
            "env": "paste",
            "agent": "word"
        },
        {
            "env": "phony",
            "agent": "word"
        },
        {
            "env": "pitch",
            "agent": "word"
        },
        {
            "env": "pixel",
            "agent": "word"
        },
        {
            "env": "plaid",
            "agent": "word"
        },
        {
            "env": "polar",
            "agent": "word"
        },
        {
            "env": "pouch",
            "agent": "word"
        },
        {
            "env": "pound",
            "agent": "word"
        },
        {
            "env": "pouty",
            "agent": "word"
        },
        {
            "env": "psalm",
            "agent": "word"
        },
        {
            "env": "pubic",
            "agent": "word"
        },
        {
            "env": "quake",
            "agent": "word"
        },
        {
            "env": "ralph",
            "agent": "word"
        },
        {
            "env": "repay",
            "agent": "word"
        },
        {
            "env": "rouge",
            "agent": "word"
        },
        {
            "env": "saner",
            "agent": "word"
        },
        {
            "env": "satyr",
            "agent": "word"
        },
        {
            "env": "scald",
            "agent": "word"
        },
        {
            "env": "scalp",
            "agent": "word"
        },
        {
            "env": "scope",
            "agent": "word"
        },
        {
            "env": "scram",
            "agent": "word"
        },
        {
            "env": "scrum",
            "agent": "word"
        },
        {
            "env": "serum",
            "agent": "word"
        },
        {
            "env": "sharp",
            "agent": "word"
        },
        {
            "env": "shied",
            "agent": "word"
        },
        {
            "env": "sixty",
            "agent": "word"
        },
        {
            "env": "slimy",
            "agent": "word"
        },
        {
            "env": "smart",
            "agent": "word"
        },
        {
            "env": "smock",
            "agent": "word"
        },
        {
            "env": "snort",
            "agent": "word"
        },
        {
            "env": "solve",
            "agent": "word"
        },
        {
            "env": "spicy",
            "agent": "word"
        },
        {
            "env": "spine",
            "agent": "word"
        },
        {
            "env": "spout",
            "agent": "word"
        },
        {
            "env": "squat",
            "agent": "word"
        },
        {
            "env": "stage",
            "agent": "word"
        },
        {
            "env": "stalk",
            "agent": "word"
        },
        {
            "env": "stead",
            "agent": "word"
        },
        {
            "env": "stern",
            "agent": "word"
        },
        {
            "env": "stomp",
            "agent": "word"
        },
        {
            "env": "store",
            "agent": "word"
        },
        {
            "env": "suite",
            "agent": "word"
        },
        {
            "env": "sulky",
            "agent": "word"
        },
        {
            "env": "swear",
            "agent": "word"
        },
        {
            "env": "swept",
            "agent": "word"
        },
        {
            "env": "swing",
            "agent": "word"
        }
    ]
}