"""
Author: F. M. (Mike) Covington

This module uses the classic formula  C₁V₁ = C₂V₂  to determine how
much non-alcoholic beverage (water) should be added to an alcoholic beverage of
a known proof and quantity to adjust its alcohol percentage to that of wine.

Usage:  whiskey2wine()
        Then, supply values when prompted.
        If no values are supplied, defaults of 80 proof (40%) and 1.5 oz (one
        shot) are used.
"""

# Equation:  C₁V₁ = C₂V₂
# C ==> concentration, V ==> volume, ABV = Alcohol by Volume
#
# Whiskey Dilution Example:
# Assume whiskey concentration == C₁% ABV (i.e. 2(C₁) proof )
# Assume whiskey volume == V₁ oz.
# Assume outcome (C₂ == 14%)  # average wine concentration (ABV)
# determine target volume V₂ (including whiskey volume and water volume)
# determine water volume to add to whiskey volume to achieve 14%  (wine ABV)
# Simplify equation:  C₁V₁ = C₂V₂ ==> V₂ = C₁V₁/C₂
# Solve for V₂
#
# Python's native floats will not suffice due to their rounding limitations.
# The decimal module is required to achieve True from various numeric
# equality tests involving fractional values in the C₁V₁ = C₂V₂ equation.
from decimal import Decimal


# This module can be tested with test_whiskey_to_wine.py and should pass.
# Without the use of decimal and Decimal, it will fail on specific values.

def whiskey2wine(proof=80, ounces=1.5):
    """Calculate amount of non-alcoholic beverage to add to whiskey to
    reduce ABV to that of wine (14%).

    Usage:  whiskey2wine()
        Then, supply values when prompted.
        If no values are supplied, defaults of 80 proof (40%) and 1.5 oz (one
        shot) are used."""
    print("\nTurning Whiskey into Wine by Using 'C₁V₁ = C₂V₂' Dilution Formula:\n")
    try:
        whiskey_ABV = Decimal(proof / 200)
    except ValueError:
        whiskey_ABV = Decimal(0.40)  # 40% ABV whiskey
    whiskey_volume = Decimal(float(ounces))
    wine_abv = Decimal(0.14)  # 14% average ABV of wine
    ending_volume = whiskey_ABV * whiskey_volume / Decimal(wine_abv)
    water_to_add = ending_volume - whiskey_volume
    # assign vars to formula varnames:
    c1, v1, c2, v2 = whiskey_ABV, whiskey_volume, wine_abv, ending_volume
    C1V1 = round(c1 * v1, 15)  # Round formula vars to 15 decimal places
    C2V2 = round(c2 * v2, 15)
    # Summarize data and return summary:
    return (f"Original ABV of whiskey: {round(whiskey_ABV * 100, 2)}%",
            f"Average ABV of wine: {round(wine_abv * 100, 2)}%",
            "-" * 30,
            f"Original volume of whiskey: {round(whiskey_volume, 2)} oz.",
            f"Water to add to whiskey: {round(water_to_add, 2)} oz.",
            f"Ending beverage volume: {round(ending_volume, 2)} oz.",
            f"Ending beverage ABV: {round(Decimal(wine_abv * 100), 2)}% (same as wine).",
            "-" * 30,
            "Verification using 'C₁V₁ = C₂V₂' dilution formula:  "
            f"Success={C1V1 == C2V2}")  # Proof by classic dilution formula


if __name__ == '__main__':
    try:
        proof = float(input("\nEnter Whiskey Proof Value:  "))
        ounces = float(input("Enter Ounces of Whiskey:  "))
        print(*whiskey2wine(proof, ounces), sep="\n")
    except ValueError:
        print("\nUsing defaults:  80 proof and 1.5 oz. (one shot).")
        print(*whiskey2wine(), sep="\n")

    # Note:  2:3 ratio (5oz) of Rum and Coke has exactly
    # the same alcohol content as a 5oz glass of wine.

    input("\nPress ENTER to exit: ")
