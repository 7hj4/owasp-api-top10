from flask import Flask, jsonify
from flask import Blueprint

app6 = Blueprint('app6', __name__)


@app6.route('/')
def home():
    return 'Hello your In LAB API6:2023 Unrestricted Access to Sensitive Business Flows'

# Simulated sensitive business flow data
business_data = {
    'report1': {'name': 'Financial Report 2023', 'content': 'This is a confidential financial report.'},
    'report2': {'name': 'HR Data', 'content': 'This is sensitive HR data.'},
}

@app6.route('/get_report/<report_id>', methods=['GET'])
def get_report(report_id):
    report = business_data.get(report_id)
    if report:
        return jsonify(report)
    else:
        return jsonify({'message': 'Report not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
