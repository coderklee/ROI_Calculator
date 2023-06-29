class CalculateROI():

	def __init__(self):
		self.income = 0
		self.expenses = 0
		self.investement = 0
		self.ROI = 0

	def incomeInput(self):
		laundry = input("How much money did you make from laundry? ")
		rental = input("How much money did you make from your rental properties? ")
		storage = input("How much money did you make from storage? ")
		misc = input("How much money did you make from misc items? ")
		self.income = int(laundry) + int(rental) + int(storage) + int(misc)   

	def expenseInput(self):
		taxes = input("How much did you spend on taxes? ")
		insurance = input("How much did you spend on insurance? ")
		electric = input("How much did you spend on electric? ")
		water = input("How much did you spend on water? ")
		sewer = input("How much did you spend on sewer? ")
		trash = input("How much did you spend on trash? ")
		gas = input("How much did you spend on gas? ")
		HOA = input("How much did you spend on HOA? ")
		landscape = input("How much did you spend on landscape? ")
		vacancy = input("How much did you spend on vacancy? ")
		repairs = input("How much did you spend on repairs? ")
		CapEx = input("How much did you spend on CapEx? ")
		mortgage = input("How much did you spend on mortgage? ")
		prop_mgmt = input("How much did you spend on property management? ")
		self.expenses =  int(taxes) + int(insurance) + int(electric) + int(water) + int(sewer) + int(trash) + int(gas) + int(HOA) + int(landscape) + int(vacancy) + int(repairs) + int(CapEx) + int(mortgage) + int(prop_mgmt)


	def investmentInput(self):
		down = input("How much did you spend on your down payment? ")
		closing = input("How much did you spend on closing costs? ")
		rehab = input("How much is your rehab budget? ")
		misc = input("How much did you spend on misc investment items? ")
		self.investement = int(down) + int(closing) + int(rehab) + int(misc)
		
	def cashFlowInput(self):
		monthlyCashFlow = self.income - self.expenses
		annualCashFlow = monthlyCashFlow * 12
		print(f"Your monthly cash flow is {monthlyCashFlow}.")
		print(f"Your annual cash flow is {annualCashFlow}.")
		
	def finalROI(self):
		monthlyCashFlow = self.income - self.expenses
		annualCashFlow = monthlyCashFlow * 12
		ROI = annualCashFlow / self.investement
		self.ROI += float(ROI*100)
		print(f"Your ROI is {self.ROI}%")


myROI = CalculateROI()

def UserInput():
	while True:
		response = input("What would you like to input? Income/Expense/Investment/Show/Quit ")
		if response.lower() == "income":
			myROI.incomeInput()
		elif response.lower() == 'expense':
			myROI.expenseInput()
		elif response == 'investment':
			myROI.investmentInput()            
		elif response.lower() == "show":
			print('You are all done!')
			myROI.cashFlowInput()
			myROI.finalROI()
		elif response.lower() == 'quit':
			print("Thank you, come again!")
			break
		else:
			print("Invalid input, please try again.")


UserInput()          