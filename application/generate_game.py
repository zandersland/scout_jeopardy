class GenerateGame:
    def __init__(self):
        self.round = 1
        self.team_one_points = 0
        self.team_two_points = 0
        self.team_three_points = 0
        self.game_data = []
        self.round_one = []
        self.round_two = []
        self.final_jeopardy = []
        self.log = []
        self.team_one_wager = 0
        self.team_two_wager = 0
        self.team_three_wager = 0
        self.team_one_answer = 0
        self.team_two_answer = 0
        self.team_three_answer = 0

    def log_game(self, message):
        self.log.append(message)

    def log_print(self):
        for l in self.log:
            print(l)

    def generate_game(self, _game):
        self.log = []
        self.round = 1
        self.team_one_points = 0
        self.team_two_points = 0
        self.team_three_points = 0
        self.team_one_wager = 0
        self.team_two_wager = 0
        self.team_three_wager = 0
        self.team_one_answer = 0
        self.team_two_answer = 0
        self.team_three_answer = 0

        if _game == '1':
            self.round_one = [('Creeds', '', '', False, 'white'),
                              ('Eagle Required Merit Badges', '', '', False, 'white'),
                              ('EDGE Method', '', '', False, 'white'),
                              ('First Aid', '', '', False, 'white'),
                              ('Grab bag', '', '', False, 'white'),
                              ('Nature', '', '', False, 'white'),
                              (100, 'To follow the Scout Slogan, do one of "these" daily', 'Good turn', False,
                               'white'),
                              (100,
                               'This badge requires planning menus for three full days of meals, plus one dessert',
                               'Cooking', False, 'white'),
                              (100, 'Use the "EDGE" method when doing this', 'Teaching a skill to others', False,
                               'white'),
                              (100, '"Leaves of three, let it be" is the common warning to stay away from this plant',
                               'Poison Ivy, Poison Oak', False, 'white'),
                              (100,
                               'When any leader holds up their hand with the scout sign, they are asking for this',
                               'Quiet, attention', False, 'white'),
                              (100, 'Conifer and Broadleaf are two types of this', 'Tree', False, 'white'),
                              (200, 'This two word phrase is known as the scout motto', 'Be Prepared', False,
                               'white'),
                              (200,
                               'This badge requires a scout to attend a meeting of their city, town, or county councilor school board;',
                               'Citizenship in the Community ', False, 'white'),
                              (200, 'This is what the third letter of the "EDGE" method stands for', 'Guide', False,
                               'white'),
                              (200,
                               'Use the RICE method to treat sprains and strains - Rest, Ice, Compression, and this',
                               'Elevation',
                               False, 'white'),
                              (200, 'This is the official magazine of boy scouts', 'Boys life', False, 'white'),
                              (200, 'A "Plant Key" is used for identifying types of these', 'Trees or plants', False,
                               'white'),
                              (
                                  300, 'Begins with the phrase "On my honor"', 'Scout Oath (or promise)', False,
                                  'white'),
                              (300, 'For this merit badge, Scouts must conduct an emergency mobilization.',
                               'Emergency Preparedness',
                               False, 'white'),
                              (300, 'The second letter of the "EDGE" method stands for this', 'Demonstrate', False,
                               'white'),
                              (300, 'To identify a poisonous coral snake, remember this rhyme: "Red on Yellow...."',
                               'Kill a fellow',
                               False, 'white'),
                              (300, 'This is the color of the background on Scout rank badge', 'Tan', False, 'white'),
                              (300, 'Minnesota\'s State bird', 'Common Loon', False, 'white'),
                              (400, 'This is the third value of the Scout Law', 'Scout Law', False, 'white'),
                              (400, 'For this merit badge, Scouts learn thrift.', 'Personal Management', False,
                               'white'),
                              (400, 'This is what the first letter of the "EDGE" method stands for', 'Explain', False,
                               'white'),
                              (400, 'This is the most common immediate treatment for chemical burns',
                               'Wash off with lots of water',
                               False, 'white'),
                              (400, 'Number of items (besides merit badges) that can be worn on the merit badge sash',
                               'Trick question! NONE!', False, 'white'),
                              (400, 'Animals can be divided into these two types (get a backbone, why don\'t you?)',
                               'Vertebrates and Invertebrates', False, 'white'),
                              (500, 'Often jokingly referred to as the 13th point of the Scout Law.',
                               'What is "hungry"', False, 'white'),
                              (500,
                               'For this merit badge, Scouts must watch a 10\'square piece of land for 60 minutes.',
                               'Environmental Science', False, 'white'), (
                                  500, 'The fourth letter of the "EDGE" method stands for this', 'Enable', False,
                                  'white'),
                              (500, 'This is the first step in the First Aid Method', 'Check the scene', False,
                               'white'),
                              (500, 'This is the number of merit badges required for Life Scout', '11', False,
                               'white'),
                              (500, 'Stinging nettle, Wisteria and Foxglove are all types of this ',
                               'Poisonous plants', False, 'white'),
                              ]
            self.round_two = [('21st Century Merit Badges', '', '', False, 'white'),
                              ('Boy Scout Activities', '', '', False, 'white'),
                              ('Grab bag 2', '', '', False, 'white'),
                              ('Knots', '', '', False, 'white'),
                              ('Life or Death', '', '', False, 'white'),
                              ('Stars (and Stripes)', '', '', False, 'white'),
                              (200,
                               'To receive this merit badge, you join two metal plates and inscribe your initials',
                               'Welding', False, 'white'),
                              (200,
                               'When Scouts swim safely, they use this system in which one Scout looks out for the other and vice versa.',
                               'Buddy System', False, 'white'),
                              (200, 'The adult leader of a Scout Troop is called this', 'Scoutmaster', False,
                               'white'),
                              (200, 'This is known as the first-aid knot.', 'Square knot', False, 'white'),
                              (200,
                               'If someone is not breathing and has no heart beat, do this after calling for help',
                               'CPR', False, 'white'),
                              (200, 'The nickname given to the flag of the United States of America',
                               'Old Glory or Star Spangled Banner', False, 'white'),
                              (400, 'The Robotics merit badge depicts this planet, but you can earn it on Earth.',
                               'Mars', False, 'white'),
                              (400,
                               'Patterns a Scout can use to build a fire include cross-ditch, pyramid, and this one named for a Native American structure.',
                               'Teepee', False, 'white'),
                              (400, 'This is the eighth point of the scout law', 'Cheerful', False, 'white'),
                              (400,
                               'This practice (also used by film editors) joins 2 ropes and makes them almost as strong as the original ones',
                               'Splicing', False, 'white'),
                              (400,
                               'Symptoms of this common condition are fatigue, head and muscle aches, and confusion',
                               'Dehydration', False, 'white'),
                              (400, 'The original US Flag had 13 stars and stripes, which stood for these',
                               'Original 13 Colonies', False, 'white'),
                              (600, 'The “S-A-R” on the badge created in 2012 stands for this lifesaving process.',
                               'Search and Rescue', False, 'white'),
                              (600,
                               'When a properly prepared Scout gets out on the water, he doesn’t leave shore without a PFD, short for this.',
                               'Personal Flotation Device', False, 'white'),
                              (600, 'This should always be carried on a hike', 'First Aid Kit', False, 'white'),
                              (600,
                               'The knot you\'d use if you were hanging from one hand on a cliff.',
                               'Bowline', False, 'white'),
                              (600,
                               'Uncomfortable pressure in the chest, unusual sweating, nausea, and shortness of breath are all common signs of this',
                               'Heart attack', False, 'white'),
                              (600, 'This is the fifth rank earned in Scouts', 'Star Scout', False, 'white'),
                              (800,
                               'There\'s a GPS unit on the badge for this new 10-letter orienteering hobby.',
                               'Geocaching', False, 'white'),
                              (800,
                               'To qualify for a Bugling merit badge, a Scout must know 15 calls including this one sounded at the end of the day.',
                               'Taps', False, 'white'),
                              (800, 'This system of communication uses a series of dots and dashes', 'Morse Code',
                               False, 'white'),
                              (800, 'Knot used to secure tents in wet weather or when using synthetic ropes.',
                               'Tautline Hitch', False, 'white'),
                              (800,
                               'When someone is choking and cannot speak, cough, or breath, use this manuever to save their life',
                               'Heimlich Maneuver', False, 'white'),
                              (800, 'This constellation  can be used to find the North Star',
                               'Ursa Major or the Big Dipper', False, 'white'),
                              (1000,
                               'Boy Scouts learn about coding and debugging while earning this computing-based merit badge.',
                               'Programming', False, 'white'),
                              (1000,
                               'From the French for summoning, it’s the practice of a Scout safely lowering himself down a mountainside.',
                               'Rappelling', False, 'white'),
                              (1000, 'This is considered the symbol of scouting around the world',
                               'Fleur de Lis  or Trefoil', False, 'white'),
                              (1000, 'Technically not a knot, it is used to start many lashings.', 'Clove Hitch',
                               False, 'white'),
                              (1000,
                               'Very hot skin, red skin damp or dry with sweat, rapid pulse and noisy breathing, confusion and irritability, unconsciousness are all signs of this',
                               'Heatstroke', False, 'white'),
                              (1000, 'The stars on the badge of some scout ranks are a symbol of these two things',
                               'Truth and knowledge (or stars in the night sky, suggesting a scouts outdoor adventures)',
                               False, 'white'),
                              ]
            self.game_data = self.round_one
            self.final_jeopardy = [('Scout Essentials',
                                    'Name at least 5 of the 10 Scout Basic Essentials, used to make any outdoor adventure better',
                                    'Pocketknife, rain gear, trail food, flashlight, extra clothing, first aid kit, sun protection, Map and compass, matches and fire starters, water bottle')]
        if _game == '2':
            self.round_one = [('Category1', '', '', False, '#0047b8'),
                              ('Category2', '', '', False, '#0047b8'),
                              ('Category3', '', '', False, '#0047b8'),
                              ('Category4', '', '', False, '#0047b8'),
                              ('Category5', '', '', False, '#0047b8'),
                              ('Category6', '', '', False, '#0047b8'),
                              (100, 'answer1', 'question1', False, '#0047b8'),
                              (100, 'answer21', 'question1', False, '#0047b8'),
                              (100, 'answer31', 'question1', False, '#0047b8'),
                              (100, 'answer41', 'question1', False, '#0047b8'),
                              (100, 'answer51', 'question1', False, '#0047b8'),
                              (100, 'answer61', 'question1', False, '#0047b8'),

                              (200, 'answer2', 'question2', False, '#0047b8'),
                              (200, 'answer22', 'question2', False, '#0047b8'),
                              (200, 'answer32', 'question2', False, '#0047b8'),
                              (200, 'answer42', 'question2', False, '#0047b8'),
                              (200, 'answer52', 'question2', False, '#0047b8'),
                              (200, 'answer62', 'question2', False, '#0047b8'),

                              (300, 'answer3', 'question3', False, '#0047b8'),
                              (300, 'answer23', 'question3', False, '#0047b8'),
                              (300, 'answer33', 'question3', False, '#0047b8'),
                              (300, 'answer43', 'question3', False, '#0047b8'),
                              (300, 'answer53', 'question3', False, '#0047b8'),
                              (300, 'answer63', 'question3', False, '#0047b8'),

                              (400, 'answer4', 'question4', False, '#0047b8'),
                              (400, 'answer24', 'question4', False, '#0047b8'),
                              (400, 'answer34', 'question4', False, '#0047b8'),
                              (400, 'answer44', 'question4', False, '#0047b8'),
                              (400, 'answer54', 'question4', False, '#0047b8'),
                              (400, 'answer64', 'question4', False, '#0047b8'),

                              (500, 'answer5', 'question5', False, '#0047b8'),
                              (500, 'answer25', 'question5', False, '#0047b8'),
                              (500, 'answer35', 'question5', False, '#0047b8'),
                              (500, 'answer45', 'question5', False, '#0047b8'),
                              (500, 'answer55', 'question5', False, 'white'),
                              (500, 'answer65', 'question5', False, '#0047b8')
                              ]
            self.round_two = [('Category7', '', '', False, '#0047b8'),
                              ('Category8', '', '', False, '#0047b8'),
                              ('Category9', '', '', False, '#0047b8'),
                              ('Category10', '', '', False, '#0047b8'),
                              ('Category11', '', '', False, '#0047b8'),
                              ('Category12', '', '', False, '#0047b8'),
                              (200, 'answer1', 'question1', False, '#0047b8'),
                              (200, 'answer21', 'question1', False, '#0047b8'),
                              (200, 'answer31', 'question1', False, '#0047b8'),
                              (200, 'answer41', 'question1', False, '#0047b8'),
                              (200, 'answer51', 'question1', False, '#0047b8'),
                              (200, 'answer61', 'question1', False, '#0047b8'),

                              (400, 'answer2', 'question2', False, '#0047b8'),
                              (400, 'answer22', 'question2', False, '#0047b8'),
                              (400, 'answer32', 'question2', False, '#0047b8'),
                              (400, 'answer42', 'question2', False, '#0047b8'),
                              (400, 'answer52', 'question2', False, '#0047b8'),
                              (400, 'answer62', 'question2', False, '#0047b8'),

                              (600, 'answer3', 'question3', False, '#0047b8'),
                              (600, 'answer23', 'question3', False, '#0047b8'),
                              (600, 'answer33', 'question3', False, '#0047b8'),
                              (600, 'answer43', 'question3', False, '#0047b8'),
                              (600, 'answer53', 'question3', False, '#0047b8'),
                              (600, 'answer63', 'question3', False, '#0047b8'),

                              (800, 'answer4', 'question4', False, '#0047b8'),
                              (800, 'answer24', 'question4', False, '#0047b8'),
                              (800, 'answer34', 'question4', False, '#0047b8'),
                              (800, 'answer44', 'question4', False, '#0047b8'),
                              (800, 'answer54', 'question4', False, '#0047b8'),
                              (800, 'answer64', 'question4', False, '#0047b8'),

                              (1000, 'answer5', 'question5', False, '#0047b8'),
                              (1000, 'answer25', 'question5', False, '#0047b8'),
                              (1000, 'answer35', 'question5', False, '#0047b8'),
                              (1000, 'answer45', 'question5', False, '#0047b8'),
                              (1000, 'answer55', 'question5', False, 'white'),
                              (1000, 'answer65', 'question5', False, '#0047b8')
                              ]
            self.game_data = self.round_one
            self.final_jeopardy = [('Final category',
                                    'Minneapolis',
                                    'Capital of Minnesota')]
