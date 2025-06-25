def create_geometries(): pass
def check_geometry_intersections(): pass
def calculate_geometry_distance(): pass
def generate_convex_hull(): pass
def fix_invalid_geometries(): pass


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
