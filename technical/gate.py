_gate_open = True

def allow_decision(signal):
    global _gate_open

    if not _gate_open:
        return False

    if not signal.get("rarity_confirmed"):
        return False

    _gate_open = False
    return True
