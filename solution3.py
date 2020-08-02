# https://leetcode.com/problems/game-of-life

# // Time Complexity : o(n*m)
# // Space Complexity : o(1)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this : None
#
#
# // Your code here along with comments explaining your approach
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                neighbor, original = divmod(board[i][j], 10)
                # print(neighbor,original)
                # count the neighbors
                # right
                if j + 1 < m:
                    if board[i][j + 1] % 10 == 1:
                        neighbor += 1
                # down
                if i + 1 < n:
                    if board[i + 1][j] % 10 == 1:
                        neighbor += 1

                    # <- diag
                    if j - 1 >= 0:
                        if board[i + 1][j - 1] % 10 == 1:
                            neighbor += 1
                    # -> diag
                    if j + 1 < m:
                        if board[i + 1][j + 1] % 10 == 1:
                            neighbor += 1
                # print("New Neighbor",neighbor)
                # update the neighbors
                if original == 1:
                    # right
                    if j + 1 < m:
                        board[i][j + 1] += 10
                        # print("update right")

                    # down
                    if i + 1 < n:
                        board[i + 1][j] += 10
                        # print("update down")

                        # <- diag
                        if j - 1 >= 0:
                            board[i + 1][j - 1] += 10
                            # print("update down <-")
                        # -> diag
                        if j + 1 < m:
                            board[i + 1][j + 1] += 10
                            # print("update down ->")

                if neighbor < 2:
                    board[i][j] = 0
                elif neighbor == 2:
                    board[i][j] = board[i][j] % 10
                elif neighbor == 3:
                    board[i][j] = 1
                elif neighbor > 3:
                    board[i][j] = 0
                # print(board)