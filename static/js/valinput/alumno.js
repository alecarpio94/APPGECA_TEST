// Validar todos los input
SoloNumeros1(["id_cedula_alumno", "id_cedula_repres", "id_telef_cel", "id_telef_res", "id_habitacione","id_num_habitan","id_num_bano","id_habitan_tra","id_habitan_apo","id_mon_apr_men", "id_cedula_familia", 
	"id_telef_cel_f", "id_telef_res_f"])

SoloLetra1(["id_primer_nombre","id_segundo_nombre","id_primer_apellido","id_segundo_apellido","id_segundo_apellido","id_lugar_nacimiento","id_nombre_repres","id_apelli_repres","id_profesion","id_ciudad","id_nombre_familia","id_apelli_familia","id_profesion_f","id_nombre_jefe","id_instru_princi","id_prof_clas_ind","id_instru_secund","id_prof_clas_sec","id_otra_razon"])


// calendario
var min = new Date();
min.setYear(min.getFullYear()-50);
var max = new Date();
max.setYear(max.getFullYear()-5);	
$('#calendar').datepicker({
<<<<<<< HEAD
=======
	'format': 'dd/mm/yyyy',
>>>>>>> 0f322c3677bb0607a05b7c8ccd2f7440164693f2
	'startDate': min,
	'endDate': max,
	"autoclose": true
});

//botones de siguiente o anterior
$("#repree").click(function(e) { 
	if ($("#id_nacionalidad").val() === "" || $("#id_cedula_alumno").val() === "" || $("#id_primer_nombre").val() === "" || $("#id_primer_apellido").val() === "" || $("#id_sexo_alumno").val() === "" || $("#calendar").val() === "" || $("#id_lugar_nacimiento").val() === "" || $("#id_institucion").val() === ""){
		return false	
	}else{
		$("#alu").removeClass('active')
		$("#repre").addClass('active')		
	}
});

<<<<<<< HEAD

=======
$("#vol1").click(function(e){
	$("#alu").addClass('active')
	$("#repre").removeClass('active')		
});

$("#vivie").click(function(e){
	if ($("#id_cedula_repres").val() === "" || $("#id_nombre_repres").val === "" || $("#id_apelli_repres").val() === "" || $("#id_ocupacion").val() === "" || $("#id_telef_cel").val() === ""){
		return false
	}else{
		$("#repre").removeClass('active')
		$("#vivi").addClass('active')
	}

});

$("#vol2").click(function(e){
	$("#repre").addClass('active')
	$("#vivi").removeClass('active')	
});

$("#dirr").click(function(e){
	if ($("#id_zona").val() === ""){
		return false
	}else{
		$("#vivi").removeClass('active')
		$("#dire").addClass('active')
	}
});

$("#vol3").click(function(e){
	$("#vivi").addClass('active')
	$("#dire").removeClass('active')	
});

$("#fam").click(function(e){
	if ($("#id_entid_feder").val() === "" || $("#id_ciudad").val() === "" || $("#id_parroquia").val() === "" || $("#id_sector").val() === "" || $("#id_barri_urban").val() === "" || $("#id_calle_avend").val() === "" || $("#id_apt_casa").val() === "" ){
		return false
	}else{
		$("#fami").addClass('active')
		$("#dire").removeClass('active')
	}
});

$("#vol4").click(function(e){
	$("#fami").removeClass('active')
	$("#dire").addClass('active')	
});

$("#edu").click(function(e){
	$("#fami").removeClass('active')
	$("#educ").addClass('active')
});

$("#vol5").click(function(e){
	$("#fami").addClass('active')
	$("#educ").removeClass('active')
});

$("#trab").click(function(e){
	if ($("#id_nivel_e").val() === ""){
		return false
	}else{
		$("#educ").removeClass('active')
		$("#empre").addClass('active')
	}
});

$("#vol6").click(function(e){
	$("#educ").addClass('active')
	$("#empre").removeClass('active')
});

$("#musi").click(function(e){
	$("#empre").removeClass('active')
	$("#edumu").addClass('active')
});

$("#vol7").click(function(e){
	$("#empre").addClass('active')
	$("#edumu").removeClass('active')
});

$("#perc").click(function(e){
	$("#edumu").removeClass('active')
	$("#perep").addClass('active')
});

$("#vol8").click(function(e){
	$("#edumu").addClass('active')
	$("#perep").removeClass('active')
});

$("#pren").click(function(e){
	$("#perep").removeClass('active')
	$("#peralu").addClass('active')
});

$("#vol9").click(function(e){
	$("#perep").addClass('active')
	$("#peralu").removeClass('active')
});
>>>>>>> 0f322c3677bb0607a05b7c8ccd2f7440164693f2
