import datetime

class RecyclingTracker:
    def __init__(self):
        # Initializes an empty list to store recycling entries
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
        # Returns the total amount of each material recycled
        summary = {}
        for entry in self.entries:
            material = entry['material']
            amount = entry['amount']
            if material in summary:
                summary[material] += amount
            else:
                summary[material] = amount
        return summary

    def materials_recycled_on_date(self, date):
        # Filters and returns entries for the given date
        filtered_entries = [entry for entry in self.entries if entry['date'] == date]
        return filtered_entries

    def calculate_monthly_recycling(self, year, month):
        # Computes and returns the total recycled amount for the given month and year
        total = 0
        for entry in self.entries:
            entry_date = datetime.datetime.strptime(entry['date'], '%Y-%m-%d')
            if entry_date.year == year and entry_date.month == month:
                total += entry['amount']
        return total

    def calculate_yearly_recycling(self, year):
        # Computes and returns the total recycled amount for the given year
        total = 0
        for entry in self.entries:
            entry_date = datetime.datetime.strptime(entry['date'], '%Y-%m-%d')
            if entry_date.year == year:
                total += entry['amount']
        return total
