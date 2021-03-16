class Field:
    def __init__(self, game):
        self.cells = []
        self.game = game
        self.check_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.magic_matrix = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]

    def check_win(self):
        checksums = []
        checksums.append(sum([self.check_matrix[i][i] for i in range(0, 3)]))
        checksums.append(sum([self.check_matrix[i][-i-1] for i in range(3)]))
        for i in range(0, 3):
            checksums.append(sum(self.check_matrix[i]))  # horizontal
            checksums.append(sum(
                [row[i] for row in self.check_matrix]
                ))  # vertical

        print(checksums)
        if 15 in checksums:
            return 'X'
        elif -15 in checksums:
            return '0'
        else:
            return '-'
