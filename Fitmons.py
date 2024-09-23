"""
Name: Amanda Teh 
Project: Fitmons 
"""

# ==========
# Q1

def fusing(fitmon_1, fitmon_2):
    """
    This is to fuse 2 fitmons together and get the cuteness_score 

    fitmon_1: A list representing the first fitmon with  [affinity_left, cuteness, affinity_right].
    fitmon_2: A list representing the second fitmon with  [affinity_left, cuteness, affinity_right].

    Return: The fused fitmon as a list [affinity_left, cuteness_score, affinity_right]

    Time Complexity:The function has a constant time complexity as it performs a fixed number of operations regardless of input size
    Space Complexity: constant space complexity as it only creates a few variables regardless of input size.
    """
    cuteness_score = int(fitmon_1[1] * fitmon_1[2] + fitmon_2[1] * fitmon_2[0])
    return [fitmon_1[0], cuteness_score, fitmon_2[2]]
  

def fuse(fitmons):
    """
    This is for fusing all the fitmons in the list into a one last fitmon with the highest cuteness_score possible 

    Return:
        cuteness_score: the highest possible fitmon obtained by fusing all fitmons.

    Time complexity: 
        Best case analysis:O(N^3) time due to the nested loops iterating over the fitmons.
        Worst case analysis:O(N^3) time due to the nested loops iterating over the fitmons and performing operations within each iteration.
    Space complexity: 
        Input space analysis: O(n^2) as the max_cuteness matrix is created to store the maximum cuteness score after fusing fitmons.
        Aux space analysis::O(1) as the function uses a constant amount of extra space regardless of input size.
    """
    n = len(fitmons)
    # Initialize a matrix to store the maximum cuteness score after fusing fitmons
    max_cuteness = [[None] * n for _ in range(n)]

    # Initialize the diagonal with the original fitmons
    for i in range(n):
        max_cuteness[i][i] = fitmons[i]

    # Fuse fitmons iteratively
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            max_cuteness[i][j] = [0, 0, 0]  # Initialize the fused fitmon
            for k in range(i, j):
                # Fuse fitmons[i] with fitmons[j]
                fused_fitmon = fusing(max_cuteness[i][k], max_cuteness[k + 1][j])
                # Update the maximum cuteness score if the fused fitmon has higher cuteness
                if max_cuteness[i][j][1] < fused_fitmon[1]:
                    max_cuteness[i][j] = fused_fitmon

    # Return the cuteness_score of the highest possible fitmon obtained
    return max_cuteness[0][-1][1]

