***Recycling Tracker Class Design Recipe*** 

1. Describe the Problem

# Users want to track their recycling activities to promote environmental sustainability. The application should allow users to add recycling entries, view summaries of their recycling activities, and optionally calculate how much they have recycled over a month or a year.

2. Design the Class Interface

# Include the initialiser, public properties, and public methods with all parameters, return values, and side-effects.


class RecyclingTracker:
    # User-facing properties:
    # entries: list of recycling entries

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Initializes an empty list of entries
        self.entries = []

    def add_recycling_entry(self, date, material, amount):
        # Parameters:
        #   date: string representing the date of recycling (format: YYYY-MM-DD)
        #   material: string representing the type of material recycled (e.g., paper, plastic)
        #   amount: float representing the amount of material recycled in kilograms
        # Returns:
        #   None
        # Side-effects:
        #   Adds a new recycling entry to the entries list
        pass # No code here yet

    def get_recycling_summary(self):
        # Returns:
        #   A summary of the total amount recycled by material type
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
