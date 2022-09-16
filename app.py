from flask import Flask, flash, redirect, render_template, request
from loguru import logger

from config import Config
from project.forms import IndexForm, GameForm, FinishForm
from escape_from_dungeons import Dungeon, Character


''' Настройки файла логов '''
logger.add(
    "log/esc_dun_debug.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="1 day",
    compression="zip"
)

app = Flask(__name__)
app.config.from_object(Config)

my_dungeon = Dungeon()
my_player = Character()


@logger.catch
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get("player_name"):
            my_player.name = request.form['player_name']
    form = IndexForm()
    return render_template('index.html', form=form)


@logger.catch
@app.route('/game/<int:room>', methods=['GET', 'POST'])
def game(room: int):
    form = GameForm()
    if request.method != 'POST':
        flash(f'{my_dungeon.rooms_text[room]}')
    if request.method == 'POST':
        if request.form.get("step"):
            next_room = my_dungeon.open_doors[room][int(request.form.get("step"))]
            if next_room == 0:
                flash('Прохода нет')
            elif next_room >= 1:
                if room == 11:
                    my_dungeon.open_doors[1][0] = 99
                    flash(f'Теперь вы знаете код от двери')
                if my_dungeon.open_doors[room][0] == 99:
                    return redirect('/finish')
                room = next_room
                return redirect(f'/game/{room}')
    return render_template(
        'game.html',
        form=form, name_room=my_dungeon.rooms[room],
        teg=f'game-content-{room}',
        name=my_player.name
    )


@logger.catch
@app.route('/game/')
def extra():
    return render_template('extra.html')


@logger.catch
@app.route('/finish', methods=['GET', 'POST'])
def finish():
    if request.method == 'POST':
        if request.form.get("new_game"):
            return redirect('/')
    flash("Поздравляю, вы прошли игру. Ваш персонаж выбрался на поверхность!")
    form = FinishForm()
    return render_template('finish.html', form=form)


if __name__ == '__main__':
    app.run()
