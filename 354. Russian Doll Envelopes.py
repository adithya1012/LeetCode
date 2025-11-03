def maxEnvelopes(envelopes):
    env = sorted(envelopes, key = lambda x: (x[0], -x[1]))
    print(env)

maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])