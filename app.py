import os
from flask import Flask, render_template, request, jsonify
from gridworld import GridWorldModel

# Configure absolute paths for Vercel deployment compatibility
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    try:
        n = int(data.get('size', 5))
        start = data.get('start')
        end = data.get('end')
        obstacles = data.get('obstacles', [])
        
        # Initialize model with user configuration
        model = GridWorldModel(size=n, start=start, end=end, obstacles=obstacles)
        
        # Run Value Iteration to find optimal V(s) and Policy
        model.value_iteration()
        
        # Extract grid data corresponding to V(s) and policy
        grid_data = model.get_grid_data()
        
        return jsonify({'status': 'success', 'grid_data': grid_data})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    # Use reloader=False to avoid issues when running programmatically
    app.run(debug=True, use_reloader=False, port=5000)
