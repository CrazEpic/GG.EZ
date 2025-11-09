const championKeyToName = {
	"266": {
		name: "Aatrox",
		id: "Aatrox",
		title: "the Darkin Blade",
	},
	"103": {
		name: "Ahri",
		id: "Ahri",
		title: "the Nine-Tailed Fox",
	},
	"84": {
		name: "Akali",
		id: "Akali",
		title: "the Rogue Assassin",
	},
	"166": {
		name: "Akshan",
		id: "Akshan",
		title: "the Rogue Sentinel",
	},
	"12": {
		name: "Alistar",
		id: "Alistar",
		title: "the Minotaur",
	},
	"799": {
		name: "Ambessa",
		id: "Ambessa",
		title: "Matriarch of War",
	},
	"32": {
		name: "Amumu",
		id: "Amumu",
		title: "the Sad Mummy",
	},
	"34": {
		name: "Anivia",
		id: "Anivia",
		title: "the Cryophoenix",
	},
	"1": {
		name: "Annie",
		id: "Annie",
		title: "the Dark Child",
	},
	"523": {
		name: "Aphelios",
		id: "Aphelios",
		title: "the Weapon of the Faithful",
	},
	"22": {
		name: "Ashe",
		id: "Ashe",
		title: "the Frost Archer",
	},
	"136": {
		name: "Aurelion Sol",
		id: "AurelionSol",
		title: "The Star Forger",
	},
	"893": {
		name: "Aurora",
		id: "Aurora",
		title: "the Witch Between Worlds",
	},
	"268": {
		name: "Azir",
		id: "Azir",
		title: "the Emperor of the Sands",
	},
	"432": {
		name: "Bard",
		id: "Bard",
		title: "the Wandering Caretaker",
	},
	"200": {
		name: "Bel'Veth",
		id: "Belveth",
		title: "the Empress of the Void",
	},
	"53": {
		name: "Blitzcrank",
		id: "Blitzcrank",
		title: "the Great Steam Golem",
	},
	"63": {
		name: "Brand",
		id: "Brand",
		title: "the Burning Vengeance",
	},
	"201": {
		name: "Braum",
		id: "Braum",
		title: "the Heart of the Freljord",
	},
	"233": {
		name: "Briar",
		id: "Briar",
		title: "the Restrained Hunger",
	},
	"51": {
		name: "Caitlyn",
		id: "Caitlyn",
		title: "the Sheriff of Piltover",
	},
	"164": {
		name: "Camille",
		id: "Camille",
		title: "the Steel Shadow",
	},
	"69": {
		name: "Cassiopeia",
		id: "Cassiopeia",
		title: "the Serpent's Embrace",
	},
	"31": {
		name: "Cho'Gath",
		id: "Chogath",
		title: "the Terror of the Void",
	},
	"42": {
		name: "Corki",
		id: "Corki",
		title: "the Daring Bombardier",
	},
	"122": {
		name: "Darius",
		id: "Darius",
		title: "the Hand of Noxus",
	},
	"131": {
		name: "Diana",
		id: "Diana",
		title: "Scorn of the Moon",
	},
	"119": {
		name: "Draven",
		id: "Draven",
		title: "the Glorious Executioner",
	},
	"36": {
		name: "Dr. Mundo",
		id: "DrMundo",
		title: "the Madman of Zaun",
	},
	"245": {
		name: "Ekko",
		id: "Ekko",
		title: "the Boy Who Shattered Time",
	},
	"60": {
		name: "Elise",
		id: "Elise",
		title: "the Spider Queen",
	},
	"28": {
		name: "Evelynn",
		id: "Evelynn",
		title: "Agony's Embrace",
	},
	"81": {
		name: "Ezreal",
		id: "Ezreal",
		title: "the Prodigal Explorer",
	},
	"9": {
		name: "Fiddlesticks",
		id: "Fiddlesticks",
		title: "the Ancient Fear",
	},
	"114": {
		name: "Fiora",
		id: "Fiora",
		title: "the Grand Duelist",
	},
	"105": {
		name: "Fizz",
		id: "Fizz",
		title: "the Tidal Trickster",
	},
	"3": {
		name: "Galio",
		id: "Galio",
		title: "the Colossus",
	},
	"41": {
		name: "Gangplank",
		id: "Gangplank",
		title: "the Saltwater Scourge",
	},
	"86": {
		name: "Garen",
		id: "Garen",
		title: "The Might of Demacia",
	},
	"150": {
		name: "Gnar",
		id: "Gnar",
		title: "the Missing Link",
	},
	"79": {
		name: "Gragas",
		id: "Gragas",
		title: "the Rabble Rouser",
	},
	"104": {
		name: "Graves",
		id: "Graves",
		title: "the Outlaw",
	},
	"887": {
		name: "Gwen",
		id: "Gwen",
		title: "The Hallowed Seamstress",
	},
	"120": {
		name: "Hecarim",
		id: "Hecarim",
		title: "the Shadow of War",
	},
	"74": {
		name: "Heimerdinger",
		id: "Heimerdinger",
		title: "the Revered Inventor",
	},
	"910": {
		name: "Hwei",
		id: "Hwei",
		title: "the Visionary",
	},
	"420": {
		name: "Illaoi",
		id: "Illaoi",
		title: "the Kraken Priestess",
	},
	"39": {
		name: "Irelia",
		id: "Irelia",
		title: "the Blade Dancer",
	},
	"427": {
		name: "Ivern",
		id: "Ivern",
		title: "the Green Father",
	},
	"40": {
		name: "Janna",
		id: "Janna",
		title: "the Storm's Fury",
	},
	"59": {
		name: "Jarvan IV",
		id: "JarvanIV",
		title: "the Exemplar of Demacia",
	},
	"24": {
		name: "Jax",
		id: "Jax",
		title: "Grandmaster at Arms",
	},
	"126": {
		name: "Jayce",
		id: "Jayce",
		title: "the Defender of Tomorrow",
	},
	"202": {
		name: "Jhin",
		id: "Jhin",
		title: "the Virtuoso",
	},
	"222": {
		name: "Jinx",
		id: "Jinx",
		title: "the Loose Cannon",
	},
	"145": {
		name: "Kai'Sa",
		id: "Kaisa",
		title: "Daughter of the Void",
	},
	"429": {
		name: "Kalista",
		id: "Kalista",
		title: "the Spear of Vengeance",
	},
	"43": {
		name: "Karma",
		id: "Karma",
		title: "the Enlightened One",
	},
	"30": {
		name: "Karthus",
		id: "Karthus",
		title: "the Deathsinger",
	},
	"38": {
		name: "Kassadin",
		id: "Kassadin",
		title: "the Void Walker",
	},
	"55": {
		name: "Katarina",
		id: "Katarina",
		title: "the Sinister Blade",
	},
	"10": {
		name: "Kayle",
		id: "Kayle",
		title: "the Righteous",
	},
	"141": {
		name: "Kayn",
		id: "Kayn",
		title: "the Shadow Reaper",
	},
	"85": {
		name: "Kennen",
		id: "Kennen",
		title: "the Heart of the Tempest",
	},
	"121": {
		name: "Kha'Zix",
		id: "Khazix",
		title: "the Voidreaver",
	},
	"203": {
		name: "Kindred",
		id: "Kindred",
		title: "The Eternal Hunters",
	},
	"240": {
		name: "Kled",
		id: "Kled",
		title: "the Cantankerous Cavalier",
	},
	"96": {
		name: "Kog'Maw",
		id: "KogMaw",
		title: "the Mouth of the Abyss",
	},
	"897": {
		name: "K'Sante",
		id: "KSante",
		title: "the Pride of Nazumah",
	},
	"7": {
		name: "LeBlanc",
		id: "Leblanc",
		title: "the Deceiver",
	},
	"64": {
		name: "Lee Sin",
		id: "LeeSin",
		title: "the Blind Monk",
	},
	"89": {
		name: "Leona",
		id: "Leona",
		title: "the Radiant Dawn",
	},
	"876": {
		name: "Lillia",
		id: "Lillia",
		title: "the Bashful Bloom",
	},
	"127": {
		name: "Lissandra",
		id: "Lissandra",
		title: "the Ice Witch",
	},
	"236": {
		name: "Lucian",
		id: "Lucian",
		title: "the Purifier",
	},
	"117": {
		name: "Lulu",
		id: "Lulu",
		title: "the Fae Sorceress",
	},
	"99": {
		name: "Lux",
		id: "Lux",
		title: "the Lady of Luminosity",
	},
	"54": {
		name: "Malphite",
		id: "Malphite",
		title: "Shard of the Monolith",
	},
	"90": {
		name: "Malzahar",
		id: "Malzahar",
		title: "the Prophet of the Void",
	},
	"57": {
		name: "Maokai",
		id: "Maokai",
		title: "the Twisted Treant",
	},
	"11": {
		name: "Master Yi",
		id: "MasterYi",
		title: "the Wuju Bladesman",
	},
	"800": {
		name: "Mel",
		id: "Mel",
		title: "the Soul's Reflection",
	},
	"902": {
		name: "Milio",
		id: "Milio",
		title: "The Gentle Flame",
	},
	"21": {
		name: "Miss Fortune",
		id: "MissFortune",
		title: "the Bounty Hunter",
	},
	"62": {
		name: "Wukong",
		id: "MonkeyKing",
		title: "the Monkey King",
	},
	"82": {
		name: "Mordekaiser",
		id: "Mordekaiser",
		title: "the Iron Revenant",
	},
	"25": {
		name: "Morgana",
		id: "Morgana",
		title: "the Fallen",
	},
	"950": {
		name: "Naafiri",
		id: "Naafiri",
		title: "the Hound of a Hundred Bites",
	},
	"267": {
		name: "Nami",
		id: "Nami",
		title: "the Tidecaller",
	},
	"75": {
		name: "Nasus",
		id: "Nasus",
		title: "the Curator of the Sands",
	},
	"111": {
		name: "Nautilus",
		id: "Nautilus",
		title: "the Titan of the Depths",
	},
	"518": {
		name: "Neeko",
		id: "Neeko",
		title: "the Curious Chameleon",
	},
	"76": {
		name: "Nidalee",
		id: "Nidalee",
		title: "the Bestial Huntress",
	},
	"895": {
		name: "Nilah",
		id: "Nilah",
		title: "the Joy Unbound",
	},
	"56": {
		name: "Nocturne",
		id: "Nocturne",
		title: "the Eternal Nightmare",
	},
	"20": {
		name: "Nunu & Willump",
		id: "Nunu",
		title: "the Boy and His Yeti",
	},
	"2": {
		name: "Olaf",
		id: "Olaf",
		title: "the Berserker",
	},
	"61": {
		name: "Orianna",
		id: "Orianna",
		title: "the Lady of Clockwork",
	},
	"516": {
		name: "Ornn",
		id: "Ornn",
		title: "The Fire below the Mountain",
	},
	"80": {
		name: "Pantheon",
		id: "Pantheon",
		title: "the Unbreakable Spear",
	},
	"78": {
		name: "Poppy",
		id: "Poppy",
		title: "Keeper of the Hammer",
	},
	"555": {
		name: "Pyke",
		id: "Pyke",
		title: "the Bloodharbor Ripper",
	},
	"246": {
		name: "Qiyana",
		id: "Qiyana",
		title: "Empress of the Elements",
	},
	"133": {
		name: "Quinn",
		id: "Quinn",
		title: "Demacia's Wings",
	},
	"497": {
		name: "Rakan",
		id: "Rakan",
		title: "The Charmer",
	},
	"33": {
		name: "Rammus",
		id: "Rammus",
		title: "the Armordillo",
	},
	"421": {
		name: "Rek'Sai",
		id: "RekSai",
		title: "the Void Burrower",
	},
	"526": {
		name: "Rell",
		id: "Rell",
		title: "the Iron Maiden",
	},
	"888": {
		name: "Renata Glasc",
		id: "Renata",
		title: "the Chem-Baroness",
	},
	"58": {
		name: "Renekton",
		id: "Renekton",
		title: "the Butcher of the Sands",
	},
	"107": {
		name: "Rengar",
		id: "Rengar",
		title: "the Pridestalker",
	},
	"92": {
		name: "Riven",
		id: "Riven",
		title: "the Exile",
	},
	"68": {
		name: "Rumble",
		id: "Rumble",
		title: "the Mechanized Menace",
	},
	"13": {
		name: "Ryze",
		id: "Ryze",
		title: "the Rune Mage",
	},
	"360": {
		name: "Samira",
		id: "Samira",
		title: "the Desert Rose",
	},
	"113": {
		name: "Sejuani",
		id: "Sejuani",
		title: "Fury of the North",
	},
	"235": {
		name: "Senna",
		id: "Senna",
		title: "the Redeemer",
	},
	"147": {
		name: "Seraphine",
		id: "Seraphine",
		title: "the Starry-Eyed Songstress",
	},
	"875": {
		name: "Sett",
		id: "Sett",
		title: "the Boss",
	},
	"35": {
		name: "Shaco",
		id: "Shaco",
		title: "the Demon Jester",
	},
	"98": {
		name: "Shen",
		id: "Shen",
		title: "the Eye of Twilight",
	},
	"102": {
		name: "Shyvana",
		id: "Shyvana",
		title: "the Half-Dragon",
	},
	"27": {
		name: "Singed",
		id: "Singed",
		title: "the Mad Chemist",
	},
	"14": {
		name: "Sion",
		id: "Sion",
		title: "The Undead Juggernaut",
	},
	"15": {
		name: "Sivir",
		id: "Sivir",
		title: "the Battle Mistress",
	},
	"72": {
		name: "Skarner",
		id: "Skarner",
		title: "the Primordial Sovereign",
	},
	"901": {
		name: "Smolder",
		id: "Smolder",
		title: "the Fiery Fledgling",
	},
	"37": {
		name: "Sona",
		id: "Sona",
		title: "Maven of the Strings",
	},
	"16": {
		name: "Soraka",
		id: "Soraka",
		title: "the Starchild",
	},
	"50": {
		name: "Swain",
		id: "Swain",
		title: "the Noxian Grand General",
	},
	"517": {
		name: "Sylas",
		id: "Sylas",
		title: "the Unshackled",
	},
	"134": {
		name: "Syndra",
		id: "Syndra",
		title: "the Dark Sovereign",
	},
	"223": {
		name: "Tahm Kench",
		id: "TahmKench",
		title: "The River King",
	},
	"163": {
		name: "Taliyah",
		id: "Taliyah",
		title: "the Stoneweaver",
	},
	"91": {
		name: "Talon",
		id: "Talon",
		title: "the Blade's Shadow",
	},
	"44": {
		name: "Taric",
		id: "Taric",
		title: "the Shield of Valoran",
	},
	"17": {
		name: "Teemo",
		id: "Teemo",
		title: "the Swift Scout",
	},
	"412": {
		name: "Thresh",
		id: "Thresh",
		title: "the Chain Warden",
	},
	"18": {
		name: "Tristana",
		id: "Tristana",
		title: "the Yordle Gunner",
	},
	"48": {
		name: "Trundle",
		id: "Trundle",
		title: "the Troll King",
	},
	"23": {
		name: "Tryndamere",
		id: "Tryndamere",
		title: "the Barbarian King",
	},
	"4": {
		name: "Twisted Fate",
		id: "TwistedFate",
		title: "the Card Master",
	},
	"29": {
		name: "Twitch",
		id: "Twitch",
		title: "the Plague Rat",
	},
	"77": {
		name: "Udyr",
		id: "Udyr",
		title: "the Spirit Walker",
	},
	"6": {
		name: "Urgot",
		id: "Urgot",
		title: "the Dreadnought",
	},
	"110": {
		name: "Varus",
		id: "Varus",
		title: "the Arrow of Retribution",
	},
	"67": {
		name: "Vayne",
		id: "Vayne",
		title: "the Night Hunter",
	},
	"45": {
		name: "Veigar",
		id: "Veigar",
		title: "the Tiny Master of Evil",
	},
	"161": {
		name: "Vel'Koz",
		id: "Velkoz",
		title: "the Eye of the Void",
	},
	"711": {
		name: "Vex",
		id: "Vex",
		title: "the Gloomist",
	},
	"254": {
		name: "Vi",
		id: "Vi",
		title: "the Piltover Enforcer",
	},
	"234": {
		name: "Viego",
		id: "Viego",
		title: "The Ruined King",
	},
	"112": {
		name: "Viktor",
		id: "Viktor",
		title: "the Herald of the Arcane",
	},
	"8": {
		name: "Vladimir",
		id: "Vladimir",
		title: "the Crimson Reaper",
	},
	"106": {
		name: "Volibear",
		id: "Volibear",
		title: "the Relentless Storm",
	},
	"19": {
		name: "Warwick",
		id: "Warwick",
		title: "the Uncaged Wrath of Zaun",
	},
	"498": {
		name: "Xayah",
		id: "Xayah",
		title: "the Rebel",
	},
	"101": {
		name: "Xerath",
		id: "Xerath",
		title: "the Magus Ascendant",
	},
	"5": {
		name: "Xin Zhao",
		id: "XinZhao",
		title: "the Seneschal of Demacia",
	},
	"157": {
		name: "Yasuo",
		id: "Yasuo",
		title: "the Unforgiven",
	},
	"777": {
		name: "Yone",
		id: "Yone",
		title: "the Unforgotten",
	},
	"83": {
		name: "Yorick",
		id: "Yorick",
		title: "Shepherd of Souls",
	},
	"804": {
		name: "Yunara",
		id: "Yunara",
		title: "the Unbroken Faith",
	},
	"350": {
		name: "Yuumi",
		id: "Yuumi",
		title: "the Magical Cat",
	},
	"154": {
		name: "Zac",
		id: "Zac",
		title: "the Secret Weapon",
	},
	"238": {
		name: "Zed",
		id: "Zed",
		title: "the Master of Shadows",
	},
	"221": {
		name: "Zeri",
		id: "Zeri",
		title: "The Spark of Zaun",
	},
	"115": {
		name: "Ziggs",
		id: "Ziggs",
		title: "the Hexplosives Expert",
	},
	"26": {
		name: "Zilean",
		id: "Zilean",
		title: "the Chronokeeper",
	},
	"142": {
		name: "Zoe",
		id: "Zoe",
		title: "the Aspect of Twilight",
	},
	"143": {
		name: "Zyra",
		id: "Zyra",
		title: "Rise of the Thorns",
	},
}

export default championKeyToName
