$(document).ready(function () {
    $('.btn.btn-info').click(function () {
        var identificador = $(this).data('id');
        $.ajax({
            type: 'POST',
            url: '/get_historia',
            data: { 'id_historia': identificador },
            success: function (response) {
                var historia = response.historia;
                $('#id_historia_clinica_editar').attr('value', identificador);

                $('#inputNumExpediente').val(historia.historia_clinica.nro_expediente);
                $('#inputCama').val(historia.historia_clinica.cama_cubiculo);
                $('#inputFecha').val(historia.historia_clinica.fecha);
                $('#inputHora').val(historia.historia_clinica.hora);

                $('#inputNombre').val(historia.registro_paciente.nombres);
                $('#inputApellido').val(historia.registro_paciente.apellidos);
                $('#inputNacimiento').val(historia.registro_paciente.fecha_nacimiento);
                $('#inputEdad').val(historia.registro_paciente.edad);
                $('#inputSexo').val(historia.registro_paciente.sexo);
                $('#inputEstadoCivil').val(historia.registro_paciente.estado_civil);
                $('#inputCedula').val(historia.registro_paciente.cedula);
                $('#inputCelular').val(historia.registro_paciente.celular);
                $('#inputCorreo').val(historia.registro_paciente.correo);
                $('#inputLugarNacimiento').val(historia.registro_paciente.lugar_nacimiento);
                $('#inputLugarRecidencia').val(historia.registro_paciente.lugar_recidencia);
                $('#inputDireccionDomicilio').val(historia.registro_paciente.direccion_domicilio);
                $('#inputNivelInstruccion').val(historia.registro_paciente.nivel_instruccion);
                $('#inputOcupacion').val(historia.registro_paciente.ocupacion);
                $('#inputProfesion').val(historia.registro_paciente.profesion);
                $('#inputSeguroSocial').val(historia.registro_paciente.seguro_social);
                $('#inputRaza').val(historia.registro_paciente.raza);
                $('#inputReligion').val(historia.registro_paciente.religion);

                
                $('#input' + (historia.antecedente_heredofamiliar.congenita.padecimiento ? 'Si' : 'No') + 'Congenitas').prop('checked', true);
                $('#floatingCongenitasParentesco').val(historia.antecedente_heredofamiliar.congenita.parentesco);
                $('#floatingCongenitasEspecifique').val(historia.antecedente_heredofamiliar.congenita.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.infecciosa.padecimiento ? 'Si' : 'No') + 'Infecciosa').prop('checked', true);
                $('#floatingInfecciosaParentesco').val(historia.antecedente_heredofamiliar.infecciosa.parentesco);
                $('#floatingInfecciosaEspecifique').val(historia.antecedente_heredofamiliar.infecciosa.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.metabolica.padecimiento ? 'Si' : 'No') + 'Metabolica').prop('checked', true);
                $('#floatingMetabolicaParentesco').val(historia.antecedente_heredofamiliar.metabolica.parentesco);
                $('#floatingMetabolicaEspecifique').val(historia.antecedente_heredofamiliar.metabolica.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.musculoesqueletico.padecimiento ? 'Si' : 'No') + 'Musculoesqueletico').prop('checked', true);
                $('#floatingMusculoesqueleticoParentesco').val(historia.antecedente_heredofamiliar.musculoesqueletico.parentesco);
                $('#floatingMusculoesqueleticoEspecifique').val(historia.antecedente_heredofamiliar.musculoesqueletico.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.cardiovascular.padecimiento ? 'Si' : 'No') + 'Cardiovascular').prop('checked', true);
                $('#floatingCardiovascularParentesco').val(historia.antecedente_heredofamiliar.cardiovascular.parentesco);
                $('#floatingCardiovascularEspecifique').val(historia.antecedente_heredofamiliar.cardiovascular.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.respiratoria.padecimiento ? 'Si' : 'No') + 'Respiratoria').prop('checked', true);
                $('#floatingRespiratoriasParentesco').val(historia.antecedente_heredofamiliar.respiratoria.parentesco);
                $('#floatingRespiratoriasEspecifique').val(historia.antecedente_heredofamiliar.respiratoria.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.oncologica.padecimiento ? 'Si' : 'No') + 'Oncologica').prop('checked', true);
                $('#floatingOncologicasParentesco').val(historia.antecedente_heredofamiliar.oncologica.parentesco);
                $('#floatingOncologicasEspecifique').val(historia.antecedente_heredofamiliar.oncologica.especificar);

                $('#input' + (historia.antecedente_heredofamiliar.otra.padecimiento ? 'Si' : 'No') + 'Otra').prop('checked', true);
                $('#floatingOtrasParentesco').val(historia.antecedente_heredofamiliar.otra.parentesco);
                $('#floatingOtrasEspecifique').val(historia.antecedente_heredofamiliar.otra.especificar);

                $('#checkAlergiaAsma').prop('checked', historia.antecedente_personal.alergia.asma);
                $('#checkAlergiaRinitis').prop('checked', historia.antecedente_personal.alergia.rinitis);
                $('#checkAlergiaConjuntivitis').prop('checked', historia.antecedente_personal.alergia.conjuntivitis);
                $('#checkAlergiaAlimentos').prop('checked', historia.antecedente_personal.alergia.alimentos);
                $('#checkAlergiaMedicamentos').prop('checked', historia.antecedente_personal.alergia.medicamentos);
                $('#checkAlergiaLatex').prop('checked', historia.antecedente_personal.alergia.latex);
                $('#checkAlergiaNinguna').prop('checked', historia.antecedente_personal.alergia.ninguna);
                $('#textareaAlergiaOtra').val(historia.antecedente_personal.alergia.otra);

                $('#checkEDDermatitisAtopica').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.dermatitis_atopica);
                $('#checkEDAcne').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.acne);
                $('#checkEDUrticaria').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.urticaria);
                $('#checkEDVitiligo').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.vitiligo);
                $('#checkEDQueratosis').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.queratosis);
                $('#checkEDSarna').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.sarna);
                $('#checkEDPieAtleta').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.pie_atleta);
                $('#checkEDHongos').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.hongos);
                $('#checkEDNinguna').prop('checked', historia.antecedente_personal.enfermedad_dermatologica.ninguna);
                $('#textareaEDOtra').val(historia.antecedente_personal.enfermedad_dermatologica.otra);

                $('#radio' + (historia.antecedente_personal.quirurgico.tiene_cirugia ? 'Si' : 'No') + 'Quirurgico').prop('checked', true);
                $('#textAreaCirugia').val(historia.antecedente_personal.quirurgico.area_cirugia);
                $('#textMotivoCirugia').val(historia.antecedente_personal.quirurgico.motivo_cirugia);

                $('#radio' + (historia.antecedente_personal.farmaco.tiene_farmaco ? 'Si' : 'No') + 'Farmaco').prop('checked', true);
                $('#textNombreFarmaco').val(historia.antecedente_personal.farmaco.nombre);
                $('#textFarmacoAnticonceptivo').val(historia.antecedente_personal.farmaco.anticoncepcion);
                $('#textOtroMotivo').val(historia.antecedente_personal.farmaco.otro_motivo);
                $('#textFarmacoFrecuencia').val(historia.antecedente_personal.farmaco.frecuencia);
                $('#textFarmacoDosificacion').val(historia.antecedente_personal.farmaco.dosificacion);

                $('#checkDiu').prop('checked', historia.antecedente_personal.implantes.diu);
                $('#checkMamoplastia').prop('checked', historia.antecedente_personal.implantes.mamoplastia);
                $('#checkArticulaciones').prop('checked', historia.antecedente_personal.implantes.articulacion);
                $('#textAreaArticulacion').val(historia.antecedente_personal.implantes.area_articulacion);
                $('#checkNingunImplante').prop('checked', historia.antecedente_personal.implantes.ningun);   
                $('#textOtroImplante').val(historia.antecedente_personal.implantes.otro);

                $('#checkProblemaPlaquetario').prop('checked', historia.antecedente_personal.transtorno_sanguineo.plaquetario);
                $('#checkAnemias').prop('checked', historia.antecedente_personal.transtorno_sanguineo.anemia);
                $('#checkCoagulacionExcesiva').prop('checked', historia.antecedente_personal.transtorno_sanguineo.coagulacion_excesiva);
                $('#checkHemofilia').prop('checked', historia.antecedente_personal.transtorno_sanguineo.hemofilia);
                $('#checkTrombocitopenia').prop('checked', historia.antecedente_personal.transtorno_sanguineo.trombocitopenia);
                $('#checkTrombocitosis').prop('checked', historia.antecedente_personal.transtorno_sanguineo.trombocitosis);
                $('#textOtroTranstorno').val(historia.antecedente_personal.transtorno_sanguineo.otro);

                $('#checkEsquizofrenia').prop('checked', historia.antecedente_personal.enfermedad_mental.esquizofrenia);
                $('#checkBipolar').prop('checked', historia.antecedente_personal.enfermedad_mental.bipolar);
                $('#checkDemencia').prop('checked', historia.antecedente_personal.enfermedad_mental.demecia);
                $('#checkDepresivo').prop('checked', historia.antecedente_personal.enfermedad_mental.depresivo);
                $('#textMentalOtro').val(historia.antecedente_personal.enfermedad_mental.otro);

                $('#checkAnorexia').prop('checked', historia.antecedente_personal.transtorno_alimenticio.anorexia);
                $('#checkAtracon').prop('checked', historia.antecedente_personal.transtorno_alimenticio.atracon);
                $('#checkBulimia').prop('checked', historia.antecedente_personal.transtorno_alimenticio.bulimia);
                $('#checkAlimenticioNinguno').prop('checked', historia.antecedente_personal.transtorno_alimenticio.ninguna);
                $('#textOtroAlimenticio').val(historia.antecedente_personal.transtorno_alimenticio.otro);

                $('#checkClaustrofobia').prop('checked', historia.antecedente_personal.fobia.claustrofobia);
                $('#checkHidrofobia').prop('checked', historia.antecedente_personal.fobia.hidrofobia);
                $('#checkIatrofobia').prop('checked', historia.antecedente_personal.fobia.iatrofobia);
                $('#checkHefefobia').prop('checked', historia.antecedente_personal.fobia.hafefobia);
                $('#checkAlimenticioNinguno').prop('checked', historia.antecedente_personal.fobia.ninguna);
                $('#textFobiaOtra').val(historia.antecedente_personal.fobia.otro);

                $('input[name="habito_nro_comidas"][value="' + historia.habitos.nro_comida.conteo_comida + '"]').prop('checked', true);
                $('#textOtraComida').val(historia.habitos.nro_comida.otro_nro_comida);

                $('#checkDesayuno').prop('checked', historia.habitos.tiempo_entre_comida.princial_desayuno);
                $('#checkAlmuerzo').prop('checked', historia.habitos.tiempo_entre_comida.princial_almuerzo);
                $('#checkMerienda').prop('checked', historia.habitos.tiempo_entre_comida.princial_merienda);

                $('input[name="tiempo_refrigerio"][value="' + historia.habitos.tiempo_entre_comida.tiempo_entre_refrigerio + '"]').prop('checked', true);
                $('#textOtroTiempoRefrigerio').val(historia.habitos.tiempo_entre_comida.otro_tiempo_entre_refrigerio);

                $('#textNroVasosAgua').val(historia.habitos.consumo_agua.nro_vasos);

                $('#check' + (historia.habitos_toxicos.alcohol.consumo ? 'Si' : 'No') + 'Alcohol').prop('checked', true);
                $('#textFrecuenciaHoras').val(historia.habitos_toxicos.alcohol.frecuencia_horas);
                $('#textAlcoholFrecuenciaDias').val(historia.habitos_toxicos.alcohol.frecuencia_dias);
                $('#textAlcoholFrecuenciaSemanas').val(historia.habitos_toxicos.alcohol.frecuencia_semanas);
                $('#textUltimoConsumoAlcohol').val(historia.habitos_toxicos.alcohol.ultimo_consumo);

                $('#check' + (historia.habitos_toxicos.tabaco.consumo ? 'Si' : 'No') + 'Tabaco').prop('checked', true);
                $('#textTabacoFrecuenciaHoras').val(historia.habitos_toxicos.tabaco.frecuencia_horas);
                $('#textTabacoFrecuenciaDias').val(historia.habitos_toxicos.tabaco.frecuencia_dias);
                $('#textTabacoFrecuenciaSemanas').val(historia.habitos_toxicos.tabaco.frecuencia_semanas);
                $('#textTabacoNro').val(historia.habitos_toxicos.tabaco.nro_cajetillas);
                $('#textTabacoUltimoConsumo').val(historia.habitos_toxicos.tabaco.ultimo_consumo);

                $('#check' + (historia.habitos_toxicos.tabaco.consumo ? 'Si' : 'No') + 'Drogas').prop('checked', true);
                $('input[name="habito_drogas_consumo"][value="' + historia.habitos_toxicos.drogas.tipo_consumo + '"]').prop('checked', true);
                $('#textDrogasFrecuenciaHoras').val(historia.habitos_toxicos.drogas.frecuencia_horas);
                $('#textDrogasFrecuenciaDias').val(historia.habitos_toxicos.drogas.frecuencia_dias);
                $('#textDrogasFrecuenciaSemanas').val(historia.habitos_toxicos.drogas.frecuencia_semanas);
                $('#textDrogasUltimoConsumo').val(historia.habitos_toxicos.drogas.ultimo_consumo);

                $('#check' + (historia.actividad_personal.fisica.realizar ? 'Si' : 'No') + 'ActividadFisica').prop('checked', true);
                $('#textTipoActividad').val(historia.actividad_personal.fisica.tipo);
                $('#textActividadFrecuenciaMinutos').val(historia.actividad_personal.fisica.tiempo_minutos);
                $('#textActividadFrecuenciaHoras').val(historia.actividad_personal.fisica.tiempo_horas);
                $('input[name="frecuencia_actividad"][value="' + historia.actividad_personal.fisica.frecuencia + '"]').prop('checked', true);
                
                $('input[name="horas_descanso"][value="' + historia.actividad_personal.descanso.horas + '"]').prop('checked', true);

                $('#textMotivoConsulta').val(historia.motivo_consulta);
                $('#textEnfermedadActual').val(historia.enfermedad_actual);
                $('#textConsultaObservacion').val(historia.observacion);

                $('#check' + (historia.inspeccion.plano_antero_anterior.entrecejo ? 'Si' : 'No') + 'Entrecejo').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.punta_nariz ? 'Si' : 'No') + 'PuntaNariz').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.angulo_mentoniano ? 'Si' : 'No') + 'AnguloMentoniano').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.manubrio_esteral ? 'Si' : 'No') + 'ManubrioEsteral').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.apofisis_xifoides ? 'Si' : 'No') + 'ApofisisXifoides').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.ombligo ? 'Si' : 'No') + 'Ombligo').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.sinfisis_pubica ? 'Si' : 'No') + 'SinfisisPubica').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.centro_sustentacion ? 'Si' : 'No') + 'CentroSustentacion').prop('checked', true);

                $('#check' + (historia.inspeccion.plano_antero_anterior.altura_ojos ? 'Si' : 'No') + 'AlturaOjos').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.pabellones_auriculares ? 'Si' : 'No') + 'PabellonesAuriculares').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.altura_acromion ? 'Si' : 'No') + 'AlturaAcromion').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.pliegues_inframamarios ? 'Si' : 'No') + 'Inframamarios').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.espinas_iliacas ? 'Si' : 'No') + 'IliacasSuperiores').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.base_patela ? 'Si' : 'No') + 'BasePatela').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_anterior.maleolos_internos ? 'Si' : 'No') + 'MaleolosInternos').prop('checked', true);

                $('#check' + (historia.inspeccion.plano_antero_posterior.protuberancia_occipital ? 'Si' : 'No') + 'ProtuberanciaOccipital').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.apofisis_espinosas ? 'Si' : 'No') + 'ApofisisEspinosas').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.linea_interglutea ? 'Si' : 'No') + 'LineaInterglutea').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.centro_sustentacion ? 'Si' : 'No') + 'CentroSustentacion2').prop('checked', true);

                $('#check' + (historia.inspeccion.plano_antero_posterior.pabellones_auriculares ? 'Si' : 'No') + 'PabellonesAuriculares2').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.angulo_escapula ? 'Si' : 'No') + 'AnguloEscapula').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.espina_iliacas ? 'Si' : 'No') + 'EspinaIliacas').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.gluteo_inferior ? 'Si' : 'No') + 'GluteoInferior').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.pliegue_popliteo ? 'Si' : 'No') + 'PlieguePopliteo').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_antero_posterior.calcaneos ? 'Si' : 'No') + 'Calcaneos').prop('checked', true);

                $('#check' + (historia.inspeccion.plano_sagital_derecho.conducto_auditivo_derecho ? 'Si' : 'No') + 'ConductoAuditivoDerecho').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_sagital_derecho.acromion_derecho ? 'Si' : 'No') + 'AcromionDerecho').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_sagital_derecho.vertebras_derecho ? 'Si' : 'No') + 'VertebrasDerecho').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_sagital_derecho.trocante_derecho ? 'Si' : 'No') + 'TrocanterDerecho').prop('checked', true);
                $('#check' + (historia.inspeccion.plano_sagital_derecho.maleolo_derecho ? 'Si' : 'No') + 'MaleoloDerecho').prop('checked', true);

                $('#check' + (historia.inspeccion.planp_sagital_izquierdo.conducto_auditivo_izquierdo ? 'Si' : 'No') + 'ConductoAuditivoIzquierdo').prop('checked', true);
                $('#check' + (historia.inspeccion.planp_sagital_izquierdo.acromion_izquierdo ? 'Si' : 'No') + 'AcromionIzquierdo').prop('checked', true);
                $('#check' + (historia.inspeccion.planp_sagital_izquierdo.vertebras_izquierdo ? 'Si' : 'No') + 'VertebrasIzquierdo').prop('checked', true);
                $('#check' + (historia.inspeccion.planp_sagital_izquierdo.trocante_izquierdo ? 'Si' : 'No') + 'TrocanterIzquierdo').prop('checked', true);
                $('#check' + (historia.inspeccion.planp_sagital_izquierdo.maleolo_izquierdo ? 'Si' : 'No') + 'MaleoloIzquierdo').prop('checked', true);
                
                $('#textValoracionCamilla').val(historia.valoracion_camilla);
                $('#textPalpacion').val(historia.palpacion);
                $('#textAuscultacion').val(historia.auscultacion);
                $('#textPercusion').val(historia.percusion);

                $('#rangeDolorEVA').val(historia.escalas.eva);
                $('#emoji_id').text(historia.escalas.eva);

                $('input[name="daniels_seleccionar"][value="' + historia.escalas.daniels.calificacion + '"]').prop('checked', true);
                $('#textDanielsEspecificar').val(historia.escalas.daniels.especificar);

                $('#textHombroDerechoFlexion').val(historia.goniometria.hombro.flexion_derecha);
                $('#textHombroIzquierdoFlexion').val(historia.goniometria.hombro.flexion_izquierda);
                $('#textHombroDerechoExtension').val(historia.goniometria.hombro.extension_derecha);
                $('#textHombroIzquierdoExtension').val(historia.goniometria.hombro.extension_izquierda);
                $('#textHombroDerechoAbduccion').val(historia.goniometria.hombro.abduccion_derecha);
                $('#textHombroIzquierdoAbduccion').val(historia.goniometria.hombro.abduccion_izquierda);
                $('#textHombroDerechoAduccion').val(historia.goniometria.hombro.aduccion_derecha);
                $('#textHombroIzquierdoAduccion').val(historia.goniometria.hombro.aduccion_izquierda);
                $('#textHombroDerechoRotacionInterna').val(historia.goniometria.hombro.rotacion_interna_derecha);
                $('#textHombroIzquierdoRotacionInterna').val(historia.goniometria.hombro.rotacion_interna_izquierda);
                $('#textHombroDerechoRotacionExterna').val(historia.goniometria.hombro.rotacion_externa_derecha);
                $('#textHombroIzquierdoRotacionExterna').val(historia.goniometria.hombro.rotacion_externa_izquierda);

                $('#textCodoDerecholexion').val(historia.goniometria.codo.flexion_derecha);
                $('#textCodoIzquierdoFlexion').val(historia.goniometria.codo.flexion_izquierda);
                $('#textCodoDerechoExtension').val(historia.goniometria.codo.extension_derecha);
                $('#textCodoIzquierdoExtension').val(historia.goniometria.codo.extension_izquierda);
                $('#textCodoDerechoPronacion').val(historia.goniometria.codo.pronacion_derecha);
                $('#textCodoIzquierdoPronacion').val(historia.goniometria.codo.pronacion_izquierda);
                $('#textCodoDerechoSupinacion').val(historia.goniometria.codo.supinacion_derecha);
                $('#textCodoIzquierdoSupinacion').val(historia.goniometria.codo.supinacion_izquierda);

                $('#textMunecaDerecholexion').val(historia.goniometria.muneca.flexion_derecha);
                $('#textMunecaIzquierdoFlexion').val(historia.goniometria.muneca.flexion_izquierda);
                $('#textMunecaDerechoExtension').val(historia.goniometria.muneca.extension_derecha);
                $('#textMunecaIzquierdoExtension').val(historia.goniometria.muneca.extension_izquierda);
                $('#textMunecaDerechoRadial').val(historia.goniometria.muneca.rotacion_interna_derecha);
                $('#textMunecaIzquierdoRadial').val(historia.goniometria.muneca.rotacion_interna_izquierda);
                $('#textMunecaDerechoCubital').val(historia.goniometria.muneca.rotacion_externa_derecha);
                $('#textMunecaIzquierdoCubital').val(historia.goniometria.muneca.rotacion_externa_izquierda);

                $('#textCaderaDerechoFlexion').val(historia.goniometria.cadera.flexion_derecha);
                $('#textCaderaIzquierdoFlexion').val(historia.goniometria.cadera.flexion_izquierda);
                $('#textCaderaDerechoExtension').val(historia.goniometria.cadera.extension_derecha);
                $('#textCaderaIzquierdoExtension').val(historia.goniometria.cadera.extension_izquierda);
                $('#textCaderaDerechoAbduccion').val(historia.goniometria.cadera.abduccion_derecha);
                $('#textCaderaIzquierdoAbduccion').val(historia.goniometria.cadera.abduccion_izquierda);
                $('#textCaderaDerechoAduccion').val(historia.goniometria.cadera.aduccion_derecha);
                $('#textCaderaIzquierdoAduccion').val(historia.goniometria.cadera.aduccion_izquierda);
                $('#textCaderaDerechoRotacionInterna').val(historia.goniometria.cadera.rotacion_interna_derecha);
                $('#textCaderaIzquierdoRotacionInterna').val(historia.goniometria.cadera.rotacion_interna_izquierda);
                $('#textCaderaDerechoRotacionExterna').val(historia.goniometria.cadera.rotacion_externa_derecha);
                $('#textCaderaIzquierdoRotacionExterna').val(historia.goniometria.cadera.rotacion_externa_izquierda);

                $('#textRodillaDerechoFlexion').val(historia.goniometria.rodilla.flexion_derecha);
                $('#textRodillaIzquierdoFlexion').val(historia.goniometria.rodilla.flexion_izquierda);
                $('#textRodillaDerechoExtension').val(historia.goniometria.rodilla.extension_derecha);
                $('#textRodillaIzquierdoExtension').val(historia.goniometria.rodilla.extension_izquierda);
                $('#textRodillaDerechoRotacionInterna').val(historia.goniometria.rodilla.rotacion_interna_derecha);
                $('#textRodillaIzquierdoRotacionInterna').val(historia.goniometria.rodilla.rotacion_interna_izquierda);
                $('#textRodillaDerechoRotacionExterna').val(historia.goniometria.rodilla.rotacion_externa_derecha);
                $('#textRodillaIzquierdoRotacionExterna').val(historia.goniometria.rodilla.rotacion_externa_izquierda);

                $('#textTobilloDerechoFlexion').val(historia.goniometria.tobillo.flexion_derecha);
                $('#textTobilloIzquierdoFlexion').val(historia.goniometria.tobillo.flexion_izquierda);
                $('#textTobilloDerechoDorsiflexion').val(historia.goniometria.tobillo.dorsiflexion_derecha);
                $('#textTobilloIzquierdoDorsiflexion').val(historia.goniometria.tobillo.dorsiflexion_izquierda);
                $('#textTobilloDerechoInversion').val(historia.goniometria.tobillo.inversion_derecha);
                $('#textTobilloIzquierdoInversion').val(historia.goniometria.tobillo.inversion_izquierda);
                $('#textTobilloDerechoEversion').val(historia.goniometria.tobillo.eversion_derecha);
                $('#textTobilloIzquierdoEversion').val(historia.goniometria.tobillo.eversion_izquierda);

                console.log(historia.diagnostico_kinestico)
                $('#textDiagnosticoKinestico').val(historia.diagnostico_kinestico);
                $('#textObjetivoCorto').val(historia.objetivo_corto_plazo);
                $('#textObjetivoMediano').val(historia.objetivo_mediano_plazo);
                $('#textObjetivoLargo').val(historia.objetivo_largo_plazo);
                $('#textTratamiento').val(historia.tratamiento);

                
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



