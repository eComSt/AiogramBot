from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import make_row_keyboard

from asyncio import sleep

router = Router()

# Эти значения далее будут подставляться в итоговый текст, отсюда
# такая на первый взгляд странная форма прилагательных

N1 = 1000
N2 = 2000

class Order(StatesGroup):
    choosing_id = State()
    choosing_foto = State()
    done = State()


@router.message(Command("id"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Введите ID:")
    await state.set_state(Order.choosing_id)

@router.message(Order.choosing_id)
async def id_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_id=message.text.lower())
    await message.answer(
        text=f"Спасибо. Подождите {N1//1000} секунд",
    )
    await sleep(N1/1000)
    await message.answer(
        text=f"Пришлите фото билета",
    )
    await state.set_state(Order.choosing_foto)

@router.message(Order.choosing_foto, F.photo)
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы прислали фото билета для {user_data['chosen_id']}.\n"
             f"Спасибо! Подождите {N2//1000} секунд пока менеджер все проверит",
        reply_markup=ReplyKeyboardRemove()
    )

    await sleep(N2/1000)
    await message.answer(
        text=f"Все ок!\nПришлите адрес и ФИО",
    )
    await state.set_state(Order.done)

@router.message(Order.done)
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Через 1-2 часа к вам приедет курьер",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.update_data(chosen_address=message.text.lower())
    user_data = await state.get_data()
    print(user_data)
    await state.clear()



