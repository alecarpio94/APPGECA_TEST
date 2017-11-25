 #!/usr/bin/python
# -*- coding: utf-8 -*-
class Selects(object):

    #------------------------Select Parentesco------------------------
    def parentesco(self):
        return (
            ('' , '---------'),
            ('Madre' , 'Madre'),
            ('Padre', 'Padre'),
            ('Hijoa', 'Hijo(a)'),
            ('Tioa', 'Tio(a)'),
            ('Hermanoa', 'Hermano(a)'),
            ('Abueloa', 'Abuelo(a)'),
            ('Otroa', 'Otros(as)'),
            )
    def telefono(self):
        return(
            ('0257', '0257'),
        )

    def nacionalidad(self):
        return(
            ('' , '---------'),
            ('V', 'V'),
            ('E', 'E'),
        )

    def jefe_familia(self):
        return(
            ('Jefe(a) de Familia', 'Jefe(a) de Familia'),
        )

    def movil(self):
        return (
            ('' , '---------'),
            ('0426' , '0426'),
            ('0416', '0416'),
            ('0424', '0424'),
            ('0414', '0414'),
            ('0412', '0412'),
            )
        
    def genero(self):
        return(
            ('' , '---------'),
            ('Masculino', 'M'),
            ('Femenino', 'F'),
        )

    def ocupacion(self):
        return (
            ('' , '---------'),
            ('Comerciante', 'Comerciante'),
            ('Barbero','Barbero'),
            ('Estudiante','Estudiante'),
            ('Empleadoa','Empleado(a)'),
            ('Jubiladoa','Jubilado(a)'),
            ('Tecnico','Tecnico'),
            ('Pensionadoa','Pensionado(a)'),
            ('Obreroa','Obrero(a)'),
            ('Educadora','Educador(a)'), 
            ('Pastora','Pastor(a)'),
            ('Herrero','Herrero'),
            ('Maternal','Maternal'),
            ('Soldador','Soldador'),
            ('Estilita','Estilita'),
            ('Manicurista','Manicurista'),
            ('Amao_de_casa','Ama(o) de casa'),
            ('Nutricionista','Nutricionista'),
            ('Obreroa_Educacional','Obrero(a) Educacional'),
            ('Contador','Contador'),
            ('Cocineroa','Cocinero(a)'),
            ('Policia','Policia'),
            ('Administradorar','Administrador(ar)'),
            ('Promotora_Socia','Promotor(a) Social'),
            ('Docente','Docente'),
            ('Custodio','Custodio'),
            ('Pencionadoa','Pencionado(a)'),
            ('Mecanico','Mecanico'),
            ('Abogadoa','Abogado(a)'),
            ('Chofer','Chofer'),
            ('Empleadoa_Publico','Empleado(a) Publico'),
            ('Laboratorista','Laboratorista'),
            ('Peluqueroa','Peluquero(a)'),
            ('Educadora','Educador(a)'),
            ('Agricultora','Agricultor(a)'),
            ('TSU','TSU'),
            ('Enfermeroa','Enfermero(a)'),
            ('Carpinteroa','Carpintero(a)'),
            ('Ambientalista','Ambientalista'),
            ('Militar','Militar'),
            ('Albanil','Albañil'),
            ('Secretariao','Secretaria(o)'),
            ('Deportista','Deportista'),
            ('Vigilante','Vigilante'),
            ('Costurera','Costurera'),
            ('Discapacidad','Discapacidad'),
            ('Camarerao','Camarera(o)'),
            ('Luc_social','Luc. social'),
            ('Ejecutivoa_Bancaria','Ejecutivo(a) Bancaria'),
            ('Otroa','Otros(as)'),
        )

    def propiedad(self):
        return (
            ('' , '---------'),
            ('Propia' , 'Propia'),
            ('Arquilada', 'Arquilada'),
            )
    def consejocomunal(self):
        return(
            ('' , '---------'),
            ('1', '1'),
            ('2', '2'),
            )

    def religion(self):
        return (
            ('' , '---------'),
            ('Catolico' , 'Catolico'),
            ('Cristiano' , 'Cristiano'),
            ('Ateo' , 'Ateo'),
        )

    def turno(self):
        return (
            ('' , '---------'),
            ('Manana', 'Mañana'),
            ('Tarde', 'Tarde'),
        )

    def seccion(self):
        return (
            ('' , '---------'),
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
        )

    def grado(self):
        return (
            ('', '---------'),
            ('primero', '1''ro.'),
            ('segundo', '2''do.'),
            ('tercero', '3''ro.'),
                     
        )
    def talla(self):
        return (
            ('' , '---------'),
            ('uno', '1'),
            ('dos', '2'),
            ('tres', '3'),
            ('cuatro', '4'),
            ('cinco', '5'),
            ('seies', '6'),
            ('siete', '7'),
            ('ocho', '8'),
            ('nueve', '9'),
            ('dies', '10'),
            ('Otros', 'Otros'),
                     
        )
    def zapato(self):
        return (
            ('' , '---------'),
            ('vente', '20'),
            ('ventiuno', '21'),
            ('ventidos', '22'),
            ('ventitres', '23'),
            ('venticuatro', '24'),
            ('venticinco', '25'),
            ('ventiseis', '26'),
            ('ventisiete', '27'),
            ('ventiocho', '28'),
            ('ventinueve', '29'),
            ('treinta', '30'),
            ('treintayuno', '31'),
            ('treintaydos', '32'),
            ('treintaytres', '33'),
            ('treintaycuatro', '34'),
            ('treintaycinco', '35'),
            ('Otros', 'Otros'),
                     
        )
    def ano_escolar(self):
        return (
            ('' , '---------'),
            ('qw', '2017-2018'),
            ('qww', '2017-2018'),
            ('qwww', '2018-2019'),
            ('qwww', '2018-2019'),
            ('qwww', '2019-2020'),
            ('asa', '2019-2020'),
            ('asaa', '2020-2021'),
            ('asas', '2020-2021'),
            ('saaas', '2021-2022'),
            ('sasa', '2021-2022'),
            ('asaasa', '2022-2023'),
            ('sdsf', '2022-2023'),
            ('sffsfs', '2023-2024'),
            ('cacacs', '2023-2024'),
            ('sxaxs', '2024-2025'),
            ('awerr', '2024-2025'),
            ('asasw', '2025-2026'),
            ('csefg', '2025-2026'),
            ('Otros', 'Otros'),
        )
    def aprobado(self):
        return (
            ('' , '---------'),
            ((0),'0'),
            ((1), '1'),
            ((2), '2'),
            )