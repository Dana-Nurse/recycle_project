import datetime

class RecyclingTracker:
    def __init__(self):
        # Initialises an empty list to store recycling entries
        self.entries = []

    def add_recycling_entry(self, date, material, amount):
        # Validate the date format
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

        # Validate that the material is a non-empty string
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Material must be a non-empty string")

        # Validate that the amount is a positive float
        if not isinstance(amount, (float, int)) or amount <= 0:
            raise ValueError("Amount must be a positive number")

        # Create a new dictionary representing the recycling entry
        new_entry = {
            'date': date,
            'material': material,
            'amount': amount
        }

        # Append the new entry to the entries list
        self.entries.append(new_entry)


    def get_recycling_summary(self):
        # Returns:
        #   A summary of the total amount recycled material
        # Side-effects:
        #   Computes and returns a summary of all recycling entries
        pass # No code here yet

    def materials_recycled_on_date(self, date):
        # Parameters:
        #   date: string representing the date to filter entries (format: YYYY-MM-DD)
        # Returns:
        #   A list of recycling entries for the specified date
        # Side-effects:
        #   Filters and returns entries for the given date
        pass # No code here yet

    def calculate_monthly_recycling(self, year, month):
        # Parameters:
        #   year: integer representing the year
        #   month: integer representing the month
        # Returns:
        #   The total amount recycled in the specified month and year
        # Side-effects:
        #   Computes and returns the total recycled amount for the given month and year
        pass # No code here yet

    def calculate_yearly_recycling(self, year):
        # Parameters:
        #   year: integer representing the year
        # Returns:
        #   The total amount recycled in the specified year
        # Side-effects:
        #   Computes and returns the total recycled amount for the given year
        pass # No code here yet