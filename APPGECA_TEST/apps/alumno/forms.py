#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django import forms
from ...apps.alumno.models import *
from ...apps.utils.forms_date import DateInput
import itertools

########################FORMULARIO ALUMNO#########################
class AlumForm(forms.ModelForm):
	class Meta:
		model = Alumno
		
		fields = [
		'nacionalidad',
		'cedula_alumno', 
		'primer_nombre', 
		'segundo_nombre', 
		'primer_apellido', 
		'segundo_apellido', 
		'sexo_alumno', 
		'fecha_nacimiento', 
		'lugar_nacimiento', 
		'institucion'
		]
		widgets = {
        'fecha_nacimiento': DateInput(format='%Y-%m-%d'),
        }

######################FORMULARIO REPRESENTANTE####################
class RepreForm(forms.ModelForm):
	css_error_class = 'has-error'
	class Meta:
		model = Representante

		fields = ['cedula_repres','nombre_repres','apelli_repres','ocupacion','profesion','telef_cel','telef_res','direccion']

######################FORMULARIO VIVIENDA#########################
class VivienForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Vivienda

		fields = [
		'cedula_alumno',
		'id_vivienda',
		'tipo_vivien',
		'zona',
		'agua',
		'aseo_urbano',
		'cloacas',
		'telefono_fijo',
		'internet',
		'nevera',
		'cocina',
		'lavadora',
		'secadora',
		'computadora',
		'celular',
		'telefono_fijo',
		'calentador_de_agua',
		'habitacione',
		'num_habitan',
		'num_bano',
		'habitan_tra',
		'habitan_apo',
		'mon_apr_men'
		] 
		exclude = ('cedula_alumno',)

#######################FORMULARIO DIRECCION#######################
class DireccForm(forms.ModelForm):
	
	css_error_class = 'has-error'
	class Meta:
		model = Direccion

		fields = ['cedula_alumno','entid_feder','ciudad','parroquia','sector','barri_urban','calle_avend','apt_casa']
		exclude = ('cedula_alumno',)

#######################FORMULARIO FAMILIA#########################
class FamiliForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Familia

		fields = ['cedula_familia','nombre_familia','apelli_familia','profesion','ocupacion','direccion','telef_cel','telef_res','vive']

########################FORMULARIO EDUACION#######################
class EducaForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Educa_Alumno

		fields = ['cedula_alumno','nivel_uno','nivel_dos','nivel_tres','nivel_cuar','primer_grado','segundo_grado','tercer_grado','cuarto_grado','quinto_grado','sexto_grado','educ_med_uno','educ_med_dos','primer','segund','tercer','cuarto','quinto','curso',]
		exclude = ('cedula_alumno',)

#########################FORMULARIO EMPRESA#######################
class EmpreForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Empresa

		fields = ['nombre_empre','nombre_jefe']

################FORMULARIO EDUCACION MUSICAL######################
class EducaMusiForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Educa_Musi

		fields = ['cedula_alumno','progama_orque','instru_princi','prof_clas_ind','instru_secund','prof_clas_ind','academ_catedr','nombr_academi','clas_acad_cate','nom_aca_cate','inst_espc_mus','bec_est_esp','estu_cur','inst_empr_bec']
		exclude = ('cedula_alumno',)

################FORMULARIO PERCEPCION REPRESENTANTE###############
class PercRepreForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Percep_Repre

		fields = ['cedula_repres','grup_fam_reco_com','asis_nin_act_mus','prac_mus_ent_eco','viv_mej','otra_razon',]
		exclude = ('cedula_repres',)
		
###############FORMULARIO PERCEPCION ALUMNO#######################
class PercAlumForm(forms.ModelForm):

	css_error_class = 'has-error'
	class Meta:
		model = Percep_nino

		fields = ['cedula_alumno','m_sien_bie','m_sien_seg','sien_mejo','mas_apre_com','m_sien_cap','m_sien_mot',]
		exclude = ('cedula_alumno',)
