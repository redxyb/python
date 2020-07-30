def Game(object):
    top_score = 0

    def __init__(self,player_game):
        self.player_game = player_game

    def start_game(self):
        print("%s 开始了游戏" % self.player_game)

    @classmethod
    def show_top_score(cls):
        print("当前游戏最高分：%d" % cls.top_score)

    @staticmethod
    def show_help():
        print("这是帮助信息")

game = Game("小明")
game.start_game()
Game.show_help()
Game.show_top_score()