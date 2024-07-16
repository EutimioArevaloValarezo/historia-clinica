import uuid

from flask import request, render_template, redirect, url_for

from app import app
from routes.control import guardar_historia_clinica, get_historias

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historia_clinica')
def historia_clinica():
    return render_template('historia-clinica.html')

@app.route('/agrega_historia_clinica', methods=['POST'])
def agregar_historia_clinica(): 
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
        }
    }  
    print(historia)
    guardar_historia_clinica(historia)
    return redirect(url_for('index'))
    # return render_template('listado.html')

@app.route('/listar_historia')
def listar_historia():
    historias = get_historias()
    return render_template('listado.html', historias=historias)
