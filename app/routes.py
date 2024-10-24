from app import app
from flask import request, jsonify
from recycle_tracker import RecyclingTracker

# Instantiate the RecyclingTracker class
tracker = RecyclingTracker()

@app.route('/')
def home():
    return "Welcome to the Recycle Tracker!"

@app.route('/add-entry', methods=['POST'])
def add_recycling_entry():
    data = request.get_json()
    date = data.get('date')
    material = data.get('material')
    amount = data.get('amount')

    try:
        tracker.add_recycling_entry(date, material, amount)
        return jsonify({'message': 'Added entry successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/summary', methods=['GET'])
def get_recycling_summary():
    summary = tracker.get_recycling_summary()
    return jsonify(summary), 200

@app.route('/entries/<string:date>', methods=['GET'])
def get_recycling_by_date(date):
    entries = tracker.materials_recycled_on_date(date)
    if not entries:
        return jsonify({'message': 'Invalid, there are no enries for this date'}), 404
    return jsonify(entries), 200

@app.route('/monthly-recycling', methods=['GET'])
def get_monthly_recycling():
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))
    total = tracker.calculate_monthly_recycling(year, month)
    return jsonify({'total_recycled': total}), 200

@app.route('/yearly-recycling/<int:year>', methods=['GET'])
def get_yearly_recycling(year):
    total = tracker.calculate_yearly_recycling(year)
    return jsonify({'total_recycled': total}), 200
