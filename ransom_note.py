def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    
    # I did it a long way to practice more.
    if len(ransomNote) > len(magazine):
        return False
    
    ransome_count = {}
    magazine_count = {}

    if len(ransomNote) > len(magazine):
        return False

    for char in ransomNote:
        if char not in magazine:
            return False
        ransome_count[char] = ransome_count.get(char, 0) + 1
    
    for char in magazine:
        magazine_count[char] = magazine_count.get(char, 0) + 1
    
    for char, count in ransome_count.items():
        if magazine_count.get(char, 0) < count:
            return False
    return True

# This is a shorter version:
"""
if len(ransomNote) > len(magazine):
        return False
    
    from collections import Counter
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True
"""