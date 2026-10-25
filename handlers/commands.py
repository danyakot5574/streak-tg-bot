from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from keyboards.inline import main_menu_keyboard, back_keyboard, friends_menu_keyboard, back_to_friends_keyboard, profile_menu_keyboard

router = Router()

# ========================================
# ========================================
# ====== ОБРАБОТКА ТЕКСТОВЫХ КОМАНД ======
# ========================================
# ========================================

# ================
# == СТАРТ БОТА ==
# ================

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Главное меню:", reply_markup=main_menu_keyboard())
    
    #await message.answer(
    #    f"Привет, {message.from_user.first_name}!\n"
    #    "Это бот для накопления огонька/стрика с друзьями. \n Используй /help для списка команд.\n\n"
    #    "WORK IN PROGRESS.."
    #)

# =================
# == МЕНЮ ПОМОЩИ ==
# =================

@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "Доступные команды:\n"
        "/start - приветствие\n"
        "/help - список команд\n"
        "/menu - главное меню\n"
        "/point - подначить\n"
        "/friends - информация о друзьях\n"
    )
    await message.answer(help_text)

# ==================
# == ГЛАВНОЕ МЕНЮ ==
# ==================

@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer("Главное меню:", reply_markup=main_menu_keyboard())

# =========================================
# =========================================
# ====== ОБРАБОТКА КНОПОК КЛАВИАТУРЫ ======
# =========================================
# =========================================

# ====================================
# == ОБРАБОТКА КНОПОК ГЛАВНОГО МЕНЮ ==
# ====================================

@router.callback_query(lambda c: c.data.startswith("menu:"))
async def process_menu_callback(callback: CallbackQuery):
    action = callback.data.split(":")[1]

    if action == "main":
        await callback.message.edit_text(
            "Главное меню:", reply_markup=main_menu_keyboard()
        )
    elif action == "about":
        await callback.message.edit_text(
            "Это бот для накопления огонька/стрика с друзьями. \nAuthors: ОАО \"КЮФТА\"\n\nWORK IN PROGRESS",
            reply_markup=back_keyboard()
        )

    await callback.answer()

# ==================================
# == ОБРАБОТКА КНОПОК МЕНЮ ДРУЗЕЙ ==
# ==================================

@router.callback_query(lambda c: c.data.startswith("friends:"))
async def process_menu_callback(callback: CallbackQuery):
    action = callback.data.split(":")[1]

    if action == "main":
        await callback.message.edit_text(
            "Информация о друзьях:", reply_markup=friends_menu_keyboard()
        )
    elif action == "add_friend":
        await callback.message.edit_text(
            "Добавить друга (WorkInProgress):", reply_markup=back_to_friends_keyboard()
        )


    await callback.answer()

# ==============================
# == ОБРАБОТКА КНОПОК ПРОФИЛЯ ==
# ==============================

@router.callback_query(lambda c: c.data.startswith("profile:"))
async def process_menu_callback(callback: CallbackQuery):
    action = callback.data.split(":")[1]

    if action == "main":
        await callback.message.edit_text(
            "Ваш профиль:", reply_markup=profile_menu_keyboard(callback.from_user)
        )
    elif action == "none":
        print("INFO:kyuftabot.event:None")

    await callback.answer()


