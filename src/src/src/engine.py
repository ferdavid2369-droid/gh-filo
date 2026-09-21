"""
Motor de eventos y ciclo de vida de gh-filo.
Ejecuta la cronología de eventos, nominaciones y expulsiones.
"""
import random
from typing import List, Dict
from src.entities import Participante

class GranHermanoFilo:
    def __init__(self, participantes: List[Participante]):
        self.participantes: Dict[str, Participante] = {p.nombre: p for p in participantes}
        self.semana_actual: int = 1
        self.eliminados_cronologicos: List[str] = []

    def get_activos(self) -> List[Participante]:
        return [p for p in self.participantes.values() if p.en_casa]

    def log(self, mensaje: str):
        print(f"[GH FILO - SEMANA {self.semana_actual}] {mensaje}")

    def iniciar_juego(self):
        # Día 1: Ingresan los 31 iniciales
        for p in self.participantes.values():
            if p.dia_ingreso == 1:
                p.en_casa = True
            p.inicializar_afinidades(list(self.participantes.values()))
        
        self.log("Comienza el reality. 31 participantes ingresan a la casa.")
        self.log("Fer introduce la distinción semiótica: 'Chicas Faso' vs 'Chicas Merca'.")
        self.log("Gran Hermano sanciona a Fer con placa directa por estigmatización; el público lo salva.")
        
        # Día 2: Ingresa Rocío
        rocio = self.participantes["Rocío"]
        rocio.en_casa = True
        self.log("Día 2: Ingresa Rocío. Se consolida el núcleo de las 'Chicas Faso' y se aísla a Mika.")

    def semana_1_complot(self):
        self.semana_actual = 1
        self.log("Los varones del Grupo 4 intentan complot contra Sabrina.")
        self.log("Gran Hermano detecta el acuerdo tácito en el gimnasio: Votos del Grupo 4 anulados.")

    def gala_purga_npcs(self):
        self.semana_actual = 2
        self.log("Gala de Eliminación Múltiple: Reducción presupuestaria y purga de irrelevancia narrativa.")
        expulsados = ["Lautaro", "Juan Viñon", "Oscar", "María", "El sacerdote", "Bruno M"]
        for nombre in expulsados:
            p = self.participantes[nombre]
            p.en_casa = False
            p.expulsado = True
            self.eliminados_cronologicos.append(nombre)
        self.log(f"Expulsados por anomia social: {', '.join(expulsados)}.")

    def semana_3_caidas_iniciales(self):
        self.semana_actual = 3
        # Rodri expulsado por torpeza estratégica
        rodri = self.participantes["Rodri"]
        rodri.en_casa = False
        rodri.expulsado = True
        self.eliminados_cronologicos.append("Rodri")
        self.log("Rodri es eliminado por el voto popular tras el bochorno del complot fallido.")

        # Walter primer round: terrorismo sanitario
        walter = self.participantes["Walter"]
        walter.en_casa = False
        walter.expulsado = True
        self.eliminados_cronologicos.append("Walter (1ª vez)")
        self.log("Walter es expulsado por sabotaje higiénico recurrente en los baños.")

    def semana_4_gritos_y_cande(self):
        self.semana_actual = 4
        self.log("Grito del exterior: '¡PAZ TRAIDORA, ESTÁS CON FER!'")
        paz = self.participantes["Paz"]
        paz.en_casa = False
        paz.expulsado = True
        self.eliminados_cronologicos.append("Paz (1ª vez)")
        self.log("El Grupo 2 fulmina a Paz tras descubrir el doble juego; el público la elimina para calibrar el caos.")

        cande = self.participantes["Cande"]
        cande.en_casa = False
        cande.expulsado = True
        self.eliminados_cronologicos.append("Cande")
        self.log("Cande es eyectada por negarse sistemáticamente a las pautas comerciales.")

    def semana_5_explosiones(self):
        self.semana_actual = 5
        mika = self.participantes["Mika"]
        mika.en_casa = False
        mika.expulsado = True
        self.eliminados_cronologicos.append("Mika (1ª vez)")
        self.log("Mika colapsa dialécticamente contra Sabrina. El público la expulsa por saturación acústica.")

        fer = self.participantes["Fer"]
        fer.en_casa = False
        fer.expulsado = True
        self.eliminados_cronologicos.append("Fer (1ª vez)")
        self.log("Fer queda aislado sin Paz y es eliminado debido a su altanería académica.")

    def semana_6_ingresos_y_brenda(self):
        self.semana_actual = 6
        self.log("Ingresan 4 nuevos participantes: Ivan, Brenda, Belén y Kevin.")
        for n in ["Ivan", "Brenda", "Belén", "Kevin"]:
            self.participantes[n].en_casa = True
        
        # Brenda filtra info y es expulsada
        brenda = self.participantes["Brenda"]
        brenda.en_casa = False
        brenda.expulsado = True
        self.eliminados_cronologicos.append("Brenda")
        self.log("Brenda le revela a Fede el repudio del público hacia su persona. Expulsión disciplinaria inmediata.")

    def semana_7_repechaje(self):
        self.semana_actual = 7
        self.log("Gala de Repechaje: Reingresan Mika, Fer y Paz.")
        for n in ["Mika", "Fer", "Paz"]:
            self.participantes[n].en_casa = True
            self.participantes[n].expulsado = False
        self.participantes["Paz"].grupo = "Grupo 3 (las chicas merca)"
        self.log("Paz formaliza su pase al Grupo 3. Comienza la guerra abierta contra la hegemonía restante.")

    def semana_8_colapso_walter_anahi(self):
        self.semana_actual = 8
        self.log("Sobre Dorado: Walter reingresa arbitrariamente por decisión de la producción.")
        self.participantes["Walter"].en_casa = True
        
        anahi = self.participantes["Anahí"]
        anahi.en_casa = False
        anahi.abandono = True
        self.eliminados_cronologicos.append("Anahí (Abandono)")
        self.log("Anahí se niega a cohabitar con Walter y abandona voluntariamente por dignidad estética.")

        walter = self.participantes["Walter"]
        walter.en_casa = False
        walter.expulsado = True
        self.eliminados_cronologicos.append("Walter (Expulsión Final)")
        self.log("Walter agrede verbalmente a Sabrina y es expulsado de manera definitiva.")

    def semana_9_purga_media(self):
        self.semana_actual = 9
        # Kevin sale en placa positiva
        kevin = self.participantes["Kevin"]
        kevin.en_casa = False
        kevin.expulsado = True
        self.eliminados_cronologicos.append("Kevin")
        self.log("Kevin es eliminado en placa positiva al no registrarse intención de voto hacia su persona.")

        mailen = self.participantes["Mailen"]
        mailen.en_casa = False
        mailen.expulsado = True
        self.eliminados_cronologicos.append("Mailen")
        self.log("Mailen confronta sin filtro a Rocío y el público la sanciona con la salida.")

    def semana_10_sacrificio_joaco(self):
        self.semana_actual = 10
        self.log("Adriana ejecuta la máxima maquiavélica: entrega a Joaco en placa para asegurar su propia continuidad.")
        joaco = self.participantes["Joaco"]
        joaco.en_casa = False
        joaco.expulsado = True
        self.eliminados_cronologicos.append("Joaco")
        self.log("Joaco es expulsado; Adriana consolida su arquetipo de villana estratega.")

    def semana_11_juicio_fede_y_bajas_finales(self):
        self.semana_actual = 11
        # Paz destruye a Fede en cena
        fede = self.participantes["Fede"]
        fede.en_casa = False
        fede.expulsado = True
        self.eliminados_cronologicos.append("Fede")
        self.log("Paz expone el doble juego de Fede durante la cena. Fede es expulsado por repudio general.")

        # Salidas de descarte hacia la semifinal
        bajas = [
            ("Bruno G", "Soberbia conservadora"),
            ("Santi Baroni", "Inanición de contenido"),
            ("Mily", "Falta de estructura de apoyo"),
            ("Nestor", "Inconsistencia de alianzas"),
            ("Apa", "Dependencia simbólica de Eva"),
            ("Chapo", "Agotamiento del perfil gregario"),
            ("Forni", "Neutralidad insostenible"),
            ("Belén", "Descubierta como infiltrada"),
            ("Ivan", "Agotamiento de la planta hegemónica"),
            ("Lucía", "Dispersión del voto afín"),
            ("Sabrina", "Retiro ético ante la falta de quorum reflexivo"),
            ("Mika", "Recaída en la neurosis acústica"),
            ("Fer", "Segunda condena por desprecio hacia las masas"),
            ("Eva", "Regicidio sociológico en semifinal")
        ]
        
        for nombre, motivo in bajas:
            if nombre in self.participantes and self.participantes[nombre].en_casa:
                p = self.participantes[nombre]
                p.en_casa = False
                p.expulsado = True
                self.eliminados_cronologicos.append(nombre)
                self.log(f"{nombre} es eliminado ({motivo}).")

    def ejecutar_final(self) -> str:
        self.semana_actual = 15
        finalistas = self.get_activos()
        self.log(f"LLEGAN A LA FINAL LOS 5 SOBREVIVIENTES: {[f.nombre for f in finalistas]}")
        
        # Ponderación de votos populares finales
        # Factores: Carisma * 0.4 + Autenticidad/Estrategia * 0.4 + Voto épico * 0.2
        scores = {}
        for f in finalistas:
            puntuacion = (f.carisma * 45) + (f.estrategia * 35) + (random.uniform(10, 20))
            scores[f.nombre] = puntuacion

        ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        self.log("Resultados de la votación telefónica final:")
        for puesto, (nombre, puntaje) in enumerate(ranking, start=1):
            print(f"  {puesto}º Puesto: {nombre} con {puntaje:.2f}% de apoyo consolidado.")

        ganador = ranking[0][0]
        self.log(f"¡EL GANADOR DE GH FILO ES: {ganador.upper()}!")
        return ganador
