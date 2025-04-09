from collections import defaultdict
from typing import List

def countSentences(wordSet: List[str], sentences: List[str]) -> List[int]:
    # Step 1: Build the anagram group map
    anagram_map = defaultdict(int)
    for word in wordSet:
        signature = ''.join(sorted(word))
        anagram_map[signature] += 1

    # Step 2: Count valid sentences for each input sentence
    result = []
    for sentence in sentences:
        words = sentence.split()
        count = 1
        for word in words:
            signature = ''.join(sorted(word))
            count *= anagram_map.get(signature, 1)
        result.append(count)

    return result


wordSet = ['listen', 'silent', 'it', 'is']
sentences = ['listen it is silent']
print(countSentences(wordSet, sentences))  # Output: [4]
