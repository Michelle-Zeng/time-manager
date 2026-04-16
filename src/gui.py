# inside project/src folder

import tkinter as tk
from tkinter import ttk, messagebox
import time
from config.config import Config
import math


class Gui:
    """
    The window has 5 sections:
        - Header bar
        - Top Left: add task name + difficulty
        - Top Right: task list
        - Time row: total time entry and Generate Schedule button
        - Results (bottom): schedule generated using formula
    """

    def __init__(self):
        """
        Tkinter window and sections
        """
        pass

    def create_window(self):
        """
        Creates Tk window (title, size, background, ttk styles).
        """
        pass

    def create_header(self):
        """
        Header bar with title and labels
        """
        pass

    def create_main(self):
        """
        Creates the two-column layout (left with add assignment, right with task list)
        """
        pass

    def create_left_task(self):
        """
        Left: add assignment name and difficulty entry box --> add task button
        """
        pass

    def create_right_task(self):
        """
        Right: list of added tasks with name and difficulty
        """
        pass

    def create_time_done(self):
        """
        Add total study time entry box --> create schedule button
        """
        pass

    def display_schedule(self):
        """
        Display generated schedule using formulas in exp
        """
        pass

    def add_task_button(self):
        """
        when user clicks add button, read from assignment name and difficulty entry
        """
        pass

    def clear_button(self):
        """
        when user clicks clear button from task list, reset all sections
        """
        pass

    def schedule_button(self):
        """
        when user clicks generate schedule button, read from total time and use exp formulas
        """
        pass

    def update_task_count(self):
        """
        Update the task count label in task list section
        """
        pass
