import ifcopenshell

def load_ifc(file):
    return ifcopenshell.open(file)

def get_ifc_columns(model):
    columns = []

    for col in model.by_type("IfcColumn"):
        try:
            loc = col.ObjectPlacement.RelativePlacement.Location.Coordinates

            columns.append({
                "id": col.GlobalId,
                "x": round(loc[0], 2),
                "y": round(loc[1], 2),
                "z": round(loc[2], 2)
            })
        except:
            continue

    return columns
