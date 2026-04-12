def alphabeta(depth, node_index, isMax, values, alpha, beta):

    if depth == 3:
        return values[node_index]

    if isMax:
        best = -1000

        for i in range(2):
            val = alphabeta(depth+1, node_index*2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break   # PRUNING

        return best

    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth+1, node_index*2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break   # PRUNING

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(0, 0, True, values, -1000, 1000)
print("Optimal value:", result)
