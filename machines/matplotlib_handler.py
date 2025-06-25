def plot_static_thematic_map(): pass
def overlay_layers_on_map(): pass
def export_map_image(): pass
def plot_map_time_series(): pass
def annotate_map_plot(): pass


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
