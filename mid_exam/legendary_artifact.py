character_energy = round(float(input()), 2)

terrain = input()
artifact_found = False
mountains = 0
piece_artifact = 0

while terrain != 'Journey ends here!' and character_energy > 0 and not artifact_found:
    if terrain == 'mountain':
        character_energy -= 10
        mountains += 1
        if mountains % 3 == 0:
            piece_artifact += 1
    elif terrain == 'desert':
        character_energy -= 15
    elif terrain == 'forest':
        character_energy += 7
    if piece_artifact == 3:
        artifact_found = True
    terrain = input()

if artifact_found:
    print(f'The character reached the legendary artifact with {character_energy:.2f} energy left.')
elif character_energy <= 0:
    print('The character is too exhausted to carry on with the journey.')
else:
    print(f'The character could not find all the pieces and needs {3 - piece_artifact} more to complete the legendary artifact.')
