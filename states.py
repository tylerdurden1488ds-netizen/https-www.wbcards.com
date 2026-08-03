from aiogram.fsm.state import State, StatesGroup


class CreateCard(StatesGroup):
    waiting_photo = State()
    waiting_description = State()
    waiting_background = State()
    waiting_style = State()
    waiting_text = State()
    waiting_price = State()
    waiting_old_price = State()
    waiting_discount = State()
    waiting_logo = State()
    waiting_finish = State()


class EditCard(StatesGroup):
    waiting_edit = State()
