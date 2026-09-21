"""
gh-filo: Simulador sociológico y dialéctico de Gran Hermano.
Punto de entrada principal.
"""
from src.entities import Participante
from src.engine import GranHermanoFilo

def cargar_elenco() -> list:
    return [
        # Grupo 1
        Participante("Sabrina", "Grupo 1 (las distintas)", "Moralista / Ética", carisma=0.6, estrategia=0.5, conflictividad=0.3),
        Participante("Cande", "Grupo 1 (las distintas)", "Gótica nihilista", carisma=0.2, estrategia=0.2, conflictividad=0.8),
        # Grupo 2
        Participante("Eva", "Grupo 2 (las chicas faso)", "Líder hegemónica", carisma=0.8, estrategia=0.9, conflictividad=0.5),
        Participante("Rocío", "Grupo 2 (las chicas faso)", "Resistente carismática", carisma=0.9, estrategia=0.6, conflictividad=0.4, dia_ingreso=2),
        Participante("Lucía", "Grupo 2 (las chicas faso)", "Social y risueña", carisma=0.6, estrategia=0.4, conflictividad=0.2),
        Participante("María", "Grupo 2 (las chicas faso)", "Silenciosa / Seguidora", es_npc=True, carisma=0.3, estrategia=0.2),
        Participante("Mailen", "Grupo 2 (las chicas faso)", "Quilombera reactiva", carisma=0.4, estrategia=0.3, conflictividad=0.9),
        Participante("Apa", "Grupo 2 (las chicas faso)", "Sombra estética", carisma=0.4, estrategia=0.3, conflictividad=0.1),
        # Grupo 3
        Participante("Mika", "Grupo 3 (las chicas merca)", "Villana acústica", carisma=0.5, estrategia=0.4, conflictividad=0.95),
        Participante("Paz", "Grupo 2 (las chicas faso)", "Doble agente / Intelectual", carisma=0.7, estrategia=0.95, conflictividad=0.6),
        Participante("Anahí", "Grupo 3 (las chicas merca)", "Intelectual estética", carisma=0.7, estrategia=0.6, conflictividad=0.4),
        Participante("Nehuen", "Grupo 3 (las chicas merca)", "Vengador ético", carisma=0.85, estrategia=0.7, conflictividad=0.6),
        Participante("Fer", "Grupo 3 (las chicas merca)", "Cínico sociológico", carisma=0.6, estrategia=0.6, conflictividad=0.7),
        # Grupo 4
        Participante("Rodri", "Grupo 4 (los varones)", "Macho alfa torpe", carisma=0.5, estrategia=0.2, conflictividad=0.6),
        Participante("Lautaro", "Grupo 4 (los varones)", "Bravucón de fondo", es_npc=True, carisma=0.2, estrategia=0.1),
        Participante("Nestor", "Grupo 4 (los varones)", "Estratega fallido", carisma=0.4, estrategia=0.5, conflictividad=0.4),
        # Grupo 5: Tomistas
        Participante("Bruno G", "Grupo 5", "Conservador soberbio", carisma=0.3, estrategia=0.5, conflictividad=0.7),
        Participante("Bruno M", "Grupo 5", "Silente absoluto", es_npc=True, carisma=0.1, estrategia=0.1),
        Participante("El sacerdote", "Grupo 5", "Tímido clerical", es_npc=True, carisma=0.2, estrategia=0.1),
        Participante("Santi Baroni", "Grupo 5", "Sociable pasivo", carisma=0.4, estrategia=0.3),
        Participante("Max Pellek", "Grupo 5", "Polémico retraído", es_npc=True, carisma=0.2, estrategia=0.2),
        # Periféricos / Marginados
        Participante("Mily", "Periféricos o marginados", "Rolinga confrontativa", carisma=0.5, estrategia=0.3, conflictividad=0.7),
        Participante("Facu", "Periféricos o marginados", "Favorito popular / Primo", carisma=0.95, estrategia=0.3, conflictividad=0.05),
        Participante("Joaco", "Periféricos o marginados", "Mártir dócil", carisma=0.6, estrategia=0.2, conflictividad=0.1),
        Participante("Adriana", "Periféricos o marginados", "Maquiavelo puro", carisma=0.8, estrategia=0.98, conflictividad=0.8),
        Participante("Alex", "Periféricos o marginados", "Chivo expiatorio", carisma=0.6, estrategia=0.5, conflictividad=0.4),
        Participante("Walter", "Periféricos o marginados", "Terrorista higiénico", carisma=0.3, estrategia=0.1, conflictividad=0.99),
        Participante("Oscar", "Periféricos o marginados", "Amable prescindible", es_npc=True, carisma=0.3, estrategia=0.2),
        Participante("Fede", "Periféricos o marginados", "Manipulador a dos puntas", carisma=0.4, estrategia=0.7, conflictividad=0.85),
        Participante("Chapo", "Periféricos o marginados", "Carismático inerte", carisma=0.5, estrategia=0.2),
        Participante("Forni", "Periféricos o marginados", "Chill intrascendente", carisma=0.4, estrategia=0.2),
        # Nuevos Ingresantes (Día posterior)
        Participante("Ivan", "Periféricos o marginados", "Planta hegemónica", carisma=0.5, estrategia=0.2, dia_ingreso=6),
        Participante("Brenda", "Periféricos o marginados", "Informante letal", carisma=0.6, estrategia=0.7, dia_ingreso=6),
        Participante("Belén", "Periféricos o marginados", "Caballo de Troya", carisma=0.6, estrategia=0.6, dia_ingreso=6),
        Participante("Kevin", "Grupo 5", "NPC supremo", es_npc=True, carisma=0.1, estrategia=0.1, dia_ingreso=6)
    ]

def main():
    print("==================================================")
    print("      GH FILO: REPO SIMULATOR (GITHUB EDITION)    ")
    print("==================================================\n")
    
    elenco = cargar_elenco()
    gh = GranHermanoFilo(elenco)
    
    gh.iniciar_juego()
    gh.semana_1_complot()
    gh.gala_purga_npcs()
    gh.semana_3_caidas_iniciales()
    gh.semana_4_gritos_y_cande()
    gh.semana_5_explosiones()
    gh.semana_6_ingresos_y_brenda()
    gh.semana_7_repechaje()
    gh.semana_8_colapso_walter_anahi()
    gh.semana_9_purga_media()
    gh.semana_10_sacrificio_joaco()
    gh.semana_11_juicio_fede_y_bajas_finales()
    
    print("\n--------------------------------------------------")
    print("           GRAN GALA FINAL DE GH FILO             ")
    print("--------------------------------------------------")
    gh.ejecutar_final()
    
    print("\n==================================================")
    print("HISTORIAL CRONOLÓGICO DE BAJAS REGISTRADAS:")
    for idx, nombre in enumerate(gh.eliminados_cronologicos, start=1):
        print(f"  {idx}. {nombre}")
    print("==================================================")

if __name__ == "__main__":
    main()
