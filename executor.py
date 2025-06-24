import importlib

def execute_workflow(workflow):
    env = {}  # store intermediate results here
    results = []

    for step in workflow:
        action = step["action"]
        output_name = step.get("output")

        # Decide which machine to use based on the action
        machine = resolve_machine(action)

        if not machine:
            results.append({
                "action": action,
                "error": f"No machine found for action '{action}'"
            })
            continue

        try:
            module = importlib.import_module(f"machines.{machine}_handler")
            result = module.run(action, step, env)
            if output_name:
                env[output_name] = result
            results.append({
                "action": action,
                "output_name": output_name,
                "result": "ok"
            })
        except Exception as e:
            results.append({
                "action": action,
                "error": str(e)
            })

    return env, results


def resolve_machine(action):
    # You can extend this as more actions are defined
    rasterio_actions = {"load_raster"}
    numpy_actions = {"threshold"}
    fiona_actions = {"load_vector"}
    geopandas_actions = {"buffer", "intersect"}

    if action in rasterio_actions:
        return "rasterio"
    if action in numpy_actions:
        return "numpy"
    if action in fiona_actions:
        return "fiona"
    if action in geopandas_actions:
        return "geopandas"
    return None
