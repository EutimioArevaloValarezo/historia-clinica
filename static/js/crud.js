$(document).ready(function () {
    $('.btn.btn-info').click(function () {
        var identificador = $(this).data('id');
        $.ajax({
            type: 'POST',
            url: '/get_historia',
            data: { 'id_historia': identificador },
            success: function (response) {
                var usuario = response.usuario;
                $('#res_usuario').text(usuario);
                $('#id_res_usuario').attr('value', identificador);
            },
            error: function (error) {
                console.log('Error en la solicitud Ajax:', error);
            }
        });
    });

    $('.btn.btn-danger').click(function () {
        var identificador = $(this).data('id');
        $.ajax({
            type: 'POST',
            url: '/get_historia',
            data: { 'id_historia': identificador },
            success: function (response) {
                var paciente = response.paciente;
                var expediente = response.expediente;
                $('#info_eliminar').text("Se eliminará permanentemente la historia clinica, con Nro. de Expediente: " + expediente + " perteneciente a " + paciente + ". ¿Desea Continuar?");
                $('#id_historia_clinica').attr('value', identificador);
            },
            error: function (error) {
                console.log('Error en la solicitud Ajax:', error);
            }
        });
    });
});



