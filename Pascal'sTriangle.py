class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalstri = [[1]*i for i in range(1, numRows+1)]
        i = 1
        while i < numRows:
            for j in range(1, len(pascalstri[i-1])):
                pascalstri[i][j] = pascalstri[i-1][j] + pascalstri[i-1][j-1]
            i += 1
            
        return pascalstri