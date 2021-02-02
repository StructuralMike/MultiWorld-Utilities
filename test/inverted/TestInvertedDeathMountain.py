from test.inverted.TestInverted import TestInverted


class TestInvertedDeathMountain(TestInverted):

    def testWestDeathMountain(self):
        self.run_location_tests([
            ["Old Man", False, []],
            ["Old Man", False, [], ['Progressive Glove', 'Flute']],
            ["Old Man", False, [], ['Lamp']],
            ["Old Man", True, ['Progressive Glove', 'Lamp']],
            ["Old Man", True, ['Flute', 'Lamp']],

            ["Spectacle Rock Cave", False, []],
            ["Spectacle Rock Cave", False, [], ['Progressive Glove', 'Flute']],
            ["Spectacle Rock Cave", False, [], ['Lamp', 'Flute']],
            ["Spectacle Rock Cave", False, ['Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Spectacle Rock Cave", True, ['Flute']],
            ["Spectacle Rock Cave", True, ['Progressive Glove', 'Lamp']],
        ])
        
    def testEastDeathMountain(self):
        self.run_location_tests([
            ["Spiral Cave", False, []],
            ["Spiral Cave", False, [], ['Moon Pearl']],
            ["Spiral Cave", False, [], ['Progressive Glove', 'Flute']],
            ["Spiral Cave", False, [], ['Lamp', 'Flute']],
            ["Spiral Cave", False, ['Progressive Glove'], ['Hookshot', 'Progressive Glove']],
            ["Spiral Cave", False, ['Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Spiral Cave", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Spiral Cave", True, ['Moon Pearl', 'Flute', 'Hookshot']],
            ["Spiral Cave", True, ['Moon Pearl', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Spiral Cave", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Lamp']],
            ["Spiral Cave", True, ['Moon Pearl', 'Flute', 'Progressive Glove', 'Progressive Glove']],

            ["Paradox Cave Lower - Far Left", False, []],
            ["Paradox Cave Lower - Far Left", False, [], ['Moon Pearl']],
            ["Paradox Cave Lower - Far Left", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Far Left", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Lower - Far Left", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Left", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Left", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Left", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Paradox Cave Lower - Left", False, []],
            ["Paradox Cave Lower - Left", False, [], ['Moon Pearl']],
            ["Paradox Cave Lower - Left", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Left", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Lower - Left", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Left", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Left", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Lower - Left", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Left", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Left", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Lower - Left", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Paradox Cave Lower - Middle", False, []],
            ["Paradox Cave Lower - Middle", False, [], ['Moon Pearl']],
            ["Paradox Cave Lower - Middle", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Middle", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Lower - Middle", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Middle", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Middle", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Lower - Middle", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Lower - Middle", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Paradox Cave Lower - Right", False, []],
            ["Paradox Cave Lower - Right", False, [], ['Moon Pearl']],
            ["Paradox Cave Lower - Right", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Right", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Lower - Right", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Right", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Right", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Lower - Right", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Right", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Right", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Lower - Right", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Paradox Cave Lower - Far Right", False, []],
            ["Paradox Cave Lower - Far Right", False, [], ['Moon Pearl']],
            ["Paradox Cave Lower - Far Right", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Far Right", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Lower - Far Right", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Right", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Right", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Lower - Far Right", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Paradox Cave Upper - Left", False, []],
            ["Paradox Cave Upper - Left", False, [], ['Moon Pearl']],
            ["Paradox Cave Upper - Left", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Upper - Left", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Upper - Left", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Upper - Left", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Upper - Left", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Upper - Left", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Upper - Left", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Upper - Left", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Upper - Left", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Paradox Cave Upper - Right", False, []],
            ["Paradox Cave Upper - Right", False, [], ['Moon Pearl']],
            ["Paradox Cave Upper - Right", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Upper - Right", False, [], ['Lamp', 'Flute']],
            ["Paradox Cave Upper - Right", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Upper - Right", False, ['Progressive Glove', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Upper - Right", False, ['Flute', 'Progressive Glove', 'Hammer', 'Moon Pearl']],
            ["Paradox Cave Upper - Right", True, ['Flute', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Upper - Right", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Moon Pearl']],
            ["Paradox Cave Upper - Right", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl']],
            ["Paradox Cave Upper - Right", True, ['Flute', 'Progressive Glove', 'Progressive Glove', 'Moon Pearl']],
            
            ["Mimic Cave", False, []],
            ["Mimic Cave", False, [], ['Moon Pearl']],
            ["Mimic Cave", False, [], ['Hammer']],
            ["Mimic Cave", False, [], ['Progressive Glove', 'Flute']],
            ["Mimic Cave", False, [], ['Lamp', 'Flute']],
            ["Mimic Cave", True, ['Flute', 'Moon Pearl', 'Hammer', 'Hookshot']],
            ["Mimic Cave", True, ['Flute', 'Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hammer']],
            ["Mimic Cave", True, ['Progressive Glove', 'Lamp', 'Moon Pearl', 'Hammer', 'Hookshot']],
            ["Mimic Cave", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl', 'Hammer']],

            ["Ether Tablet", False, []],
            ["Ether Tablet", False, [], ['Moon Pearl']],
            ["Ether Tablet", False, [], ['Progressive Glove', 'Flute']],
            ["Ether Tablet", False, [], ['Lamp', 'Flute']],
            ["Ether Tablet", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Ether Tablet", False, [], ['Hammer']],
            ["Ether Tablet", False, ['Progressive Sword'], ['Progressive Sword']],
            ["Ether Tablet", False, [], ['Book of Mudora']],
            ["Ether Tablet", True, ['Flute', 'Moon Pearl', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Flute', 'Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hammer', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Moon Pearl', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl', 'Hammer', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],

            ["Spectacle Rock", False, []],
            ["Spectacle Rock", False, [], ['Moon Pearl']],
            ["Spectacle Rock", False, [], ['Progressive Glove', 'Flute']],
            ["Spectacle Rock", False, [], ['Lamp', 'Flute']],
            ["Spectacle Rock", False, ['Progressive Glove'], ['Progressive Glove', 'Hookshot']],
            ["Spectacle Rock", False, [], ['Hammer']],
            ["Spectacle Rock", True, ['Flute', 'Moon Pearl', 'Hammer', 'Hookshot']],
            ["Spectacle Rock", True, ['Flute', 'Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hammer']],
            ["Spectacle Rock", True, ['Progressive Glove', 'Lamp', 'Moon Pearl', 'Hammer', 'Hookshot']],
            ["Spectacle Rock", True, ['Progressive Glove', 'Progressive Glove', 'Lamp', 'Moon Pearl', 'Hammer']],
        ])

    def testEastDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Superbunny Cave - Top", False, []],
            ["Superbunny Cave - Top", True, ['Flute']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Lamp']],

            ["Superbunny Cave - Bottom", False, []],
            ["Superbunny Cave - Bottom", True, ['Flute']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Lamp']],

            ["Hookshot Cave - Bottom Right", False, []],
            ["Hookshot Cave - Bottom Right", False, [], ['Progressive Glove', 'Flute']],
            ["Hookshot Cave - Bottom Right", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Bottom Right", True, ['Progressive Glove', 'Lamp', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", True, ['Progressive Glove', 'Flute', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Hookshot Cave - Bottom Right", True, ['Progressive Glove', 'Flute', 'Hookshot']],

            ["Hookshot Cave - Bottom Left", False, []],
            ["Hookshot Cave - Bottom Left", False, [], ['Progressive Glove', 'Flute']],
            ["Hookshot Cave - Bottom Left", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Bottom Left", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Hookshot Cave - Bottom Left", True, ['Progressive Glove', 'Flute', 'Hookshot']],

            ["Hookshot Cave - Top Left", False, []],
            ["Hookshot Cave - Top Left", False, [], ['Progressive Glove', 'Flute']],
            ["Hookshot Cave - Top Left", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Top Left", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Hookshot Cave - Top Left", True, ['Progressive Glove', 'Flute', 'Hookshot']],

            ["Hookshot Cave - Top Right", False, []],
            ["Hookshot Cave - Top Right", False, [], ['Progressive Glove', 'Flute']],
            ["Hookshot Cave - Top Right", False, [], ['Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Top Right", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Hookshot Cave - Top Right", True, ['Progressive Glove', 'Flute', 'Hookshot']],
        ])

    def testWestDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Spike Cave", False, []],
            ["Spike Cave", False, [], ['Progressive Glove']],
            ["Spike Cave", False, [], ['Hammer']],
            ["Spike Cave", False, [], ['Cape', 'Cane of Byrna']],
            ["Spike Cave", False, [], ['Cane of Byrna', 'AnyBottle', 'Magic Upgrade (1/2)']],
            ["Spike Cave", False, [], ['AnyBottle', 'Magic Upgrade (1/2)', 'Pegasus Boots', 'Boss Heart Container', 'Piece of Heart', 'Sanctuary Heart Container']],

            ["Spike Cave", True, ['Bottle', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],

            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],

            ["Spike Cave", True, ['Pegasus Boots', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Pegasus Boots', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
            ["Spike Cave", True, ['Boss Heart Container', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Boss Heart Container', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
        ])

