import os
import dotenv

from passlib.hash import pbkdf2_sha256
from functools import wraps
from flask import request, render_template, redirect, url_for, session, jsonify
from routes.control import guardar_historia_clinica, obtener_historias, obtener_usuario, crear_usuario
from app import app
from db import db

dotenv.load_dotenv()
app.secret_key = str(os.getenv('SECRET_KEY')).encode()

def requerir_logeo(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logeado' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    
    return wrap

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

@app.route('/iniciar_sesion_usuario', methods=['POST'])
def iniciar_sesion_usuario(): 
    cedula = request.form.get('cedula')
    contrasenia = request.form.get('contrasenia')
    usuario = obtener_usuario(cedula)
    if usuario and pbkdf2_sha256.verify(contrasenia, usuario['contrasenia']):
        session['logeado'] = True
        session['user'] = usuario
        return jsonify(usuario), 200
    else:
        return jsonify({ 'error': 'Credenciales incorrectas' }), 401

@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    cedula = request.form.get('cedula')
    contrasenia = request.form.get('contrasenia')

    if db['usuario'].find_one({ 'cedula': cedula }):
        return jsonify({ 'error': 'Ya existe un usuario con esta cédula' }), 400
    
    usuario = crear_usuario(nombres, apellidos, cedula, contrasenia)
    if db['usuario'].insert_one(usuario):
        return jsonify({'success': 'Se ha creado correctamente el usuario :'+str(usuario)}), 200

    return jsonify({ 'error': 'Se produjo un error' }), 400

@app.route('/perfil_usuario')
@requerir_logeo
def perfil_usuario():
    return render_template('perfil_usuario.html')

@app.route('/editar_usuario', methods=['POST'])
@requerir_logeo
def editar_administrador():
    switch = request.form.get('get_switch')
    nombre = request.form.get('get_nombre')
    apellido = request.form.get('get_apellido')
    cedula = request.form.get('get_cedula')
    user = session.get('user', None)

    if(switch):
        pass_actual = request.form.get('get_contrasenia_actual')
        pass_nueva = request.form.get('get_contrasenia_nueva')
        if pbkdf2_sha256.verify(pass_actual, user['contrasenia']):
            pass_nueva = pbkdf2_sha256.encrypt(pass_nueva)
            db['usuario'].update_one({'_id': user['_id']}, {'$set': {'contrasenia': pass_nueva}})
            return jsonify({ 'success': 'Se ha actualizado los datos y la contraseña correctamente' }), 200
        else:
            return jsonify({ 'error': 'No se ha podido actualizar la contraseña, verifica la información' }), 401
    else:
        res = db['usuario'].update_one({'_id': user['_id']}, {'$set': {'nombre': nombre, 'apellido': apellido, 'cedula': cedula}})
        if res:
            return jsonify({ 'success': 'Se han actualizado los datos correctamente' }), 200
        return jsonify({ 'error': 'No se han podido actualizar los datos' }), 401

@app.route('/cerrar_sesion_usuario')
@requerir_logeo
def cerrar_sesion_usuario():
    session.clear()
    return redirect('/')

@app.route('/historia_clinica')
@requerir_logeo
def historia_clinica():
    return render_template('historia-clinica.html')

@app.route('/agrega_historia_clinica', methods=['POST'])
@requerir_logeo
def agregar_historia_clinica(): 
    guardar_historia_clinica(request)
    return redirect(url_for('index'))

@app.route('/listar_historia')
@requerir_logeo
def listar_historia():
    historias = obtener_historias()
    return render_template('listado.html', historias=historias)
