"""
Módulo de entidades para gh-filo.
Modela el comportamiento de cada jugador según su perfil discursivo y táctico.
"""
from typing import List, Dict, Optional

class Participante:
    def __init__(
        self,
        nombre: str,
        grupo: str,
        arquetipo: str,
        es_npc: bool = False,
        estrategia: float = 0.5,
        carisma: float = 0.5,
        conflictividad: float = 0.5,
        dia_ingreso: int = 1
    ):
        self.nombre = nombre
        self.grupo = grupo
        self.arquetipo = arquetipo
        self.es_npc = es_npc
        self.estrategia = estrategia
        self.carisma = carisma
        self.conflictividad = conflictividad
        self.dia_ingreso = dia_ingreso
        
        self.en_casa: bool = False
        self.expulsado: bool = False
        self.abandono: bool = False
        self.votos_recibidos: int = 0
        self.afinidades: Dict[str, float] = {}

    def inicializar_afinidades(self, todos: List['Participante']):
        for p in todos:
            if p.nombre == self.nombre:
                continue
            if p.grupo == self.grupo and self.grupo not in ["Periféricos o marginados", "Grupo 5"]:
                self.afinidades[p.nombre] = 0.8
            else:
                self.afinidades[p.nombre] = 0.4

    def emitir_votos(self, candidatos: List['Participante']) -> List['Participante']:
        elegibles = [p for p in candidatos if p.nombre != self.nombre and p.en_casa]
        if not elegibles:
            return []

        elegibles.sort(key=lambda x: (self.afinidades.get(x.nombre, 0.5), -x.carisma))
        
        primer_voto = elegibles[0]
        segundo_voto = elegibles[1] if len(elegibles) > 1 else elegibles[0]
        return [primer_voto, segundo_voto]

    def __repr__(self):
        return f"<Participante: {self.nombre} ({self.grupo}) - Estado: {'Activo' if self.en_casa else 'Fuera'}>"
