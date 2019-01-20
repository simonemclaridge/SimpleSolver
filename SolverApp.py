# ################################################################
# File name: SolverApp.py                                        #
# Author: Simone Claridge                                        #
# Date created: 12/20/2018                                       #
# Python Version: 3.7.2                                          #
# Test Tkinter GUI for solving numeric and relational operations #
##################################################################
from tkinter import *
from tkinter import ttk


class SolverApp:

	def __init__(self, master):
		master.resizable(False, False)
		master.geometry("527x124+748+154")
		master.title("Simple Solver")
		master.iconbitmap(r'C:\Users\Simone\PycharmProjects\Hello_Tkinter\sample\images\math_icon.ico')

		self.first_number_lbl = ttk.Label(master)

		self.first_number_lbl.place(relx=0.095, rely=0.081, height=39, width=96)

		self.first_number_lbl.configure(font="TkDefaultFont")
		self.first_number_lbl.configure(relief='flat')
		self.first_number_lbl.configure(text='''Enter number''')
		self.first_number_lbl.configure(width=96)

		self.first_number_entry = ttk.Entry(master)
		self.first_number_entry.place(relx=0.076, rely=0.323, relheight=0.169
									  , relwidth=0.201)
		self.first_number_entry.configure(width=106)
		self.first_number_entry.configure(takefocus="")
		self.first_number_entry.configure(cursor="ibeam")

		self.operator_lbl = ttk.Label(master)
		self.operator_lbl.place(relx=0.323, rely=0.161, height=19, width=66)

		self.operator_lbl.configure(font="TkDefaultFont")
		self.operator_lbl.configure(relief='flat')
		self.operator_lbl.configure(text='''Operator''')
		self.operator_lbl.configure(width=96)

		self.operator_combo = ttk.Combobox(master)
		self.operator_combo.place(relx=0.304, rely=0.323, relheight=0.169
								  , relwidth=0.157)

		self.operator_combo.configure(width=83)
		self.operator_combo.configure(takefocus="")

		self.second_number_entry = ttk.Entry(master)
		self.second_number_entry.place(relx=0.493, rely=0.323, relheight=0.169
									   , relwidth=0.201)
		self.second_number_entry.configure(takefocus="")
		self.second_number_entry.configure(cursor="ibeam")

		self.second_number_lbl = ttk.Label(master)
		self.second_number_lbl.place(relx=0.512, rely=0.161, height=19, width=76)

		self.second_number_lbl.configure(font="TkDefaultFont")
		self.second_number_lbl.configure(relief='flat')
		self.second_number_lbl.configure(text='''Enter number''')
		self.second_number_lbl.configure(width=96)

		self.result_entry = ttk.Entry(master)
		self.result_entry.place(relx=0.721, rely=0.323, relheight=0.169
								, relwidth=0.201)
		self.result_entry.configure(width=106)
		self.result_entry.configure(takefocus="")
		self.result_entry.configure(cursor="ibeam")

		self.result_lbl = ttk.Label(master)
		self.result_lbl.place(relx=0.778, rely=0.161, height=19, width=96)

		self.result_lbl.configure(font="TkDefaultFont")
		self.result_lbl.configure(relief='flat')
		self.result_lbl.configure(text='''Result''')
		self.result_lbl.configure(width=96)

		self.solve_button = ttk.Button(master)
		self.solve_button.place(relx=0.342, rely=0.565, height=25, width=76)
		self.solve_button.configure(takefocus="")
		self.solve_button.configure(text='''Solve''')

		self.reset_button = ttk.Button(master)
		self.reset_button.place(relx=0.55, rely=0.565, height=25, width=76)
		self.reset_button.configure(takefocus="")
		self.reset_button.configure(text='''Reset''')


def main():
	root = Tk()
	app = SolverApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()
