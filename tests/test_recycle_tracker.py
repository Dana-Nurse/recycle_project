import pytest
from recycle_tracker import RecyclingTracker

# Test class for RecyclingTracker
class TestRecyclingTracker:
    def setup_method(self):
        self.tracker = RecyclingTracker()

    def test_add_recycling_entry_valid(self):
        self.tracker.add_recycling_entry('2024-10-01', 'plastic', 1.5)
        assert len(self.tracker.entries) == 1
        assert self.tracker.entries[0] == {
            'date': '2024-10-01',
            'material': 'plastic',
            'amount': 1.5
        }

    def test_add_recycling_entry_invalid_date(self):
        with pytest.raises(ValueError, match="Incorrect date format, it should be YYYY-MM-DD"):
            self.tracker.add_recycling_entry('01-10-2024', 'plastic', 1.5)

    def test_add_recycling_entry_empty_material(self):
        with pytest.raises(ValueError, match="Material has to be a non-empty string"):
            self.tracker.add_recycling_entry('2024-10-01', '', 1.5)

    def test_add_recycling_entry_invalid_amount(self):
        with pytest.raises(ValueError, match="Amount cannot be a negative number"):
            self.tracker.add_recycling_entry('2024-10-01', 'plastic', -1.0)

    def test_get_recycling_summary(self):
        self.tracker.add_recycling_entry('2024-10-01', 'plastic', 1.5)
        self.tracker.add_recycling_entry('2024-10-02', 'glass', 2.0)
        summary = self.tracker.get_recycling_summary()
        assert summary == 3.5  

    def test_materials_recycled_on_date(self):
        self.tracker.add_recycling_entry('2024-10-01', 'plastic', 1.5)
        self.tracker.add_recycling_entry('2024-10-01', 'glass', 2.0)
        entries = self.tracker.materials_recycled_on_date('2024-10-01')
        assert len(entries) == 2

    def test_calculate_monthly_recycling(self):
        self.tracker.add_recycling_entry('2024-10-01', 'plastic', 1.5)
        self.tracker.add_recycling_entry('2024-10-15', 'glass', 2.0)
        total = self.tracker.calculate_monthly_recycling(2024, 10)
        assert total == 3.5

    def test_calculate_yearly_recycling(self):
        self.tracker.add_recycling_entry('2024-10-01', 'plastic', 1.5)
        self.tracker.add_recycling_entry('2024-11-15', 'glass', 2.0)
        total = self.tracker.calculate_yearly_recycling(2024)
        assert total == 3.5
