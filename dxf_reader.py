import ezdxf

def read_dxf(file):
    doc = ezdxf.readfile(file)
    return doc.modelspace()

def extract_columns(msp):
    columns = []

    for entity in msp:
        if entity.dxftype() == "INSERT":
            point = entity.dxf.insert

            columns.append({
                "name": entity.dxf.name,
                "x": round(point.x, 2),
                "y": round(point.y, 2)
            })

    return columns
