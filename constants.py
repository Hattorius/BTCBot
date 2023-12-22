CURRENCY_FORMAT_DICT = {
    "default": "${:,.2f} ",
    "gbp": "£{:,.2f} British Pounds",
    "eur": "€{:,.2f} Euros",
    "brl": "R${:,.2f} Brazillian Reais",
    "vef": "B${:,.0f} Venezuelan Bolívar",
    "jpy": "¥{:,.0f} Japanese Yen",
    "cny": "¥{:,.0f} Chinese Renminbi",
    "ils": "₪{:,.0f} Israeli Shekalim",
    "inr": "₹{:,.2f} Indian Rupees",
    "zar": "R{:,.2f} South African Rands",
    "rub": "₽{:,.2f} Russian Rubles",
    "xau": "{:,.2f} ounces of gold",
    "xag": "{:,.2f} ounces of silver",
	"btc": "{:,.0f} Bitcoin"
}

ITEM_DICT = {
    "mac": {"cost": 5.71, "name": "Big Macs", "emoji": ":hamburger:", "single": False},
    "mcr": {"cost": 4.29, "name": "McRibs", "emoji": ":pig2:", "single": False},
    "cru": {
        "cost": 2.99,
        "name": "Crunchwraps Supreme",
        "emoji": ":taco:",
        "single": False,
    },
    "beer": {"cost": 4.75, "name": "Pints of Beer", "emoji": ":beer:", "single": False},
    "but": {
        "cost": 0.75,
        "name": "Sticks of Butter",
        "emoji": ":butter:",
        "single": False,
    },
    "coldcards": {
        "cost": 119.27,
        "name": "Coldcards",
        "emoji": ":pager:",
        "single": False,
    },
    "egg": {"cost": 0.1208333, "name": "Large Eggs", "emoji": ":egg:", "single": False},
    "420": {
        "cost": 200,
        "name": "Ounces of Marijuana",
        "emoji": ":maple_leaf:",
        "single": False,
    },
    "gum": {
        "cost": 8.37,
        "name": "Kilograms of Gummie Bears",
        "emoji": ":teddy_bear:",
        "single": False,
    },
    "rbx": {"cost": 0.0125, "name": "Robux", "emoji": ":bricks:", "single": False},
    "thc": {
        "cost": 40,
        "name": "THC distillate cartridges (1 gram)",
        "emoji": ":maple_leaf:",
        "single": False,
    },
    "pod": {"cost": 5.2475, "name": "JUUL pods", "emoji": ":smoking:", "single": False},
    "furby": {"cost": 300, "name": "Rare Furbies", "emoji": ":owl:", "single": False},
    "avo": {
        "cost": 10,
        "name": "Serves of Avocado Toast",
        "emoji": ":avocado:",
        "single": False,
    },
    "chicken": {
        "cost": 2.85,
        "name": "Rhode Island Red Chickens",
        "emoji": ":chicken:",
        "single": False,
    },
    "nana": {"cost": 0.23, "name": "Bananas", "emoji": ":banana:", "single": False},
    "bre": {
        "cost": 2.04,
        "name": "Loaves of bread",
        "emoji": ":bread:",
        "single": False,
    },
    # Seperating out items that should be displayed as cost for a single item
    "lam": {
        "cost": 521465,
        "name": "Lamborghini Aventador SVJ",
        "emoji": ":race_car:",
        "single": True,
    },
    "act": {
        "cost": 32410,
        "name": "Average College Tuition (4 years)",
        "emoji": ":student:",
        "single": True,
    },
    "lar": {
        "cost": 259000,
        "name": "McLaren 600LT 2020",
        "emoji": ":race_car:",
        "single": True,
    },
    "tm3": {
        "cost": 36990,
        "name": "Tesla Model 3",
        "emoji": ":red_car:",
        "single": True,
    },
    "rds": {
        "cost": 200000,
        "name": "Tesla Roadster 2020",
        "emoji": ":race_car:",
        "single": True,
    },
    "f40": {
        "cost": 1350000,
        "name": "Ferrari F40",
        "emoji": ":race_car:",
        "single": True,
    },
    "tay": {
        "cost": 232904,
        "name": "Porche Taycan Turbo S",
        "emoji": ":red_car:",
        "single": True,
    },
    "mus": {
        "cost": 75000,
        "name": "Ford Mustang Shelby GT500 2020",
        "emoji": ":blue_car:",
        "single": True,
    },
    "fc9": {
        "cost": 62000000,
        "name": "SpaceX Falcon 9 Launch",
        "emoji": ":rocket:",
        "single": True,
    },
    "trn": {
        "cost": 139900,
        "name": "Audi RS e-tron GT 2022",
        "emoji": ":race_car:",
        "single": True,
    },
    "bug": {
        "cost": 2990000,
        "name": "Bugatti Chiron 2020",
        "emoji": ":race_car:",
        "single": True,
    },
    "nev": {
        "cost": 2440000,
        "name": "Rimac Nevera",
        "emoji": ":race_car:",
        "single": True,
    },
    "gef": {
        "cost": 1499,
        "name": "Nvidia GEFORCE RTX 3090",
        "emoji": ":desktop_computer:",
        "single": True,
    },
    "rov": {
        "cost": 2725000000,
        "name": "trip to Mars + rover/drone/skycrane package",
        "emoji": ":robot: :rocket:",
        "single": True,
    },
    "bez": {
        "cost": 74598,
        "name": "One minute of Jeff Bezos' time",
        "emoji": ":man_office_worker:",
        "single": True,
    },
    "kid": {
        "cost": 200000,
        "name": "black market kidney",
        "emoji": ":detective: :aubergine:",
        "single": True,
    },
    "ukb": {
        "cost": 850000000000,
        "name": "British banking bailout",
        "emoji": ":flag_gb: :bank:",
        "single": True,
    },
}

FUN_FACTS = ["**Fun Fact:** Bitcoin is the first and only decentralized digital currency",
					"**Fun Fact:** Bitcoin was created by Satoshi Nakamoto in 2009",
					"**Fun Fact:** Bitcoin is not a cryptocurrency, it predates them and the term only exists to create a false association to Bitcoin",
					"**Fun Fact:** Blockchain technology is neither novel nor valuable. It has none of the properties commonly ascribed to it like immutability, or decentralization, or security. This comes instead from other properties unique to Bitcoin, such as true Nakamoto consensus.",
					"**Fun Fact:** Proof of work is where Bitcoin's cost to attack and economic mutability come from.",
					"**Fun Fact:** Bitcoin's distributed ledger, the blockchain, is simply where we store the data for Bitcoin network state. It has no other valuable function or properties.",
					"**Fun Fact:** Bitcoin's peer-to-peer (p2p) network is where most of the valuable properties associated with Bitcoin emerge from, specifically the behaviour of the network actors verifying all transactions and acting in a self interested manner.",
					"**Fun Fact:** Bitcoin has a super-majority of all SHA-256 computing in the world, and without that super-majority it would be vulnerable to attacks.",
					"**Fun Fact:** The smallest unit of Bitcoin is called a Satoshi, worth one hundred millionth of a single Bitcoin.",
					"**Fun Fact:** In 2021, El Salvador became the first country to adopt Bitcoin as legal tender.",
					"**Fun Fact:** At one point, the FBI was one of the world’s largest owners of Bitcoin, due to seizures from the Silk Road, an online black market.",
					"**Fun Fact:** The world's first Bitcoin ATM was installed in Vancouver, Canada, in 2013.",
					"**Fun Fact:** The first Bitcoin transaction was made by Satoshi Nakamoto to Hal Finney in 2009.",
					"**Fun Fact:** It’s estimated that around 20% of all Bitcoins are lost or inaccessible, mainly due to forgotten passwords or broken hard drives.",
					"**Fun Fact:** The first real-world transaction using Bitcoin was in 2010, when a programmer named Laszlo Hanyecz bought two pizzas for 10,000 Bitcoins. Just 3 years later, in October of 2013, those Bitcoins could have bought him over 100,000 pizzas.",
					"**Fun Fact:** In 2010, a vulnerability in the Bitcoin protocol was exploited, creating billions of Bitcoins. The bug was quickly fixed, and the extra Bitcoins were erased. This is the only time a 'free Bitcoin' bug was exploited on the network.",
					"**Fun Fact:** Bitcoin is the only decentralized entity in the 'crypto' space and 'cryptocurrency' is generally a by-word for scams.",
					"**Fun Fact:** Bitcoin operates on a decentralized network, meaning it isn’t controlled by any single entity or government.",
					"**Fun Fact:** Bitcoins are created through a process called mining, which involves using electricity to run many special computers called ASICs. These are used to search for the correct random number that entitles them to mint new bitcoins, publish bitcoin transactions, and take their fees. The more powerful ASICs you have, the more likely you are to gain this privilege at any given time. Because ASICs are distributed all around the world and owned by many different entities, Bitcoin is economically secured.",
					"**Fun Fact:** Approximately every four years, the reward for Bitcoin mining halves, an event known as 'halving.' This reduces the rate at which new Bitcoins are created.",
					"**Fun Fact:** There will only ever be 21 million Bitcoins in existence, making it a deflationary currency once it is all printed or the loss rate is greater than the printed rate. Until then it is inflationary. As of this writing 95% of all Bitcoin have been mined.",
					"**Fun Fact:** Public spaces like r/bitcoin, twitter, and telegram are full of misinformation. Each of us can make our communities better places by verifying the information we see and refuting misinformation. Though if you do, expect to be banned from those spaces. Entrenched interests stand against Bitcoin as do petty egos.",
					"**Fun Fact:** Bitcoin is for enemies. It doesn't care about you, your ideology, or your grudges. It caters to your political opponents, it caters to those you believe to be unethical. If it did any less, then it would be subject to the whims of popular culture and tyranny of the majority. Bitcoin is a tool and it can be used for many ends, even those you may disagree with.",
					"**Fun Fact:** When Bitcoin is attacked it relies on the decentralized-economic security model. What this means is that those misusing blockspace will pay for it as a function of time, bankrupting them. Failing that, nodes have the power to fork and defend themselves. These are the economic and decentralized foundations of Bitcoin's security model, so run a node!",
					"**Fun Fact:** Bitcoin is thankless. It owes you nothing, so expect nothing. Your node and your will defines Bitcoin, so use it and stand for yourself.",
					"**Fun Fact:** Bitcoin addresses are most commonly the hash of 'smart contracts' and the process of spending enables verification of their execution.",
					"**Fun Fact:** A scam built on Bitcoin is a still a scam, is still fraud, is still worthless. NFT's, ordinals, shitcoin emulating layers, federations, stablecoins, and others fall into this category.",
					"**Fun Fact:** Custodying your own Bitcoin isn't difficult. If you don't, please do. Download a wallet, create some keys offline in an air gapped environment, ideally provide your own entropy with dice or corrected coin flips, and backup your seed in metal. These simple steps make you more secure than LukeJr.",
					"**Fun Fact:** The speaker doesn't matter, the message matters. Evaluate and verify the things you're told in Bitcoin and this discord. Trust no one and verify everything.",
					"**Fun Fact:** Bitcoin hasn't slept since 2013 when it took a 6 hour nap to reorg. I don't think I've slept since then either, come to mention it.",
					"**Fun Fact:** In 2018 a [vulnerability was discovered](https://bitcoincore.org/en/2018/09/20/notice/), originally introduced in 2017, which enabled DoS attacks against nodes as well as inflation of the Bitcoin supply. This was all BlueMatts fault. The issue was patched and deployed before being exploited, but stands to remind us that we must peer review code and run diverse node clients.",
					"**Fun Fact:** Between 2015 and 2017 the community engaged in what has become known as the Blocksize Wars, wherein over 80% of the traditionally powerful actors of any ecosystem - the rich, the businesses, and in our case the miners as well - attempted to change Bitcoin's consensus to reduce their technical costs at the expense of node runners. A minority of node runners threatening a user activated soft fork effectively stopped the attack by holding an economic gun to the businesses heads.",
					"**Fun Fact:** There are no shortcuts to verification or security.",
					"**Fun Fact:** Those obsessed with the Bitcoin price would (and have tried to) destroy its valuable properties such as decentralization (ability to run a node) and economic security (cost to transact) because they are too short sighted to care about Bitcoin, they only care about fiat.",
					"**Not Fun Fact:** People end their life every cycle by failing to plan for the turmoil of shitcoins crashing and middlemen collapsing, entire lives and families have been ruined. Don't be one of them. Don't borrow, don't over leverage, don't shitcoin, and don't use middlemen. Bitcoin fixes this.",
					"**Fun Fact:** There is no free Bitcoin. There is only spam and scams.",
					"**Fun Fact:** Bitcoin artists like tip_nz, BWA, ZhouTonged, and many others bring Bitcoin education to music, check them out.",
					"**Fun Fact:** Bitcoin is one of the greenest industries on the planet, especially of its size, with around half of all energy coming from renewables and subsidizing renewable energy sources. Other energy consumed includes curtailment - i.e. power that would otherwise be lost to ground - and displacing natural gas vents and flares thus displacing pollution. Bitcoin also uses significantly less energy than the traditional banking sector.",
					"**Fun Fact:** Half of Bitcoiners identify as left leaning, while the other half identify as right leaning. Bitcoin is for everyone who chooses to verify. Because of its unique properties, it is protected and removed from ideology.",
					"**Fun Fact:** Bitcoin saves lives in conflicts, enabling the escape of abuse and allowing would-be conscripts an opportunity to escape through unconfiscatable money and bribery.",
					"**Fun Fact:** If every would-be victim of abuse held Bitcoin they would have more options to escape that abuse. Bitcoin is a liberator.",
					"**Fun Fact:** Lots of people in the Bitcoin space have no idea what they are talking about, often and especially veterans and influencers.",
					"**Fun Fact:** Michael Saylor told noobies to buy the top with debt and remortgage their homes, says Bitcoin isn't a currency, spreads environmental FUD, and attempts to coordinate large groups of miners. If you listen to him you're as big of a fool as he is.",
					"**Fun Fact:** Andreas Antonopoulos is a scamming shitcoiner who spreads FUD and misinformation out of both ignorance and a desire to lead his followers.",
					"**Fun Fact:** Bitcoin Magazine and David Bailey are actually all about shitcoins, NFT's and scams. They even make and sell their own. They were founded by one of the most prolific shitcoiners in history as well.",
					"**Fun Fact:** There are no heroes in Bitcoin, no one to look up to. Everyone who has ever elevated a peer be that peer Gavin Anderson or Roger Ver or Bruce Fenton or Andraes Andreas Antonopoulos or Michael Saylor or David Bailey any other influencer has at some point been betrayed by that peer's greed.",
					"**Fun Fact:** Bitcoin means you don't need to trust middlemen. Are you trusting any middlemen? Why?",
					"**Fun Fact:** Middlemen want to capture you and your business, but Bitcoin means you don't need them. So stop enabling middlemen, especially custodians. Opt for low trust businesses that leverage Bitcoin's innate features to keep your coins in your possession.",
					"**Fun Fact:** Did you know the 50 Bitcoin coinbase reward in the first Bitcoin Block Minted by Satoshi, Block 0, is unspendable even by him?",
					"**Fun Fact:** Miners are responsible for economic security, but nodes are responsible for decentralization and verification and paying miners. If miners ever collude or misbehave it's nodes that have the power to keep them in line - as happened during the blocksize wars.",
					"**Fun Fact:** China banned Bitcoin a dozen times with different price results each time. An ETF was denied a dozen times in the USA with a different price outcome each time. Price is not directly correlated to events the way you might think."
					]

REMOVE_HELP = ["tipUser", "help", "ban", "banafter"]

BLACKLIST = {"xdg": True, "ltc": True, "eth": True, "xrp": True, "bch": True}

BITCOIN_IN_SATS = 100000000
