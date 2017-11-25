#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ...apps.utils.selects import Selects
from ...apps.utils.forms_date import DateInput, TimeInput

#####################MODELO ALUMNO########################
class Alumno(models.Model):

	sex = (('Masculino','Masculino'),('Femenino','Femenino'))
	naci = (('V','V'),('E','E'))

	nacionalidad = models.CharField(max_length=5,choices=naci,default=2)
	cedula_alumno = models.IntegerField(primary_key=True ,unique=True)
	primer_nombre = models.CharField(max_length=50)
	segundo_nombre = models.CharField(max_length=50)
	primer_apellido = models.CharField(max_length=50)
	segundo_apellido = models.CharField(max_length=50)
	sexo_alumno = models.CharField(max_length=10,choices=sex,default=2)
	fecha_nacimiento = models.DateField(auto_now=False)
	lugar_nacimiento = models.CharField(max_length=100)
	institucion = models.CharField(max_length=200)

	def __unicode__(self):
		Dato = "%i"% (self.cedula_alumno)
		return Dato

#################MODELO REPRESENTANTE#####################
class Representante(models.Model):
	
	cedula_repres = models.IntegerField(primary_key=True, unique=True)
	nombre_repres = models.CharField(max_length=50)
	apelli_repres = models.CharField(max_length=50)
	ocupacion = models.CharField(max_length=100, choices=Selects().ocupacion())
	profesion = models.CharField(max_length=100)
	telef_cel = models.IntegerField()
	telef_res = models.IntegerField()
	direccion = models.CharField(max_length=150)

	def __unicode__(self):
		Dato = "%i"% (self.cedula_repres)
		return Dato

####################MODELO VIVIENDA#######################
class Vivienda(models.Model):

	vivien = (('Casa','Casa'),('Quinta','Quinta'),('Apartamento','Apartamento'),('Anexo','Anexo'),('Vivienda Rural','Vivienda Rural'),('Otra','Otra'))

	arte = (('Nevera','Nevera'),('Cocina','Cocina'),('Lavadora','Lavadora'),('Secadora','Secadora'),('Computadora','Computadora'),('Celular','Celular'),('Telefono Fijo','Telefono Fijo'),('Calentador De Agua','Calentador De Agua'))

	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	id_vivienda = models.IntegerField(primary_key=True,unique=True)
	tipo_vivien = models.CharField(max_length=15,choices=vivien,default=6)
	zona = models.CharField('Zona',max_length=100)
	agua = models.BooleanField('Agua')
	aseo_urbano = models.BooleanField('Aseo Urbano')
	cloacas = models.BooleanField('Cloacas')
	telefono_fijo = models.BooleanField('Telefono Fijo')
	internet = models.BooleanField('Internet')
	nevera = models.BooleanField('Nevera')
	cocina = models.BooleanField('Cocina')
	lavadora = models.BooleanField('Lavadora')
	secadora = models.BooleanField('Secadora')
	computadora = models.BooleanField('Computadora')
	celular = models.BooleanField('Celular')
	telefono_fijo = models.BooleanField('Telefono Fijo')
	calentador_de_agua = models.BooleanField('Calentador De Agua')
	habitacione = models.IntegerField()
	num_habitan = models.IntegerField()
	num_bano = models.IntegerField()
	habitan_tra = models.IntegerField()
	habitan_apo = models.IntegerField()
	mon_apr_men = models.IntegerField()
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_alumno)
		return Dato

###################MODELO DIRECCION#######################
class Direccion(models.Model):
	
	enti = (('Distrito Capital','Distrito Capital'),('Miranda','Miranda'),('Aragua','Aragua'),('Monagas','Monagas'),('Falcon','Falcon'),('Carabobo','Carabobo'),('Nueva Esparta','Nueva Esparta'),('Anzoategui','Anzoategui'),('Vargas','Vargas'),('Zulia','Zulia'),('Bolivar','Bolivar'),('Lara','Lara'),('Merida','Merida'),('Tachira','Tachira'),('Guarico','Guarico'),('Cojedes','Cojedes'),('Trujillo','Trujillo'),('Barinas','Barinas'),('Sucre','Sucre'),('Yaracuy','Yaracuy'),('Portuguesa','Portuguesa'),('Delta Amacuro','Delta Amacuro'),('Apure','Apure'),('Amazonas','Amazonas'))
	
	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	entid_feder = models.CharField(max_length=20,choices=enti,default=0)
	ciudad = models.CharField(max_length=100)
	parroquia = models.CharField(max_length=100)
	sector = models.CharField(max_length=100)
	barri_urban = models.CharField(max_length=250)
	calle_avend = models.CharField(max_length=150)
	apt_casa = models.CharField(max_length=100)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_alumno)
		return Dato

####################MODELO FAMILIA########################
class Familia(models.Model):
	
	cedula_familia = models.IntegerField(primary_key=True, unique=True)
	nombre_familia = models.CharField(max_length=50)
	apelli_familia = models.CharField(max_length=50)
	profesion = models.CharField(max_length=100)
	ocupacion = models.CharField(max_length=100)
	direccion = models.CharField(max_length=150)
	telef_cel = models.IntegerField()
	telef_res = models.IntegerField()
	vive = models.BooleanField(blank=True, default=False)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_familia)
		return Dato

#################MODELO EDUCACION ALUMNO##################
class Educa_Alumno(models.Model):
	
	cedula_alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	nivel_uno = models.BooleanField('Nivel I', default=False)
	nivel_dos = models.BooleanField('Nivel II', default=False)
	nivel_tres = models.BooleanField('Nivel III', default=False)
	nivel_cuar = models.BooleanField('Nivel IV', default=False)

	primer_grado = models.BooleanField('Primer Grado', default=False)
	segundo_grado = models.BooleanField('Primer Grado', default=False)
	tercer_grado = models.BooleanField('Segundo Grado', default=False)
	cuarto_grado = models.BooleanField('Cuarto Grado', default=False)
	quinto_grado = models.BooleanField('Quinto Grado', default=False)
	sexto_grado = models.BooleanField('Sexto Grado', default=False)

	educ_med_uno = models.BooleanField('Media I', default=False)
	educ_med_dos = models.BooleanField('Media II',default=False)

	primer = models.BooleanField('Primer Año', default=False)
	segund = models.BooleanField('Segundo Año', default=False)
	tercer = models.BooleanField('Tercer Año', default=False)
	cuarto = models.BooleanField('Cuarto Año', default=False)
	quinto = models.BooleanField('Quinto Año', default=False)
	

	curso = models.CharField(max_length=100)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_alumno)
		return Dato

###################MODELO INSTITUCION#####################
class Empresa(models.Model):

	nombre_empre = models.CharField('Nombre De La Empresa',max_length=150)
	nombre_jefe = models.CharField('Jefe De La Empresa',max_length=100)
	
	def __unicode__(self):
		Dato = "%s"% (self.nombre_empre)
		return Dato

################MODELO EDUCACION MUSICAL##################
class Educa_Musi(models.Model):

	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	progama_orque = models.CharField('Programas Orquestales Y/O Corales En Los Que Participa',max_length=100)
	instru_princi = models.CharField('Instrumento Principal',max_length=100)
	prof_clas_ind = models.CharField('Profesor De Clase Individial',max_length=100)
	instru_secund = models.CharField('Instrumento Secundario',max_length=100)
	prof_clas_ind = models.CharField('Profesor De Clase Individial',max_length=100)
	academ_catedr = models.BooleanField('El Alumno Recibe Clases En Una Academia O Catedra Nacional?',blank=True, default=False)
	nombr_academi = models.CharField('Escriba El Nombre De La Catedra Nacional En La Cual Cursa Estudios',max_length=100)
	clas_acad_cate = models.CharField('Ha Sido Selecionado(a) Para Pertenecer A Una Orquesta/Coro Nacional?',max_length=100)
	nom_aca_cate = models.CharField('Ha Sido Selecionado(a) Para Pertenecer A Una Orquesta/Coro Regional?',max_length=100)
	inst_espc_mus = models.CharField('Cursa Estudios En Una Institucion Especializada En Musica?',max_length=100)
	bec_est_esp = models.BooleanField('Recibe Alguna Beca O Ayuda Para Cursar Estudios Especializados En Musica?',blank=True, default=False)
	estu_cur = models.CharField('Que Estudios Cursa?',max_length=100)
	inst_empr_bec = models.CharField('Que Institucion O Empresa Otorga La Beca',max_length=100)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_alumno)
		return Dato

###########MODELO PERCEPCION DEL REPRESENTANTE#############
class Percep_Repre(models.Model):

	cedula_repres = models.OneToOneField(Representante, null=True, blank=True, on_delete=models.CASCADE )
	grup_fam_reco_com = models.BooleanField('Como Grupo Familiar Somos Reconocidos En La Comunidad (Nos Respetan Mas)',blank=True, default=False)
	asis_nin_act_mus = models.BooleanField('La Asistencia De Mis Niños Al La Actividad Musical, Mejoro Las Relaciones Familiares',blank=True, default=False)
	prac_mus_ent_eco = models.BooleanField('La Practica Musical Produce Una Entrada Economica Mas En El Grupo Familiar',blank=True, default=False)
	viv_mej = models.BooleanField('Ahora Vivo Mejor',blank=True, default=False)
	otra_razon = models.CharField('Otra Razon',max_length=100)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_repres)
		return Dato

###############MODELO PERCEPCION DEL NINO##################
class Percep_nino(models.Model):

	cedula_alumno = models.OneToOneField(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	m_sien_bie = models.BooleanField('Me Siento Bien',blank=True, default=False)
	m_sien_seg = models.BooleanField('Me Siento Seguro',blank=True, default=False)
	sien_mejo = models.BooleanField('Siento Que He Mejorado Como Ser Humano',blank=True, default=False)
	mas_apre_com = models.BooleanField('Soy Mas Apreciado En La Comunidad',blank=True, default=False)
	m_sien_cap = models.BooleanField('Me Siento Cansado',blank=True, default=False)
	m_sien_mot = models.BooleanField('Me Siento Desmotivado',blank=True, default=False)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_alumno)
		return Dato
