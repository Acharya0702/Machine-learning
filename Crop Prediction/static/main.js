function validation(){
    var Temperature = document.getElementById('f1').value;
    var Humidity = document.getElementById('f2').value;
    var Ph = document.getElementById('f3').value;
    var Rainfall = document.getElementById('f4').value;
    if(Temperature == ""){
        document.getElementById("Temperature").innerHTML="Temperature can't be empty!";
        return false;
    }
    else if(Temperature < 8.825675){
        document.getElementById("Temperature").innerHTML="Temperature can't be less than 8.825675!";
        return false;
    }
    else if(Temperature > 54.986760){
        document.getElementById("Temperature").innerHTML="Temperature can't greater than 54.986760!";
        return false;
    }
    else{
        document.getElementById("Temperature").innerHTML="";
    }
    if(Humidity == ""){
        document.getElementById("Humidity").innerHTML="Humidity can't be empty!";
        return false;
    }
    else if(Humidity < 10.034048){
        document.getElementById("Humidity").innerHTML="Humidity can't be less than 10.034048!";
        return false;
    }
    else if(Humidity > 99.981876){
        document.getElementById("Humidity").innerHTML="Humidity can't greater than 99.981876!";
        return false;
    }
    else{
        document.getElementById("Humidity").innerHTML="";
    }
    if(Ph == ""){
        document.getElementById("Ph").innerHTML="Ph can't be empty!";
        return false;
    }
    else if(Ph < 3.504752){
        document.getElementById("Ph").innerHTML="Ph can't be less than 3.504752!";
        return false;
    }
    else if(Ph > 9.935091){
        document.getElementById("Ph").innerHTML="Ph can't greater than 9.935091";
        return false;
    }
    else{
        document.getElementById("Ph").innerHTML="";
    }
    if(Rainfall == ""){
        document.getElementById("Rainfall").innerHTML="Rainfall can't be empty!";
        return false;
    }
    else if(Rainfall < 20.211267){
        document.getElementById("Rainfall").innerHTML="Rainfall can't be less than 20.211267!";
        return false;
    }
    else if(Rainfall > 397.315380){Rainfall
        document.getElementById("Rainfall").innerHTML="Rainfall can't greater than 397.315380!";
        return false;
    }
    else{
        document.getElementById("Rainfall").innerHTML="";
    }
}