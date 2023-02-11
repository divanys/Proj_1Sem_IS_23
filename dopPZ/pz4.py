# import pgzrun
#
# TITLE = "Arkanoid clone"
# WIDTH = 800
# HEIGHT = 500
#
# paddle = Actor("paddleblue.png")
# paddle.x = 120
# paddle.y = 420
#
# ball = Actor("ballblue.png")
# ball.x = 30
# ball.y = 300
#
# paddle.x = 120
# paddle.y = 420
#
#
# def draw():
#     screen.blit("background.png", (0,0))
#     paddle.draw()
#     ball.draw()
#

# print(sum([int(input('00 ')), int(input('01 '))]) if input('Действие+: ') == '+' else int(input('10 ')) - int(input('11 ')) if input('Действие-: ') == '-' else int(input('20 ')) * int(input('21 ')) if input('Действе*: ') == '*' else int(input('30 ')) / int(input('31 ')) if input('Действие/: ') == '/' else 'Ошибка!!')

print(sum([int(input('00 ')), int(input('01 '))]) if input('Действие+: ') == '+' else int(input('10 ')) - int(input('11 ')) if input('Действие-: ') == '-' else int(input('20 ')) * int(input('21 ')) if input('Действе*: ') == '*' else int(input('30 ')) / int(input('31 ')) if input('Действие/: ') == '/' else 'Ошибка!!')


