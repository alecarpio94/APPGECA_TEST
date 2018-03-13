#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.db import models
from ...apps.utils.selects import Selects
from ...apps.utils.forms_date import DateInput, TimeInput

#####################MODELO ALUMNO########################
class Alumno(models.Model):

	sex = (('Masculino','Masculino'),('Femenino','Femenino'))
	naci = (('V','V'),('E','E'))

	nacionalidad = models.CharField(apodo('Nacionalidad*'),max_length=5,choices=naci,default=2)
	cedula_alumno = models.CharField(apodo('Cedula*'),unique=True, max_length=8, primary_key=True)
	primer_nombre = models.CharField(apodo('Primer Nombre*'),max_length=50)
	segundo_nombre = models.CharField(apodo('Segundo Nombre'),max_length=50, blank=True, null=True)
	primer_apellido = models.CharField(apodo('Primer Apellido*'),max_length=50)
	segundo_apellido = models.CharField(apodo('Segundo Apellido'),max_length=50, blank=True, null=True)
	sexo_alumno = models.CharField(apodo('Sexo*'),max_length=10,choices=sex,default=2)
	fecha_nacimiento = models.DateField(apodo('Fecha De Nacimiento*'),auto_now=False)
	lugar_nacimiento = models.CharField(apodo('Lugar De Nacimiento*'),max_length=100)
	institucion = models.CharField(apodo('Institucion*'),max_length=200)

	def __unicode__(self):
		return '%s %s'%(self.primer_nombre, self.primer_apellido)

	def get_full_name(self):
		return '%s %s'%(self.primer_nombre, self.primer_apellido)
		
#################MODELO REPRESENTANTE#####################
class Representante(models.Model):
	
	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	cedula_repres = models.CharField(apodo('Cedula Representante*'),max_length=8,primary_key=True, unique=True)
	nombre_repres = models.CharField(apodo('Nombre Del Representante*'),max_length=50)
	apelli_repres = models.CharField(apodo('Apellido Del Representante*'),max_length=50)
	ocupacion = models.CharField(apodo('Ocupacion*'),max_length=100, choices=Selects().ocupacion())
	profesion = models.CharField(apodo('Profesion'),max_length=100, null=True, blank=True)
	telef_cel = models.CharField(apodo('Telefono Celular*'), max_length=11 ,blank=True)
	telef_res = models.CharField(apodo('Telefono Residencial'), max_length=11 ,blank=True, null=True)
	direccion = models.CharField(apodo('Direccion*'),max_length=150,blank=True, null=True)

	def __unicode__(self):
		return '%i %i'%(self.cedula_repres, self.cedula_alumno)

####################MODELO VIVIENDA#######################
class Vivienda(models.Model):

	vivien = (('Casa','Casa'),('Quinta','Quinta'),('Apartamento','Apartamento'),('Anexo','Anexo'),('Vivienda Rural','Vivienda Rural'),('Otra','Otra'))

	arte = (('Nevera','Nevera'),('Cocina','Cocina'),('Lavadora','Lavadora'),('Secadora','Secadora'),('Computadora','Computadora'),('Celular','Celular'),('Telefono Fijo','Telefono Fijo'),('Calentador De Agua','Calentador De Agua'))

	cedula_alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
	#id_vivienda = models.IntegerField(primary_key=True,unique=True)
	tipo_vivien = models.CharField('Tipo De Vivienda',max_length=15,choices=vivien,default=6)
	zona = models.CharField('Zona',max_length=100)
	agua = models.BooleanField('Agua', default=False )
	aseo_urbano = models.BooleanField('Aseo Urbano', default=False )
	cloacas = models.BooleanField('Cloacas', default=False )
	telefono_fijo = models.BooleanField('Telefono Fijo', default=False )
	internet = models.BooleanField('Internet', default=False )
	nevera = models.BooleanField('Nevera', default=False )
	cocina = models.BooleanField('Cocina', default=False )
	lavadora = models.BooleanField('Lavadora', default=False )
	secadora = models.BooleanField('Secadora', default=False )
	computadora = models.BooleanField('Computadora', default=False )
	celular = models.BooleanField('Celular', default=False )
	calentador_de_agua = models.BooleanField('Calentador De Agua', default=False )
	habitacione = models.CharField('Numero De Habitaciones En La Vivienda', max_length=10 ,blank=True, null=True)
	num_habitan = models.CharField('Numero De Habitantes En La Vivienda', max_length=10 ,blank=True, null=True)
	num_bano = models.CharField('Numero De Baños En La Vivienda', max_length=10 ,blank=True, null=True)
	habitan_tra = models.CharField('Habitantes Que Trabajan', max_length=10 ,blank=True, null=True)
	habitan_apo = models.CharField('Habitantes Que Aportan', max_length=10 ,blank=True, null=True)
	mon_apr_men = models.CharField('Monto Aproximado De Ingresos Total Mensual En El Hogar(Bs)', max_length=100 ,blank=True, null=True)
	
	def __unicode__(self):
		return '%s'%(self.cedula_alumno)

###################MODELO DIRECCION#######################
class Direccion(models.Model):
	
	enti = (('Distrito Capital','Distrito Capital'),('Miranda','Miranda'),('Aragua','Aragua'),('Monagas','Monagas'),('Falcon','Falcon'),('Carabobo','Carabobo'),('Nueva Esparta','Nueva Esparta'),('Anzoategui','Anzoategui'),('Vargas','Vargas'),('Zulia','Zulia'),('Bolivar','Bolivar'),('Lara','Lara'),('Merida','Merida'),('Tachira','Tachira'),('Guarico','Guarico'),('Cojedes','Cojedes'),('Trujillo','Trujillo'),('Barinas','Barinas'),('Sucre','Sucre'),('Yaracuy','Yaracuy'),('Portuguesa','Portuguesa'),('Delta Amacuro','Delta Amacuro'),('Apure','Apure'),('Amazonas','Amazonas'))
	
	cedula_alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
	entid_feder = models.CharField(apodo('Entidad Federal*'),max_length=20,choices=enti,default=0)
	ciudad = models.CharField(apodo('Ciudad*'),max_length=100)
	parroquia = models.CharField(apodo('Parroquia*'),max_length=100)
	sector = models.CharField(apodo('Sector*'),max_length=100)
	barri_urban = models.CharField(apodo('Barrio/Urbanizacion*'),max_length=250)
	calle_avend = models.CharField(apodo('Calle/Avenida*'),max_length=150)
	apt_casa = models.CharField(apodo('Apartamento/Casa*'),max_length=100)
	
	def __unicode__(self):
		return '%s'%(self.cedula_alumno)

####################MODELO FAMILIA########################
class Familia(models.Model):
	
	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	cedula_familia = models.CharField(apodo('Cedula Del Familiar*'),max_length=8, null=True, unique=True, blank=True)
	nombre_familia = models.CharField(apodo('Nombre Del Familiar*'),max_length=50, blank=True, null=True)
	apelli_familia = models.CharField(apodo('Apellido Del Familiar*'),max_length=50, blank=True, null=True)
	ocupacion_f = models.CharField(apodo('Ocupacion*'),max_length=100, choices=Selects().ocupacion(), blank=True, null=True)
	profesion_f = models.CharField(apodo('Profesion'),max_length=100, null=True, blank=True)
	direccion = models.CharField(apodo('Direccion*'),max_length=150, blank=True, null=True)
	telef_cel_f = models.CharField(apodo('Telefono Celular*'), max_length=11 ,blank=True, null=True)
	telef_res_f = models.CharField(apodo('Telefono Residencial'), max_length=11 ,null=True, blank=True)
	vive = models.BooleanField(apodo('Vive Con El Alumno?*'),blank=True, default=False)
	
	def __unicode__(self):
		return '%i'%(self.cedula_familia)

#################MODELO EDUCACION ALUMNO##################
class EducaAlumno(models.Model):
	
	nivel = (('Nivel Uno','Nivel Uno'),('Nivel Dos','Nivel Dos'),('Nivel Tres','Nivel Tres'),('Primer Grado','Primer Grado'),('Segundo Grado','Segundo Grado'),('Tercer Grado','Tercer Grado'),('Cuarto Grado','Cuarto Grado'),('Quinto Grado','Quinto Grado'),('Sexto Grado','Sexto Grado'),('Educacion Media Uno','Educacion Media Uno'),('Educacion Media Dos','Educacion Media Dos'),('Primer Año','Primer Año'),('Segundo Año','Segundo Año'),('Tercer Año','Tercer Año'),('Cuarto Año','Cuarto Año'),('Quinto Año','Quinto Año'),('Sexto Año','Sexto Año'))

	cedula_alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	nivel_e = models.CharField(apodo('Nivel Educativo*'),choices=nivel, max_length=20)
	curso = models.CharField(max_length=100, blank=True, null=True)
	
	def __unicode__(self):
		return '%s'%(self.cedula_alumno)

###################MODELO INSTITUCION#####################
class Empresa(models.Model):

	nombre_empre = models.CharField('Nombre De La Empresa',max_length=150, null=True, blank=True)
	nombre_jefe = models.CharField('Jefe De La Empresa',max_length=100, null=True, blank=True)
	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	
	def __unicode__(self):
		return '%s %s'%(self.nombre_empre, self.cedula_alumno)

################MODELO EDUCACION MUSICAL##################
class EducaMusi(models.Model):

	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	progama_orque = models.CharField('Programas Orquestales Y/O Corales En Los Que Participa',max_length=100, null=True, blank=True)
	instru_princi = models.CharField('Instrumento Principal',max_length=100, null=True, blank=True)
	prof_clas_ind = models.CharField('Profesor De Clase Individial',max_length=100, null=True, blank=True)
	instru_secund = models.CharField('Instrumento Secundario',max_length=100, null=True, blank=True)
	prof_clas_sec = models.CharField('Profesor De Clase Individial',max_length=100, null=True, blank=True)
	academ_catedr = models.BooleanField('El Alumno Recibe Clases En Una Academia O Catedra Nacional?',default=False)
	nombr_academi = models.CharField('Escriba El Nombre De La Catedra Nacional En La Cual Cursa Estudios',max_length=100, null=True, blank=True)
	clas_acad_cate = models.CharField('Ha Sido Selecionado Para Pertenecer A Una Orquesta/Coro Nacional?',max_length=100, null=True, blank=True)
	nom_aca_cate = models.CharField('Ha Sido Selecionado Para Pertenecer A Una Orquesta/Coro Regional?',max_length=100, null=True, blank=True)
	inst_espc_mus = models.CharField('Cursa Estudios En Una Institucion Especializada En Musica?',max_length=100, null=True, blank=True)
	bec_est_esp = models.BooleanField('Recibe Alguna Beca O Ayuda Para Cursar Estudios Especializados En Musica?', default=False)
	estu_cur = models.CharField('Que Estudios Cursa?',max_length=100, null=True, blank=True)
	inst_empr_bec = models.CharField('Que Institucion O Empresa Otorga La Beca',max_length=100, null=True, blank=True)
	
	def __unicode__(self):
		return '%s'%(self.cedula_alumno)

###########MODELO PERCEPCION DEL REPRESENTANTE#############
class PercepRepre(models.Model):

	cedula_repres = models.OneToOneField(Representante, null=True, blank=True, on_delete=models.CASCADE )
	grup_fam_reco_com = models.BooleanField('Como Grupo Familiar Somos Reconocidos En La Comunidad (Nos Respetan Mas)', default=False)
	asis_nin_act_mus = models.BooleanField('La Asistencia De Mis Niños Al La Actividad Musical, Mejoro Las Relaciones Familiares', default=False)
	prac_mus_ent_eco = models.BooleanField('La Practica Musical Produce Una Entrada Economica Mas En El Grupo Familiar', default=False)
	viv_mej = models.BooleanField('Ahora Vivo Mejor',default=False)
	otra_razon = models.CharField('Otra Razon',max_length=100, blank=True, null=True)
	
	def __unicode__(self):
		return '%s'%(self.cedula_alumno)

###############MODELO PERCEPCION DEL NINO##################
class PercepNino(models.Model):

	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	m_sien_bie = models.BooleanField('Me Siento Bien', default=False)
	m_sien_seg = models.BooleanField('Me Siento Seguro', default=False)
	sien_mejo = models.BooleanField('Siento Que He Mejorado Como Ser Humano', default=False)
	mas_apre_com = models.BooleanField('Soy Mas Apreciado En La Comunidad', default=False)
	m_sien_cap = models.BooleanField('Me Siento Cansado', default=False)
	m_sien_mot = models.BooleanField('Me Siento Desmotivado', default=False)
	
	def __unicode__(self):
		return '%s'%(self.cedula_alumno)
