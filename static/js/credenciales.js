
$("form[name=form_iniciar_sesion]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".alert");
    var data = $form.serialize();

    $.ajax({
        url: "/iniciar_sesion_usuario",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = '/'
        },
        error: function (resp) {
            console.log(resp);
            $error.removeClass("visually-hidden");
        }

    });

    e.preventDefault();
})

$('form[name=form_registrar]').submit(function (e) {
    var $form = $(this);
    var data = $form.serialize();
    var $alert = $form.find('.alert');
    $.ajax({
        url: '/registrar_usuario',
        type: 'POST',
        data: data,
        dataType: 'json',
        success: function (resp) {
            window.location.href = '/'
        },
        error: function (resp) {
            console.log(resp);
            $alert.text(resp.responseJSON.error).removeClass('visually-hidden');
        }

    });

    e.preventDefault();
});


$("form[name=form_editar_usuario]").submit(function (e) {
    var $form = $(this);
    var $alert = $form.find(".alert");
    var data = $form.serialize();
    var passwordInputs = $('#div-contenedor input[type="password"]');

    $.ajax({
        url: "/editar_usuario",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            console.log("SUCCESS: ", resp.success)
            $('#alertaTitulo').text('Listo!! ');
            $('#alertaCuerpo').text(resp.success);
            $alert.addClass("alert-success").removeClass("visually-hidden");
            $("#swtich_contrasenia").prop("checked", false);
            $('#div-contenedor').addClass('visually-hidden');
            passwordInputs.val('');
        },
        error: function (resp) {
            console.log("ERROR: ", resp);
            $('#alertaTitulo').text('Error ');
            $('#alertaCuerpo').text(resp.responseJSON.error);
            $alert.addClass("alert-danger").removeClass("visually-hidden");
            $("#swtich_contrasenia").prop("checked", false);
            $('#div-contenedor').addClass('visually-hidden');
            passwordInputs.val('');
        }

    });

    e.preventDefault();
})