from aocd import data, submit
# data = '''30373
# 25512
# 65332
# 33549
# 35390'''


if __name__ == '__main__':
    trees = data.split('\n')
    # counter = 0
    scores = []

    # assuming square... it is actually
    dim = len(trees)

    for i in range(dim):
        for j in range(dim):
            # on the border
            if i in (0, dim - 1) or j in (0, dim - 1):
                # counter += 1
                continue
            
            score_a = 0
            for x in range(i-1, -1, -1):
                score_a += 1
                if trees[x][j] >= trees[i][j]:
                    break
                    
            score_b = 0
            for x in range(i + 1, dim):
                score_b += 1
                if trees[x][j] >= trees[i][j]:
                    break

            score_c = 0
            for y in range(j - 1, -1, -1):
                score_c += 1
                if trees[i][y] >= trees[i][j]:
                    break
        
            score_d = 0
            for y in range(j + 1, dim):
                score_d += 1
                if trees[i][y] >= trees[i][j]:
                    break

            scores.append(score_a*score_b*score_c*score_d)

    print(max(scores))
    submit(max(scores))