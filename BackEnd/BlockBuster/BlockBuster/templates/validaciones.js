function validarJuego(){
    var id_juego = document.form_registrar_juego.txt_j_id.value;
    //
    if ((id_juego.charAt(0) != 'P')){
        alert("El codigo del juego debe comenzar con P mayuscula")
        document.form_registrar_juego.txt_j_id.focus()
        return false
    }      
}