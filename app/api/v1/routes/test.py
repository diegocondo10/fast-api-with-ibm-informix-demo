from fastapi import APIRouter

from app.db.client import sp_return_list, select_return_list
from app.services.test.models import MedicoIn
from app.services.test.service import TestService

test_router = APIRouter()


@test_router.get('/hola-mundo')
def hola_mundo():
    return {
        'mensaje': 'Hola mundo'
    }


@test_router.get('/obtener-datos/{i_nombre_medico}')
async def obtener_datos(i_nombre_medico):
    '''
    Obtiene un listado de todos los médicos registrados en la base de datos.

    ### Descripción

    Esta operación recupera una lista completa de médicos, incluyendo sus detalles personales y profesionales. Es útil para obtener una visión general de todos los profesionales médicos registrados en el sistema.

    ### Campos de respuesta (`Array/Listado`):
    - **idmedico**: int - El identificador único de cada médico.
    - **nombre**: str - Nombres del médico.
    - **apellidos**: str - Apellidos del médico.
    - **ruc**: str - Registro Único de Contribuyentes (RUC), único para cada médico.
    - **direccion**: str - Dirección residencial del médico.
    - **correo**: str - Correo electrónico del médico.
    - **telefono**: str - Número de teléfono celular del médico.
    - **id_ciudad**: int - Identificador de la ciudad donde reside el médico.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_obtiene_medicos(:i_nombre_medico);`
    - **Método HTTP**: GET
    - **Ruta**: `/obtener-datos`
    '''

    sql = f"EXECUTE PROCEDURE fn_obtiene_medicos(:i_nombre_medico);"

    parameters = {
        "i_nombre_medico": i_nombre_medico
    }

    index_column_names = [
        "idmedico",
        "nombre",
        "apellidos",
        "ruc",
        "direccion",
        "correo",
        "telefono",
        "id_ciudad"
    ]

    return [
        {
            "idmedico": 4,
            "nombre": "Ana",
            "apellidos": "RamÃ­rez",
            "ruc": "4234567890123",
            "direccion": "Calle 4, Ciudad D",
            "correo": "ana.ramirez@email.com",
            "telefono": "423-456-7890",
            "id_ciudad": "C004 "
        }
    ]

    return sp_return_list(
        sql,
        index_column_names=index_column_names,
        parameters=parameters
    )


@test_router.post('/test-body')
def test_body(body: MedicoIn):
    '''
    Obtiene un listado de todos los médicos registrados en la base de datos.

    ### Descripción

    Esta operación recupera una lista completa de médicos, incluyendo sus detalles personales y profesionales. Es útil para obtener una visión general de todos los profesionales médicos registrados en el sistema.

    ### Campos de respuesta (`Array/Listado`):
    - **idmedico**: int - El identificador único de cada médico.
    - **nombre**: str - Nombres del médico.
    - **apellidos**: str - Apellidos del médico.
    - **ruc**: str - Registro Único de Contribuyentes (RUC), único para cada médico.
    - **direccion**: str - Dirección residencial del médico.
    - **correo**: str - Correo electrónico del médico.
    - **telefono**: str - Número de teléfono celular del médico.
    - **id_ciudad**: int - Identificador de la ciudad donde reside el médico.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_obtiene_medicos(:i_nombre_medico);`
    - **Método HTTP**: GET
    - **Ruta**: `/obtener-datos`
    '''
    return TestService.guardar_medico(body)



@test_router.get('/prueba-bd')
def prueba_bd():
    return select_return_list('SELECT * FROM am_comunica')