# streak-tg-bot
TikTok-Streak analogue, but for Telegram. 

WORK IN PROGRESS..

# TODO

- [ ] Integrate with DB (PosgreSQL)
- [ ] Implement inter-user interaction (add friends, nudge)
- [ ] Implement streak

# CHANGELOG

## 25.10.26

There are only basic tg-bot features.

### Commands

- `/start` : Opens main menu;
- `/help`: Shows help menu (the main menu is currently not displaying correctly);
- `/point`: Starting multi-step dialog requesting data from user.

### Buttons and menus

#### Main menu:

- Profile (Профиль): Opens profile menu;
- Friends (Друзья): Opens friends menu;
- About (О боте): Shows info about bot and developers.

#### Profile menu:

- Text-buttons with user's data;
- Back (Назад): Opens previous menu.

#### Friends menu:

- Add friend (Добавить друга): Opens non-working menu for adding friends;
- Back (Назад): Opens previous menu.
