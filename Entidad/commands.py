# command help
 
class ConmandInfo:
    def __init__(self, nombre: str, descripcion: str, sudo: bool = False, super_sudo: bool = False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.sudo = sudo
        self.super_sudo = super_sudo

