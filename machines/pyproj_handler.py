def transform_latlon_to_utm(): pass
def convert_epsg_codes(): pass
def build_crs_pipeline(): pass
def validate_projection_metadata(): pass
def reproject_point_data(): pass


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
