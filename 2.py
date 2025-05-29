def find_min_subsequence_length(sequence):
    last_pos = {}
    min_length = float('inf')
    for idx, num in enumerate(sequence):
        if 1 <= num <= 26:
            last_pos[num] = idx
            if len(last_pos) == 26:
                current_length = idx - min(last_pos.values()) + 1
                if current_length < min_length:
                    min_length = current_length
    
    return min_length if min_length != float('inf') else "NONE"

with open('data_prog_contest_problem_2.txt', 'r') as file:
    lines = file.readlines()
    n = int(lines[0].split()[0])
    sequence = list(map(int, lines[1].split()))

result = find_min_subsequence_length(sequence)
print(result)