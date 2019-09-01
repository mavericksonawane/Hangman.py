""" following code is a program of hangman in python.
    it contains the name of top 100 fortune companies.
    programmer: maverick sonawane
    github: mavericksonawane
    email : mavericksonawane@gmail.com
    ************************* MAYUR SONAWANE ********************************
    i hope its not that much irritating
        ENJOY :)
"""



import random

def get_word():
    words = ['Walmart',
             'ExxonMobil',
             'Apple',
             'BerkshireHathaway',
             'Amazon',
             'UnitedHealthGroup',
             'McKesson',
             'CVSHealth',
             'AT&T',
             'AmerisourceBergen',
             'Chevron',
             'Ford',
            'GeneralMotors',
            'Costco',
            'Alphabet',
            'CardinalHealth',
            'WalgreensBootsAlliance',
            'JPMorganChase',
            'Verizon',
            'Kroger',
            'GeneralElectric',
            'FannieMae',
            'Phillips66',
            'ValeroEnergy',
            'BankofAmerica',
            'Microsoft',
            'HomeDepot',
            'Boeing',
            'WellsFargo',
            'Citigroup',
            'MarathonPetroleum',
            'Comcast',
            'Anthem',
            'Dell',
            'DowDuPont',
            'StateFarmInsurance',
            'Johnson&Johnson',
            'IBM',
            'Target',
            'FreddieMac',
            'UPS',
            'Lowe',
            'Intel',
            'MetLife',
            'ProcterandGamble',
            'UnitedTechnologies',
            'FedEx',
            'Pepsi',
            'ArcherDanielsMidland',
            'PrudentialFinancial',
            'Centene',
            'Albertsons',
            'Disney',
            'Sysco',
            'HP',
            'Humana',
            'Facebook',
            'Caterpillar',
            'EnergyTransferEquity',
            'LockheedMartin',
            'Pfizer',
            'GoldmanSachsGroup',
            'MorganStanley',
            'CiscoSystems',
            'Cigna',
            'AIG',
            'HCAHoldings',
            'AmericanAirlinesGroup',
            'DeltaAirLines',
            'CharterCommunications',
            'NewYorkLifeInsurance',
            'AmericanExpress',
            'Nationwide',
            'BestBuy',
            'LibertyMutualInsuranceGroup',
            'Merck',
            'HoneywellInternational',
            'UnitedContinentalHoldings',
            'TIAA',
            'TysonFoods',
            'Oracle',
            'Allstate',
            'WorldFuelServices',
            'MassachusettsMutualLifeInsurance',
            'TJX',
            'ConocoPhillips',
            'Deere',
            'TechData',
            'EnterpriseProductsPartners',
            'Nike',
            'PublixSuperMarkets',
            'GeneralDynamics',
            'Exelon',
            'PlainsGPHoldings',
            '3M',
            'AbbVie',
            'CHS',
            'CapitalOneFinancial',
            'Progressive',
            'CocaCola']

    return random.choice(words).upper()

def check(word,guesses,guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            matches += 1

    if matches > 1:
        print('Yah boii! The word Contains',matches,'"' + guess + '"' + 's')
    elif matches ==1:
        print('Yeah Boii! The word contains the letter "' + guess + '"')
    else:
        print('Nah! The word doesnt contain the letter "' + guess + '"')

    return status

def main():
    word = get_word()
    #print(word)
    guesses = []
    guessed = False
    print("The word is a name of one of the fortune 100 companies")
    print("HINT: The word contains", len(word), 'letters.')
    while not guessed:
        text = "Please enter one letter of the word in your mind:  ".format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('Yeah! But you already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is not what we want.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True

            else:
                print(result)
        else:
            print('Not a Valid Entry. Use Better English.')

    print('Yeasss, the word is', word + '! You made it in', len(guesses), 'tries.')


main()

















                  




















    








              
























    
