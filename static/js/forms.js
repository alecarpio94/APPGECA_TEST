$("#alumForm").validate({

  rules:
  {
    nacionalidad:{
        required: true,
    }
    cedula_alumno: {
    required: true,
        minlength: 8
    },
    primer_nombre: {
        required: true,
    }
    segundo_nombre: {
        required: true,
    }
    primer_apellido: {
        required: true,
    }
    segundo_apellido: {
        required: true,
    }
    sexo_alumno:{
        required: true,
    }
    fecha_nacimiento:{
        required: true,
    }
    lugar_nacimiento:{
        required: true
    }
    institucion:{
        required: true,
    }
  },
  messages:
  {
    cedula_alumno: {
      required: "Tu Nombre y Apellidos son Importantes",
      minlength: "Cedula/Codigo es invalido"
    },
  },
  errorPlacement : function(error, element) {
    $(element).closest('.form-group').find('.help-block').html(error.html());
  },
  highlight : function(element) {
    $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
  },
  unhighlight: function(element, errorClass, validClass) {
    $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    $(element).closest('.form-group').find('.help-block').html('');
  },

  submitHandler: function(form) { 
    form.submit(); 

    alert('ok');
  }
}); 
