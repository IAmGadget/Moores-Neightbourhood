
def debug(code):
    print(f"""
{'#'*15} DEBUGGING {'#'*15}
    {code}
{'#' * (32 + len("DEBUGGING")) }
    """)


class Sprite(object):
    def __init__(self):
        self.pos = {"x": 3, "y": 2}
        self.sprite = "🤖"
        self.name = "Sprite_1"
        self.ai = False

    def __repr__(self):
        return f"{self.name} -> {self.sprite}"



class Terrain(object):
    def __init__(self, user: object, y_max=10, x_max=10):
        self.user = user
        self.x_max = x_max
        self.y_max = y_max
        self.terrain_icon = "⬛"
        self.grid = [] # Rows with collums
        self._createGrid()

    def _createGrid(self):
        _rowX = []
        _rowY = []
        for i in range(self.y_max):
            _rowX.append(self.terrain_icon)
        for x in range(len(_rowX)):
            _rowY.append(_rowX)
        self.grid.append(_rowY)

    def displayGrid(self):
        _gridDisplay = ""
        for yidx, Yrow in enumerate(self.grid[0]):
            for xidx, Xrow in enumerate(Yrow):
                if yidx == self.user.pos['y'] and xidx == self.user.pos['x']:
                    _gridDisplay += self.user.sprite + "  "
                    continue
                _gridDisplay += Xrow + "  " # Added spacer for easier viewing
            _gridDisplay += "\n" # Break into next row

        return _gridDisplay # Return the string for further display use

class Controller():
    def __init__(self, user, terrain):
        self.user = user
        self.terrain = terrain
        self.availableSpaces = "💢"
        self.newGrid = self.terrain.displayGrid()
        self.showNextMoves()

    def _checkObstacles(self, x:int, y:int): # Check if there are any obstacles incoming on the move
        _obstacle = False
        _grid = self.newGrid.splitlines()
        currRow = _grid[self.user.pos['y']]
        abvRow = _grid[self.user.pos['y'] - 1]
        blwRow = _grid[self.user.pos['y'] + 1]
        if x:
            print(x)

        return _obstacle
    def _moveSprite(self, x:int=0, y:int=0):  # Both arguments have a default of 0 so if only one co-ordinate is given, adding a None value will effect it.
        if self._checkObstacles(x, y):
            self.user.pos['y'] += y
            self.user.pos['x'] += x

    def showNextMoves(self):
        noSpaces = self.newGrid.splitlines()
        # Current row
        currRow = noSpaces[self.user.pos['y']].split("  ")
        before = currRow[self.user.pos['x'] - 1]
        after = currRow[self.user.pos['x'] + 1]
        # Set the new icon
        before = after = self.availableSpaces
        # Setting the new icons to the new grid variable
        currRow[self.user.pos['x'] - 1] = before
        currRow[self.user.pos['x'] + 1] = after

        # Above current row
        if self.user.pos['y'] - 1 >= 0: #    If the above row is below 0 then do not display
            abvRow = noSpaces[self.user.pos['y'] -1]
            abvRow = abvRow.split("  ")
            abvRow = list(abvRow)
            abvRow[self.user.pos['x']] = self.availableSpaces
            abvRow[self.user.pos['x']-1] = self.availableSpaces
            abvRow[self.user.pos['x']+1] = self.availableSpaces
            noSpaces[self.user.pos['y'] - 1] = "  ".join(abvRow)

        # Below current row
        if self.user.pos['y'] + 1 <= self.terrain.y_max: #  If the row below the current row is outside the box then do not display
            blwRow = noSpaces[self.user.pos['y'] + 1]
            blwRow = blwRow.split("  ")
            blwRow = list(blwRow)

            blwRow[self.user.pos['x']] = self.availableSpaces
            blwRow[self.user.pos['x']-1] = self.availableSpaces
            blwRow[self.user.pos['x']+1] = self.availableSpaces
            noSpaces[self.user.pos['y'] + 1] = "  ".join(blwRow)


        # Join all the edited roles back to the original
        noSpaces[self.user.pos['y']] = "  ".join(currRow)
        newMovesGrid = ""
        for row in noSpaces: # Convert the grid back to original with edited data
            print(row)
            newMovesGrid.join(row)
        self.newGrid = newMovesGrid

    def run(self):
        print(self.newGrid)

user = Sprite() # Sprite is only decorative for the script. It has no main functions. All movements are handled in Terrain

grid = Terrain(user) # Terrain takes the user argument to handle the movements etc

Controller(user, grid).run()
