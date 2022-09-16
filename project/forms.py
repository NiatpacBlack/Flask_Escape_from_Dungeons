from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class IndexForm(FlaskForm):
    player_name = StringField("Имя персонажа", default='Алексей', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField("Сменить имя")
    new_game = SubmitField("Начать игру")


class GameForm(FlaskForm):
    step = SelectField(
        'Выберите в какую сторону идти',
        coerce=int,
        choices=[
            (0, "Север"),
            (1, "Юг"),
            (2, "Восток"),
            (3, "Запад"),
        ],
        render_kw={
            'class': 'game-form'
        }
    )
    submit = SubmitField("Двигаться")


class FinishForm(FlaskForm):
    new_game = SubmitField("Начать заново")
