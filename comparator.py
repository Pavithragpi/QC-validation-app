def compare(structural, erection, tol=1.0):
    missing = []

    for s in structural:
        found = False

        for e in erection:
            if abs(s["x"] - e["x"]) < tol and abs(s["y"] - e["y"]) < tol:
                found = True
                break

        if not found:
            missing.append(s)

    return missing
