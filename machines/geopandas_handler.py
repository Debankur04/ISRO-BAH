def load_clean_vector_data(): pass
def filter_features_by_attribute(): pass
def spatial_join_analysis(): pass
def create_buffer_zones(): pass
def convert_crs_geodata(): return "geopandas"


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
