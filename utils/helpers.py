def limpiar_campos(campos_dict):
    for entry in campos_dict.values():
        entry.delete(0, "end")