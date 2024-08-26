from app.recycle_tracker import RecyclingTracker

"""
Given a specific date and a list of materials, 
# add_recycling_entry adds the entry to the recycling log.
"""
tracker = RecyclingTracker()
tracker.add_recycling_entry("2024-03-11", "Wood", 5.0)
assert len(tracker.entries) == 1
assert tracker.entries[0] == {"date": "2024-03-11", "material": "Wood", "amount": 5.0}
