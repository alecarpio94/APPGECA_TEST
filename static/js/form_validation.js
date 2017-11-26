//Se utiliza para que el campo de texto solo acepte numeros
function SoloNumeros(evt){
 if(window.event){//asignamos el valor de la tecla a keynum
  keynum = evt.keyCode; //IE
 }
 else{
  keynum = evt.which; //FF
 } 
 //comprobamos si se encuentra en el rango numérico y que teclas no recibirá.
 if((keynum > 47 && keynum < 58) || keynum == 8 || keynum == 13 || keynum == 6 ){
  return true;
 }
 else{
  return false;
 }
}

//Se utiliza para que el campo de texto solo acepte letras
function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ";//Se define todo el abecedario que se quiere que se muestre.
    especiales = [8, 37, 39, 46, 6]; //Es la validación del KeyCodes, que teclas recibe el campo de texto.

    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if(letras.indexOf(tecla) == -1 && !tecla_especial){
  //alert('Tecla no aceptada');
        return false;
      }
}

function Disable()
{
  document.auth.id_is_secretaria.disabled=false;
  document.auth.id_is_profesor.disabled=false;
  document.auth.id_is_alumno.checked=false;
  document.auth.id_is_superuser.disabled=false;
  document.auth.id_is_staff.checked=false;
}
function Enable()
{
  document.auth.id_is_alumno.checked=false;
  document.auth.id_is_secretaria.disabled=false;
  document.auth.id_is_profesor.disabled=false;
  document.auth.id_is_superuser.disabled=false;
  document.auth.id_is_staff.checked=false;
}

function habilitarCincoTextBox()
{
   var Check1 = document.getElementById('id_is_secretaria'); 
   var Check2 = document.getElementById('id_is_profesor'); 
   var Check3 = document.getElementById('id_is_alumno');
   var Check4 = document.getElementById('id_is_superuser');
   var Check5 = document.getElementById('id_is_staff');
 
    if (Check1.checked==true) 
    {
        Check2.disabled = true;
        Check3.disabled = true;
        Check4.disabled = false;
        Check5.disabled = true;
    }
    else
    {   
        Check2.disabled = false;
        Check3.disabled = false;
        Check4.disabled = true;
        Check5.disabled = true;
   }
  }

function habilitarCincoTextBox2()
{
  var Check1 = document.getElementById('id_is_secretaria'); 
  var Check2 = document.getElementById('id_is_profesor'); 
  var Check3 = document.getElementById('id_is_alumno');
  var Check4 = document.getElementById('id_is_superuser');
  var Check5 = document.getElementById('id_is_staff');
 
  if (Check2.checked==true)
  {
    Check1.disabled = true;
    Check3.disabled = true;
    Check4.disabled = true;
    Check5.disabled = false;
  }
  else
  {   
        Check1.disabled = false;
        Check3.disabled = false;
        Check4.disabled = true;
        Check5.disabled = true;
   }

}

function habilitarCincoTextBox3()
{
  var Check1 = document.getElementById('id_is_secretaria'); 
  var Check2 = document.getElementById('id_is_profesor'); 
  var Check3 = document.getElementById('id_is_alumno');
  var Check4 = document.getElementById('id_is_superuser');
  var Check5 = document.getElementById('id_is_staff');
 
  if (Check3.checked==true)
  {
    Check1.disabled = true;
    Check2.disabled = true;
    Check4.disabled = true;
    Check5.disabled = true;
  }
  else
  {   
        Check1.disabled = false;
        Check2.disabled = false;
        Check4.disabled = true;
        Check5.disabled = true;
   }

}

function copiar()
{
  document.getElementById("id_password").value=document.getElementById("id_ci").value;
  document.getElementById("id_password2").value=document.getElementById("id_ci").value;
}