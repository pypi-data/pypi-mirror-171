# ColorBytes

A simple module to make your python code come alive with color.

This is the new and updated version of ColorKeys.
https://pypi.org/project/colorkeys/ (Outdated)


## Installation
```
pip install colorbytes
```
**Requirements**:

- colorama >= 0.4.4
- colr >= 0.9.1
- psutil >= 5.8.0

## Remove

```
pip uninstall -y colorbytes
```

## Example Usage

```python
from colorbytes import colors

name = input("What's your name? ")
print("Hello " + colors.BRIGHT_GREEN + name + colors.RESET)
```

## List of colors

```python

    # - - - - - - BLACKS - - - - - -

    BLACK = C().hex("000000")
    CHARCOAL = C().hex("36454F")
    DARK_GREEN = C().hex("023020")
    DARK_PURPLE = C().hex("301934")
    JET_BLACK = C().hex("343434")
    LICORICE = C().hex("1B1212")
    MATTE_BLACK = C().hex("28282B")
    MIDNIGHT_BLUE = C().hex("191970")
    ONYX = C().hex("353935")


    # - - - - - - BLUES - - - - - -

    AQUA = C().hex("00FFFF")
    AZURE = C().hex("F0FFFF")
    BABY_BLUE = C().hex("89CFF0")
    BLUE = C().hex("0000FF")
    BLUE_GRAY = C().hex("7393B3")
    BLUE_GREEN = C().hex("088F8F")
    BRIGHT_BLUE = C().hex("0096FF")
    CADET_BLUE = C().hex("5F9EA0")
    COBALT_BLUE = C().hex("0047AB")
    CORNFLOWER_BLUE = C().hex("6495ED")
    DARK_BLUE = C().hex("00008B")
    DENIM = C().hex("6F8FAF")
    EGYPTIAN_BLUE = C().hex("1434A4")
    ELECTRIC_BLUE = C().hex("7DF9FF")
    GLAUCOUS = C().hex("6082B6")
    JADE = C().hex("00A36C")
    INDIGO = C().hex("3F00FF")
    IRIS = C().hex("5D3FD3")
    LIGHT_BLUE = C().hex("ADD8E6")
    NAVY_BLUE = C().hex("000080")
    NEON_BLUE = C().hex("1F51FF")
    PASTEL_BLUE = C().hex("A7C7E7")
    PERIWINKLE = C().hex("CCCCFF")
    POWDER_BLUE = C().hex("B6D0E2")
    ROBIN_EGG_BLUE = C().hex("96DED1")
    ROYAL_BLUE = C().hex("4169E1")
    SAPPHIRE_BLUE = C().hex("0F52BA")
    SEAFOAM_GREEN = C().hex("9FE2BF")
    SKY_BLUE = C().hex("87CEEB")
    STEEL_BLUE = C().hex("4682B4")
    TEAL = C().hex("008080")
    TURQUOISE = C().hex("40E0D0")
    ULTRAMARINE = C().hex("0437F2")
    VERDIGRIS = C().hex("40B5AD")
    ZAFFRE = C().hex("0818A8")


    # - - - - - - BROWNS - - - - - -

    ALMOND = C().hex("EADDCA")
    BRASS = C().hex("E1C16E")
    BRONZE = C().hex("CD7F32")
    BROWN = C().hex("A52A2A")
    BUFF = C().hex("DAA06D")
    BURGUNDY = C().hex("800020")
    BURNT_SIENNA = C().hex("E97451")
    BURNT_UMBER = C().hex("6E260E")
    CAMEL = C().hex("C19A6B")
    CHESTNUT = C().hex("954535")
    CHOCOLATE = C().hex("7B3F00")
    CINNAMON = C().hex("D27D2D")
    COFFEE = C().hex("6F4E37")
    COGNAC = C().hex("834333")
    COPPER = C().hex("B87333")
    CORDOVAN = C().hex("814141")
    DARK_BROWN = C().hex("5C4033")
    DARK_RED = C().hex("8B0000")
    DARK_TAN = C().hex("988558")
    ECRU = C().hex("C2B280")
    FAWN = C().hex("E5AA70")
    GARNET = C().hex("9A2A2A")
    GOLDEN_BROWN = C().hex("966919")
    KHAKI = C().hex("F0E68C")
    LIGHT_BROWN = C().hex("C4A484")
    MAHOGANY = C().hex("C04000")
    MAROON = C().hex("800000")
    MOCHA = C().hex("967969")
    NUDE = C().hex("F2D2BD")
    OCHRE = C().hex("CC7722")
    OLIVE_GREEN = C().hex("808000")
    OXBLOOD = C().hex("4A0404")
    PUCE = C().hex("A95C68")
    RED_OCHRE = C().hex("913831")
    RUSSET = C().hex("80461B")
    SADDLE_BROWN = C().hex("8B4513")
    SIENNA = C().hex("A0522D")
    TAN = C().hex("D2B48C")
    TAUPE = C().hex("483C32")
    TUSCAN_RED = C().hex("7C3030")
    WHEAT = C().hex("F5DEB3")
    WINE = C().hex("722F37")


    # - - - - - - GREYS - - - - - -

    ASH_GRAY = C().hex("B2BEB5")
    DARK_GRAY = C().hex("A9A9A9")
    GRAY = C().hex("808080")
    GUNMETAL_GRAY = C().hex("818589")
    LIGHT_GRAY = C().hex("D3D3D3")
    PEWTER = C().hex("899499")
    PLATINUM = C().hex("E5E4E2")
    SAGE_GREEN = C().hex("8A9A5B")
    SILVER = C().hex("C0C0C0")
    SLATE_GRAY = C().hex("708090")
    SMOKE = C().hex("848884")
    STEEL_GRAY = C().hex("71797E")


    # - - - - - - GREENS - - - - - -

    AQUAMARINE = C().hex("7FFFD4")
    ARMY_GREEN = C().hex("454B1B")
    BRIGHT_GREEN = C().hex("AAFF00")
    CADMIUM_GREEN = C().hex("097969")
    CELADON = C().hex("AFE1AF")
    CHARTREUSE = C().hex("DFFF00")
    CITRINE = C().hex("E4D00A")
    EMERALD_GREEN = C().hex("50C878")
    EUCALYPTUS = C().hex("5F8575")
    FERN_GREEN = C().hex("4F7942")
    FOREST_GREEN = C().hex("228B22")
    GRASS_GREEN = C().hex("7CFC00")
    GREEN = C().hex("008000")
    HUNTER_GREEN = C().hex("355E3B")
    JUNGLE_GREEN = C().hex("2AAA8A")
    KELLY_GREEN = C().hex("4CBB17")
    LIGHT_GREEN = C().hex("90EE90")
    LIME_GREEN = C().hex("32CD32")
    LINCOLN_GREEN = C().hex("478778")
    MALACHITE = C().hex("0BDA51")
    MINT_GREEN = C().hex("98FB98")
    NEON_GREEN = C().hex("0FFF50")
    NYANZA = C().hex("ECFFDC")
    PASTEL_GREEN = C().hex("C1E1C1")
    PEAR = C().hex("C9CC3F")
    PERIDOT = C().hex("B4C424")
    PISTACHIO = C().hex("93C572")
    SEA_GREEN = C().hex("2E8B57")
    SHAMROCK_GREEN = C().hex("009E60")
    SPRING_GREEN = C().hex("00FF7F")
    VEGAS_GOLD = C().hex("C4B454")
    VIRIDIAN = C().hex("40826D")


    # - - - - - - ORANGE - - - - - -

    AMBER = C().hex("FFBF00")
    APRICOT = C().hex("FBCEB1")
    BRIGHT_ORANGE = C().hex("FFAC1C")
    BURNT_ORANGE = C().hex("CC5500")
    BUTTERSCOTCH = C().hex("E3963E")
    CADMIUM_ORANGE = C().hex("F28C28")
    CORAL = C().hex("FF7F50")
    CORAL_PINK = C().hex("F88379")
    DARK_ORANGE = C().hex("8B4000")
    DESERT = C().hex("FAD5A5")
    GAMBOGE = C().hex("E49B0F")
    GOLDEN_YELLOW = C().hex("FFC000")
    GOLDENROD = C().hex("DAA520")
    LIGHT_ORANGE = C().hex("FFD580")
    MANGO = C().hex("F4BB44")
    NAVAJO_WHITE = C().hex("FFDEAD")
    NEON_ORANGE = C().hex("FF5F1F")
    ORANGE = C().hex("FFA500")
    PASTEL_ORANGE = C().hex("FAC898")
    PEACH = C().hex("FFE5B4")
    PERSIMMON = C().hex("EC5800")
    PINK_ORANGE = C().hex("F89880")
    POPPY = C().hex("E35335")
    PUMPKIN_ORANGE = C().hex("FF7518")
    RED_ORANGE = C().hex("FF4433")
    SAFETY_ORANGE = C().hex("FF5F15")
    SALMON = C().hex("FA8072")
    SEASHELL = C().hex("FFF5EE")
    SUNSET_ORANGE = C().hex("FA5F55")
    TANGERINE = C().hex("F08000")
    TERRA_COTTA = C().hex("E3735E")
    YELLOW_ORANGE = C().hex("FFAA33")


    # - - - - - - PINKS - - - - - -

    AMARANTH = C().hex("9F2B68")
    CERISE = C().hex("DE3163")
    CLARET = C().hex("811331")
    CRIMSON = C().hex("DC143C")
    DARK_PINK = C().hex("AA336A")
    DUSTY_ROSE = C().hex("C9A9A6")
    FUCHSIA = C().hex("FF00FF")
    HOT_PINK = C().hex("FF69B4")
    LIGHT_PINK = C().hex("FFB6C1")
    MILLENNIAL_PINK = C().hex("F3CFC6")
    MULBERRY = C().hex("770737")
    NEON_PINK = C().hex("FF10F0")
    ORCHID = C().hex("DA70D6")
    PASTEL_PINK = C().hex("F8C8DC")
    PASTEL_RED = C().hex("FAA0A0")
    PINK = C().hex("FFC0CB")
    PLUM = C().hex("673147")
    PURPLE = C().hex("800080")
    RASPBERRY = C().hex("E30B5C")
    RED_PURPLE = C().hex("953553")
    ROSE = C().hex("F33A6A")
    ROSE_GOLD = C().hex("E0BFB8")
    ROSE_RED = C().hex("C21E56")
    RUBY_RED = C().hex("E0115F")
    THISTLE = C().hex("D8BFD8")
    WATERMELON_PINK = C().hex("E37383")


    # - - - - - - PURPLES - - - - - -

    BRIGHT_PURPLE = C().hex("BF40BF")
    BYZANTIUM = C().hex("702963")
    EGGPLANT = C().hex("483248")
    LAVENDER = C().hex("E6E6FA")
    LIGHT_PURPLE = C().hex("CBC3E3")
    LIGHT_VIOLET = C().hex("CF9FFF")
    LILAC = C().hex("AA98A9")
    MAUVE = C().hex("E0B0FF")
    MAUVE_TAUPE = C().hex("915F6D")
    PASTEL_PURPLE = C().hex("C3B1E1")
    QUARTZ = C().hex("51414F")
    TYRIAN_PURPLE = C().hex("630330")
    VIOLET = C().hex("7F00FF")
    WISTERIA = C().hex("BDB5D5")


    # - - - - - - REDS - - - - - -

    BLOOD_RED = C().hex("880808")
    BRICK_RED = C().hex("AA4A44")
    BRIGHT_RED = C().hex("EE4B2B")
    CADMIUM_RED = C().hex("D22B2B")
    CARDINAL_RED = C().hex("C41E3A")
    CARMINE = C().hex("D70040")
    CHERRY = C().hex("D2042D")
    FALU_RED = C().hex("7B1818")
    MARSALA = C().hex("986868")
    NEON_RED = C().hex("FF3131")
    RED = C().hex("FF0000")
    SCARLET = C().hex("FF2400")
    VENETIAN_RED = C().hex("A42A04")
    VERMILLION = C().hex("E34234")


    # - - - - - - WHITES - - - - - -

    ALABASTER = C().hex("EDEADE")
    BEIGE = C().hex("F5F5DC")
    BONE_WHITE = C().hex("F9F6EE")
    CORNSILK = C().hex("FFF8DC")
    CREAM = C().hex("FFFDD0")
    EGGSHELL = C().hex("F0EAD6")
    IVORY = C().hex("FFFFF0")
    LINEN = C().hex("E9DCC9")
    OFF_WHITE = C().hex("FAF9F6")
    PARCHMENT = C().hex("FCF5E5")
    PEARL = C().hex("E2DFD2")
    VANILLA = C().hex("F3E5AB")
    WHITE = C().hex("FFFFFF")


    # - - - - - - YELLOWS - - - - - -

    BRIGHT_YELLOW = C().hex("FFEA00")
    CADMIUM_YELLOW = C().hex("FDDA0D")
    CANARY_YELLOW = C().hex("FFFF8F")
    DARK_YELLOW = C().hex("8B8000")
    FLAX = C().hex("EEDC82")
    GOLD = C().hex("FFD700")
    ICTERINE = C().hex("FCF55F")
    JASMINE = C().hex("F8DE7E")
    LEMON_YELLOW = C().hex("FAFA33")
    MAIZE = C().hex("FBEC5D")
    MUSTARD_YELLOW = C().hex("FFDB58")
    NAPLES_YELLOW = C().hex("FADA5E")
    PASTEL_YELLOW = C().hex("FFFAA0")
    SAFFRON = C().hex("F4C430")
    YELLOW = C().hex("FFFF00")

    RESET = "\033[0m"
```

# Changelog

<!---  VERSION 1.0.1 --->

<h1>

```diff
        V1.0.1
```

</h1>

<h3>
    
```diff
+ Added
```
    
</h3>

- Added A Changelog
- Added VENETIAN_RED
- Added PASTEL_YELLOW

<h3>
    
```diff
! Changed
```
    
</h3>

- Updated README
- Updated CORNFLOWER_BLUE, Gives A More Accurate Color Now

<h3>
    
```diff
- Removed
```
    
</h3>

- Removed NEON_YELLOW, Hex Was Invalid




<!---  VERSION 1.0.0 --->
#
<h1>

```diff
        V1.0.0
```

</h1>

<h3>
    
```diff
+ Added
```
    
</h3>

- Initial Release

<h3>
    
```diff
! Changed
```
    
</h3>

- Nothing


<h3>
    
```diff
- Removed
```
    
</h3>

- Nothing
