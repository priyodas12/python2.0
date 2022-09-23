score_card = {'mike': 334, 'jill': 462, 'keyra': 342}

# print keys and values
print(list(score_card.keys()))
print(list(score_card.values()))

for key, value in score_card.items():
    print(f" {key} -> {value}")
