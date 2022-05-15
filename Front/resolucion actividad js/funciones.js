function calcular_area()
{
    var radio = document.form_area_circulo.number_radio
    area = parseFloat( 2 * radio * Math.PI )
    document.form_area_circulo.txt_resultado_radio.value =area
}