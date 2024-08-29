from color import Color

class Theme:

    def __init__(self, light_bg, dark_bg,
                       light_trace, dark_trace,
                       light_moves, dark_moves):
        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)

        """
        light_bg = light colored square of game board
        dark_bg = dark colored square of game board
        light_trace = light colored square of last move
        dark_trace = dark colored square of last move
        light_moves = light colored square of valid moves of piece
        dark_moves = dark colored square of valid moves of piece
        """