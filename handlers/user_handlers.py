from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.keyboards import keyboard
import numexpr  # type: ignore

rt = Router()
@rt.message(Command("start"))
async def start(message: Message):
    await message.answer("1+1", reply_markup=keyboard)

@rt.callback_query(F.data == "=")
async def make_result(callback: CallbackQuery):
    equation = callback.message.text
    try:
        result = numexpr.evaluate(equation)
        await callback.message.edit_text(text=str(result), reply_markup=keyboard)
    except ZeroDivisionError:
        await callback.message.edit_text(text="Can't devide by zero", reply_markup=keyboard)
    except Exception:
        await callback.message.edit_text(text="Syntax error", reply_markup=keyboard)

@rt.callback_query(F.data == "C")
async def clear(callback: CallbackQuery):
    if callback.message.text != "0":
        await callback.message.edit_text(text="0", reply_markup=keyboard)
    else:
        await callback.answer()

@rt.callback_query(F.data)
async def change_equation(callback: CallbackQuery):
    if callback.message.text != "0" or callback.data in "/*-+.":
        text_before = callback.message.text
        text_after = text_before + callback.data
        await callback.message.edit_text(text=text_after, reply_markup=keyboard)
    else:
        await callback.message.edit_text(text=callback.data, reply_markup=keyboard)