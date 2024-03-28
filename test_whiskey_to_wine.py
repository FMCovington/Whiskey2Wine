# Simple unit test of whiskey_to_wine.py

from whiskey_to_wine import whiskey2wine


def test_whiskey2wine(proof=80, ounces=1.5):
    result = whiskey2wine(proof, ounces)
    print("Result: ", result)
    print(proof, ounces, result)
    assert result[-1][-4:] == 'True', f"Result does not equal expectation: {result[-1][-4:]}"


# test defaults
print('Testing defaults (80,1.5):')
test_whiskey2wine()
print()

# test reasonable combinations of proof and volume
print('Testing all reasonable values for each parameter:')
for prf in range(40, 195):
    for vol in range(1, 10):
        test_whiskey2wine(prf, vol)

# Only prints if no assertion errors.
print("\n100% Success")

input("\nPress ENTER to exit.")
