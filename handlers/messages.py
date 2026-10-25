from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.user_states import RegistrationState

router = Router()

# ===========================
# ====== КОМАНДЫ С FSM ======
# ===========================

# ===============
# == ПОДНАЧИТЬ ==
# ===============

# == СТАРТОВАЯ КОМАНДА ==

@router.message(Command("point"))
async def cmd_register(message: Message, state: FSMContext):
    await state.set_state(RegistrationState.waiting_for_name)
    await message.answer("Введите тэг друга:")

# == ЗАПРОС ДАННЫХ ==

@router.message(RegistrationState.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    data = await state.get_data()
    
    await message.answer(data['name'])
    await state.clear()

# == ОБРАБОТКА НЕКОРРЕКТНОЙ КОМАНДЫ ==

@router.message(F.text)
async def handle_text(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(
            "Не понимаю эту команду. Используй /help для списка команд."
        )
