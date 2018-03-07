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


