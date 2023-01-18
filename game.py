"""
Consider a row of N coins of values V1 . . . Vn, where N is even. 
We play a game against an opponent by alternating turns. 
In each turn, a player selects either the first or last coin from the row, 
removes it from the row permanently, and receives the value of the coin. 
Determine the maximum possible amount of money we can definitely win if we 
move first.
"""

def coin_game(coins: list) -> int:
    # Recursively find maximum value first player can win
    def dfs(l, r):
        # Base case
        if l >= r:
            return 0
        
        # Determine if player's choice ... [10, 20, 10] != player's choice
        if (r - l) % 2 != 0:
            players_choice = True
        else:
            players_choice = False
        
        # Examine all possible moves for player
        if players_choice:
            left_coin = coins[l]
            right_coin = coins[r]
            return max(dfs(l + 1, r) + left_coin,
                    dfs(l, r - 1) + right_coin)
        # Second player takes greedy approach
        else:
            if coins[l] >= coins[r]:
                l += 1
            else:
                r -= 1
    
            return max(dfs(l, r), dfs(l, r))

    return dfs(0, len(coins) - 1)


def coin_game_dp(coins: list) -> int:
    # key = tuple (l, r), value = maximum player value from that position
    dp = {}

    # Recursively find maximum value first player can win
    def dfs(l, r):
        # Base case
        if l > r:
            return 0
        # Solution for this l and r has been found
        if (l, r) in dp:
            return dp[(l, r)]

        # Determine if player's choice ... [10, 20, 10] != player's choice
        if (r - l) % 2 != 0:
            players_choice = True
        else:
            players_choice = False

        # Examine all possible moves for player
        if players_choice:
            left_coin = coins[l]
            right_coin = coins[r]

            dp[(l, r)] = max(dfs(l + 1, r) + left_coin,
                            dfs(l, r - 1) + right_coin)
        
        # Second player takes greedy approach
        else:
            if coins[l] >= coins[r]:
                l += 1
            else:
                r -= 1

            dp[(l, r)] = max(dfs(l , r), dfs(l, r))

        return dp[(l, r)]

    return dfs(0, len(coins) - 1)
