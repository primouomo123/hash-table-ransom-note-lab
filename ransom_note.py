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
    if len(ransomNote) > len(magazine):
        return False
    
    from collections import Counter
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True