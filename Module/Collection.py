from collections import Counter


testList1 = [1, 2, 4, 5, 3, 1, 6, 8, 2, 1, 8, 9, 3, 1, 5, 7, 8]
testList2 = ['s', 'd', 's', 'h', 't', 12, 12, 13, 14, 12]
testSentence = "This is banaglore,sub area in marathalli, pin code 560037, this is a village"
testString = "ndjkalisjfascoqiwjamcamsl"
print(Counter(testList1))
print(Counter(testList2))
print(type(Counter(testList2)))
print(Counter(testSentence.lower().split()))
print(Counter(testString).most_common())
