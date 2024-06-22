def gen_vector(index, vector):
    if index >= len(vector):
        print(''.join([str(x) for x in vector]))
        return
    for number in range(0, 2):
        vector[index] = number
        gen_vector(index+1, vector)


gen_vector(0, [0, 0, 0])
