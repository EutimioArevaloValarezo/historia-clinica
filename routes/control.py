import uuid
from db import db
from passlib.hash import pbkdf2_sha256

def obtener_usuario(cedula):
    usuario = db['usuario'].find_one({"cedula":cedula})
    return usuario

def crear_usuario(nombres, apellidos, cedula, contrasenia):
    usuario = {
        "_id": uuid.uuid4().hex,
        "nombres": nombres,
        "apellidos": apellidos,
        "cedula": cedula,
        "contrasenia": pbkdf2_sha256.encrypt(contrasenia)
    }
    return usuario


def guardar_historia_clinica(request):
    historia = {
        '_id': uuid.uuid4().hex,
        'historia_clinica': {
            'nro_expediente': request.form.get('num_expediente'),
            'cama_cubiculo': request.form.get('cama_cubiculo'),
            'fecha': request.form.get('fecha'),
            'hora': request.form.get('hora')
        },
        'registro_paciente': {
            'nombres': request.form.get('nombres'),
            'apellidos': request.form.get('apellidos'),
            'fecha_nacimiento': request.form.get('fecha_nacimiento'),
            'edad': request.form.get('edad'),
            'sexo': request.form.get('sexo'),
            'estado_civil': request.form.get('estado_civil'),
            'cedula': request.form.get('cedula'),
            'celular': request.form.get('celular'),
            'correo': request.form.get('correo'),
            'celular': request.form.get('celular'),
            'lugar_nacimiento': request.form.get('lugar_nacimiento'),
            'lugar_recidencia': request.form.get('lugar_recidencia'),
            'direccion_domicilio': request.form.get('direccion_domicilio'),
            'nivel_instruccion': request.form.get('nivel_instruccion'),
            'ocupacion': request.form.get('ocupacion'),
            'profesion': request.form.get('profesion'),
            'seguro_social': request.form.get('seguro_social'),
            'raza': request.form.get('raza'),
            'religion': request.form.get('religion')
        },
        'antecedente_heredofamiliar': {
            'congenita': {
                'padecimiento': bool(request.form.get('enfermedad_congenita')),
                'parentesco': request.form.get('congenita_parentesco'),
                'especificar': request.form.get('congenita_especificar')
            },
            'infecciosa': {
                'padecimiento': bool(request.form.get('enfermedad_infecciosa')),
                'parentesco': request.form.get('infecciosa_parentesco'),
                'especificar': request.form.get('infecciosa_especificar')
            },
            'metabolica': {
                'padecimiento': bool(request.form.get('enfermedad_metabolica')),
                'parentesco': request.form.get('metabolica_parentesco'),
                'especificar': request.form.get('metabolica_especificar')
            },
            'musculoesqueletico': {
                'padecimiento': bool(request.form.get('enfermedad_musculoesqueletico')),
                'parentesco': request.form.get('musculoesqueletico_parentesco'),
                'especificar': request.form.get('musculoesqueletico_especificar')
            },
            'cardiovascular': {
                'padecimiento': bool(request.form.get('enfermedad_cardiovascular')),
                'parentesco': request.form.get('cardiovascular_parentesco'),
                'especificar': request.form.get('cardiovascular_especificar')
            },
            'respiratoria': {
                'padecimiento': bool(request.form.get('enfermedad_respiratoria')),
                'parentesco': request.form.get('respiratoria_parentesco'),
                'especificar': request.form.get('respiratoria_especificar')
            },
            'oncologica': {
                'padecimiento': bool(request.form.get('enfermedad_oncologica')),
                'parentesco': request.form.get('oncologica_parentesco'),
                'especificar': request.form.get('oncologica_especificar')
            },
            'otra': {
                'padecimiento': bool(request.form.get('enfermedad_otra')),
                'parentesco': request.form.get('otra_parentesco'),
                'especificar': request.form.get('otra_especificar')
            }
        },
        'antecedente_personal': {
            'alergia': {
                'asma': True if request.form.get('alergia_asma') else False,
                'rinitis': True if request.form.get('alergia_rinitis') else False,
                'conjuntivitis': True if request.form.get('alergia_conjuntivitis') else False,
                'alimentos': True if request.form.get('alergia_alimentos') else False,
                'medicamentos': True if request.form.get('alergia_medicamentos') else False,
                'latex': True if request.form.get('alergia_latex') else False,
                'ninguna': True if request.form.get('alergia_ninguna') else False,
                'otra': request.form.get('alergia_otra') 
            },
            'enfermedad_dermatologica':{
                'dermatitis_atopica': True if request.form.get('ed_dermatitis_atopica') else False,
                'acne': True if request.form.get('ed_acne') else False,
                'urticaria': True if request.form.get('ed_urticaria') else False,
                'vitiligo': True if request.form.get('ed_vitiligo') else False,
                'queratosis': True if request.form.get('ed_queratosis') else False,
                'sarna': True if request.form.get('ed_sarna') else False,
                'pie_atleta': True if request.form.get('ed_pie_atleta') else False,
                'hongos': True if request.form.get('ed_hongos') else False,
                'ninguna': True if request.form.get('ed_ninguna') else False,
                'otra': request.form.get('ed_otra') 
            },
            'quirurgico':{
                'tiene_cirugia': bool(request.form.get('tiene_cirugia')),
                'area_cirugia': request.form.get('area_cirugia'),
                'motivo_cirugia': request.form.get('motivo_cirugia')
            },
            'farmaco':{
                'nombre': request.form.get('nombre_farmaco'),
                'tiene_farmaco': bool(request.form.get('tiene_farmaco')),
                'anticoncepcion': request.form.get('farmaco_anticoceptivo'),
                'otro_motivo': request.form.get('farmaco_otro_motivo'),
                'frecuencia': request.form.get('farmaco_frecuencia'),
                'dosificacion': request.form.get('farmaco_dosificacion')
            },
            'implantes':{
                'diu': True if request.form.get('implante_diu') else False,
                'mamoplastia': True if request.form.get('implante_mamoplastia') else False,
                'articulacion': True if request.form.get('implante_articulacion') else False,
                'area_articulacion': request.form.get('area_articulacion'),
                'ningun': True if request.form.get('ningun_implante') else False,
                'otro': request.form.get('otro_implante')
            },
            'transtorno_sanguineo':{
                'plaquetario':  True if request.form.get('transtorno_plaquetas') else False,
                'anemia': True if request.form.get('transtorno_anemia') else False,
                'coagulacion_excesiva': True if request.form.get('transtorno_coagulacion') else False,
                'hemofilia': True if request.form.get('transtorno_hemofilia') else False,
                'trombocitopenia': True if request.form.get('transtorno_trombocitopenia') else False,
                'trombocitosis': True if request.form.get('transtorno_trombocitosis') else False,
                'otro': request.form.get('transtorno_otro')
            },
            'enfermedad_mental': {
                'esquizofrenia':True if request.form.get('mental_esquizofrenia') else False,
                'bipolar':True if request.form.get('mental_bipolar') else False,
                'demecia':True if request.form.get('mental_demencia') else False,
                'depresivo':True if request.form.get('mental_depresivo') else False,
                'otro':request.form.get('mental_otra')
            },
            'transtorno_alimenticio':{
                'anorexia': True if request.form.get('transtorno_anorexia') else False,
                'atracon':True if request.form.get('transtorno_atracon') else False,
                'bulimia':True if request.form.get('transtorno_bulimia') else False,
                'ninguna':True if request.form.get('transtorno_alimenticio_ningun') else False,
                'otro': request.form.get('transtorno_alimenticio_otro')
            },
            'fobia': {
                'claustrofobia': True if request.form.get('fobia_claustrofobia') else False,
                'hidrofobia':True if request.form.get('fobia_hidrofobia') else False,
                'iatrofobia':True if request.form.get('fobia_iatrofobia') else False,
                'hafefobia':True if request.form.get('fobia_hafefobia') else False,
                'ninguna':True if request.form.get('fobia_ninguna') else False,
                'otro': request.form.get('fobia_otra')
            }
        },
        'habitos':{
            'nro_comida': { 
                'conteo_comida': request.form.get('habito_nro_comidas'),
                'otro_nro_comida': request.form.get('habito_otro_nro_comidas')
            },
            'tiempo_entre_comida': {
                'princial_desayuno': True if request.form.get('comida_desayuno') else False,
                'princial_almuerzo': True if request.form.get('comida_almuerzo') else False,
                'princial_merienda': True if request.form.get('comida_merienda') else False,
                'tiempo_entre_refrigerio': request.form.get('tiempo_refrigerio'),
                'otro_tiempo_entre_refrigerio': request.form.get('otro_tiempo_refrigerio')
            },
            'consumo_agua':{
                'nro_vasos': request.form.get('nro_vasos_agua') 
            }
        },
        'habitos_toxicos':{
            'alcohol':{
                'consumo': bool(request.form.get('habito_toxico_alcohol')),
                'frecuencia_horas': request.form.get('habito_alcohol_horas'),
                'frecuencia_dias': request.form.get('habito_alcohol_dias'),
                'frecuencia_semanas': request.form.get('habito_alcohol_semanas'),
                'ultimo_consumo': request.form.get('habito_alcohol_ultimo_consumo')
            },
            'tabaco': {
                'consumo': bool(request.form.get('habito_toxico_tabaco')),
                'frecuencia_horas': request.form.get('habito_tabaco_horas'),
                'frecuencia_dias': request.form.get('habito_tabaco_dias'),
                'frecuencia_semanas': request.form.get('habito_tabaco_semanas'),
                'nro_cajetillas': request.form.get('habito_tabaco_nro'),
                'ultimo_consumo': request.form.get('habito_tabaco_ultimo_consumo'),
            },
            'drogas':{
                'consumo': bool(request.form.get('habito_toxico_drogas')),
                'tipo_consumo': request.form.get('habito_drogas_consumo'),
                'frecuencia_horas': request.form.get('habito_drogas_horas'),
                'frecuencia_dias': request.form.get('habito_drogas_dias'),
                'frecuencia_semanas': request.form.get('habito_drogas_semanas'),
                'ultimo_consumo': request.form.get('habito_drogas_ultimo_consumo'),
            }
        },
        'actividad_personal':{
            'fisica': {
                'realizar': bool(request.form.get('habito_toxico_drogas')),
                'tipo': request.form.get('actividad_tipo'),
                'tiempo_minutos': request.form.get('actividad_minutos'),
                'tiempo_horas': request.form.get('actividad_horas'),
                'frecuencia': request.form.get('actividad_horas'),
            },
            'descanso': {
                'horas': request.form.get('horas_descanso'),
            }
        },
        'motivo_consulta': request.form.get('motivo_consulta'),
        'enfermedad_actual': request.form.get('enfermedad_actual'),
        'observacion': request.form.get('consulta_observacion'),
        'inspeccion': {
            'panto_antero_anterior': {
                'entrecejo': bool(request.form.get('inspeccion_entrecejo')),
                'punta_nariz': bool(request.form.get('inspeccion_punta_nariz')),
                'angulo_mentoniano': bool(request.form.get('inspeccion_angulo_mentoniano')),
                'manubrio_esteral': bool(request.form.get('inspeccion_manubrio_esteral')),
                'apofisis_xifoides': bool(request.form.get('inspeccion_apofisis_xifoides')),
                'ombligo': bool(request.form.get('inspeccion_ombligo')),
                'sinfisis_pubica': bool(request.form.get('inspeccion_sinfisis_pubica')),
                'centro_sustentacion': bool(request.form.get('inspeccion_centro_sustentacion')),
                'altura_ojos': bool(request.form.get('inspeccion_altura_ojos')),
                'pabellones_auriculares': bool(request.form.get('inspeccion_pabellones_auriculares')),
                'altura_acromion': bool(request.form.get('inspeccion_altura_acromion')),
                'pliegues_inframamarios': bool(request.form.get('inspeccion_inframamarios')),
                'espinas_iliacas': bool(request.form.get('inspeccion_iliacas_superiores')),
                'base_patela': bool(request.form.get('inspeccion_base_patela')),
                'maleolos_internos': bool(request.form.get('inspeccion_maleolos_internos')),
            },
            'plano_antero_posterior':{
                'protuberancia_occipital': bool(request.form.get('inspeccion_protuberancia_occipital')),
                'apofisis_espinosas': bool(request.form.get('inspeccion_apofisis_espinosas')),
                'linea_interglutea': bool(request.form.get('inspeccion_linea_interglutea')),
                'centro_sustentacion': bool(request.form.get('inspeccion_centro_sustentacion_2')),
                'pabellones_auriculares': bool(request.form.get('inspeccion_pabellones_auriculares_2')),
                'angulo_escapula': bool(request.form.get('inspeccion_angulo_escapula')),
                'espina_iliacas': bool(request.form.get('inspeccion_espina_iliacas')),
                'gluteo_inferior': bool(request.form.get('inspeccion_gluteo_inferior')),
                'pliegue_popliteo': bool(request.form.get('inspeccion_pliegue_popliteo')),
                'calcaneos': bool(request.form.get('inspeccion_calcaneos'))
            },
            'plano_sagital_derecho':{
                'conducto_auditivo_derecho': bool(request.form.get('inspeccion_conducto_auditivo_derecho')),
                'acromion_derecho': bool(request.form.get('inspeccion_acromion_derecho')),
                'vertebras_derecho': bool(request.form.get('inspeccion_vertebras_derecho')),
                'trocante_derecho': bool(request.form.get('inspeccion_trocante_derecho')),
                'maleolo_derecho': bool(request.form.get('inspeccion_maleolo_derecho')),    
            },
            'planp_sagital_izquierdo':{
                'conducto_auditivo_izquierdo': bool(request.form.get('inspeccion_conducto_auditivo_izquierdo')),
                'acromion_izquierdo': bool(request.form.get('inspeccion_acromion_izquierdo')),
                'vertebras_izquierdo': bool(request.form.get('inspeccion_vertebras_izquierdo')),
                'trocante_izquierdo': bool(request.form.get('inspeccion_trocante_izquierdo')),
                'maleolo_izquierdo': bool(request.form.get('inspeccion_maleolo_izquierdo')),   
            }
        },
        'valoracion_camilla': request.form.get('valoracion_camilla'),
        'palpacion': request.form.get('palpacion'),
        'auscultacion': request.form.get('auscultacion'),
        'percusion': request.form.get('percusion'),
        'escalas':{
            'eva': request.form.get('escala_dolor_eva'),
            'daniels': {
                'calificacion': request.form.get('daniels_seleccionar'), 
                'especificar': request.form.get('daniels_especificar')
            },
        },
        'goniometria': {
            'hombro':{
                'flexion_derecha': request.form.get('hombro_flexion_derecha'),
                'flexion_izquierda': request.form.get('hombro_flexion_izquierda'),
                'extension_derecha': request.form.get('hombro_extension_derecha'),
                'extension_izquierda': request.form.get('hombro_extension_izquierda'),
                'abduccion_derecha': request.form.get('hombro_abduccion_derecha'),
                'abduccion_izquierda': request.form.get('hombro_abduccion_izquierda'),
                'aduccion_derecha': request.form.get('hombro_aduccion_derecha'),
                'aduccion_izquierda': request.form.get('hombro_aduccion_izquierda'),
                'rotacion_interna_derecha': request.form.get('hombro_rotacion_interna_derecha'),
                'rotacion_interna_izquierda': request.form.get('hombro_rotacion_interna_izquierda'),
                'rotacion_externa_derecha': request.form.get('hombro_rotacion_externa_derecha'),
                'rotacion_externa_izquierda': request.form.get('hombro_rotacion_externa_izquierda'),
            },
            'codo':{
                'flexion_derecha': request.form.get('codo_flexion_derecha'),
                'flexion_izquierda': request.form.get('codo_flexion_izquierda'),
                'extension_derecha': request.form.get('codo_extension_derecha'),
                'extension_izquierda': request.form.get('codo_extension_izquierda'),
                'pronacion_derecha': request.form.get('codo_pronacion_derecha'),
                'pronacion_izquierda': request.form.get('codo_pronacion_izquierda'),
                'supinacion_derecha': request.form.get('codo_supinacion_derecha'),
                'supinacion_izquierda': request.form.get('codo_supinacion_izquierda')
            },
            'muneca':{
                'flexion_derecha': request.form.get('muneca_flexion_derecha'),
                'flexion_izquierda': request.form.get('muneca_flexion_izquierda'),
                'extension_derecha': request.form.get('muneca_extension_derecha'),
                'extension_izquierda': request.form.get('muneca_extension_izquierda'),
                'radial_derecha': request.form.get('muneca_radial_derecha'),
                'radial_izquierda': request.form.get('muneca_radial_izquierda'),
                'cubital_derecha': request.form.get('muneca_cubital_derecha'),
                'cubital_izquierda': request.form.get('muneca_cubital_izquierda')
            },
            'cadera':{
                'flexion_derecha': request.form.get('cadera_flexion_derecha'),
                'flexion_izquierda': request.form.get('cadera_flexion_izquierda'),
                'extension_derecha': request.form.get('cadera_extension_derecha'),
                'extension_izquierda': request.form.get('cadera_extension_izquierda'),
                'abduccion_derecha': request.form.get('cadera_abduccion_derecha'),
                'abduccion_izquierda': request.form.get('cadera_abduccion_izquierda'),
                'aduccion_derecha': request.form.get('cadera_aduccion_derecha'),
                'aduccion_izquierda': request.form.get('cadera_aduccion_izquierda'),
                'rotacion_interna_derecha': request.form.get('cadera_rotacion_interna_derecha'),
                'rotacion_interna_izquierda': request.form.get('cadera_rotacion_interna_izquierda'),
                'rotacion_externa_derecha': request.form.get('cadera_rotacion_externa_derecha'),
                'rotacion_externa_izquierda': request.form.get('cadera_rotacion_externa_izquierda'),
            },
            'rodilla':{
                'flexion_derecha': request.form.get('rodilla_flexion_derecha'),
                'flexion_izquierda': request.form.get('rodilla_flexion_izquierda'),
                'extension_derecha': request.form.get('rodilla_extension_derecha'),
                'extension_izquierda': request.form.get('rodilla_extension_izquierda'),
                'rotacion_interna_derecha': request.form.get('rodilla_rotacion_interna_derecha'),
                'rotacion_interna_izquierda': request.form.get('rodilla_rotacion_interna_izquierda'),
                'rotacion_externa_derecha': request.form.get('rodilla_rotacion_externa_derecha'),
                'rotacion_externa_izquierda': request.form.get('rodilla_rotacion_externa_izquierda')
            },
            'tobillo':{
                'flexion_derecha': request.form.get('tobillo_flexion_derecha'),
                'flexion_izquierda': request.form.get('tobilla_flexion_izquierda'),
                'dorsiflexion_derecha': request.form.get('tobillo_dorsiflexion_derecha'),
                'dorsiflexion_izquierda': request.form.get('tobillo_dorsiflexion_izquierda'),
                'inversion_derecha': request.form.get('tobillo_inversion_derecha'),
                'inversion_izquierda': request.form.get('tobillo_inversion_izquierda'),
                'eversion_derecha': request.form.get('tobillo_eversion_derecha'),
                'eversion_izquierda': request.form.get('tobillo_eversion_izquierda')
            }
        },
        'diagnostico_kinestico': request.form.get('diagnostico_kinestico'),
        'objetivo_corto_plazo': request.form.get('objetivo_corto_plazo'),
        'objetivo_mediano_plazo': request.form.get('objetivo_mediano_plazo'),
        'objetivo_largo_plazo': request.form.get('objetivo_largo_plazo'),
        'tratamiento': request.form.get('tratamiento'),
        
    }  
    db['historia'].insert_one(historia)
    
def editar_historia_clinica(request, id_historia):
    update_historia = {
        'historia_clinica': {
            'nro_expediente': request.form.get('num_expediente'),
            'cama_cubiculo': request.form.get('cama_cubiculo'),
            'fecha': request.form.get('fecha'),
            'hora': request.form.get('hora')
        },
        'registro_paciente': {
            'nombres': request.form.get('nombres'),
            'apellidos': request.form.get('apellidos'),
            'fecha_nacimiento': request.form.get('fecha_nacimiento'),
            'edad': request.form.get('edad'),
            'sexo': request.form.get('sexo'),
            'estado_civil': request.form.get('estado_civil'),
            'cedula': request.form.get('cedula'),
            'celular': request.form.get('celular'),
            'correo': request.form.get('correo'),
            'celular': request.form.get('celular'),
            'lugar_nacimiento': request.form.get('lugar_nacimiento'),
            'lugar_recidencia': request.form.get('lugar_recidencia'),
            'direccion_domicilio': request.form.get('direccion_domicilio'),
            'nivel_instruccion': request.form.get('nivel_instruccion'),
            'ocupacion': request.form.get('ocupacion'),
            'profesion': request.form.get('profesion'),
            'seguro_social': request.form.get('seguro_social'),
            'raza': request.form.get('raza'),
            'religion': request.form.get('religion')
        },
        'antecedente_heredofamiliar': {
            'congenita': {
                'padecimiento': bool(request.form.get('enfermedad_congenita')),
                'parentesco': request.form.get('congenita_parentesco'),
                'especificar': request.form.get('congenita_especificar')
            },
            'infecciosa': {
                'padecimiento': bool(request.form.get('enfermedad_infecciosa')),
                'parentesco': request.form.get('infecciosa_parentesco'),
                'especificar': request.form.get('infecciosa_especificar')
            },
            'metabolica': {
                'padecimiento': bool(request.form.get('enfermedad_metabolica')),
                'parentesco': request.form.get('metabolica_parentesco'),
                'especificar': request.form.get('metabolica_especificar')
            },
            'musculoesqueletico': {
                'padecimiento': bool(request.form.get('enfermedad_musculoesqueletico')),
                'parentesco': request.form.get('musculoesqueletico_parentesco'),
                'especificar': request.form.get('musculoesqueletico_especificar')
            },
            'cardiovascular': {
                'padecimiento': bool(request.form.get('enfermedad_cardiovascular')),
                'parentesco': request.form.get('cardiovascular_parentesco'),
                'especificar': request.form.get('cardiovascular_especificar')
            },
            'respiratoria': {
                'padecimiento': bool(request.form.get('enfermedad_respiratoria')),
                'parentesco': request.form.get('respiratoria_parentesco'),
                'especificar': request.form.get('respiratoria_especificar')
            },
            'oncologica': {
                'padecimiento': bool(request.form.get('enfermedad_oncologica')),
                'parentesco': request.form.get('oncologica_parentesco'),
                'especificar': request.form.get('oncologica_especificar')
            },
            'otra': {
                'padecimiento': bool(request.form.get('enfermedad_otra')),
                'parentesco': request.form.get('otra_parentesco'),
                'especificar': request.form.get('otra_especificar')
            }
        },
        'antecedente_personal': {
            'alergia': {
                'asma': True if request.form.get('alergia_asma') else False,
                'rinitis': True if request.form.get('alergia_rinitis') else False,
                'conjuntivitis': True if request.form.get('alergia_conjuntivitis') else False,
                'alimentos': True if request.form.get('alergia_alimentos') else False,
                'medicamentos': True if request.form.get('alergia_medicamentos') else False,
                'latex': True if request.form.get('alergia_latex') else False,
                'ninguna': True if request.form.get('alergia_ninguna') else False,
                'otra': request.form.get('alergia_otra') 
            },
            'enfermedad_dermatologica':{
                'dermatitis_atopica': True if request.form.get('ed_dermatitis_atopica') else False,
                'acne': True if request.form.get('ed_acne') else False,
                'urticaria': True if request.form.get('ed_urticaria') else False,
                'vitiligo': True if request.form.get('ed_vitiligo') else False,
                'queratosis': True if request.form.get('ed_queratosis') else False,
                'sarna': True if request.form.get('ed_sarna') else False,
                'pie_atleta': True if request.form.get('ed_pie_atleta') else False,
                'hongos': True if request.form.get('ed_hongos') else False,
                'ninguna': True if request.form.get('ed_ninguna') else False,
                'otra': request.form.get('ed_otra') 
            },
            'quirurgico':{
                'tiene_cirugia': bool(request.form.get('tiene_cirugia')),
                'area_cirugia': request.form.get('area_cirugia'),
                'motivo_cirugia': request.form.get('motivo_cirugia')
            },
            'farmaco':{
                'nombre': request.form.get('nombre_farmaco'),
                'tiene_farmaco': bool(request.form.get('tiene_farmaco')),
                'anticoncepcion': request.form.get('farmaco_anticoceptivo'),
                'otro_motivo': request.form.get('farmaco_otro_motivo'),
                'frecuencia': request.form.get('farmaco_frecuencia'),
                'dosificacion': request.form.get('farmaco_dosificacion')
            },
            'implantes':{
                'diu': True if request.form.get('implante_diu') else False,
                'mamoplastia': True if request.form.get('implante_mamoplastia') else False,
                'articulacion': True if request.form.get('implante_articulacion') else False,
                'area_articulacion': request.form.get('area_articulacion'),
                'ningun': True if request.form.get('ningun_implante') else False,
                'otro': request.form.get('otro_implante')
            },
            'transtorno_sanguineo':{
                'plaquetario':  True if request.form.get('transtorno_plaquetas') else False,
                'anemia': True if request.form.get('transtorno_anemia') else False,
                'coagulacion_excesiva': True if request.form.get('transtorno_coagulacion') else False,
                'hemofilia': True if request.form.get('transtorno_hemofilia') else False,
                'trombocitopenia': True if request.form.get('transtorno_trombocitopenia') else False,
                'trombocitosis': True if request.form.get('transtorno_trombocitosis') else False,
                'otro': request.form.get('transtorno_otro')
            },
            'enfermedad_mental': {
                'esquizofrenia':True if request.form.get('mental_esquizofrenia') else False,
                'bipolar':True if request.form.get('mental_bipolar') else False,
                'demecia':True if request.form.get('mental_demencia') else False,
                'depresivo':True if request.form.get('mental_depresivo') else False,
                'otro':request.form.get('mental_otra')
            },
            'transtorno_alimenticio':{
                'anorexia': True if request.form.get('transtorno_anorexia') else False,
                'atracon':True if request.form.get('transtorno_atracon') else False,
                'bulimia':True if request.form.get('transtorno_bulimia') else False,
                'ninguna':True if request.form.get('transtorno_alimenticio_ningun') else False,
                'otro': request.form.get('transtorno_alimenticio_otro')
            },
            'fobia': {
                'claustrofobia': True if request.form.get('fobia_claustrofobia') else False,
                'hidrofobia':True if request.form.get('fobia_hidrofobia') else False,
                'iatrofobia':True if request.form.get('fobia_iatrofobia') else False,
                'hafefobia':True if request.form.get('fobia_hafefobia') else False,
                'ninguna':True if request.form.get('fobia_ninguna') else False,
                'otro': request.form.get('fobia_otra')
            }
        },
        'habitos':{
            'nro_comida': { 
                'conteo_comida': request.form.get('habito_nro_comidas'),
                'otro_nro_comida': request.form.get('habito_otro_nro_comidas')
            },
            'tiempo_entre_comida': {
                'princial_desayuno': True if request.form.get('comida_desayuno') else False,
                'princial_almuerzo': True if request.form.get('comida_almuerzo') else False,
                'princial_merienda': True if request.form.get('comida_merienda') else False,
                'tiempo_entre_refrigerio': request.form.get('tiempo_refrigerio'),
                'otro_tiempo_entre_refrigerio': request.form.get('otro_tiempo_refrigerio')
            },
            'consumo_agua':{
                'nro_vasos': request.form.get('nro_vasos_agua') 
            }
        },
        'habitos_toxicos':{
            'alcohol':{
                'consumo': bool(request.form.get('habito_toxico_alcohol')),
                'frecuencia_horas': request.form.get('habito_alcohol_horas'),
                'frecuencia_dias': request.form.get('habito_alcohol_dias'),
                'frecuencia_semanas': request.form.get('habito_alcohol_semanas'),
                'ultimo_consumo': request.form.get('habito_alcohol_ultimo_consumo')
            },
            'tabaco': {
                'consumo': bool(request.form.get('habito_toxico_tabaco')),
                'frecuencia_horas': request.form.get('habito_tabaco_horas'),
                'frecuencia_dias': request.form.get('habito_tabaco_dias'),
                'frecuencia_semanas': request.form.get('habito_tabaco_semanas'),
                'nro_cajetillas': request.form.get('habito_tabaco_nro'),
                'ultimo_consumo': request.form.get('habito_tabaco_ultimo_consumo'),
            },
            'drogas':{
                'consumo': bool(request.form.get('habito_toxico_drogas')),
                'tipo_consumo': request.form.get('habito_drogas_consumo'),
                'frecuencia_horas': request.form.get('habito_drogas_horas'),
                'frecuencia_dias': request.form.get('habito_drogas_dias'),
                'frecuencia_semanas': request.form.get('habito_drogas_semanas'),
                'ultimo_consumo': request.form.get('habito_drogas_ultimo_consumo'),
            }
        },
        'actividad_personal':{
            'fisica': {
                'realizar': bool(request.form.get('habito_toxico_drogas')),
                'tipo': request.form.get('actividad_tipo'),
                'tiempo_minutos': request.form.get('actividad_minutos'),
                'tiempo_horas': request.form.get('actividad_horas'),
                'frecuencia': request.form.get('actividad_horas'),
            },
            'descanso': {
                'horas': request.form.get('horas_descanso'),
            }
        },
        'motivo_consulta': request.form.get('motivo_consulta'),
        'enfermedad_actual': request.form.get('enfermedad_actual'),
        'observacion': request.form.get('consulta_observacion'),
        'inspeccion': {
            'panto_antero_anterior': {
                'entrecejo': bool(request.form.get('inspeccion_entrecejo')),
                'punta_nariz': bool(request.form.get('inspeccion_punta_nariz')),
                'angulo_mentoniano': bool(request.form.get('inspeccion_angulo_mentoniano')),
                'manubrio_esteral': bool(request.form.get('inspeccion_manubrio_esteral')),
                'apofisis_xifoides': bool(request.form.get('inspeccion_apofisis_xifoides')),
                'ombligo': bool(request.form.get('inspeccion_ombligo')),
                'sinfisis_pubica': bool(request.form.get('inspeccion_sinfisis_pubica')),
                'centro_sustentacion': bool(request.form.get('inspeccion_centro_sustentacion')),
                'altura_ojos': bool(request.form.get('inspeccion_altura_ojos')),
                'pabellones_auriculares': bool(request.form.get('inspeccion_pabellones_auriculares')),
                'altura_acromion': bool(request.form.get('inspeccion_altura_acromion')),
                'pliegues_inframamarios': bool(request.form.get('inspeccion_inframamarios')),
                'espinas_iliacas': bool(request.form.get('inspeccion_iliacas_superiores')),
                'base_patela': bool(request.form.get('inspeccion_base_patela')),
                'maleolos_internos': bool(request.form.get('inspeccion_maleolos_internos')),
            },
            'plano_antero_posterior':{
                'protuberancia_occipital': bool(request.form.get('inspeccion_protuberancia_occipital')),
                'apofisis_espinosas': bool(request.form.get('inspeccion_apofisis_espinosas')),
                'linea_interglutea': bool(request.form.get('inspeccion_linea_interglutea')),
                'centro_sustentacion': bool(request.form.get('inspeccion_centro_sustentacion_2')),
                'pabellones_auriculares': bool(request.form.get('inspeccion_pabellones_auriculares_2')),
                'angulo_escapula': bool(request.form.get('inspeccion_angulo_escapula')),
                'espina_iliacas': bool(request.form.get('inspeccion_espina_iliacas')),
                'gluteo_inferior': bool(request.form.get('inspeccion_gluteo_inferior')),
                'pliegue_popliteo': bool(request.form.get('inspeccion_pliegue_popliteo')),
                'calcaneos': bool(request.form.get('inspeccion_calcaneos'))
            },
            'plano_sagital_derecho':{
                'conducto_auditivo_derecho': bool(request.form.get('inspeccion_conducto_auditivo_derecho')),
                'acromion_derecho': bool(request.form.get('inspeccion_acromion_derecho')),
                'vertebras_derecho': bool(request.form.get('inspeccion_vertebras_derecho')),
                'trocante_derecho': bool(request.form.get('inspeccion_trocante_derecho')),
                'maleolo_derecho': bool(request.form.get('inspeccion_maleolo_derecho')),    
            },
            'planp_sagital_izquierdo':{
                'conducto_auditivo_izquierdo': bool(request.form.get('inspeccion_conducto_auditivo_izquierdo')),
                'acromion_izquierdo': bool(request.form.get('inspeccion_acromion_izquierdo')),
                'vertebras_izquierdo': bool(request.form.get('inspeccion_vertebras_izquierdo')),
                'trocante_izquierdo': bool(request.form.get('inspeccion_trocante_izquierdo')),
                'maleolo_izquierdo': bool(request.form.get('inspeccion_maleolo_izquierdo')),   
            }
        },
        'valoracion_camilla': request.form.get('valoracion_camilla'),
        'palpacion': request.form.get('palpacion'),
        'auscultacion': request.form.get('auscultacion'),
        'percusion': request.form.get('percusion'),
        'escalas':{
            'eva': request.form.get('escala_dolor_eva'),
            'daniels': {
                'calificacion': request.form.get('daniels_seleccionar'), 
                'especificar': request.form.get('daniels_especificar')
            },
        },
        'goniometria': {
            'hombro':{
                'flexion_derecha': request.form.get('hombro_flexion_derecha'),
                'flexion_izquierda': request.form.get('hombro_flexion_izquierda'),
                'extension_derecha': request.form.get('hombro_extension_derecha'),
                'extension_izquierda': request.form.get('hombro_extension_izquierda'),
                'abduccion_derecha': request.form.get('hombro_abduccion_derecha'),
                'abduccion_izquierda': request.form.get('hombro_abduccion_izquierda'),
                'aduccion_derecha': request.form.get('hombro_aduccion_derecha'),
                'aduccion_izquierda': request.form.get('hombro_aduccion_izquierda'),
                'rotacion_interna_derecha': request.form.get('hombro_rotacion_interna_derecha'),
                'rotacion_interna_izquierda': request.form.get('hombro_rotacion_interna_izquierda'),
                'rotacion_externa_derecha': request.form.get('hombro_rotacion_externa_derecha'),
                'rotacion_externa_izquierda': request.form.get('hombro_rotacion_externa_izquierda'),
            },
            'codo':{
                'flexion_derecha': request.form.get('codo_flexion_derecha'),
                'flexion_izquierda': request.form.get('codo_flexion_izquierda'),
                'extension_derecha': request.form.get('codo_extension_derecha'),
                'extension_izquierda': request.form.get('codo_extension_izquierda'),
                'pronacion_derecha': request.form.get('codo_pronacion_derecha'),
                'pronacion_izquierda': request.form.get('codo_pronacion_izquierda'),
                'supinacion_derecha': request.form.get('codo_supinacion_derecha'),
                'supinacion_izquierda': request.form.get('codo_supinacion_izquierda')
            },
            'muneca':{
                'flexion_derecha': request.form.get('muneca_flexion_derecha'),
                'flexion_izquierda': request.form.get('muneca_flexion_izquierda'),
                'extension_derecha': request.form.get('muneca_extension_derecha'),
                'extension_izquierda': request.form.get('muneca_extension_izquierda'),
                'radial_derecha': request.form.get('muneca_radial_derecha'),
                'radial_izquierda': request.form.get('muneca_radial_izquierda'),
                'cubital_derecha': request.form.get('muneca_cubital_derecha'),
                'cubital_izquierda': request.form.get('muneca_cubital_izquierda')
            },
            'cadera':{
                'flexion_derecha': request.form.get('cadera_flexion_derecha'),
                'flexion_izquierda': request.form.get('cadera_flexion_izquierda'),
                'extension_derecha': request.form.get('cadera_extension_derecha'),
                'extension_izquierda': request.form.get('cadera_extension_izquierda'),
                'abduccion_derecha': request.form.get('cadera_abduccion_derecha'),
                'abduccion_izquierda': request.form.get('cadera_abduccion_izquierda'),
                'aduccion_derecha': request.form.get('cadera_aduccion_derecha'),
                'aduccion_izquierda': request.form.get('cadera_aduccion_izquierda'),
                'rotacion_interna_derecha': request.form.get('cadera_rotacion_interna_derecha'),
                'rotacion_interna_izquierda': request.form.get('cadera_rotacion_interna_izquierda'),
                'rotacion_externa_derecha': request.form.get('cadera_rotacion_externa_derecha'),
                'rotacion_externa_izquierda': request.form.get('cadera_rotacion_externa_izquierda'),
            },
            'rodilla':{
                'flexion_derecha': request.form.get('rodilla_flexion_derecha'),
                'flexion_izquierda': request.form.get('rodilla_flexion_izquierda'),
                'extension_derecha': request.form.get('rodilla_extension_derecha'),
                'extension_izquierda': request.form.get('rodilla_extension_izquierda'),
                'rotacion_interna_derecha': request.form.get('rodilla_rotacion_interna_derecha'),
                'rotacion_interna_izquierda': request.form.get('rodilla_rotacion_interna_izquierda'),
                'rotacion_externa_derecha': request.form.get('rodilla_rotacion_externa_derecha'),
                'rotacion_externa_izquierda': request.form.get('rodilla_rotacion_externa_izquierda')
            },
            'tobillo':{
                'flexion_derecha': request.form.get('tobillo_flexion_derecha'),
                'flexion_izquierda': request.form.get('tobilla_flexion_izquierda'),
                'dorsiflexion_derecha': request.form.get('tobillo_dorsiflexion_derecha'),
                'dorsiflexion_izquierda': request.form.get('tobillo_dorsiflexion_izquierda'),
                'inversion_derecha': request.form.get('tobillo_inversion_derecha'),
                'inversion_izquierda': request.form.get('tobillo_inversion_izquierda'),
                'eversion_derecha': request.form.get('tobillo_eversion_derecha'),
                'eversion_izquierda': request.form.get('tobillo_eversion_izquierda')
            }
        },
        'diagnostico_kinestico': request.form.get('diagnostico_kinestico'),
        'objetivo_corto_plazo': request.form.get('objetivo_corto_plazo'),
        'objetivo_mediano_plazo': request.form.get('objetivo_mediano_plazo'),
        'objetivo_largo_plazo': request.form.get('objetivo_largo_plazo'),
        'tratamiento': request.form.get('tratamiento'),
    }  

    filtro = {'_id': id_historia}
    actualizacion = {'$set': update_historia}
    db['historia'].update_one(filtro, actualizacion)

def obtener_historias():
    historias = list(db['historia'].find())
    return historias

def obtener_historia(id):
    historia = db["historia"].find_one({ '_id': id })
    return historia