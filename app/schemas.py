from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, StringConstraints, condecimal

#amount: 0 < amount <= 10000, 2 decimals, positive - reject the rest
Money = condecimal(gt=0, le=10000, max_digits=10, decimal_places=2)

#payer: ^[a-z0-9_.-]{3,32}$
MemberName = Annotated[str, StringConstraints(pattern=r"^[a-z0-9_.-]{3,32}$")]

#currency: in {"EUR","USD","GBP"} - exactly
Currency = Literal["EUR", "USD", "GBP"]


class ExpenseIn(BaseModel):
    amount: Money
    payer: MemberName
    payer_email: Annotated[str, StringConstraints(max_length=254, pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")]
    description: Annotated[str, StringConstraints(max_length=200, pattern=r"^[^\x00-\x1f\x7f\u200b-\u200f\u202a-\u202e]*$")] = ""
    currency: Currency = "EUR"