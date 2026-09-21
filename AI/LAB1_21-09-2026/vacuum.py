def REFLEX_VACUUM_AGENT(percept):
    location, status = percept
    if status == "Dirty":
        return "Pick the Dirt"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Example Usage
print(REFLEX_VACUUM_AGENT(['A', 'Dirty']))  # Output: Pick the Dirt
print(REFLEX_VACUUM_AGENT(['A', 'Clean']))  # Output: Right
print(REFLEX_VACUUM_AGENT(['B', 'Clean']))  # Output: Left
