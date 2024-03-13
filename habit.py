import datetime


class Habit:
    def __init__(
        self,
        habit_name,
        category,
        periodicity,
        date_created,
        # last_date_checked=None,  # optional fields
        streak=0,
        # position=0,
        status=1,
    ):  # optional fields
        # self.position = position  # check if position argument exists
        self.habit_name = habit_name  # initialiize task
        self.category = category  # initialize category
        self.periodicity = periodicity  # weekly or daily

        self.date_created = date_created  # check if date_added argument exists, isoformat outputs string
        # self.last_date_checked = (
        #     last_date_checked if last_date_checked is not None else None
        # )  # check if date_completed argument exists
        self.streak = streak if streak != 0 else 0
        self.status = status  # 1 = open, 2 = completed

    # def __repr__(self) -> str:
    #     return f"({self.position}, {self.habit_name}, {self.category}, {self.periodicity}, {self.date_created}, {self.last_date_checked}, {self.streak}, {self.status})"  # print everything in consolea
