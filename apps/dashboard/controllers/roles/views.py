from django.shortcuts import render, redirect
from django.http import JsonResponse
from .usp import *

def getRolesPage(request):
    data = {
        'breadcrumb': "Roles",
        'title': 'Lista de Roles',
        'subtitle': 'Lista completa de roles de Usuario o Profesional',
        'button_add': 'Añadir Rol',
    }

    return render(request, "roles.html", data)


def insertRol(request):
    if request.method == "POST":
        v_idRol = request.POST.get("idRol")

        if (v_idRol == ""):
            # INSERTAR Roles
            v_nombre_roles = request.POST.get("txtNombreRol")
            v_descripcion_roles = request.POST.get("txtDescripcionRol")
            fc_insert_roles(v_nombre_roles, v_descripcion_roles)
            return redirect("getRolesPage")

        else:
            # ACTUALIZAR Roles
            exist = fc_get_roles(v_idRol)
            if (exist != ()):
                v_nombre_roles = request.POST.get("txtNombreRol")
                v_descripcion_roles = request.POST.get("txtDescripcionRol")
                fc_update_roles(v_nombre_roles, v_descripcion_roles)
                return redirect("getRolesPage")
            else:
                return redirect("getRolesPage")
                
    else:
        return redirect("getRolesPage")


def getAllRoles(request):
    data_modulos = list(fc_get_all_roles())
    data_to_array = []
    # Convertir TUPLA a Array Modificable
    for i in data_modulos:
        data_to_array.append({
            "id_rol": i[0],
            "nombre_rol": i[1],
            "descripcion_rol": i[2],
            "status_rol": i[3],
        })

    # Añadir HTML
    for i in data_to_array:
        if (i['status_rol'] == 1):
            i['status_rol'] = "<div class='text-center'><button class='btn btn-success'>Activado</button></div>"
        else:
            i['status_rol'] = "<div class='text-center'><button class='btn btn-warning'>Desactivado</button></div>"
        
        i['options'] = """
            <div class='text-center'>
                <button type='button' class='btn btn-sm btn-primary' onclick='fntEditRol("%s")' data-bs-toggle='modal' data-bs-target='#modalRoles'><i class='bx bxs-edit' ></i></button>
                <a onclick='enableRol(%s)' class='btn btn-sm btn-success'><i class='bx bx-power-off' ></i></a>
                <a onclick='disableRol("%s")' class='btn btn-sm btn-warning'><i class='bx bx-power-off' ></i></a>
                <a onclick='deleteRol("%s")' class='btn btn-sm btn-danger'><i class='bx bxs-trash-alt'></i></a>
            </div>
        """ % (i['id_rol'], i['id_rol'], i['id_rol'], i['id_rol'])

    return JsonResponse(data_to_array, safe=False, json_dumps_params={'ensure_ascii': False})

def getRol(request):
    v_idMRol = request.GET.get('idRol')
    if (v_idMRol != ""):
        data_rol = list(fc_get_roles(v_idMRol))
        data_to_array = []
        if (data_rol != ()):
            for i in data_rol:
                data_to_array.append({
                    "id_rol": i[0],
                    "nombre_rol": i[1],
                    "descripcion_rol": i[2],
                    "status_rol": i[3],
                })
            return JsonResponse(data_to_array, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return redirect("getRolesPage")
    else:
        return redirect("getRolesPage")

def enableRol(request):
    if request.method == "GET":
        v_idRol = request.GET.get("idRol")
        exist = fc_get_roles(v_idRol)
        if (exist != ()):
            fc_enable_roles(v_idRol)
            return redirect("getRolesPage")
        else:
            return redirect("getRolesPage")
    else:
        return redirect("getRolesPage")

def disableRol(request):
    if request.method == "GET":
        v_idRol = request.GET.get("idRol")
        exist = fc_get_roles(v_idRol)
        if (exist != ()):
            fc_deactivate_roles(v_idRol)
            return redirect("getRolesPage")
        else:
            return redirect("getRolesPage")
    else:
        return redirect("getRolesPage")

def deleteRol(request):
    if request.method == "GET":
        v_idRol = request.GET.get("idRol")
        exist = fc_get_roles(v_idRol)
        if (exist != ()):
            fc_delete_roles(v_idRol)
            return redirect("getRolesPage")
        else:
            return redirect("getRolesPage")
    else:
        return redirect("getRolesPage")