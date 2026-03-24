class GridWorldModel:
    def __init__(self, size: int, start=None, end=None, obstacles=None):
        self.size = size
        self.states = [(i, j) for i in range(size) for j in range(size)]
        self.start = tuple(start) if start else None
        self.end = tuple(end) if end else None
        self.terminals = [self.end] if self.end else []
        self.obstacles = [tuple(o) for o in obstacles] if obstacles else []
        self.actions = ['U', 'D', 'L', 'R']
        
        self.values = [[0.0 for _ in range(size)] for _ in range(size)]
        self.policy = {s: [] for s in self.states}

    def get_next_state(self, state, action):
        i, j = state
        if action == 'U':
            next_s = (max(i - 1, 0), j)
        elif action == 'D':
            next_s = (min(i + 1, self.size - 1), j)
        elif action == 'L':
            next_s = (i, max(j - 1, 0))
        elif action == 'R':
            next_s = (i, min(j + 1, self.size - 1))
        else:
            next_s = state
            
        if next_s in self.obstacles:
            return state # Obstacle bounces agent back
        return next_s

    def value_iteration(self, gamma=1.0, theta=1e-4):
        self.values = [[0.0 for _ in range(self.size)] for _ in range(self.size)]
        
        while True:
            delta = 0.0
            new_values = [[0.0 for _ in range(self.size)] for _ in range(self.size)]
            
            for s in self.states:
                if s in self.terminals or s in self.obstacles:
                    continue
                    
                best_value = -float('inf')
                for a in self.actions:
                    next_s = self.get_next_state(s, a)
                    reward = -1.0 # Step reward
                    v = reward + gamma * self.values[next_s[0]][next_s[1]]
                    if v > best_value:
                        best_value = v
                
                new_values[s[0]][s[1]] = best_value
                delta = max(delta, abs(best_value - self.values[s[0]][s[1]]))
                
            self.values = new_values
            if delta < theta:
                break
                
        # Derive optimal policy
        self.policy = {}
        for s in self.states:
            if s in self.terminals or s in self.obstacles:
                self.policy[s] = []
                continue
                
            best_value = -float('inf')
            best_actions = []
            
            for a in self.actions:
                next_s = self.get_next_state(s, a)
                reward = -1.0
                v = reward + gamma * self.values[next_s[0]][next_s[1]]
                
                if v > best_value + 1e-7:
                    best_value = v
                    best_actions = [a]
                elif abs(v - best_value) <= 1e-7:
                    best_actions.append(a)
                    
            self.policy[s] = best_actions

        return self.values

    def get_grid_data(self):
        grid_data = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                state = (i, j)
                is_terminal = state in self.terminals
                is_obstacle = state in self.obstacles
                is_start = state == self.start
                
                cell_data = {
                    'value': self.values[i][j],
                    'is_terminal': is_terminal,
                    'is_obstacle': is_obstacle,
                    'is_start': is_start,
                    'actions': self.policy.get(state, [])
                }
                row.append(cell_data)
            grid_data.append(row)
        return grid_data
