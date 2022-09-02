from apps.dashboard.views import *

# TODOS LOS ROLES
def fc_get_all_roles():
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("CALL USP_ROLES_ALL()")
            result = cursor.fetchall()
        cx.close()
        return result
    except Exception as ex:
        print (ex)

# OBTENER UN ROL
def fc_get_roles (id_modulo):
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("CALL USP_ROLES_GET({0})" % (id_modulo))
            result = cursor.fetchall()
        cx.close()
        return result
    except Exception as ex:
        print (ex)

# INSERTAR ROL
def fc_insert_roles (nombre_rol, descripcion_rol):
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("call usp_roles_insert('%s', '%s', %s)" % (nombre_rol, descripcion_rol, 0))
            cx.commit()
        cx.close()
        return "Realizado con Éxito"
    except Exception as ex:
        print (ex)
        return "Error en el Proceso"


# ACTUALIZAR ROL
def fc_update_roles(id_rol, nombre_rol, descripcion_rol):
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("call usp_roles_udpate(%s, '%s', '%s', %s)" %
                           (id_rol, nombre_rol, descripcion_rol, 0))
            cx.commit()
        cx.close()
        return "Realizado con Éxito"
    except Exception as ex:
        print(ex)
        return "Error en el Proceso"


# Activar / Habilitar Rol
def fc_enable_roles(id_rol):
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("call usp_roles_enable(%s)" % (id_rol))
            cx.commit()
        cx.close()
        return "Realizado con Éxito"
    except Exception as ex:
        print(ex)
        return "Error en el Proceso"


# Desactivar / Deshabilitar Rol
def fc_deactivate_roles(id_rol):
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("call usp_roles_deactivate(%s)" % (id_rol))
            cx.commit()
        cx.close()
        return "Realizado con Éxito"
    except Exception as ex:
        print(ex)
        return "Error en el Proceso"


# Eliminar Rol
def fc_delete_roles(id_rol):
    try:
        cx = get_connection()
        with cx.cursor() as cursor:
            cursor.execute("call usp_roles_delete(%s)" % (id_rol))
            cx.commit()
        cx.close()
        return "Realizado con Éxito"
    except Exception as ex:
        print(ex)
        return "Error en el Proceso"
