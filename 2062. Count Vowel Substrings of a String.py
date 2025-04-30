
def countVowelSubstrings(word):
    vowels = 'aeiou'
    cnt = 0
    freq = {}
    start = 0
    for i, c in enumerate(word):
        if c in vowels:
            # find string
            if not freq:
                start = i
            freq[c] = i
            if len(freq) == 5:
                cnt += min(freq.values()) - start + 1
        else:
            freq = {}
    return cnt

print(countVowelSubstrings("cuaieuouac"))