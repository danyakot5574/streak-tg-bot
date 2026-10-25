from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import User

# ==================
# == ГЛАВНОЕ МЕНЮ ==
# ==================

# == ГЛАВНОЕ МЕНЮ ==

def main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Профиль", callback_data="profile:main")
    builder.button(text="Друзья", callback_data="friends:main")
    builder.button(text="О боте", callback_data="menu:about")
    builder.adjust(2)  # по 2 кнопки в ряду
    return builder.as_markup()

# == ВЕРНУТЬСЯ К ГЛАВНОМУ МЕНЮ ==

def back_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data="menu:main")
    return builder.as_markup()

# =================
# == МЕНЮ ДРУЗЕЙ ==
# =================

# == ГЛАВНОЕ МЕНЮ ДРУЗЕЙ ==

def friends_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить друга", callback_data="friends:add_friend")
    builder.button(text="Назад", callback_data="menu:main")
    return builder.as_markup()

# == ВЕРНУТЬСЯ К ГЛАВНОМУ МЕНЮ ДРУЗЕЙ ==

def back_to_friends_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data="friends:main")
    return builder.as_markup()

# ==================
# == МЕНЮ ПРОФИЛЯ ==
# ==================

# == ГЛАВНОЕ МЕНЮ ПРОФИЛЯ ==

def profile_menu_keyboard(user: User) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=f"ID: {user.id}", callback_data="profile:none")
    builder.button(text=f"Имя: {user.full_name}", callback_data="profile:none")
    builder.button(text=f"Username: @{user.username or 'не указан'}", callback_data="profile:none")
    builder.button(text="Назад", callback_data="menu:main")

    builder.adjust(1)

    return builder.as_markup()